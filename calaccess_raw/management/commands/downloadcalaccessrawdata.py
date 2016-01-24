from __future__ import unicode_literals
import os
import sys
import codecs
import locale
import shutil
import zipfile
import requests
from datetime import datetime
from hurry.filesize import size
from clint.textui import progress
from django.utils.timezone import utc
from django.utils.six.moves import input
from calaccess_raw import get_download_directory
from dateutil.parser import parse as datetime_parse
from django.template.loader import render_to_string
from calaccess_raw.management.commands import CalAccessCommand
from django.contrib.humanize.templatetags.humanize import naturaltime


class Command(CalAccessCommand):
    help = "Download, unzip and prep the latest CAL-ACCESS database ZIP"
    url = 'http://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--resume",
            action="store_true",
            dest="resume",
            default=False,
            help="Resume downloading of the ZIP archive from a previous attempt"
        )
        parser.add_argument(
            "--keep-files",
            action="store_true",
            dest="keep_files",
            default=False,
            help="Keep downloaded zip and unzipped files"
        )
        parser.add_argument(
            "--noinput",
            action="store_true",
            dest="noinput",
            default=False,
            help="Download the ZIP archive without asking permission"
        )

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)

        # get the dir were data goes from app settings
        self.data_dir = get_download_directory()
        # if data_dir doesn't exist, create it
        os.path.exists(self.data_dir) or os.makedirs(self.data_dir)

        # downloaded zipfile will go in data_dir
        self.zip_path = os.path.join(self.data_dir, 'calaccess.zip')
        # so will the file where we track the last download
        self.zip_metadata_path = os.path.join(
            self.data_dir,
            '.lastdownload'
        )

        self.tsv_dir = os.path.join(self.data_dir, "tsv/")

        self.csv_dir = os.path.join(self.data_dir, "csv/")
        os.path.exists(self.csv_dir) or os.makedirs(self.csv_dir)

        self.download_metadata = self.get_download_metadata()
        self.local_metadata = self.get_local_metadata()

        total_size = self.download_metadata['content-length']
        last_modified = self.download_metadata['last-modified']
        last_download = self.local_metadata['last-download']
        cur_size = 0

        # if the user tries to resume, also have to make sure there is a zip file
        self.resume_download = (options['resume'] and os.path.exists(self.zip_path))

        if self.resume_download:
            # Make sure the downloaded chunk is newer than the
            #   last update to the remote data.
            timestamp = os.path.getmtime(self.zip_path)
            chunk_datetime = datetime.fromtimestamp(timestamp, utc)
            self.resume_download = chunk_datetime > last_modified
            # reset this vars if still resuming
            if self.resume_download:
                last_download = chunk_datetime
                cur_size = os.path.getsize(self.zip_path)

        # setting up the prompt
        prompt_context = dict(
            resuming=self.resume_download,
            already_downloaded=last_modified == last_download,
            last_modified=last_modified,
            last_download=last_download,
            time_ago=naturaltime(last_download),
            total_size=size(total_size),
            cur_size=size(cur_size),
            download_dir=self.data_dir,
        )

        self.prompt = render_to_string(
            'calaccess_raw/downloadcalaccessrawdata.txt',
            prompt_context,
        )

        # If we're taking user input, make sure the user says exactly 'yes'
        if not options['noinput'] and self.confirm_download() != 'yes':
            self.failure("Download cancelled")
            return

        self.download()
        self.unzip()

        if not options['keep_files']:
            os.remove(self.zip_path)

        self.prep()

        if not options['keep_files']:
            shutil.rmtree(os.path.join(self.data_dir, 'CalAccess'))

    def confirm_download(self):
        """
        Prompts the user to confirm they wish to download.
        """
        # Ensure stdout can handle Unicode data: http://bit.ly/1C3l4eV
        locale_encoding = locale.getpreferredencoding()
        old_stdout = sys.stdout
        sys.stdout = codecs.getwriter(locale_encoding)(sys.stdout)

        confirm = input(self.prompt)

        # Set things back to the way they were before continuing.
        sys.stdout = old_stdout
        return confirm.lower()

    def get_download_metadata(self):
        """
        Returns basic metadata about the current CAL-ACCESS snapshot,
        like its size and the last time it was updated while stopping
        short of actually downloading it.
        """
        request = requests.head(self.url)
        return {
            'content-length': int(request.headers['content-length']),
            'last-modified': datetime_parse(request.headers['last-modified'])
        }

    def get_local_metadata(self):
        """
        Retrieves a local file that records past downloads and returns
        a dictionary that includes a timestamp with a timestamp marking
        the last update.

        If no file exists it returns the dictionary with null values.
        """
        metadata = {
            'last-download': None
        }
        if os.path.isfile(self.zip_metadata_path):
            with open(self.zip_metadata_path) as f:
                metadata['last-download'] = datetime_parse(f.readline())
        return metadata

    def set_local_metadata(self):
        """
        Creates a file that stories the date and time vintage of the last
        CAL-ACCESS archive download.
        """
        with open(self.zip_metadata_path, 'w') as f:
            f.write(str(self.download_metadata['last-modified']))

    def download(self):
        """
        Download the ZIP file in pieces.
        """

        if self.verbosity:
            self.header("Downloading ZIP file")

        expected_size = self.download_metadata['content-length']

        if expected_size is None:
            resp = requests.head(self.url)
            expected_size = int(resp.headers.get('content-length', 0))

        # Prep
        headers = dict()
        if os.path.exists(self.zip_path):
            if self.resume_download:
                cur_sz = os.path.getsize(self.zip_path)
                headers['Range'] = 'bytes=%d-' % cur_sz
                expected_size = expected_size - cur_sz
            else:
                os.remove(self.zip_path)

        # Stream the download
        chunk_size = 1024
        req = requests.get(self.url, stream=True, headers=headers)
        n_iters = float(expected_size) / chunk_size + 1
        with open(self.zip_path, 'ab') as fp:
            for chunk in progress.bar(req.iter_content(chunk_size=chunk_size),
                                      expected_size=n_iters):
                fp.write(chunk)
                fp.flush()

        # store the last completed download
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
