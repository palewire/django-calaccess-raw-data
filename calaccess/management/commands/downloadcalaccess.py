import os
import shutil
import zipfile
import requests
from hurry.filesize import size
from django.conf import settings
from optparse import make_option
from django.utils.six.moves import input
from dateutil.parser import parse as dateparse
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
)

class Command(BaseCommand):
    help = 'Download the latest snapshot of the CalAccess database'
    option_list = BaseCommand.option_list + custom_options

    def set_options(self, *args, **kwargs):
        self.url = 'http://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip'
        self.data_dir = settings.CALACCESS_DOWNLOAD_DIR
        self.zip_path = os.path.join(self.data_dir, 'calaccess.zip')
        self.metadata = self.get_metadata()
        self.prompt = PROMPT % (
            dateformat(self.metadata['last-modified'], 'N j, Y'),
            dateformat(self.metadata['last-modified'], 'P'),
            naturaltime(self.metadata['last-modified']),
            self.metadata['content-length'],
            self.data_dir,
        )

    def handle(self, *args, **options):
        self.set_options(*args, **options)
        if options['download']:
            confirm = input(self.prompt)
            if confirm != 'yes':
                print "Download cancelled."
                return False
            else:
                self.download()
        if options['unzip']:
            self.unzip()
        if options['prep']:
            self.prep()

    def prep(self):
        """
        Rearrange the unzipped files and get rid of the stuff we don't want.
        """
        print "Prepping unzipped data"
        # Move the deep down directory we want out
        shutil.move(
            os.path.join(
                self.data_dir,
                'CalAccess/DATA/CalAccess/DATA/'
            ),
            self.data_dir
        )
        # Rename it
        shutil.move(
            os.path.join(self.data_dir, "DATA/"),
            os.path.join(self.data_dir, "tsv/"),
        )
        # Delete the other stuff
        shutil.rmtree(os.path.join(self.data_dir, 'CalAccess'))
        os.remove(os.path.join(self.data_dir, 'calaccess.zip'))

    def unzip(self):
        """
        Unzip the snapshot file.
        """
        print "Unzipping archive"
        with zipfile.ZipFile(self.zip_path) as zf:
            for member in zf.infolist():
                words = member.filename.split('/')
                path = self.data_dir
                for word in words[:-1]:
                    drive, word = os.path.splitdrive(word)
                    head, word = os.path.split(word)
                    if word in (os.curdir, os.pardir, ''): continue
                    path = os.path.join(path, word)
                zf.extract(member, path)

    def download(self):
        """
        Download the ZIP file in pieces.
        """
        print "Downloading ZIP file"
        r = requests.get(self.url, stream=True)
        with open(self.zip_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()

    def get_metadata(self):
        """
        Returns basic metadata about the current CalAccess snapshot,
        like its size and the last time it was updated, while stopping
        of short of actually downloading it.
        """
        request = requests.head(self.url)
        return {
            'content-length': size(int(request.headers['content-length'])),
            'last-modified': dateparse(request.headers['last-modified'])
        }
