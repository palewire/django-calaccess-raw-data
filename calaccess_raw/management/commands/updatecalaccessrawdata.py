#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Download, unzip, clean and load the latest CAL-ACCESS database ZIP.
"""
from django.conf import settings

# Files
import os
from django.core.files import File
from zipfile import ZIP_DEFLATED, ZIP_STORED, ZipFile

# Time
from time import sleep
from django.utils.timezone import now

# Templating
from django.template.loader import render_to_string
from django.contrib.humanize.templatetags.humanize import naturaltime

# Commands
from sys import exit
from django.core.management import call_command
from django.core.management.base import CommandError
from calaccess_raw.management.commands import CalAccessCommand

# Models
from calaccess_raw import get_model_list
from calaccess_raw.models.tracking import RawDataVersion

# Logging
import logging
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
            help="Update or resume previous update without asking permission"
        )
        parser.add_argument(
            "-a",
            "--app-name",
            dest="app_name",
            default="calaccess_raw",
            help="Name of Django app with models into which data will "
                 "be imported (if not calaccess_raw)"
        )

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)

        # set / compute any attributes that multiple class methods need
        self.app_name = options["app_name"]
        self.keep_files = options["keep_files"]
        self.noinput = options['noinput']

        download_metadata = self.get_download_metadata()
        logger.debug('Server: %s' % download_metadata['server'])
        logger.debug('ETag: %s' % download_metadata['etag'])
        logger.debug('Last-Modified: %s' % download_metadata['last-modified'])
        logger.debug('Content-Length: %s' % download_metadata['content-length'])
        # get or create the RawDataVersion
        latest_version, created = self.get_or_create_version(
            download_metadata['content-length'],
            self.parse_imf_datetime_str(
                download_metadata['last-modified']
            ),
        )
        # log if latest version is new
        if created:
            logger.info('New CAL-ACCESS version available.')

        previous_version = None
        since_previous_release = None
        can_resume_previous = False
        # if update to latest version has not yet started, check to see if previous
        #   version can resume
        if not latest_version.update_start_datetime:
            # get previous versions
            prev_downloaded_versions = RawDataVersion.objects.filter(
                download_start_datetime__isnull=False
            ).exclude(id=latest_version.id)
            # if there are any
            if prev_downloaded_versions:
                # get the last one started
                previous_version = prev_downloaded_versions.latest(
                    'download_start_datetime'
                )
                # for prompt, get time since previous release
                since_previous_release = naturaltime(
                    previous_version.release_datetime
                )
                # if the previous version finished downloading and didn't finish updating
                if (
                    previous_version.download_completed
                    and not previous_version.update_completed
                ):
                    # can resume if zip file has not been deleted
                    #   or if the raw files have been extracted
                    if (
                        os.path.exists(self.zip_path)
                        or previous_version.extract_completed
                    ):
                        can_resume_previous = True

        # if not accepting input
        if self.noinput:
            # skip if up-to-date
            if latest_version.update_completed:
                self.log('Your database is already up-to-date.')
                exit(0)
            else:
                # set to resume if update to latest is stalled or can resume previous
                self.resume = latest_version.update_stalled or can_resume_previous
        else:
            # set up prompt
            prompt_context = dict(
                latest_version=latest_version,
                previous_version=previous_version,
                can_resume_previous=can_resume_previous,
                since_previous_release=since_previous_release,
            )
            # render prompt string
            prompt = render_to_string(
                'calaccess_raw/updatecalaccessrawdata.txt',
                prompt_context,
            )
            # if the user can resume (latest or previous)
            if latest_version.update_stalled or can_resume_previous:
                # and initially confirms
                if self.confirm_proceed(prompt):
                    # go into resume mode
                    self.resume = True
                # if user does not initially confirm
                else:
                    self.resume = False
                    # if can resume latest (but doesn't) prompt restart
                    if latest_version.update_stalled:
                        confirm_restart = self.confirm_proceed(
                            'Do you want re-start your update?\n'
                        )
                    # if can resume previous (but doesn't) prompt for update to latest
                    elif can_resume_previous:
                        confirm_restart = self.confirm_proceed(
                            'Do you want to update to the latest version?\n'
                        )
                    # cancel if user doesn't confirm restart
                    if not confirm_restart:
                        raise CommandError("Update cancelled")
            # if can't resume
            else:
                self.resume = False
                # cancel if user doesn't initially confirm
                if not self.confirm_proceed(prompt):
                    raise CommandError("Update cancelled")

        # set to force restart if the user could have resumed but didn't
        # or no new version is available
        self.force_restart = (
            (
                latest_version.update_stalled
                or can_resume_previous
                or not created
            ) and not self.resume
        )

        # set the version to be updated
        if not self.force_restart and can_resume_previous:
            self.version = previous_version
        else:
            self.version = latest_version

        if self.verbosity:
            if self.resume:
                self.header(
                    "Resuming update to {:%m-%d-%Y %H:%M:%S} snapshot".format(
                        self.version.release_datetime
                    )
                )
            else:
                self.header(
                    "Updating to {:%m-%d-%Y %H:%M:%S} snapshot".format(
                        self.version.release_datetime
                    )
                )

        # if not resuming, reset the update start datetime
        if not self.resume:
            self.version.update_start_datetime = now()
        # if restarting, also erase all the other datetimes
        if self.force_restart:
            self.version.update_finish_datetime = None
            self.version.download_start_datetime = None
            self.version.download_finish_datetime = None
            self.version.extract_start_datetime = None
            self.version.extract_finish_datetime = None

        # save here in case the command doesn't finish
        self.version.save()

        # handle download
        # can only download the latest version:
        if self.version == latest_version:
            # if download completed and not forcing restart
            if self.version.download_completed and not self.force_restart:
                self.log('Already downloaded.')
            # otherwise try downloading
            else:
                self.download()
                if self.verbosity:
                    self.duration()

        # handle file extraction
        # if the last extract of the version completed and not forcing restart
        if self.version.extract_completed and not self.force_restart:
            self.log('Already extracted.')
        else:
            # if the zip isn't there
            if not os.path.exists(self.zip_path):
                # if updating to the lastest
                if self.version == latest_version:
                    self.log(
                        '%s not found. Re-downloading before extracting.' % self.zip_path
                    )
                    self.download()
                    if self.verbosity:
                        self.duration()
                else:
                    raise CommandError(
                        'Incomplete file extraction and %s not found.' % self.zip_path
                    )
            # now extract
            call_command(
                'extractcalaccessrawfiles',
                keep_files=self.keep_files
            )
            if self.verbosity:
                self.duration()

        # refresh the version (to get timestamp field values)
        self.version.refresh_from_db()

        self.clean()
        if self.verbosity:
            self.duration()

        # if archive setting is enabled, zip up all of the csv and error logs
        if getattr(settings, 'CALACCESS_STORE_ARCHIVE', False):
            # skip if resuming and the clean zip file is already saved
            if self.resume and bool(self.version.clean_zip_archive):
                self.log('File already zipped.')
            else:
                self.archive()
                if self.verbosity:
                    self.duration()

        self.load()
        if self.verbosity:
            self.duration()

        # store update finish time
        self.version.update_finish_datetime = now()
        # and save the RawDataVersion
        self.version.save()

        if self.verbosity:
            self.success("Done!")

    def download(self):
        """
        Try downloading the zip. Wait and re-try if certain CommandErrors are raised.
        """
        try:
            call_command(
                "downloadcalaccessrawdata",
                verbosity=self.verbosity,
                noinput=True,
                restart=self.force_restart
            )
        except CommandError as e:
            # if the expected and actual zip size are not the same
            if (
                'expected' in e.message.lower()
                or 'modified' in e.message.lower()
                or 'version' in e.message.lower()
            ):
                logger.debug('Waiting five minutes before re-trying')
                # wait five minutes
                sleep(300)
                # then try again
                call_command(
                    "downloadcalaccessrawdata",
                    verbosity=self.verbosity,
                    noinput=True,
                    # force a restart on second try
                    restart=True,
                )

    def clean(self):
        """
        Clean up the raw data files from the state so they are ready to get loaded into the database.
        """
        if self.verbosity:
            self.header("Cleaning data files")

        tsv_list = [f for f in os.listdir(self.tsv_dir) if '.TSV' in f.upper()]

        if self.resume:
            # get finished clean command logs of last update
            prev_cleaned = [
                x.file_name + '.TSV'
                for x in self.version.files.filter(clean_finish_datetime__isnull=False)
            ]
            self.log("{} files already cleaned.".format(len(prev_cleaned)))
            # remove these from tsv_list
            tsv_list = [x for x in tsv_list if x not in prev_cleaned]

        # Loop through all the files in the source directory
        for name in tsv_list:
            call_command(
                "cleancalaccessrawfile",
                name,
                verbosity=self.verbosity,
                keep_file=self.keep_files,
            )

    def archive(self):
        """
        Zip up and archive the .csv and error log files.
        """
        if self.verbosity:
            self.header("Zipping cleaned files")
        # Remove previous zip file
        self.version.clean_zip_archive.delete()
        clean_zip_path = os.path.join(self.data_dir, 'raw.zip')

        # enable zipfile compression
        compression = ZIP_DEFLATED

        try:
            zf = ZipFile(clean_zip_path, 'w', compression, allowZip64=True)
        except RuntimeError:
            logger.error('Zip file cannot be compressed (check zlib module).')
            compression = ZIP_STORED
            zf = ZipFile(clean_zip_path, 'w', compression, allowZip64=True)

        # loop over and save files in csv dir
        for f in os.listdir(self.csv_dir):
            if self.verbosity > 2:
                self.log(" Adding %s to zip" % f)
            csv_path = os.path.join(self.csv_dir, f)
            zf.write(csv_path, f)

        # same for errors dir
        errors_dir = os.path.join(self.data_dir, 'log')
        for f in os.listdir(errors_dir):
            if self.verbosity > 2:
                self.log(" Adding %s to zip" % f)
            error_path = os.path.join(errors_dir, f)
            zf.write(error_path, f)

        # close the zip file
        zf.close()
        if self.verbosity > 2:
            self.log(" All files zipped")

        # save the clean zip size
        self.version.clean_zip_size = os.path.getsize(clean_zip_path)
        with open(clean_zip_path, 'rb') as zf:
            # Save the zip on the raw data version
            if self.verbosity > 2:
                self.log(" Archiving zip")
            self.version.clean_zip_archive.save(
                os.path.basename(clean_zip_path), File(zf)
            )
        if self.verbosity > 2:
            self.log(" Zip archived.")

    def load(self):
        """
        Loads the cleaned up csv files into the database.
        """
        if self.verbosity:
            self.header("Loading data files")

        model_list = [x for x in get_model_list() if os.path.exists(x.objects.get_csv_path())]

        if self.resume:
            # get finished load command logs of last update
            prev_loaded = [
                x.file_name
                for x in self.version.files.filter(load_finish_datetime__isnull=False)
            ]
            self.log("{} models already loaded.".format(len(prev_loaded)))
            # remove these from model_list
            model_list = [x for x in model_list if x._meta.db_table not in prev_loaded]

        for model in model_list:
            call_command(
                "loadcalaccessrawfile",
                model.__name__,
                verbosity=self.verbosity,
                keep_file=self.keep_files,
                app_name=self.app_name,
            )
