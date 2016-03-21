#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import shutil
import zipfile
import requests
from datetime import datetime
from hurry.filesize import size
from clint.textui import progress
from django.conf import settings
from django.core.files import File
from django.utils.timezone import utc, now
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
        parser.add_argument(
            "--force-restart",
            "--restart",
            action="store_true",
            dest="restart",
            default=False,
            help="Force re-start (overrides auto-resume)."
        )

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)

        # get the dir where data goes from app settings
        self.data_dir = get_download_directory()
        # if data_dir doesn't exist, create it
        os.path.exists(self.data_dir) or os.makedirs(self.data_dir)

        # downloaded zip file will go in data_dir
        self.zip_path = os.path.join(self.data_dir, self.url.split('/')[-1])
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

        # can resume only if possible and not forcing re-start
        self.resume_download = self.check_can_resume() and not options['restart']

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

        if not options['noinput'] and not options['restart']:

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

            prompt = render_to_string(
                'calaccess_raw/downloadcalaccessrawdata.txt',
                prompt_context,
            )

            if not self.confirm_proceed(prompt):
                raise CommandError("Download cancelled")

        if self.resume_download:
            self.log_record = self.last_started_download
            self.version = self.log_record.version
        else:
            # get or create a version record
            # .get_or_create() throws IntegrityError
            try:
                self.version = self.raw_data_versions.get(
                    release_datetime=self.current_release_datetime
                )
            except RawDataVersion.DoesNotExist:
                self.version = self.raw_data_versions.create(
                    release_datetime=self.current_release_datetime,
                    size=download_metadata['content-length']
                )
            # create a log record
            self.log_record = self.command_logs.create(
                version=self.version,
                command=self,
                called_by=self.get_caller_log()
            )

        self.download()
        self.unzip()
        self.prep()
        self.track_files()

        if getattr(settings, 'CALACCESS_STORE_ARCHIVE', False):
            self.archive()

        if not options['keep_files']:
            os.remove(self.zip_path)
            shutil.rmtree(os.path.join(self.data_dir, 'CalAccess'))

        self.log_record.finish_datetime = now()
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

    def download(self):
        """
        Download the ZIP file in pieces.
        """
        if self.verbosity:
            if self.resume_download:
                self.header("Resuming download of ZIP file")
            else:
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

    def track_files(self):
        """
        Create a RawDataFile for each download .TSV file
        """
        for f in os.listdir(self.tsv_dir):
            if '.TSV' in f:
                file_name = f.upper().replace('.TSV', '')
                self.raw_data_files.get_or_create(
                    version=self.version,
                    file_name=file_name,
                )

    def archive(self):
        """
        Save a copy of the download zip file on RawDataVersion and a copy of
        each .TSV file on the associated RawDataFile.
        """
        if self.verbosity:
            self.log(" Archiving original files")
        # Remove previous zip file
        self.version.zip_file_archive.delete()
        # Open up the zipped file so we can wrap it in the Django File obj
        zipped_file = open(self.zip_path)
        # Save the zip on the raw data version
        self.version.zip_file_archive.save(
            self.url.split('/')[-1],
            File(zipped_file)
        )
        zipped_file.close()

        # make the RawDataFile records
        for raw_data_file in self.raw_data_files.filter(version=self.version):
            # Remove previous .TSV file
            raw_data_file.download_file_archive.delete()
            # Open up the .TSV file so we can wrap it in the Django File obj
            with open(self.tsv_dir + raw_data_file.file_name + '.TSV') as f:
                # Save the .TSV on the raw data file
                raw_data_file.download_file_archive.save(
                    raw_data_file.file_name + '.TSV',
                    File(f)
                )
