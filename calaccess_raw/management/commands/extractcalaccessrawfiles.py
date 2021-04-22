#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Extract the CAL-ACCESS raw data files from downloaded ZIP.
"""
# Files
import os
import shutil
import zipfile
from django.core.files import File

# Misc.
import re
from django.conf import settings
from django.utils.timezone import now

# Commands
from django.core.management.base import CommandError
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.models.tracking import RawDataVersion, RawDataFile


class Command(CalAccessCommand):
    """
    Extract the CAL-ACCESS raw data files from downloaded ZIP.
    """
    help = "Extract the CAL-ACCESS raw data files from downloaded ZIP"

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
            help="Keep downloaded zipped files"
        )

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)

        # Get the most recently downloaded RawDataVersion
        try:
            self.version = RawDataVersion.objects.latest_download()
        except RawDataVersion.DoesNotExist:
            raise CommandError('No record of a downloaded zip (run `python manage.py downloadcalaccessrawdata`).')

        # Raise exception if extract step did not finish
        if not self.version.download_completed:
            raise CommandError('Previous download did not finish (run `python manage.py downloadcalaccessrawdata`).')

        # Store extraction start time
        self.version.extract_start_datetime = now()
        # Reset the finish time
        self.version.extract_finish_datetime = None
        # Save in case the command doesn't finish
        self.version.save()

        self.header("Extracting raw data files")

        # flush tsv dir
        if os.path.exists(self.tsv_dir):
            shutil.rmtree(self.tsv_dir)
        os.mkdir(self.tsv_dir)

        self.extract_tsv_files()

        if getattr(settings, 'CALACCESS_STORE_ARCHIVE', False):
            self.archive()

        if not options['keep_files']:
            shutil.rmtree(self.download_dir)

        # store extraction finish time
        self.version.extract_finish_datetime = now()

        # and save the RawDataVersion
        self.version.save()

    def extract_tsv_files(self):
        """
        Extract all files with .TSV extension from downloaded zip.
        """
        if self.verbosity:
            self.log(" Extracting .TSV files")
        pattern = r'^.+\.TSV$'
        with zipfile.ZipFile(self.zip_path) as zf:
            tsv_files = [f for f in zf.namelist() if re.match(pattern, f)]
            for f in tsv_files:
                # extract
                extracted_path = zf.extract(f, self.download_dir)
                # move
                file_name = os.path.basename(extracted_path).upper()
                shutil.move(
                    extracted_path,
                    os.path.join(self.tsv_dir, file_name),
                )
                # track
                self.track_file(file_name)

    def track_file(self, file_name):
        """
        Create a RawDataFile object for for each download .TSV file.
        """
        raw_file, created = RawDataFile.objects.get_or_create(
            version=self.version,
            file_name=file_name.replace('.TSV', '')
        )
        # if raw file was already there, clear out timestamp fields
        if not created:
            raw_file.clean_start_datetime = None
            raw_file.clean_finish_datetime = None
            raw_file.load_start_datetime = None
            raw_file.load_finish_datetime = None
            raw_file.save()

    def archive(self):
        """
        Save a copy of the download zip file and each file inside.
        """
        if self.verbosity:
            self.log(" Archiving original files")
        if self.verbosity > 2:
            self.log(" Archiving {}".format(os.path.basename(self.zip_path)))

        for raw_file in self.version.files.all():
            if self.verbosity > 2:
                self.log(" Archiving {0}.TSV".format(raw_file.file_name))
            # Remove previous .TSV file
            raw_file.download_file_archive.delete()
            # Open up the .TSV file so we can wrap it in the Django File obj
            file_path = os.path.join(self.tsv_dir, raw_file.file_name + '.TSV')
            with open(file_path, 'rb') as f:
                # Save the .TSV on the raw data file
                raw_file.download_file_archive.save(
                    raw_file.file_name + '.TSV',
                    File(f)
                )
        return
