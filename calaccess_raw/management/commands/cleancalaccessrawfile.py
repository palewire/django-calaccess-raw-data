#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Clean a source CAL-ACCESS TSV file and reformat it as a CSV.
"""
import time

# Files
import os
import pandas as pd
from django.core.files import File

# Django
from django.conf import settings
from django.utils.timezone import now

# Commands
from django.core.management.base import CommandError
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.models.tracking import RawDataVersion, RawDataFile


class Command(CalAccessCommand):
    """
    Clean a source CAL-ACCESS TSV file and reformat it as a CSV.
    """
    help = 'Clean a source CAL-ACCESS TSV file and reformat it as a CSV'

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            'file_name',
            help="Name of the TSV file to be cleaned and discarded for a CSV"
        )
        parser.add_argument(
            "--keep-file",
            action="store_true",
            dest="keep_file",
            default=False,
            help="Keep original TSV file"
        )

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)

        # Set all the config options
        self.set_options(options)

        # Get the tracking object from the database
        self.raw_file = self.get_file_obj()

        if os.path.getsize(self.tsv_path):
            # Walk through the raw TSV file and create a clean CSV file
            if self.verbosity > 1:
                self.log(" Cleaning %s" % self.file_name)
            self.clean()

            # If requested, archive the files
            if getattr(settings, 'CALACCESS_STORE_ARCHIVE', False):
                self.archive()

        # Unless keeping files, remove the raw TSV file
        if not options['keep_file']:
            os.remove(self.tsv_path)

        # Store the finish time in the database
        self.raw_file.clean_finish_datetime = now()

        # Save the tracking record in the database one last time
        self.raw_file.save()

    def set_options(self, options):
        """
        Set options for use in other methods.
        """
        # Set options
        self.file_name = options['file_name']

        # Input and output paths
        self.tsv_path = os.path.join(self.tsv_dir, self.file_name)
        self.csv_name = self.file_name.lower().replace("tsv", "csv")
        self.csv_path = os.path.join(self.csv_dir, self.csv_name)

    def get_file_obj(self):
        """
        Get the file object from our tracking database table.
        """
        # Get most recently extracted RawDataVersion
        try:
            version = RawDataVersion.objects.latest_extract()
        except RawDataVersion.DoesNotExist:
            raise CommandError('No record of extracting zip (run `python manage.py extractcalaccessrawfiles`)')

        # Raise exception if extract step did not finish
        if not version.extract_completed:
            raise CommandError('Previous extraction did not finish (run `python manage.py extractcalaccessrawfiles`)')

        # Get the raw file record
        raw_file = RawDataFile.objects.get(
            file_name=self.file_name.replace('.TSV', ''),
            version=version
        )

        # store the start time for the clean
        raw_file.clean_start_datetime = now()

        # reset the finish time for the clean
        raw_file.clean_finish_datetime = None

        # Save here in case command doesn't finish
        raw_file.save()

        # Pass it back
        return raw_file

    def clean(self):
        """
        Cleans the provided source TSV file and writes it out in CSV format.
        """
        # Read in raw TSV
        df = pd.read_csv(
            self.tsv_path,
            delimiter='\t',
            dtype=str,
            on_bad_lines="skip"  # Skip bad rows
        )

        # Wrote out CSV
        df.to_csv(self.csv_path, index=False)

        # Add counts to raw_file_record
        self.raw_file.clean_columns_count = len(df.columns)
        self.raw_file.clean_records_count = len(df)

        # Add file size to the raw_file_record
        self.raw_file.download_file_size = os.path.getsize(self.tsv_path) or 0
        self.raw_file.clean_file_size = os.path.getsize(self.csv_path) or 0

        # Save it in case it crashes in the next step
        self.raw_file.save()

    def archive(self, suffix=None):
        """
        Archive the file.
        """
        if self.verbosity > 2:
            self.log(" Archiving {}".format(os.path.basename(self.csv_path)))

        identifier = "ccdc-raw-data-{dt:%Y-%m-%d_%H-%M-%S}".format(dt=self.raw_file.version.release_datetime)
        if suffix:
            identifier += suffix

        # Open up the .CSV file so we can wrap it in the Django File obj
        with open(self.csv_path, 'rb') as csv_file:
            # Save the .CSV on the raw data file
            try:
                self.raw_file.clean_file_archive.save(
                    identifier,
                    File(csv_file)
                )
            except FileExistsError:
                self.raw_file.clean_file_archive.delete()
                self.raw_file.clean_file_archive.save(
                    identifier,
                    File(csv_file)
                )
            time.sleep(.25)
