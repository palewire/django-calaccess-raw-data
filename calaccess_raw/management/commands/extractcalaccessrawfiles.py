"""
Extract the CAL-ACCESS raw data files from downloaded ZIP.
"""
import re
import os
import shutil
import zipfile

from calaccess_raw.management.commands import CalAccessCommand


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
        self.header("Extracting raw data files")

        # flush tsv dir
        if os.path.exists(self.tsv_dir):
            shutil.rmtree(self.tsv_dir)
        os.mkdir(self.tsv_dir)

        # Do it
        self.extract_tsv_files()

        # Nuke it, unless we want to keep it
        if not options['keep_files']:
            shutil.rmtree(self.download_dir)

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
