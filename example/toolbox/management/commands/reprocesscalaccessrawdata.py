#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Re-process an archived version of the CAL-ACCESS data.
"""
import os
import logging
from datetime import datetime
import shutil
import zipfile
from hurry.filesize import size
from clint.textui import progress
from django.utils.timezone import now
from django.core.management import call_command
from django.core.management.base import CommandError
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.models.tracking import RawDataVersion
from calaccess_raw import get_data_directory, get_model_list
logger = logging.getLogger(__name__)


class Command(CalAccessCommand):
    """
    Re-process an archived version of the CAL-ACCESS data.
    """
    help = "Re-process an archived version of the CAL-ACCESS data."

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            'release-date',
            help="Date that the version was released (format: YYYY-MM-DD)"
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
        self.release_date = datetime.strptime(
            options['release-date'],
            '%Y-%m-%d'
        ).date()
        self.app_name = options["app_name"]
        self.keep_files = options["keep_files"]
        self.cleaning = options['clean']
        self.loading = options['load']
        self.data_dir = get_download_directory()

        os.path.exists(self.data_dir) or os.makedirs(self.data_dir)

        self.zip_path = os.path.join(self.data_dir, 'calaccess.zip')
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        self.csv_dir = os.path.join(self.data_dir, "csv/")

        os.path.exists(self.csv_dir) or os.makedirs(self.csv_dir)
        
        try:
            version = self.raw_data_versions.get(
                release_datetime__year=self.release_date.year,
                release_datetime__month=self.release_date.month,
                release_datetime__day=self.release_date.day,
            )
        except RawDataVersion.DoesNotExist:
            raise CommandError(
                "No release from {0} in archive.".format(self.release_date)
            )

        last_started_reprocess = self.get_last_log()

        self.resume_mode = False

        if last_started_reprocess:
            if last_started_reprocess.finish_datetime:
                if last_started_reprocess.version == version:
                    if len(last_started_reprocess.called) > 0:
                        self.log('Resuming previous re-processing job.')
                        self.resume_mode = True

        if self.resume_mode:
            self.log_record = last_started_reprocess
        else:
            # create a new log record
            self.log_record = self.command_logs.create(
                version=version,
                command=self,
                called_by=self.get_caller_log()
            )

        if self.verbosity:
            self.header("Copying archived zip file to data directory")

        if not self.resume_mode:
            # copy the zip file to the data directory
            with open(self.zip_path, 'w') as local_zip:
                version.zip_file_archive.open()
                local_zip.write(version.zip_file_archive.read())
                version.zip_file_archive.close()

            self.unzip()
            self.prep()

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

        self.log_record.finish_datetime = now()
        self.log_record.save()

        if self.verbosity:
            self.success("Done!")
        logger.info("Done!")

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
