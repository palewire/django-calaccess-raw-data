#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom managers for working with CAL-ACCESS data.
"""
from __future__ import unicode_literals
import os
from django.db import models, connection
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

    def add_constraints_and_indexes(self):
        """
        Re-create constraints and indexes on the model and its fields.
        """
        with connection.schema_editor() as schema_editor:
            schema_editor.alter_unique_together(
                self.model,
                (),
                self.model._meta.unique_together,
            )

            schema_editor.alter_index_together(
                self.model,
                (),
                self.model._meta.index_together,
            )

            for field in self.model.objects.constrained_fields:
                field_copy = field.__copy__()
                field_copy.db_constraint = False
                schema_editor.alter_field(
                    self.model, field_copy, field
                )

            for field in self.model.objects.indexed_fields:
                field_copy = field.__copy__()
                field_copy.db_index = False
                schema_editor.alter_field(
                    self.model, field_copy, field
                )

    def drop_constraints_and_indexes(self):
        """
        Temporarily drop constraints and indexes on the model and its fields.
        """
        with connection.schema_editor() as schema_editor:
            schema_editor.alter_unique_together(
                self.model,
                self.model._meta.unique_together,
                (),
            )

            schema_editor.alter_index_together(
                self.model,
                self.model._meta.index_together,
                (),
            )

            for field in self.model.objects.constrained_fields:
                field_copy = field.__copy__()
                field_copy.db_constraint = False
                schema_editor.alter_field(
                    self.model, field, field_copy
                )

            for field in self.model.objects.indexed_fields:
                field_copy = field.__copy__()
                field_copy.db_index = False
                schema_editor.alter_field(
                    self.model, field, field_copy
                )

    @property
    def constrained_fields(self):
        """
        Returns list of model's fields with db_constraint set to True.
        """
        return [
            f for f in self.model._meta.fields
            if hasattr(f, 'db_constraint') and f.db_constraint
        ]

    @property
    def indexed_fields(self):
        """
        Returns list of model's fields with db_index set to True.
        """
        return [
            f for f in self.model._meta.fields if f.db_index
        ]


class RawDataVersionQuerySet(models.QuerySet):
    """
    Custom methods for working with a RawDataVersion QuerySet.
    """
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

    def complete(self):
        """
        Filters down QuerySet to return only version that have a complete update.
        """
        return self.get_queryset().complete()
