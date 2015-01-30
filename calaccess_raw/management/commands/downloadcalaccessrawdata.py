import os
import shutil
import zipfile
import requests
from hurry.filesize import size
from optparse import make_option
from clint.textui import progress
from django.utils.six.moves import input
from dateutil.parser import parse as dateparse
from django.core.management import call_command
from django.template.loader import render_to_string
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw import get_download_directory, get_model_list
from django.contrib.humanize.templatetags.humanize import naturaltime


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


class Command(CalAccessCommand):
    help = 'Download, unzip, clean and load the latest snapshot of the \
CAL-ACCESS database'
    option_list = CalAccessCommand.option_list + custom_options

    def set_options(self, *args, **kwargs):
        self.url = 'http://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip'
        self.data_dir = get_download_directory()
        os.path.exists(self.data_dir) or os.mkdir(self.data_dir)
        self.zip_path = os.path.join(self.data_dir, 'calaccess.zip')
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        self.csv_dir = os.path.join(self.data_dir, "csv/")
        os.path.exists(self.csv_dir) or os.mkdir(self.csv_dir)
        if kwargs['download']:
            self.download_metadata = self.get_download_metadata()
            self.local_metadata = self.get_local_metadata()
            prompt_context = dict(
                last_updated=self.download_metadata['last-modified'],
                time_ago=naturaltime(self.download_metadata['last-modified']),
                size=size(self.download_metadata['content-length']),
                last_download=self.local_metadata['last-download'],
                download_dir=self.data_dir,
            )
            self.prompt = render_to_string(
                'calaccess_raw/downloadcalaccessrawdata.txt',
                prompt_context,
            )
        self.verbosity = int(kwargs['verbosity'])

    def handle(self, *args, **options):
        # Set the options
        self.set_options(*args, **options)
        # Get to work
        if options['download']:
            if options['noinput']:
                self.download()
            else:
                confirm = input(self.prompt.encode('utf-8'))
                if confirm != 'yes':
                    self.failure("Download cancelled")
                    return
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
        self.success("Done!")

    def get_download_metadata(self):
        """
        Returns basic metadata about the current CAL-ACCESS snapshot,
        like its size and the last time it was updated while stopping
        short of actually downloading it.
        """
        request = requests.head(self.url)
        return {
            'content-length': int(request.headers['content-length']),
            'last-modified': dateparse(request.headers['last-modified'])
        }

    def get_local_metadata(self):
        """
        Retrieves a local file that records past downloads and returns
        a dictionary that includes a timestamp with a timestamp marking
        the last update.

        If no file exists it returns the dictionary with null values.
        """
        file_path = os.path.join(self.data_dir, 'download_metadata.txt')
        metadata = {
            'last-download': None
        }
        if os.path.isfile(file_path):
            with open(file_path) as f:
                metadata['last-download'] = dateparse(f.readline())
        return metadata

    def set_local_metadata(self):
        """
        Creates a file that stories the date and time vintage of the last
        CAL-ACCESS archive download.
        """
        file_path = os.path.join(self.data_dir, 'download_metadata.txt')
        with open(file_path, 'wb') as f:
            f.write(str(self.download_metadata['last-modified']))

    def download(self):
        """
        Download the ZIP file in pieces.
        """
        if self.verbosity:
            self.header("Downloading ZIP file")

        r = requests.get(self.url, stream=True)
        length = float(self.download_metadata['content-length'])
        with open(self.zip_path, 'wb') as f:
            for chunk in progress.bar(
                r.iter_content(chunk_size=1024),
                expected_size=(length/1024)+1,
                label="Progress: "
            ):
                f.write(chunk)
                f.flush()
        self.set_local_metadata()

    def unzip(self):
        """
        Unzip the snapshot file.
        """
        if self.verbosity:
            self.log(" Unzipping archive")
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
            self.log(" Prepping unzipped data")
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
            self.log(" Clearing out unneeded files")
        shutil.rmtree(os.path.join(self.data_dir, 'CalAccess'))
        os.remove(self.zip_path)

    def clean(self):
        """
        Clean up the raw data files from the state so they are
        ready to get loaded into the database.
        """
        if self.verbosity:
            self.header("Cleaning data files")

        # Loop through all the files in the source directory
        for name in os.listdir(self.tsv_dir):
            call_command("cleancalaccessrawfile", name)

    def load(self):
        """
        Loads the cleaned up csv files into the database
        """
        if self.verbosity:
            self.header("Loading data files")

        for model in get_model_list():
            call_command("loadcalaccessrawfile", model.__name__)
