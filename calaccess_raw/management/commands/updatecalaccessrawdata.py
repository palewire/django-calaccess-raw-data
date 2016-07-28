#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Download, unzip, clean and load the latest CAL-ACCESS database ZIP.
"""
import os
import logging
from sys import exit
from zipfile import ZipFile
from hurry.filesize import size
from django.core.files import File
from django.conf import settings
from clint.textui import progress
from django.utils.timezone import now
from django.core.management import call_command
from calaccess_raw.management import handle_command
from django.core.management.base import CommandError
from django.template.loader import render_to_string
from calaccess_raw.models.tracking import RawDataVersion
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.management.commands.extractcalaccessrawfiles import TestCommand as TestExtractCommand
from calaccess_raw import (
    get_download_directory,
    get_test_download_directory,
    get_model_list
)
logger = logging.getLogger(__name__)


class Command(CalAccessCommand):
    """
    Download, unzip, clean and load the latest CAL-ACCESS database ZIP.
    """
    help = "Download, unzip, clean and load the latest CAL-ACCESS database ZIP"

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
            help="Keep zip, unzipped, TSV and CSV files"
        )
        parser.add_argument(
            "--noinput",
            action="store_true",
            dest="noinput",
            default=False,
            help="Download the ZIP archive without asking permission"
        )
        parser.add_argument(
            "--test",
            "--use-test-data",
            action="store_true",
            dest="test_data",
            default=False,
            help="Use sampled test data (skips download, clean a load)"
        )
        parser.add_argument(
            "-a",
            "--app-name",
            dest="app_name",
            default="calaccess_raw",
            help="Name of Django app with models into which data will "
                 "be imported (if other not calaccess_raw)"
        )

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)

        # set / compute any attributes that multiple class methods need
        self.app_name = options["app_name"]
        self.keep_files = options["keep_files"]
        self.test_mode = options['test_data']
        self.noinput = options['noinput']

        if self.test_mode:
            # and always keep files when running test data
            self.keep_files = True
            self.data_dir = get_test_download_directory()
            # need to set this app-wide because cleancalaccessrawfile
            #   also calls get_download_directory
            settings.CALACCESS_DOWNLOAD_DIR = self.data_dir
            self.noinput = True
        else:
            self.data_dir = get_download_directory()

        # set the download zip file path
        self.zip_path = os.path.join(self.data_dir, self.url.split('/')[-1])
        # make the data dir if necessary
        os.path.exists(self.data_dir) or os.makedirs(self.data_dir)
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        # Immediately check that the tsv directory exists when using test data,
        #   so we can stop immediately.
        if self.test_mode:
            if not os.path.exists(self.tsv_dir):
                raise CommandError("Data tsv directory does not exist "
                                   "at %s" % self.tsv_dir)
            elif self.verbosity:
                self.log("Using test data")

        # set up the dir for clean files
        self.csv_dir = os.path.join(self.data_dir, "csv/")
        os.path.exists(self.csv_dir) or os.makedirs(self.csv_dir)

        # in test mode, get download metadata from local file
        if self.test_mode:
            with open(self.data_dir + "/sampled_version.txt", "r") as f:
                latest_release_datetime = f.readline()
                latest_expected_size = f.readline()
        # else request it
        else:
            download_metadata = self.get_download_metadata()
            latest_release_datetime = download_metadata['last-modified']
            latest_expected_size = download_metadata['content-length']

        # get the last update
        last_update = self.get_last_log()

        up_to_date = False
        can_resume = False
        # if there's a last update
        if last_update:
            # if the last update's release date matches the currently available one
            #   and it finished
            if (
                last_update.version.release_datetime == latest_release_datetime and
                last_update.finish_datetime
            ):
                up_to_date = True
            # else if last update's release date matches the currently available one
            elif last_update.version.release_datetime == latest_release_datetime:
                can_resume = True
            # else if no other versions have been downloaded since last update attempt
            #   and the last download completed
            elif last_update.version.is_last_downloaded():
                # if the zip file is still, there can resume
                if os.path.exists(self.zip_path):
                    can_resume = True
                # else if no other versions have been extracted
                #   and the last extraction completed
                elif last_update.version.is_last_extracted():
                    can_resume = True

        # if not accepting input
        if self.noinput:
            # and already up-to-date
            if up_to_date:
                # skip
                self.log('Your database is already up-to-date.')
                logger.debug("Your database is already up-to-date.")
                exit(0)
            # if not taking input and can resume, go into resume mode
            self.resume_mode = can_resume
        else:
            # set up prompt
            prompt_context = dict(
                latest_release_datetime=latest_release_datetime,
                latest_expected_size=size(latest_expected_size),
                last_update=last_update,
                up_to_date=up_to_date,
                can_resume=can_resume,
            )
            # then prompt
            prompt = render_to_string(
                'calaccess_raw/updatecalaccessrawdata.txt',
                prompt_context,
            )
            # if the user can resume
            if can_resume:
                # and initially confirms
                if self.confirm_proceed(prompt):
                    # go into resume mode
                    self.resume_mode = True
                # if does not initially confirm
                else:
                    self.resume_mode = False
                    # prompt restart
                    if last_update.version.release_datetime == latest_release_datetime:
                        confirm_restart = self.confirm_proceed(
                            'Do you want re-start your update?\n'
                        )
                    else:
                        confirm_restart = self.confirm_proceed(
                            'Do you want to update to the latest version?\n'
                        )
                    if not confirm_restart:
                        raise CommandError("Update cancelled")
            else:
                self.resume_mode = False
                if not self.confirm_proceed(prompt):
                    raise CommandError("Update cancelled")

        # set up RawDataCommand record
        if self.resume_mode:
            version = last_update.version
            self.log_record = last_update
        else:
            # get or create a version
            try:
                version = self.raw_data_versions.get(
                    release_datetime=latest_release_datetime
                )
            except RawDataVersion.DoesNotExist:
                version = self.raw_data_versions.create(
                    release_datetime=latest_release_datetime,
                    size=latest_expected_size
                )
            # create a new log record
            self.log_record = self.command_logs.create(
                version=version,
                command=self,
                called_by=self.get_caller_log()
            )

        # set to force restart if the user could have resumed but didn't
        force_restart = can_resume and not self.resume_mode

        # handle download
        if self.test_mode:
            pass
        # if the last download of the version completed and not forcing restart
        #   and the zip file is still there
        elif (
            version.is_last_downloaded() and
            not force_restart and
            os.path.exists(self.zip_path)
        ):
            self.log('Already downloaded.')
        else:
            call_command(
                "downloadcalaccessrawdata",
                keep_files=self.keep_files,
                verbosity=self.verbosity,
                noinput=True,
                restart=force_restart,
            )
            if self.verbosity:
                self.duration()

        # handle file extraction
        if self.test_mode:
            handle_command(TestExtractCommand, verbosity=self.verbosity)
        # if the last extact of the version completed and not forcing restart
        elif version.is_last_extracted() and not force_restart:
            self.log('Already extracted.')
        else:
            call_command(
                'extractcalaccessrawfiles',
                keep_files=self.keep_files
            )
            if self.verbosity:
                self.duration()

        self.clean()
        if self.verbosity:
            self.duration()

        self.load()
        if self.verbosity:
            self.duration()

        self.log_record.finish_datetime = now()
        self.log_record.save()

        if self.verbosity:
            self.success("Done!")
        logger.info("Done!")

    def clean(self):
        """
        Clean up the raw data files from the state so they are ready to get loaded into the database.
        """
        if self.verbosity:
            self.header("Cleaning data files")

        tsv_list = os.listdir(self.tsv_dir)

        if self.resume_mode:
            # get finished clean command logs of last update
            prev_cleaned = [
                x.file_name + '.TSV'
                for x in self.log_record.called.filter(
                    command='cleancalaccessrawfile',
                    finish_datetime__isnull=False
                )
            ]
            self.log("{} files already cleaned.".format(len(prev_cleaned)))
            # remove these from tsv_list
            tsv_list = [x for x in tsv_list if x not in prev_cleaned]

        # Loop through all the files in the source directory
        if self.verbosity:
            tsv_list = progress.bar(tsv_list)
        for name in tsv_list:
            call_command(
                "cleancalaccessrawfile",
                name,
                verbosity=self.verbosity,
                keep_files=self.keep_files,
            )

        # if archive setting is enabled, zip up all of the csv and error logs
        if getattr(settings, 'CALACCESS_STORE_ARCHIVE', False):
            if self.verbosity:
                self.header("Zipping cleaned files")
            # Remove previous zip file
            self.log_record.version.clean_zip_archive.delete()
            clean_zip_path = os.path.join(self.data_dir, 'calaccess_cleaned.zip')
            with ZipFile(clean_zip_path, 'w', allowZip64=True) as zf:
                # loop over and save files in csv dir
                for f in os.listdir(self.csv_dir):
                    csv_path = os.path.join(self.csv_dir, f)
                    zf.write(csv_path, f)
                # same for errors dir
                errors_dir = os.path.join(self.data_dir, 'log')
                for f in os.listdir(errors_dir):
                    error_path = os.path.join(errors_dir, f)
                    zf.write(error_path, f)
            if not self.test_mode:
                # Save the zip on the raw data version
                zipped_file = open(clean_zip_path)
                self.log_record.version.clean_zip_archive.save(
                    os.path.basename(clean_zip_path),
                    File(zipped_file),
                )
                zipped_file.close()

    def load(self):
        """
        Loads the cleaned up csv files into the database.
        """
        if self.verbosity:
            self.header("Loading data files")

        model_list = [
            x for x in get_model_list() if os.path.exists(x.objects.get_csv_path())
        ]

        if self.resume_mode:
            # get finished load command logs of last update
            prev_loaded = [
                x.file_name
                for x in self.log_record.called.filter(
                    command='loadcalaccessrawfile',
                    finish_datetime__isnull=False
                )
            ]
            self.log("{} models already loaded.".format(len(prev_loaded)))
            # remove these from model_list
            model_list = [x for x in model_list if x._meta.db_table not in prev_loaded]

        if self.verbosity:
            model_list = progress.bar(model_list)
        for model in model_list:
            call_command(
                "loadcalaccessrawfile",
                model.__name__,
                verbosity=self.verbosity,
                keep_files=self.keep_files,
                app_name=self.app_name,
            )
