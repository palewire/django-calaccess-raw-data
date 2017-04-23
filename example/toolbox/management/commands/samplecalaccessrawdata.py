import os
import shutil
import zipfile
from datetime import datetime
from itertools import chain
from optparse import make_option
from clint.textui import progress
from subsample.file_input import FileInput
from subsample.algorithms import two_pass_sample
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw import get_download_directory, get_test_download_directory
from calaccess_raw.models import RawDataVersion


class Command(CalAccessCommand):
    help = 'Create smaller sampled TSV files for unit tests'

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--sample-rows",
            action="store",
            dest="samplerows",
            default=1000,
            help="Number of rows to grab from each table"
        )
    
    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)

        # Set options
        self.data_dir = get_download_directory()
        self.test_data_dir = get_test_download_directory()
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        self.sample_dir = os.path.join(self.test_data_dir, "tsv/")
        self.sample_rows = int(options['samplerows'])
        self.tsv_list = os.listdir(self.tsv_dir)
        self.verbosity = int(options['verbosity'])

        self.header("Sampling %i rows from %s source files" % (
            self.sample_rows,
            len(self.tsv_list),
        ))

        # Make sure sample dir exists and is empty
        os.path.exists(self.test_data_dir) or os.makedirs(self.test_data_dir)
        os.path.exists(self.sample_dir) and shutil.rmtree(self.sample_dir)
        os.makedirs(self.sample_dir)

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
            with open(out_file, 'wb') as out:

                # Write it out
                for line in chain(fi.header, sample):
                    out.write(line)

        self.header("Compressing zip file...")
        self.save_zip()

        # Stash the release_datetime and size of the last completed download
        version = RawDataVersion.objects.latest('download_finish_datetime')

        with open(self.test_data_dir + '/sampled_version.txt', 'w') as f:
            f.write(str(version.expected_size) + '\n')
            f.write(
                version.release_datetime.strftime('%a, %d %b %Y %H:%M:%S GMT')
            )
    
    def save_zip(self):
        """
        Save a zip file containing all the sampled .TSV files
        """
        with zipfile.ZipFile(
                self.test_data_dir + "/dbwebexport.zip", 
                'w'
            ) as zf:
            for name in os.listdir(self.sample_dir):
                f = os.path.join(self.sample_dir, name)
                zf.write(f, 'CalAccess/DATA/' + name)
