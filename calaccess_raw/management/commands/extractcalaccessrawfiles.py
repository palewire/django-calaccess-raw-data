#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Extract the CAL-ACCESS raw data files from the database export ZIP.
"""
import os
import shutil
import zipfile
from django.conf import settings
from django.core.files import File
from django.core.management import call_command
from django.utils.timezone import now
from calaccess_raw import get_download_directory, get_test_download_directory
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.models.tracking import RawDataVersion, RawDataFile


class Command(CalAccessCommand):
    """
    Extract the CAL-ACCESS raw data files from the database export ZIP.
    """
    help = "Extract the CAL-ACCESS raw data files from the database export ZIP"

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

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)

        # get the dir where data goes from app settings
        self.data_dir = get_download_directory()

        # get path to download zip file
        self.zip_path = os.path.join(self.data_dir, self.url.split('/')[-1])
        # raw tsv files go in same data_dir in tsv/
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")

        # get the most recent download
        last_download = self.command_logs.filter(
            command='downloadcalaccessrawdata'
        ).latest('start_datetime')

        # if it finished, use that version
        if last_download.finish_datetime:
            self.version = last_download.version
        else:
            self.failure('Previous download did not complete.')
            call_command("downloadcalaccessrawdata", noinput=True)
            last_download = self.command_logs.filter(
                command='downloadcalaccessrawdata'
            ).latest('finish_datetime')
            self.version = last_download.version

        # always create a new RawDataCommand (i.e., no resume mode)
        self.log_record = self.command_logs.create(
            version=self.version,
            command=self,
            called_by=self.get_caller_log()
        )

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
        Create a RawDataFile for each download .TSV file.
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
        Save a copy of the download zip file and each file inside.
        """
        if self.verbosity:
            self.log(" Archiving original files")
        if self.verbosity > 2:
            self.log(" Archiving {0}".format(os.path.basename(self.zip_path)))

        for raw_data_file in self.raw_data_files.filter(version=self.version):
            if self.verbosity > 2:
                self.log(" Archiving {0}.TSV".format(raw_data_file.file_name))
            # Remove previous .TSV file
            raw_data_file.download_file_archive.delete()
            # Open up the .TSV file so we can wrap it in the Django File obj
            with open(self.tsv_dir + raw_data_file.file_name + '.TSV') as f:
                # Save the .TSV on the raw data file
                raw_data_file.download_file_archive.save(
                    raw_data_file.file_name + '.TSV',
                    File(f)
                )


class TestCommand(Command):
    """
    Simulates the unzipping and preping of CAL-ACCESS raw data for testing.
    """
    help = "Simulates the unzipping and preping of CAL-ACCESS raw data for testing"

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(TestCommand, self).add_arguments(parser)

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        self.verbosity = options.get("verbosity")
        self.no_color = options.get("no_color")
        self.raw_data_files = RawDataFile.objects
        self.data_dir = get_test_download_directory()
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        self.zip_path = os.path.join(self.data_dir, self.url.split('/')[-1])

        with open(self.data_dir + "/sampled_version.txt", "r") as f:
            release_datetime = f.readline()
            size = f.readline()

        try:
            self.version = RawDataVersion.objects.get(
                release_datetime=release_datetime
            )
        except RawDataVersion.DoesNotExist:
            self.version = RawDataVersion.objects.create(
                release_datetime=release_datetime,
                size=size
            )

        self.unzip()
        self.prep()
        self.track_files()

        if getattr(settings, 'CALACCESS_STORE_ARCHIVE', False):
            self.archive()
