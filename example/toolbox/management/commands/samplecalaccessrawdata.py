import os
import shutil
from itertools import chain
from optparse import make_option
from clint.textui import progress
from subsample.file_input import FileInput
from subsample.algorithms import two_pass_sample
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw import get_download_directory, get_test_download_directory

custom_options = (
    make_option(
        "--sample-rows",
        action="store",
        dest="samplerows",
        default=1000,
        help="Number of rows to grab from each table"
    ),
)


class Command(CalAccessCommand):
    help = 'Create smaller sampled TSV files for unit tests'
    option_list = CalAccessCommand.option_list + custom_options

    def set_config(self, *args, **options):
        self.data_dir = get_download_directory()
        self.test_data_dir = get_test_download_directory()
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        self.sample_dir = os.path.join(self.test_data_dir, "tsv/")
        self.sample_rows = int(options['samplerows'])
        self.tsv_list = os.listdir(self.tsv_dir)
        self.verbosity = int(options['verbosity'])

    def handle(self, *args, **options):
        self.set_config(*args, **options)
        self.header("Sampling %i rows from %s source files" % (
            self.sample_rows,
            len(self.tsv_list),
        ))

        # Make sure sample dir exists and is empty
        os.path.exists(self.test_data_dir) or os.mkdir(self.test_data_dir)
        os.path.exists(self.sample_dir) and shutil.rmtree(self.sample_dir)
        os.mkdir(self.sample_dir)

        # Loop through all the files in the source directory
        for name in progress.bar(self.tsv_list):

            # Find the input
            file = os.path.join(self.tsv_dir, name)
            out_file = os.path.join(self.sample_dir, name)

            if self.verbosity > 2:
                self.log(" Sampling %s" % file)

            # Open the file
            fi = FileInput(file, True)

            # Generate our sample
            sample = two_pass_sample(fi, sample_size=self.sample_rows)

            # Open our output file
            out = open(out_file, 'wb')

            # Write it out
            for line in chain(fi.header, sample):
                out.write(line)
