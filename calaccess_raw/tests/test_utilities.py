#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import calaccess_raw
from datetime import datetime
from calaccess_raw import models
from django.test import TestCase
from django.test.utils import override_settings
logger = logging.getLogger(__name__)


class UtilityTestCase(TestCase):
    """
    Tests related to our hodgepodge of utilities.
    """
    multi_db = True

    @override_settings(CALACCESS_DOWNLOAD_DIR=None)
    @override_settings(CALACCESS_TEST_DOWNLOAD_DIR=None)
    @override_settings(BASE_DIR=None)
    def test_dir_errors(self):
        with self.assertRaises(ValueError):
            calaccess_raw.get_download_directory()

    @override_settings(CALACCESS_DOWNLOAD_DIR=None)
    @override_settings(CALACCESS_TEST_DOWNLOAD_DIR=None)
    @override_settings(BASE_DIR=None)
    def test_testdir_errors(self):
        with self.assertRaises(ValueError):
            calaccess_raw.get_test_download_directory()

    @override_settings(CALACCESS_DOWNLOAD_DIR="/foo/bar/")
    @override_settings(CALACCESS_TEST_DOWNLOAD_DIR="/foo/bar/tests/")
    def test_dir_configured(self):
        """
        Tests for directory functions __init__.py file
        """
        calaccess_raw.get_download_directory()
        calaccess_raw.get_test_download_directory()

    @override_settings(CALACCESS_DOWNLOAD_DIR=None)
    @override_settings(CALACCESS_TEST_DOWNLOAD_DIR=None)
    @override_settings(BASE_DIR="/foo/bar/")
    def test_dir_basedir(self):
        """
        Tests for directory functions __init__.py file
        """
        calaccess_raw.get_download_directory()
        calaccess_raw.get_test_download_directory()

    def test_model_methods(self):
        """
        Test the methods that hook up with our models
        """
        version = models.RawDataVersion(release_datetime=datetime.now())
        calaccess_raw.archive_directory_path(version, 'foobar.csv')
        datafile = models.RawDataFile(version=version)
        calaccess_raw.archive_directory_path(datafile, 'foobar.csv')
        with self.assertRaises(TypeError):
            calaccess_raw.archive_directory_path(
                models.RcptCd(),
                'foobar.csv'
            )
        calaccess_raw.get_model_list()
