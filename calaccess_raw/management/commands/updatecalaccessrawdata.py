#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime
from django.conf import settings
from clint.textui import progress
from django.core.management import call_command
from django.core.management.base import CommandError
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw import (
    get_download_directory,
    get_test_download_directory,
    get_model_list
)
from calaccess_raw.models.tracking import RawDataVersion


class Command(CalAccessCommand):
    help = "Download, unzip, clean and load the latest CAL-ACCESS database ZIP"

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--skip-download",
            action="store_false",
            dest="download",
            default=True,
            help="Skip downloading of the ZIP archive"
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
        super(Command, self).handle(*args, **options)

        # set / compute any attributes that multiple class methods need
        self.app_name = options["app_name"]
        self.keep_files = options["keep_files"]

        if options['test_data']:
            # if using test data, we don't need to download
            options['download'] = False
            # and always keep files when running test data
            self.keep_files = True

        if options['test_data']:
            self.data_dir = get_test_download_directory()
            # need to set this app-wide because cleancalaccessrawfile
            #   also calls get_download_directory
            settings.CALACCESS_DOWNLOAD_DIR = self.data_dir
        else:
            self.data_dir = get_download_directory()

        os.path.exists(self.data_dir) or os.makedirs(self.data_dir)
        self.zip_path = os.path.join(self.data_dir, 'calaccess.zip')
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

        download_metadata = self.get_download_metadata()
        self.current_release_datetime = download_metadata['last-modified']
        self.last_update = self.get_last_log()
        self.resume_download = self.check_can_resume_download()
        self.log_record = None

        # if this isn't a test
        if not options['test_data']:
            # and there's a previous update
            if self.last_update:
                # which did not finish
                if not self.last_update.finish_datetime:
                    # and either can resume download or skipping it altogether
                    if self.resume_download or not options['download']:
                        # can resume
                        self.log_record = self.last_update

            # if not testing, but can't resume
            if not self.log_record:
                # get or create a version
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
                # create a new log record
                self.log_record = self.command_logs.create(
                    version=version,
                    command=self,
                    called_by=self.get_caller()
                )

        if options['download']:
            call_command(
                "downloadcalaccessrawdata",
                keep_files=self.keep_files,
                verbosity=self.verbosity,
                noinput=options['noinput'],
            )
            if self.verbosity:
                self.duration()

        # execute the other steps that haven't been skipped
        if options['clean']:
            self.clean()
            if self.verbosity:
                self.duration()

        if options['load']:
            self.load()
            if self.verbosity:
                self.duration()

        if self.verbosity:
            self.success("Done!")

        if not options['test_data']:
            self.log_record.finish_datetime = datetime.now()
            self.log_record.save()

    def check_can_resume_download(self):
        """
        Run a series of checks to see if the previous download can be resumed

        If so, return True, else False.
        """
        result = False
        # if there's a zip file
        if os.path.exists(self.zip_path):
            # and there's a previous incomplete download
            try:
                last_download = self.command_logs.filter(
                    command='downloadcalaccessrawdata'
                ).order_by('-start_datetime')[0]
            except IndexError:
                # can't resume
                pass
            else:
                # and the last download did not finish
                if not last_download.finish_datetime:
                    prev_release = last_download.version.release_datetime
                    # and the current release datetime is the same as
                    #  the one on the last incomplete download
                    if self.current_release_datetime == prev_release:
                        result = True
        return result

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
                verbosity=self.verbosity,
                keep_files=self.keep_files,
            )

    def load(self):
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
                keep_files=self.keep_files,
                app_name=self.app_name,
            )
