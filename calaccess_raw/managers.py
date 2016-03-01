#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.db import models
from calaccess_raw import get_download_directory


class CalAccessManager(models.Manager):

    def get_csv_name(self):
        return "%s.csv" % self.model._meta.db_table.lower()

    def get_csv_path(self):
        return os.path.join(
            get_download_directory(),
            'csv',
            self.get_csv_name()
        )

    def get_tsv_name(self):
        return "%s.TSV" % self.model._meta.db_table

    def get_tsv_path(self):
        return os.path.join(
            get_download_directory(),
            'tsv',
            self.get_tsv_name()
        )
