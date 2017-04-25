#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests the management commands that interact with the database.
"""
from __future__ import unicode_literals
import logging
import warnings
from requests import HTTPError
from datetime import datetime
from django.utils import timezone
from django.core.management import call_command
from django.test import TestCase
from django.test.utils import override_settings
from calaccess_raw import get_model_list
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.models import RawDataVersion
logger = logging.getLogger(__name__)


class CommandTestCase(TestCase):
    """
    Tests the management commands that interact with the database.
    """
    multi_db = True

    @classmethod
    def setUpClass(cls):
        """
        Load data into the database before running other tests.
        """
        super(CommandTestCase, cls).setUpClass()
        kwargs = dict(verbosity=3, test_data=True, noinput=True)
        call_command("updatecalaccessrawdata", **kwargs)

    def test_download_metadata(self):
        """
        Test the bit that downloads metadata about the latest dump.
        """
        try:
            CalAccessCommand().get_download_metadata()
        except HTTPError as e:
            warnings.warn(
                "Could not verify download metadata: %s".format(e)
            )

    @override_settings(BASE_DIR='example/')
    def test_csv_gettrs(self):
        """
        Verify that get_csv_name methods work for all models.
        """
        for m in get_model_list():
            self.assertEqual(m.objects.get_csv_name(), m().get_csv_name())
            self.assertEqual(m.objects.get_csv_path(), m().get_csv_path())

    def test_verifycalacessrawfile(self):
        """
        Test that verifycalaccessrawfile management command is working.
        """
        call_command("verifycalaccessrawfile", 'RcptCd')
        call_command("verifycalaccessrawfile", 'AcronymsCd')

    def test_totalcalacessrawdata(self):
        """
        Test that totalcalaccessrawdata management command is working.
        """
        call_command("totalcalaccessrawdata")


class DifferentFileSizesTestCase(TestCase):
    """
    Test case when file size on CAL-ACCESS server and latest RawDataVersion differ.

    A new RawDataVersion should be created, even though last-modified from HEAD
    response and release_datetime from latest RawDataVersion are similar.
    """
    fixtures = ['raw_data_versions.json']

    def test(self):
        """Confirm that an existing RawDataVersion is returned."""
        version, created = CalAccessCommand().get_or_create_version(
            805713743,
            datetime(2017, 4, 19, 11, 24, 29, 0, timezone.utc)
        )
        self.assertNotEqual(version.id, 1)
        self.assertTrue(created)


class DifferentReleaseDatetimesTestCase(TestCase):
    """
    Test case when release datetimes on CAL-ACCESS server and latest RawDataVersion differ.

    A new RawDataVersion should be created, even though content-length from HEAD
    response and expected_size from latest RawDataVersion are equal.
    """
    fixtures = ['raw_data_versions.json']

    def test(self):
        """Confirm that a new RawDataVersion is created."""
        version, created = CalAccessCommand().get_or_create_version(
            805713742,
            datetime(2017, 4, 19, 11, 26, 29, 0, timezone.utc)
        )
        self.assertNotEqual(version.id, 1)
        self.assertTrue(created)


class SimilarReleaseDatetimesTestCase(TestCase):
    """
    Test case when release datetimes on CAL-ACCESS server and latest RawDataVersion are similar.

    Confirm that the lastest RawDataVersion is returned.
    """
    fixtures = ['raw_data_versions.json']
    
    def test(self):
        """Confirm that an existing RawDataVersion is returned."""
        version, created = CalAccessCommand().get_or_create_version(
            805713742,
            datetime(2017, 4, 19, 11, 23, 29, 0, timezone.utc)
        )
        self.assertEqual(version.id, 1)
        self.assertFalse(created)
