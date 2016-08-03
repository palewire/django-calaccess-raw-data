#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the models.py files.
"""
from __future__ import unicode_literals
import logging
from copy import deepcopy
from django.test import TestCase
from calaccess_raw import models
from calaccess_raw.admin import BaseAdmin
from django.contrib.admin import AdminSite
logger = logging.getLogger(__name__)


class ModelTestCase(TestCase):
    """
    Tests related to the database models.
    """
    multi_db = True

    def test_model_methods(self):
        """
        Test the extra methods we've added to models.
        """
        # CAL-ACCESS models
        m = models.RcptCd()
        m.__str__()
        m.doc()
        m.__doc__ = "RcptCd"
        m.doc()
        m.db_table
        m.klass
        m.get_tsv_name()
        m.get_tsv_path()
        m.get_unique_key_list()
        m.get_documentcloud_pages()
        m.get_filing_forms_w_sections()
        unique_key = deepcopy(models.RcptCd.UNIQUE_KEY)
        models.RcptCd.UNIQUE_KEY = None
        models.RcptCd().get_unique_key_list()
        models.RcptCd.UNIQUE_KEY = unique_key

        # Our tracking models
        models.RawDataVersion().__str__()
        models.RawDataVersion().pretty_download_size()
        models.RawDataVersion().pretty_clean_size()
        models.RawDataFile().__str__()

    def test_admins(self):
        """
        Text the extra methods we've added to the admins.
        """
        BaseAdmin(models.RcptCd, AdminSite()).get_readonly_fields()
