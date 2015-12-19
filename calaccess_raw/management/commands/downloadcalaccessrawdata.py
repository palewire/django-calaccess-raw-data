from __future__ import unicode_literals
import os
import sys
import codecs
import locale
import shutil
import zipfile
import requests
from hurry.filesize import size
from optparse import make_option
from django.conf import settings
from clint.textui import progress
from django.utils.six.moves import input
from datetime import datetime
from dateutil.parser import parse as dateparse
from django.core.management import call_command
from django.template.loader import render_to_string
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw import (
    get_download_directory,
    get_test_download_directory,
    get_model_list
)
from django.contrib.humanize.templatetags.humanize import naturaltime
from tzlocal import get_localzone


def download_file(url, out_path, resume=False, verbosity=1,
                  output_stream=sys.stdout, expected_size=None,
                  chunk_size=1024):

    if verbosity and output_stream:
        output_stream("Downloading ZIP file")

    if expected_size is None:
        resp = requests.head(url)
        expected_size = int(resp.headers.get('content-length', 0))

    # Prep
    headers = dict()
    if os.path.exists(out_path):
        if resume:
            cur_sz = os.path.getsize(out_path)
            headers['Range'] = 'bytes=%d-' % cur_sz
            expected_size = expected_size - cur_sz
        else:
            os.remove(out_path)

    # Stream the download
    req = requests.get(url, stream=True, headers=headers)
    n_iters = float(expected_size) / chunk_size + 1
    with open(out_path, 'ab') as fp:
        for chunk in progress.bar(req.iter_content(chunk_size=chunk_size),
                                  expected_size=n_iters):
            fp.write(chunk)
            fp.flush()


custom_options = (
    make_option(
        "--resume-download",
        action="store_true",
        dest="resume-download",
        default=False,
        help="Resume downloading of the ZIP archive from a previous attempt"
    ),
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
    make_option(
        "--use-test-data",
        action="store_true",
        dest="test_data",
        default=False,
        help="Use sampled test data (skips download, unzip, prep, clear)"
    ),
)


class Command(CalAccessCommand):
    help = 'Download, unzip, clean and load the latest snapshot of the \
CAL-ACCESS database'
    option_list = CalAccessCommand.option_list + custom_options

    def set_options(self, *args, **kwargs):
        self.url = 'http://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip'
        self.verbosity = int(kwargs['verbosity'])

        if kwargs['test_data']:
            self.data_dir = get_test_download_directory()
            settings.CALACCESS_DOWNLOAD_DIR = self.data_dir
            if self.verbosity:
                self.log("Using test data")
        else:
            self.data_dir = get_download_directory()

        os.path.exists(self.data_dir) or os.makedirs(self.data_dir)
        self.zip_path = os.path.join(self.data_dir, 'calaccess.zip')
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        self.csv_dir = os.path.join(self.data_dir, "csv/")
        os.path.exists(self.csv_dir) or os.makedirs(self.csv_dir)
        if kwargs['download']:
            self.download_metadata = self.get_download_metadata()
            self.local_metadata = self.get_local_metadata()

            self.resume_download = kwargs['resume-download'] and os.path.exists(self.zip_path)
            if self.resume_download:
                # Make sure the downloaded chunk is newer than the
                # last update to the remote data.
                timestamp = os.path.getmtime(self.zip_path)
                last_download = datetime.fromtimestamp(timestamp, get_localzone())
                self.resume_download = last_download >= self.download_metadata['last-modified']

            total_size = self.download_metadata['content-length']

            if self.resume_download:
                cur_size = os.path.getsize(self.zip_path)
                # last_download was set above.
            else:
                cur_size = 0
                last_download = self.local_metadata['last-download']

            prompt_context = dict(
                resuming=self.resume_download,
                last_updated=self.download_metadata['last-modified'],
                time_ago=naturaltime(self.download_metadata['last-modified']),
                total_size=size(total_size),
                cur_size=size(cur_size),
                last_download=last_download,
                download_dir=self.data_dir,
            )
            self.prompt = render_to_string(
                'calaccess_raw/downloadcalaccessrawdata.txt',
                prompt_context,
            )

    def handle(self, *args, **options):
        if options['test_data']:
            # disable the steps that don't apply to test data
            options["download"] = False
            options["unzip"] = False
            options["prep"] = False
            options["clear"] = False
        self.set_options(*args, **options)

        # Get the data
        if not options['download']:
            # if the directory doesn't exist, abort
            if not os.path.exists(self.tsv_dir):
                self.failure("Data tsv directory does not exist at %s" % self.tsv_dir)
                return
        else:
            if not options['noinput'] and self.confirm_download() != 'yes':
                self.failure("Download cancelled")
                return
            self.download(resume=self.resume_download)

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
        if self.verbosity:
            self.success("Done!")

    def confirm_download(self):
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
            'last-modified': dateparse(request.headers['last-modified']).astimezone(get_localzone())
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
                metadata['last-download'] = dateparse(f.readline()).astimezone(get_localzone())
        return metadata

    def set_local_metadata(self):
        """
        Creates a file that stories the date and time vintage of the last
        CAL-ACCESS archive download.
        """
        file_path = os.path.join(self.data_dir, 'download_metadata.txt')
        with open(file_path, 'w') as f:
            f.write(str(self.download_metadata['last-modified']))

    def download(self, resume=False):
        """
        Download the ZIP file in pieces.
        """

        download_file(self.url, self.zip_path, resume=resume,
                      verbosity=self.verbosity, output_stream=self.header,
                      expected_size=self.download_metadata['content-length'])
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
        tsv_list = os.listdir(self.tsv_dir)
        if self.verbosity:
            tsv_list = progress.bar(tsv_list)
        for name in tsv_list:
            call_command(
                "cleancalaccessrawfile",
                name,
                verbosity=self.verbosity
            )

    def load(self):
        """
        Loads the cleaned up csv files into the database
        """
        if self.verbosity:
            self.header("Loading data files")

        model_list = get_model_list()
        if self.verbosity:
            model_list = progress.bar(model_list)
        for model in model_list:
            call_command(
                "loadcalaccessrawfile",
                model.__name__,
                verbosity=self.verbosity,
            )
