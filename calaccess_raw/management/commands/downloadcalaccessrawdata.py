#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from django.db.utils import IntegrityError
from django.utils.timezone import utc
from django.utils.six.moves import input
from calaccess_raw import get_download_directory
from django.template.loader import render_to_string
from django.core.management.base import CommandError
from calaccess_raw.management.commands import CalAccessCommand
from django.contrib.humanize.templatetags.humanize import naturaltime
from calaccess_raw.models.tracking import RawDataVersion


class Command(CalAccessCommand):
    help = "Download, unzip and prep the latest CAL-ACCESS database ZIP"

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--resume",
            "--resume-download",
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

        # get the dir where data goes from app settings
        self.data_dir = get_download_directory()
        # if data_dir doesn't exist, create it
        os.path.exists(self.data_dir) or os.makedirs(self.data_dir)

        # downloaded zip file will go in data_dir
        self.zip_path = os.path.join(self.data_dir, 'calaccess.zip')
        # raw tsv files go in same data_dir in tsv/
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")

        download_metadata = self.get_download_metadata()

        self.current_release_datetime = download_metadata['last-modified']
        self.current_release_size = download_metadata['content-length']

        self.last_started_download = self.get_last_log()
        self.last_finished_download = self.get_last_log(finished=True)

        if self.last_finished_download:
            last_release_datetime = self.last_finished_download.version.release_datetime
            since_prev_version = naturaltime(last_release_datetime)
        else:
            last_release_datetime = None
            since_prev_version = None

        if last_release_datetime == self.current_release_datetime:
            already_downloaded = True
        else:
            already_downloaded = False

        # if the user tries to resume, check to see if possible
        self.resume_download = (options['resume'] and self.check_can_resume())

        if self.resume_download:
            # set current size to partially downloaded zip
            self.local_file_size = os.path.getsize(self.zip_path)
            # set the datetime of last download to last modified date
            # of zip file
            timestamp = os.path.getmtime(self.zip_path)
            self.local_file_datetime = datetime.fromtimestamp(timestamp, utc)
        else:
            self.local_file_size = 0
            self.local_file_datetime = None

        # setting up the prompt
        prompt_context = dict(
            current_release_datetime=self.current_release_datetime,
            resuming=self.resume_download,
            already_downloaded=already_downloaded,
            expected_size=size(self.current_release_size),
            local_file_size=size(self.local_file_size),
            download_dir=self.data_dir,
            since_prev_version=since_prev_version,
            since_local_file_modified=naturaltime(self.local_file_datetime)
        )

        self.prompt = render_to_string(
            'calaccess_raw/downloadcalaccessrawdata.txt',
            prompt_context,
        )

        # If we're taking user input, make sure the user says exactly 'yes'
        if not options['noinput'] and self.confirm_download() != 'yes':
            raise CommandError("Download cancelled")

        if self.resume_download:
            self.log_record = self.last_started_download
        else:
            # get or create a version record
            # .get_or_create() throws IntegrityError
            try:
                version = self.raw_data_versions.get(
                    release_datetime=self.current_release_datetime
                )
            except RawDataVersion.DoesNotExist:
                version = self.raw_data_versions.create(
                    release_datetime=self.current_release_datetime,
                    size=download_metadata['content-length']
                )
            # create a log record
            self.log_record = self.command_logs.create(
                version=version,
                command=self,
                called_by=self.get_caller()
            )

        self.download()
        self.unzip()

        if not options['keep_files']:
            os.remove(self.zip_path)

        self.prep()

        if not options['keep_files']:
            shutil.rmtree(os.path.join(self.data_dir, 'CalAccess'))

        self.log_record.finish_datetime = datetime.now()
        self.log_record.save()

    def check_can_resume(self):
        """
        Run a series of checks to see if the previous download can be resumed

        If so, return True, else False.
        """

        result = False

        # if there's a zip file
        if os.path.exists(self.zip_path):
            # and there's a previous download
            if self.last_started_download:
                # that did not finish
                if not self.last_started_download.finish_datetime:

                    prev_release = self.last_started_download.version.release_datetime

                    # and the current release datetime is the same as
                    #  the one on the last incomplete download
                    if self.current_release_datetime == prev_release:
                        result = True

        return result

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

    def download(self):
        """
        Download the ZIP file in pieces.
        """

        if self.verbosity:
            self.header("Downloading ZIP file")

        expected_size = self.current_release_size

        # Prep
        headers = dict()
        if os.path.exists(self.zip_path):
            if self.resume_download:

                headers['Range'] = 'bytes=%d-' % self.local_file_size
                expected_size = expected_size - self.local_file_size
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

        # make the RawDataFile records
        for f in os.listdir(self.tsv_dir):
            try:
                self.raw_data_files.create(
                    version=self.log_record.version,
                    file_name=f.upper().replace('.TSV', ''),
                )
            except IntegrityError:
                pass
