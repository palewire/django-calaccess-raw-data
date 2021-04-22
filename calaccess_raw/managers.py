#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom managers for working with CAL-ACCESS data.
"""
import os
import calaccess_raw
from django.db import models
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
            calaccess_raw.get_data_directory(),
            'csv',
            self.get_csv_name()
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
            calaccess_raw.get_data_directory(),
            'tsv',
            self.get_tsv_name()
        )


class RawDataVersionQuerySet(models.QuerySet):
    """
    Custom methods for working with a RawDataVersion QuerySet.
    """
    def latest_download(self):
        """
        Returns the most recently completed download.
        """
        return self.filter(download_start_datetime__isnull=False).latest('download_start_datetime')

    def latest_extract(self):
        """
        Returns the most recently extracted download.
        """
        return self.filter(extract_start_datetime__isnull=False).latest('extract_start_datetime')

    def complete(self):
        """
        Filters down QuerySet to return only version that have a complete update.
        """
        return self.exclude(update_finish_datetime__isnull=True)


class RawDataVersionManager(models.Manager):
    """
    Custom methods for working with the RawDataVersion model.
    """
    def get_queryset(self):
        """
        Returns the custom QuerySet we want for this manager.
        """
        return RawDataVersionQuerySet(self.model, using=self._db)

    def latest_download(self):
        """
        Returns the most recently completed download.
        """
        return self.get_queryset().latest_download()

    def latest_extract(self):
        """
        Returns the most recently extracted download.
        """
        return self.get_queryset().latest_extract()

    def complete(self):
        """
        Filters down QuerySet to return only version that have a complete update.
        """
        return self.get_queryset().complete()
