from __future__ import unicode_literals
import os
import csv
from io import StringIO
import six
from csvkit import CSVKitReader, CSVKitWriter
from calaccess_raw import get_download_directory
from django.core.management.base import LabelCommand
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand, LabelCommand):
    help = 'Clean a source CAL-ACCESS file and reformat it as a CSV'
    args = '<file path>'

    def handle_label(self, label, **options):
        # Set options
        self.verbosity = options.get("verbosity")
        self.data_dir = get_download_directory()
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        self.csv_dir = os.path.join(self.data_dir, "csv/")
        self.log_dir = os.path.join(self.data_dir, "log/")
        # Do it
        self.clean(label)

    def clean(self, name):
        """
        Cleans the provided source TSV file and writes it out in CSV format
        """
        if self.verbosity:
            self.log(" Cleaning %s" % name)

        # Up the CSV data limit
        csv.field_size_limit(1000000000)

        # Input and output paths
        tsv_path = os.path.join(self.tsv_dir, name)
        csv_path = os.path.join(
            self.csv_dir,
            name.lower().replace("tsv", "csv")
        )

        # Writer
        csv_file = open(csv_path, 'w')
        csv_writer = CSVKitWriter(csv_file, quoting=csv.QUOTE_ALL)

        # Reader
        tsv_file = open(tsv_path, 'rb')

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

        has_errors = False
        log_rows = [[
            'Line number',
            'Headers len',
            'Fields len',
            'Line value'
        ]]
        # Loop through the rest of the data
        line_number = 1
        for tsv_line in tsv_file:

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

            # Split on tabs so we can later spit it back out as CSV
            # and remove extra newlines while we are there.
            csv_field_list = tsv_line.replace("\r\n", "").split("\t")

            # Check if our values line up with our headers
            # and if not, see if CSVkit can sort out the problems
            if not len(csv_field_list) == headers_count:
                csv_field_list = next(CSVKitReader(
                    StringIO(tsv_line),
                    delimiter=str('\t')
                ))
                if not len(csv_field_list) == headers_count:
                    if self.verbosity:
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
                        has_errors = True
                        continue

            # Write out the row
            csv_writer.writerow(csv_field_list)
            line_number += 1
        # Log errors if there are any
        if has_errors is True:
            msg = '%s had %s errors'
            self.failure(msg % (
                name,
                len(log_rows) - 1
            ))
            self.log_errors(name, log_rows)
        # Shut it down
        tsv_file.close()
        csv_file.close()

    def log_errors(self, name, rows):
        """
        Log any errors to a csv file
        """
        # Log writer
        try:
            os.makedirs(self.log_dir)  # Try to make sure log_dir exists
        except OSError:
            pass
        log_path = os.path.join(
            self.log_dir,
            name.lower().replace("tsv", "errors.csv")
        )
        log_file = open(log_path, 'w')
        log_writer = CSVKitWriter(log_file, quoting=csv.QUOTE_ALL)
        log_writer.writerows(rows)
        log_file.close()
