#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom managers for working with CAL-ACCESS data.
"""
from __future__ import unicode_literals
import os
from django.db import models
from calaccess_raw import get_download_directory


class CalAccessManager(models.Manager):
    """
    Utilities for accessing the raw data associated with a model.
    """
    def get_csv_name(self):
        """
        Returns the name of the model's CSV data file.
        """
        return "%s.csv" % self.model._meta.db_table.lower()

    def get_csv_path(self):
        """
        Returns the path to the model's CSV data file.
        """
        return os.path.join(
            get_download_directory(),
            'csv',
            self.get_csv_name()
        )

    def get_tsv_name(self):
        """
        Returns the name of the model's raw TSV data file.
        """
        return "%s.TSV" % self.model._meta.db_table

    def get_tsv_path(self):
        """
        Returns the path to the model's raw TSV data file.
        """
        return os.path.join(
            get_download_directory(),
            'tsv',
            self.get_tsv_name()
        )
