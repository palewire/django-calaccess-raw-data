#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Clean a source CAL-ACCESS TSV file and reformat it as a CSV.
"""
from __future__ import unicode_literals
import os
import csv
from io import StringIO
from django.conf import settings
from django.core.files import File
from django.core.management.base import CommandError
from django.utils import six
from django.utils.timezone import now
from csvkit import CSVKitReader, CSVKitWriter
from calaccess_raw import get_download_directory
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

        # Set options
        self.file_name = options['file_name']
        self.data_dir = get_download_directory()
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        self.csv_dir = os.path.join(self.data_dir, "csv/")
        self.log_dir = os.path.join(self.data_dir, "log/")
        self.error_log_path = os.path.join(
            self.log_dir,
            self.file_name.lower().replace("tsv", "errors.csv")
        )

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
        self.raw_file = RawDataFile.objects.get(
            file_name=self.file_name.replace('.TSV', ''), version=version
        )
        # store the start time for the clean
        self.raw_file.clean_start_datetime = now()
        # reset the finish time for the clean
        self.raw_file.clean_finish_datetime = None
        # save here in case command doesn't finish
        self.raw_file.save()

        if self.verbosity > 2:
            self.log(" Cleaning %s" % self.file_name)

        self.clean()

        # unless keeping files, remove tsv files
        if not options['keep_file']:
            os.remove(os.path.join(self.tsv_dir, options['file_name']))

        # store the finish time for the clean
        self.raw_file.clean_finish_datetime = now()
        # and save the RawDataFile
        self.raw_file.save()

    def clean(self):
        """
        Cleans the provided source TSV file and writes it out in CSV format.
        """
        # Up the CSV data limit
        csv.field_size_limit(1000000000)

        # Input and output paths
        tsv_path = os.path.join(self.tsv_dir, self.file_name)
        csv_path = os.path.join(
            self.csv_dir,
            self.file_name.lower().replace("tsv", "csv")
        )

        # Reader
        tsv_file = open(tsv_path, 'rbU')

        # Writer
        csv_file = open(csv_path, 'w')
        csv_writer = CSVKitWriter(csv_file)

        # Pull and clean the headers
        try:
            headers = tsv_file.readline()
        except StopIteration:
            return
        headers = headers.decode("ascii", "replace")
        headers_csv = CSVKitReader(StringIO(headers), delimiter=str('\t'))
        try:
            headers_list = next(headers_csv)
        except StopIteration:
            return
        headers_count = len(headers_list)
        csv_writer.writerow(headers_list)

        log_rows = []

        # Loop through the rest of the data
        line_number = 1
        for tsv_line in tsv_file:
            line_number += 1
            # Log empty lines, then skip
            if (
                tsv_line.decode("ascii", "replace") == '\n' or
                tsv_line.decode("ascii", "replace") == '\r\n'
            ):
                if self.verbosity > 2:
                    msg = '  Line %s is empty'
                    self.failure(msg % (
                        line_number,
                    ))
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
            if not len(csv_field_list) == headers_count:
                csv_field_list = next(CSVKitReader(
                    StringIO(tsv_line),
                    delimiter=str('\t')
                ))

                if not len(csv_field_list) == headers_count:
                    if self.verbosity > 2:
                        msg = '  Bad parse of line %s (%s headers, %s values)'
                        self.failure(msg % (
                            line_number,
                            len(headers_list),
                            len(csv_field_list)
                        ))
                    log_rows.append([
                        line_number,
                        len(headers_list),
                        len(csv_field_list),
                        ','.join(csv_field_list)
                    ])
                    continue

            # Write out the row
            csv_writer.writerow(csv_field_list)

        # Log errors if there are any
        if log_rows:
            if self.verbosity > 1:
                msg = '  %s errors logged (not including empty lines)'
                self.failure(msg % (len(log_rows)))
            self.log_errors(log_rows)

        # Add counts to raw_file_record
        self.raw_file.download_columns_count = headers_count
        self.raw_file.download_records_count = line_number - 1
        self.raw_file.clean_columns_count = headers_count
        self.raw_file.clean_records_count = line_number - 1 - len(log_rows)
        self.raw_file.error_count = len(log_rows)

        # Shut it down
        tsv_file.close()
        csv_file.close()

        # Add file size to the raw_file_record
        self.raw_file.download_file_size = os.path.getsize(tsv_path) or 0
        self.raw_file.clean_file_size = os.path.getsize(csv_path) or 0

        if getattr(settings, 'CALACCESS_STORE_ARCHIVE', False):
            if self.verbosity > 2:
                self.log(" Archiving {0}".format(os.path.basename(csv_path)))
            # Remove previous .CSV and error log files
            self.raw_file.clean_file_archive.delete()
            self.raw_file.error_log_archive.delete()

            # Open up the .CSV file so we can wrap it in the Django File obj
            with open(csv_path, 'rb') as csv_file:
                # Save the .CSV on the raw data file
                self.raw_file.clean_file_archive.save(
                    self.file_name.lower().replace("tsv", "csv"),
                    File(csv_file),
                )
            # if there are any errors, archive the log too
            if log_rows:
                if self.verbosity > 2:
                    self.log(" Archiving {0}".format(
                        os.path.basename(self.error_log_path)
                    ))
                with open(self.error_log_path, 'rb') as error_file:
                    self.raw_file.error_log_archive.save(
                        os.path.basename(self.error_log_path),
                        File(error_file),
                    )

    def log_errors(self, rows):
        """
        Log any errors to a CSV file.
        """
        # Make sure the log directory exists
        os.path.exists(self.log_dir) or os.makedirs(self.log_dir)

        # Log writer
        log_file = open(self.error_log_path, 'w')
        log_writer = CSVKitWriter(log_file, quoting=csv.QUOTE_ALL)

        # Add the headers
        log_writer.writerow([
            'Line number',
            'Headers len',
            'Fields len',
            'Line value'
        ])

        # Log out the rows
        log_writer.writerows(rows)

        # Shut it down
        log_file.close()
