import os
import shutil
from optparse import make_option
from calaccess_raw import get_download_directory, get_test_download_directory
from django.core.management.base import LabelCommand
from calaccess_raw.management.commands import CalAccessCommand

from subsample.algorithms import reservoir_sample, approximate_sample, two_pass_sample
from subsample.file_input import FileInput
from itertools import chain

custom_options = (
    make_option(
        "--sample-rows",
        action="store",
        dest="samplerows",
        default=1000,
        help="Number of rows to grab from each table"
    ),
)
class Command(CalAccessCommand, LabelCommand):
    help = 'Create sampled TSV files for easy test runs'
    option_list = CalAccessCommand.option_list + custom_options

    def handle(self, *args, **options):
        self.sample_rows = int(options['samplerows'])
        self.log("sample rows is %i" % self.sample_rows)

        self.data_dir       = get_download_directory()
        self.test_data_dir  = get_test_download_directory()

        self.tsv_dir        = os.path.join(self.data_dir, "tsv/")
        self.sample_dir     = os.path.join(self.test_data_dir, "tsv/")

        # make sure sample dir exists and is empty
        os.path.exists(self.test_data_dir) or os.mkdir(self.test_data_dir)
        os.path.exists(self.sample_dir) and shutil.rmtree(self.sample_dir)
        os.mkdir(self.sample_dir)

        # Loop through all the files in the source directory
        for name in os.listdir(self.tsv_dir):
            file = os.path.join(self.tsv_dir,name)
            out_file = os.path.join(self.sample_dir,name)

            self.log("Sample %s" % file)

            # open the file
            fi = FileInput(file, True)

            # generate our sample
            sample = two_pass_sample(fi, sample_size=self.sample_rows)

            # open our output file
            out = open(out_file, 'wb')

            for line in chain(fi.header, sample):
                out.write(line)
