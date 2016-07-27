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
from django.contrib.humanize.templatetags.humanize import naturaltime
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

        # get the context
        self.context = self.get_context()

        # if not accepting input
        if self.noinput:
            # and already up-to-date
            if self.context['up_to_date']:
                # skip
                self.log('Your database is already up-to-date.')
                logger.debug("Your database is already up-to-date.")
                exit(0)
            # if not taking input and can resume, automatically go into resume mode
            self.resume_mode = self.context['can_resume']
        else:
            # prompt user
            prompt = render_to_string(
                'calaccess_raw/updatecalaccessrawdata.txt',
                self.context,
            )
            # if the user can resume
            if self.context['can_resume']:
                # and initially confirms
                if self.confirm_proceed(prompt):
                    # go into resume mode
                    self.resume_mode = True
                # if does not initially confirm
                else:
                    self.resume_mode = False
                    # prompt restart
                    if not self.confirm_proceed('Do you want re-start your update?\n'):
                        raise CommandError("Update cancelled")
            else:
                self.resume_mode = False
                if not self.confirm_proceed(prompt):
                    raise CommandError("Update cancelled")

        if self.resume_mode:
            self.log_record = self.context['last_started_update']
        else:
            # get or create a version
            try:
                version = self.raw_data_versions.get(
                    release_datetime=self.context['latest_release_datetime']
                )
            except RawDataVersion.DoesNotExist:
                version = self.raw_data_versions.create(
                    release_datetime=self.context['latest_release_datetime'],
                    size=self.context['raw_expected_size']
                )
            # create a new log record
            self.log_record = self.command_logs.create(
                version=version,
                command=self,
                called_by=self.get_caller_log()
            )

        # set to force restart download if the user could have resumed but didn't
        force_restart_download = self.context['can_resume'] and not self.resume_mode

        # handle download
        if self.test_mode:
            pass
        # if not forcing restart and there is a last download
        elif not force_restart_download and self.context['last_download']:
            # if the version for the last download matches version of this update
            # and it finished
            if (
                self.log_record.version == self.context['last_download'].version and
                self.context['last_download'].finish_datetime
            ):
                self.log('Already downloaded.')
            else:
                call_command(
                    "downloadcalaccessrawdata",
                    keep_files=self.keep_files,
                    verbosity=self.verbosity,
                    noinput=True,
                    restart=force_restart_download,
                )
                if self.verbosity:
                    self.duration()
        else:
            call_command(
                "downloadcalaccessrawdata",
                keep_files=self.keep_files,
                verbosity=self.verbosity,
                noinput=True,
                restart=force_restart_download,
            )
            if self.verbosity:
                self.duration()

        # handle extract
        if self.test_mode:
            handle_command(TestExtractCommand, verbosity=self.verbosity)
        else:
            if self.context['last_extract']:
                if (
                    self.context['last_extract'].version == self.log_record.version and
                    self.context['last_extract'].finish_datetime
                ):
                    pass
                else:
                    call_command(
                        'extractcalaccessrawfiles',
                        keep_files=self.keep_files
                    )
                    if self.verbosity:
                        self.duration()
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

    def get_context(self):
        """
        Returns a dict with key/values describing the current context of the database.
        """
        context = {}

        if self.test_mode:
            with open(self.data_dir + "/sampled_version.txt", "r") as f:
                context['latest_release_datetime'] = f.readline()
                context['raw_expected_size'] = f.readline()
        else:
            download_metadata = self.get_download_metadata()
            context['latest_release_datetime'] = download_metadata['last-modified']
            context['raw_expected_size'] = download_metadata['content-length']
            context['pretty_expected_size'] = size(context['raw_expected_size'])

        context['last_started_update'] = self.get_last_log()
        context['last_finished_update'] = self.get_last_log(finished=True)

        previous_downloads = self.command_logs.filter(
            command='downloadcalaccessrawdata'
        ).order_by('-start_datetime')

        if previous_downloads:
            context['last_download'] = previous_downloads[0]
        else:
            context['last_download'] = None

        previous_extracts = self.command_logs.filter(
            command='extractcalaccessrawfiles'
        ).order_by('-start_datetime')

        if previous_extracts:
            context['last_extract'] = previous_extracts[0]
        else:
            context['last_extract'] = None

        context['current_db_version'] = None
        context['up_to_date'] = False
        context['new_version_available'] = False
        context['can_resume'] = False

        # if there is a previous update
        if context['last_started_update'] and not self.test_mode:
            context['current_db_version'] = context['last_started_update'].version
            # if the current db version release date is less than latest
            if context['current_db_version'].release_datetime < context['latest_release_datetime']:
                context['new_version_available'] = True
            # else if the current db version release datetime is the same as the latest
            elif context['current_db_version'].release_datetime == context['latest_release_datetime']:
                # and the last started updated finished
                if context['last_started_update'].finish_datetime:
                    context['up_to_date'] = True
                else:
                    # if the last update didn't finish
                    # (but is still for the current version)
                    context['can_resume'] = True
            # else if the last update did not finish
            elif not context['last_started_update'].finish_datetime:
                # but if there's a last download
                if context['last_download']:
                    # and it was for the same version
                    if context['current_db_version'] == context['last_download'].version:
                        # and the download finished
                        if context['last_download'].finish_datetime:
                            # can resume if the zip file is still there
                            if os.path.exists(self.zip_path):
                                context['can_resume'] = True
                            # or if there's a last extract
                            elif context['last_extract']:
                                # and it finished
                                if context['last_extract'].finish_datetime:
                                    context['can_resume'] = True
        # if there's a previously finished update
        if context['last_finished_update']:
            # calculate the time since it was loaded
            context['since_loaded_version'] = naturaltime(
                context['last_finished_update'].finish_datetime
            )
        else:
            context['since_loaded_version'] = None

        return context

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
