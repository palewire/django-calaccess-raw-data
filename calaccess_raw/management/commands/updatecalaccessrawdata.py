"""
Download, unzip, clean and load the latest CAL-ACCESS database ZIP.
"""
# Files
import os

# Commands
from django.core.management import call_command
from calaccess_raw.management.commands import CalAccessCommand

# Models
from calaccess_raw import get_model_list

# Logging
import logging
logger = logging.getLogger(__name__)


class Command(CalAccessCommand):
    """
    Download, unzip, clean and load the latest CAL-ACCESS database ZIP.
    """
    help = "Download, unzip, clean and load the latest CAL-ACCESS database ZIP"

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
            help="Keep zip, unzipped, TSV and CSV files"
        )

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)

        # set / compute any attributes that multiple class methods need
        self.keep_files = options["keep_files"]

        # Download
        call_command(
            "downloadcalaccessrawdata",
            verbosity=self.verbosity,
            noinput=True,
            restart=self.force_restart
        )
        if self.verbosity:
            self.duration()

        # Extract
        call_command(
            'extractcalaccessrawfiles',
            keep_files=self.keep_files
        )
        if self.verbosity:
            self.duration()

        # Clean
        self.clean()
        if self.verbosity:
            self.duration()

        # Load
        self.load()
        if self.verbosity:
            self.duration()
            self.success("Done!")

    def clean(self):
        """
        Clean up the raw data files from the state so they are ready to get loaded into the database.
        """
        if self.verbosity:
            self.header("Cleaning data files")

        tsv_list = [f for f in os.listdir(self.tsv_dir) if '.TSV' in f.upper()]

        # Loop through all the files in the source directory
        for name in tsv_list:
            call_command(
                "cleancalaccessrawfile",
                name,
                verbosity=self.verbosity,
                keep_file=self.keep_files,
            )

    def load(self):
        """
        Loads the cleaned up csv files into the database.
        """
        if self.verbosity:
            self.header("Loading data files")

        model_list = [x for x in get_model_list() if os.path.exists(x.objects.get_csv_path())]

        for model in model_list:
            call_command(
                "loadcalaccessrawfile",
                model.__name__,
                verbosity=self.verbosity,
                keep_file=self.keep_files,
                app_name=self.app_name,
            )
