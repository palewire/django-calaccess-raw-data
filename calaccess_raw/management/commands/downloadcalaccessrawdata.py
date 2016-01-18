from __future__ import unicode_literals
import os
import sys
import codecs
import locale
import shutil
import zipfile
import requests
from hurry.filesize import size
from django.conf import settings
from clint.textui import progress
from django.utils.six.moves import input
from datetime import datetime
from dateutil.parser import parse as datetime_parse
from django.core.management import call_command
from django.template.loader import render_to_string
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw import (
    get_download_directory,
    get_test_download_directory,
    get_model_list
)
from django.core.management.base import CommandError
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.timezone import utc


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


class Command(CalAccessCommand):
    help = ("Download, unzip, clean and load the latest snapshot of the "
            "CAL-ACCESS database")

    def add_arguments(self, parser):

        parser.add_argument(
            "--resume-download",
            action="store_true",
            dest="resume",
            default=False,
            help="Resume downloading of the ZIP archive from a previous attempt"
        )

        parser.add_argument(
            "--skip-download",
            action="store_false",
            dest="download",
            default=True,
            help="Skip downloading of the ZIP archive"
        )

        parser.add_argument(
            "--skip-unzip",
            action="store_false",
            dest="unzip",
            default=True,
            help="Skip unzipping of the archive"
        )

        parser.add_argument(
            "--skip-prep",
            action="store_false",
            dest="prep",
            default=True,
            help="Skip prepping of the unzipped archive"
        )

        parser.add_argument(
            "--skip-clean",
            action="store_false",
            dest="clean",
            default=True,
            help="Skip cleaning up the raw data files"
        )

        parser.add_argument(
            "--skip-load",
            action="store_false",
            dest="load",
            default=True,
            help="Skip loading up the raw data files"
        )

        parser.add_argument(
            "--keep-files",
            action="store_true",
            dest="keep_files",
            default=False,
            help="Skip delete files"
        )

        parser.add_argument(
            "--noinput",
            action="store_true",
            dest="noinput",
            default=False,
            help="Download the ZIP archive without asking permission"
        )

        parser.add_argument(
            "--use-test-data",
            action="store_true",
            dest="test_data",
            default=False,
            help="Use sampled test data (skips download, unzip, prep, clear)"
        )

        parser.add_argument(
            "-d",
            "--database",
            dest="database",
            default=None,
            help="Alias of database where data will be inserted. Defaults to the 'default' database."
        )

    def handle(self, **options):
        self.url = 'http://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip'
        self.verbosity = options.get("verbosity")
        self.database = options["database"]

        if options['test_data']:
            # disable the steps that don't apply to test data
            options["download"] = False
            options["unzip"] = False
            options["prep"] = False
            options["keep_files"] = True

        if options['test_data']:
            self.data_dir = get_test_download_directory()
            settings.CALACCESS_DOWNLOAD_DIR = self.data_dir
        else:
            self.data_dir = get_download_directory()

        os.path.exists(self.data_dir) or os.makedirs(self.data_dir)
        self.zip_path = os.path.join(self.data_dir, 'calaccess.zip')
        self.zip_metadata_path = os.path.join(self.data_dir,
                                              '.lastdownload')
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
            
        # Immediately check that the tsv directory exists when using test data,
        #   so we can stop immediately.
        if options['test_data']:
            if not os.path.exists(self.tsv_dir):
                raise CommandError("Data tsv directory does not exist "
                                   "at %s" % self.tsv_dir)
            elif self.verbosity:
                self.log("Using test data")

        self.csv_dir = os.path.join(self.data_dir, "csv/")
        os.path.exists(self.csv_dir) or os.makedirs(self.csv_dir)
        
        if options['download']:
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
                # last update to the remote data.
                timestamp = os.path.getmtime(self.zip_path)
                chunk_datetime = datetime.fromtimestamp(timestamp, utc)
                self.resume_download = chunk_datetime > last_modified
                if self.resume_download:
                    last_download = chunk_datetime
                    cur_size = os.path.getsize(self.zip_path)

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

            # Get the data
            if not options['noinput'] and self.confirm_download() != 'yes':
                self.failure("Download cancelled")
                return
            self.download(resume=self.resume_download)

        # wtf is up with the clear options?
        if options['unzip']:
            self.unzip(clear=not options['keep_files'])
        if options['prep']:
            self.prep(clear=not options['keep_files'])
        if options['clean']:
            self.clean(clear=not options['keep_files'])
        if options['load']:
            self.load(clear=not options['keep_files'])

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

    def download(self, resume=False):
        """
        Download the ZIP file in pieces.
        """
        download_file(self.url, self.zip_path, resume=resume,
                      verbosity=self.verbosity, output_stream=self.header,
                      expected_size=self.download_metadata['content-length'])
        self.set_local_metadata()

    def unzip(self, clear=False):
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

        if clear:
            # TODO: We intentionally leave behind zip_metadata_path,
            # to keep track of the last download. This cycle should be
            # kept in the database; when it is, we should delete
            # that file. (note: cron may be enough?)
            os.remove(self.zip_path)

    def prep(self, clear=False):
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

        if clear:
            shutil.rmtree(os.path.join(self.data_dir, 'CalAccess'))

    def clean(self, clear=False):
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
            if clear:
                os.remove(os.path.join(self.tsv_dir, name))

    def load(self, clear=False):
        """
        Loads the cleaned up csv files into the database
        """

        if self.verbosity:
            self.header("Loading data files")

        # This check enables resuming partially completed load with clear
        csv_list = [(model, model.objects.get_csv_path())
                    for model in get_model_list()
                    if os.path.exists(model.objects.get_csv_path())]
        if self.verbosity:
            csv_list = progress.bar(csv_list)
        for model, csv_path in csv_list:
            call_command(
                "loadcalaccessrawfile",
                model.__name__,
                verbosity=self.verbosity,
                database=self.database,
            )
            if clear:
                os.remove(csv_path)
