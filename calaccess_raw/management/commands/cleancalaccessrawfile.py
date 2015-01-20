import os
import csv
from cStringIO import StringIO
from csvkit import CSVKitReader
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
        csv_file = open(csv_path, 'wb')
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Reader
        tsv_file = open(tsv_path, 'rb')

        # Pull and clean the headers
        try:
            headers = tsv_file.next()
        except StopIteration:
            return
        headers = headers.decode("ascii", "replace").encode('utf-8')
        headers_csv = CSVKitReader(StringIO(headers), delimiter='\t')
        headers_list = headers_csv.next()
        headers_count = len(headers_list)
        csv_writer.writerow(headers_list)

        # Loop through the rest of the data
        line_number = 1
        for tsv_line in tsv_file:

            # Nuke any null bytes
            null_bytes = tsv_line.count('\x00')
            if null_bytes:
                tsv_line = tsv_line.replace('\x00', ' ')

            # Nuke ASCII 26 char, the "substitute character"
            # or chr(26) in python
            sub_char = tsv_line.count('\x1a')
            if sub_char:
                tsv_line = tsv_line.replace('\x1a', '')

            # Goofing around with the encoding while we're in there.
            tsv_line = tsv_line.decode("ascii", "replace").encode('utf-8')

            # Split on tabs so we can later spit it back out as CSV
            # and remove extra newlines while we are there.
            csv_field_list = tsv_line.replace("\r\n", "").split("\t")

            # Check if our values line up with our headers
            # and if not, see if CSVkit can sort out the problems
            if not len(csv_field_list) == headers_count:
                csv_field_list = CSVKitReader(
                    StringIO(tsv_line),
                    delimiter='\t'
                ).next()
                if not len(csv_field_list) == headers_count:
                    if self.verbosity:
                        msg = '  Bad parse of line %s (%s headers, %s values)'
                        self.failure(msg % (
                            line_number,
                            len(headers_list),
                            len(csv_field_list)
                        ))
                        continue

            # Write out the row
            csv_writer.writerow(csv_field_list)
            line_number += 1

        # Shut it down
        tsv_file.close()
        csv_file.close()
