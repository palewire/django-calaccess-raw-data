#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Clean a source CAL-ACCESS TSV file and reformat it as a CSV.
"""
from __future__ import unicode_literals
from django.utils import six

# Files
import os
import csv
import csvkit
from io import StringIO
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

        # Walk through the raw TSV file and create a clean CSV file
        if self.verbosity > 2:
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

        # Set log variables
        self.log_dir = os.path.join(self.data_dir, "log/")
        self.log_name = self.file_name.lower().replace("tsv", "errors.csv")
        self.error_log_path = os.path.join(self.log_dir, self.log_name)

        # Make sure the log directory exists
        os.path.exists(self.log_dir) or os.makedirs(self.log_dir)

        # Input and output paths
        self.tsv_path = os.path.join(self.tsv_dir, self.file_name)
        self.csv_name = self.file_name.lower().replace("tsv", "csv")
        self.csv_path = os.path.join(self.csv_dir, self.csv_name)

        # Pull and clean the headers
        self.headers = self.get_headers()
        self.headers_count = len(self.headers)

    def get_headers(self):
        """
        Returns the headers from the TSV file.
        """
        with open(self.tsv_path, "rb") as tsv_file:
            tsv_reader = csvkit.reader(tsv_file, delimiter=str("\t"))
            return next(tsv_reader)

    def get_file_obj(self):
        """
        Get the file object from our tracking database table.
        """
        # get most recently extracted RawDataVersion
        try:
            version = RawDataVersion.objects.filter(
                extract_start_datetime__isnull=False
            ).latest('extract_start_datetime')
        except RawDataVersion.DoesNotExist:
            raise CommandError(
                'No record of extracting files from download zip '
                '(run `python manage.py extractcalaccessrawfiles`).'
            )

        # raise exception if extract step did not finish
        if not version.extract_completed:
            raise CommandError(
                'Previous extraction files from download zip did not finish '
                '(run `python manage.py extractcalaccessrawfiles`).'
            )

        # get the raw file record
        raw_file = RawDataFile.objects.get(
            file_name=self.file_name.replace('.TSV', ''),
            version=version
        )

        # store the start time for the clean
        raw_file.clean_start_datetime = now()

        # reset the finish time for the clean
        raw_file.clean_finish_datetime = None

        # save here in case command doesn't finish
        raw_file.save()

        # Pass it back
        return raw_file

    def clean(self):
        """
        Cleans the provided source TSV file and writes it out in CSV format.
        """
        # Up the CSV data limit
        csv.field_size_limit(1000000000)

        # Reader
        tsv_file = open(self.tsv_path, 'rb')

        # Writer
        csv_file = open(self.csv_path, 'w')
        csv_writer = csvkit.writer(csv_file)

        # Write the headers
        csv_writer.writerow(self.headers)
        # Pop them out of the source file
        next(tsv_file)

        # Get ready to log errors
        self.log_rows = []

        # Loop through the rest of the rows
        line_number = 1
        for tsv_line in tsv_file:
            line_number += 1
            # Log empty lines, then skip
            if (
                tsv_line.decode("ascii", "replace") == '\n' or
                tsv_line.decode("ascii", "replace") == '\r\n'
            ):
                if self.verbosity > 2:
                    msg = '  Line {} is empty'.format(line_number)
                    self.failure(msg)
                continue

            # Goofing around with the encoding while we're in there.
            tsv_line = tsv_line.decode("ascii", "replace")
            if six.PY2:
                tsv_line = tsv_line.replace('\ufffd', '?')

            # Nuke any null bytes
            null_bytes = tsv_line.count('\x00')
            if null_bytes:
                tsv_line = tsv_line.replace('\x00', ' ')

            # Nuke ASCII 26 char, the "substitute character"
            # or chr(26) in python
            sub_char = tsv_line.count('\x1a')
            if sub_char:
                tsv_line = tsv_line.replace('\x1a', '')

            # Remove any extra newline chars
            tsv_line = tsv_line.replace("\r\n", "").replace("\r", "").replace("\n", "")

            # Split on tabs so we can later spit it back out as CSV
            csv_field_list = tsv_line.split("\t")

            # Check if our values line up with our headers
            # and if not, see if CSVkit can sort out the problems
            if not len(csv_field_list) == self.headers_count:
                line_io = StringIO(tsv_line)
                line_reader = csvkit.reader(line_io, delimiter=str('\t'))
                csv_field_list = next(line_reader)

                if not len(csv_field_list) == self.headers_count:
                    if self.verbosity > 2:
                        msg = '  Bad parse of line {} ({} headers, {} values)'
                        self.failure(msg.format(line_number, self.headers_count, len(csv_field_list)))
                    self.log_rows.append([
                        line_number,
                        self.headers_count,
                        len(csv_field_list),
                        ','.join(csv_field_list)
                    ])
                    continue

            # Write out the row
            csv_writer.writerow(csv_field_list)

        # Log errors if there are any
        if self.log_rows:
            # Log to the terminal
            if self.verbosity > 1:
                msg = '  %s errors logged (not including empty lines)'
                self.failure(msg % (len(self.log_rows)))
            # Log to the file
            with open(self.error_log_path, 'w') as log_file:
                log_writer = csvkit.writer(log_file, quoting=csv.QUOTE_ALL)
                log_writer.writerow(['line', 'headers', 'fields', 'value'])
                log_writer.writerows(self.log_rows)

        # Add counts to raw_file_record
        self.raw_file.download_columns_count = self.headers_count
        self.raw_file.download_records_count = line_number - 1
        self.raw_file.clean_columns_count = self.headers_count
        self.raw_file.clean_records_count = line_number - 1 - len(self.log_rows)
        self.raw_file.error_count = len(self.log_rows)

        # Shut it down
        tsv_file.close()
        csv_file.close()

        # Add file size to the raw_file_record
        self.raw_file.download_file_size = os.path.getsize(self.tsv_path) or 0
        self.raw_file.clean_file_size = os.path.getsize(self.csv_path) or 0

    def archive(self):
        """
        Archive the file.
        """
        if self.verbosity > 2:
            self.log(" Archiving {0}".format(os.path.basename(self.csv_path)))

        # Remove previous .CSV and error log files
        self.raw_file.clean_file_archive.delete()
        self.raw_file.error_log_archive.delete()

        # Open up the .CSV file so we can wrap it in the Django File obj
        with open(self.csv_path, 'rb') as csv_file:
            # Save the .CSV on the raw data file
            self.raw_file.clean_file_archive.save(
                self.file_name.lower().replace("tsv", "csv"),
                File(csv_file),
            )
        # if there are any errors, archive the log too
        if self.log_rows:
            error_log_name = os.path.basename(self.error_log_path)
            if self.verbosity > 2:
                self.log(" Archiving {}".format(error_log_name))
            with open(self.error_log_path, 'rb') as error_file:
                self.raw_file.error_log_archive.save(error_log_name, File(error_file))
