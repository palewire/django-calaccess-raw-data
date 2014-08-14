import os
import shutil
import zipfile
import requests
import progressbar
from hurry.filesize import size
from django.conf import settings
from optparse import make_option
from django.utils.six.moves import input
from calaccess import get_download_directory
from csvkit import CSVKitReader
from django.db import connection, transaction
from dateutil.parser import parse as dateparse
from django.core.management import call_command
from django.db.models import get_models, get_app
from django.template.defaultfilters import date as dateformat
from django.core.management.base import BaseCommand, CommandError
from django.contrib.humanize.templatetags.humanize import naturaltime

PROMPT = """
The CalAccess snapshot was last updated %s at %s, %s.

It is %s in size.

Do you want to download the file to %s

Type 'yes' to do it, or 'no' to back out: """


custom_options = (
    make_option(
        "--skip-download",
        action="store_false",
        dest="download",
        default=True,
        help="Skip downloading of the ZIP archive"
    ),
    make_option(
        "--skip-unzip",
        action="store_false",
        dest="unzip",
        default=True,
        help="Skip unzipping of the archive"
    ),
    make_option(
        "--skip-prep",
        action="store_false",
        dest="prep",
        default=True,
        help="Skip prepping of the unzipped archive"
    ),
    make_option(
        "--skip-clear",
        action="store_false",
        dest="clear",
        default=True,
        help="Skip clearing out ZIP archive and extra files"
    ),
    make_option(
        "--skip-clean",
        action="store_false",
        dest="clean",
        default=True,
        help="Skip cleaning up the raw data files"
    ),
    make_option(
        "--skip-load",
        action="store_false",
        dest="load",
        default=True,
        help="Skip loading up the raw data files"
    ),
    make_option(
        "--noinput",
        action="store_true",
        dest="noinput",
        default=False,
        help="Download the ZIP archive without asking permission"
    ),
)


class Command(BaseCommand):
    help = 'Download the latest snapshot of the CalAccess database'
    option_list = BaseCommand.option_list + custom_options

    def set_options(self, *args, **kwargs):
        self.url = 'http://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip'
        self.data_dir = get_download_directory()
        os.path.exists(self.data_dir) or os.mkdir(self.data_dir)
        self.zip_path = os.path.join(self.data_dir, 'calaccess.zip')
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        self.csv_dir = os.path.join(self.data_dir, "csv/")
        os.path.exists(self.csv_dir) or os.mkdir(self.csv_dir)
        self.metadata = self.get_metadata()
        self.prompt = PROMPT % (
            dateformat(self.metadata['last-modified'], 'N j, Y'),
            dateformat(self.metadata['last-modified'], 'P'),
            naturaltime(self.metadata['last-modified']),
            size(self.metadata['content-length']),
            self.data_dir,
        )
        self.pbar = progressbar.ProgressBar(
            widgets=[
                progressbar.Percentage(),
                progressbar.Bar(),
                ' ',
                progressbar.ETA(),
                ' ',
                progressbar.FileTransferSpeed()
            ],
            maxval=self.metadata['content-length']
        )
        self.verbosity = int(kwargs['verbosity'])

    def handle(self, *args, **options):
        """
        If DEBUG is not set to false Django imports will fail on MySQL errors.
        This data comes with a bunch of encoding issues and malformed
        TSV files.

        The import will not be perfect. But the errors should only constitute
        a minority of the total informations.
        """
        # Execute the commands only if DEBUG is set to False
        if settings.DEBUG:
            raise CommandError("DEBUG is not set to False. Please change \
before running `downloadcalaccess`")

        # Set the options
        self.set_options(*args, **options)

        # Get to work
        if options['download']:
            if options['noinput']:
                self.download()
            else:
                confirm = input(self.prompt.encode('utf-8'))
                if confirm != 'yes':
                    print "Download cancelled."
                    return False
                self.download()
        if options['unzip']:
            self.unzip()
        if options['prep']:
            self.prep()
        if options['clear']:
            self.clear()
        if options['clean']:
            self.clean()
        if options['load']:
            self.load()

    def get_metadata(self):
        """
        Returns basic metadata about the current CalAccess snapshot,
        like its size and the last time it was updated, while stopping
        short of actually downloading it.
        """
        request = requests.head(self.url)
        return {
            'content-length': int(request.headers['content-length']),
            'last-modified': dateparse(request.headers['last-modified'])
        }

    def download(self):
        """
        Download the ZIP file in pieces.
        """
        if self.verbosity:
            print "Downloading ZIP file"
        r = requests.get(self.url, stream=True)
        bytes = 0
        self.pbar.start()
        with open(self.zip_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    bytes += len(chunk)
                    self.pbar.update(bytes)
                    f.flush()
        self.pbar.finish()

    def unzip(self):
        """
        Unzip the snapshot file.
        """
        if self.verbosity:
            print "Unzipping archive"
        with zipfile.ZipFile(self.zip_path) as zf:
            for member in zf.infolist():
                words = member.filename.split('/')
                path = self.data_dir
                for word in words[:-1]:
                    drive, word = os.path.splitdrive(word)
                    head, word = os.path.split(word)
                    if word in (os.curdir, os.pardir, ''):
                        continue
                    path = os.path.join(path, word)
                zf.extract(member, path)

    def prep(self):
        """
        Rearrange the unzipped files and get rid of the stuff we don't want.
        """
        if self.verbosity:
            print "Prepping unzipped data"
        # Move the deep down directory we want out
        shutil.move(
            os.path.join(
                self.data_dir,
                'CalAccess/DATA/CalAccess/DATA/'
            ),
            self.data_dir
        )
        # Clear out target if it exists
        if os.path.exists(self.tsv_dir):
            shutil.rmtree(self.tsv_dir)
        # Rename it to the target
        shutil.move(
            os.path.join(self.data_dir, "DATA/"),
            self.tsv_dir,
        )

    def clear(self):
        """
        Delete ZIP archive and files we don't need.
        """
        if self.verbosity:
            print "Clearing out unneeded files"
        shutil.rmtree(os.path.join(self.data_dir, 'CalAccess'))
        os.remove(self.zip_path)

    def clean(self):
        """
        Clean up the raw data files from the state so they are
        ready to get loaded into the database.
        """
        if self.verbosity:
            print "Cleaning data files"

        # Loop through all the files in the source directory
        for name in os.listdir(self.tsv_dir):
            call_command("cleancalaccessfile", name)

    def load(self):
        """
        Loads the cleaned up csv files into the database
        """
        model_list = get_models(get_app("calaccess"))
        for model in model_list:
            call_command("loadcalaccessfile", model.__name__)
