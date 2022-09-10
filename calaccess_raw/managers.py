"""
Custom managers for working with CAL-ACCESS data.
"""
import os
import calaccess_raw
from postgres_copy import CopyManager


class CalAccessManager(CopyManager):
    """
    Utilities for accessing the raw data associated with a model.
    """

    def get_csv_name(self):
        """
        Returns the name of the model's CSV data file.
        """
        return "{}.csv".format(self.model._meta.db_table.lower())

    def get_csv_path(self):
        """
        Returns the path to the model's CSV data file.
        """
        return os.path.join(
            calaccess_raw.get_data_directory(), "csv", self.get_csv_name()
        )

    def get_tsv_name(self):
        """
        Returns the name of the model's raw TSV data file.
        """
        return "{}.TSV".format(self.model._meta.db_table)

    def get_tsv_path(self):
        """
        Returns the path to the model's raw TSV data file.
        """
        return os.path.join(
            calaccess_raw.get_data_directory(), "tsv", self.get_tsv_name()
        )
