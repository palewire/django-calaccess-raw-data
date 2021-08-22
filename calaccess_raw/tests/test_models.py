#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the models.py files.
"""
# Testing
from django.test import TestCase

# Stuff to test
from calaccess_raw import models
from calaccess_raw.admin import BaseAdmin
from django.contrib.admin import AdminSite

# Python misc.
from copy import deepcopy
from datetime import datetime

# Logging
import logging
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

        # Tracking model methods
        models.RawDataVersion().__str__()
        models.RawDataVersion().pretty_expected_size()
        models.RawDataVersion().pretty_clean_size()
        models.RawDataVersion(expected_size=100).pretty_expected_size()
        models.RawDataVersion(clean_zip_size=100).pretty_clean_size()

        models.RawDataFile().__str__()
        models.RawDataFile().pretty_download_file_size()
        models.RawDataFile().pretty_clean_file_size()
        models.RawDataFile(download_file_size=100).pretty_download_file_size()
        models.RawDataFile(clean_file_size=100).pretty_clean_file_size()
        models.RawDataFile().model

        # Tracking model properties
        models.RawDataVersion().download_file_count
        models.RawDataVersion().clean_file_count
        models.RawDataVersion().clean_record_count

        completed_version = models.RawDataVersion(
            download_start_datetime=datetime.now(),
            download_finish_datetime=datetime.now(),
            extract_start_datetime=datetime.now(),
            extract_finish_datetime=datetime.now(),
            update_start_datetime=datetime.now(),
            update_finish_datetime=datetime.now(),
        )
        stalled_version = models.RawDataVersion(
            download_start_datetime=datetime.now(),
            extract_start_datetime=datetime.now(),
            update_start_datetime=datetime.now(),
        )
        self.assertTrue(completed_version.download_completed)
        self.assertTrue(completed_version.extract_completed)
        self.assertTrue(completed_version.update_completed)
        self.assertFalse(stalled_version.download_completed)
        self.assertFalse(stalled_version.extract_completed)
        self.assertFalse(stalled_version.update_completed)

        self.assertTrue(stalled_version.download_stalled)
        self.assertTrue(stalled_version.extract_stalled)
        self.assertTrue(stalled_version.update_stalled)
        self.assertFalse(completed_version.download_stalled)
        self.assertFalse(completed_version.extract_stalled)
        self.assertFalse(completed_version.update_stalled)

    def test_admins(self):
        """
        Text the extra methods we've added to the admins.
        """
        BaseAdmin(models.RcptCd, AdminSite()).get_readonly_fields()
