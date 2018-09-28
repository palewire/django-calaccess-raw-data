#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests the management commands that interact with the database.
"""
from __future__ import unicode_literals

# Files
import io
import os

# Testing
import warnings
import requests_mock
from requests import HTTPError
from django.test import TransactionTestCase
from django.test.utils import override_settings

# Times
from datetime import datetime
from django.utils import timezone

# Django etc.
from django.conf import settings
from calaccess_raw import get_model_list
from django.core.management import call_command
from calaccess_raw.management.commands import CalAccessCommand

# Logging
import logging
logger = logging.getLogger(__name__)


@override_settings(
    CALACCESS_DATA_DIR=os.path.join(settings.BASE_DIR, 'test-data'),
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'test-data', '.media'),
    CALACCESS_STORE_ARCHIVE=True
)
class CommandTestCase(TransactionTestCase):
    """
    Tests the management commands that interact with the database.
    """
    multi_db = True

    @classmethod
    @requests_mock.Mocker()
    def setUpClass(cls, m):
        """
        Load data into the database before running other tests.
        """
        super(CommandTestCase, cls).setUpClass()
        test_zip_path = os.path.join(
            settings.BASE_DIR,
            settings.CALACCESS_DATA_DIR,
            'dbwebexport.zip',
        )
        headers = {
            'Content-Length': str(os.stat(test_zip_path).st_size),
            'Accept-Ranges': 'bytes',
            'Last-Modified': 'Mon, 11 Jul 2017 11:20:31 GMT',
            'Connection': 'keep-alive',
            'Date': 'Mon, 10 Jul 2017 21:25:40 GMT',
            'Content-Type': 'application/zip',
            'ETag': '2320c8-30619331-c54f7dc0',
            'Server': 'Apache/2.2.3 (Red Hat)',
        }
        m.register_uri(
            'HEAD',
            'https://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip',
            headers=headers,
        )
        m.register_uri(
            'GET',
            'https://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip',
            headers=headers,
            content=io.open(test_zip_path, mode='rb').read(),
        )
        kwargs = dict(verbosity=3, noinput=True)
        call_command("updatecalaccessrawdata", **kwargs)

    def test_download_metadata(self):
        """
        Test the bit that downloads metadata about the latest dump.
        """
        try:
            CalAccessCommand().get_download_metadata()
        except HTTPError as e:
            warnings.warn("Could not verify download metadata: %s".format(e))

    def test_csv_gettrs(self):
        """
        Verify that get_csv_name methods work for all models.
        """
        for m in get_model_list():
            self.assertEqual(m.objects.get_csv_name(), m().get_csv_name())
            self.assertEqual(m.objects.get_csv_path(), m().get_csv_path())


class DifferentFileSizesTestCase(TransactionTestCase):
    """
    Test case when file size on CAL-ACCESS server and latest RawDataVersion differ.

    A new RawDataVersion should be created, even though last-modified from HEAD
    response and release_datetime from latest RawDataVersion are similar.
    """
    fixtures = ['raw_data_versions.json']

    def test_command(self):
        """Confirm that an existing RawDataVersion is returned."""
        version, created = CalAccessCommand().get_or_create_version(
            805713743,
            datetime(2017, 4, 19, 11, 24, 29, 0, timezone.utc)
        )
        self.assertNotEqual(version.id, 1)
        self.assertTrue(created)


class DifferentReleaseDatetimesTestCase(TransactionTestCase):
    """
    Test case when release datetimes on CAL-ACCESS server and latest RawDataVersion differ.

    A new RawDataVersion should be created, even though content-length from HEAD
    response and expected_size from latest RawDataVersion are equal.
    """
    fixtures = ['raw_data_versions.json']

    def test_command(self):
        """Confirm that a new RawDataVersion is created."""
        version, created = CalAccessCommand().get_or_create_version(
            805713742,
            datetime(2017, 4, 19, 11, 26, 29, 0, timezone.utc)
        )
        self.assertNotEqual(version.id, 1)
        self.assertTrue(created)


class SimilarReleaseDatetimesTestCase(TransactionTestCase):
    """
    Test case when release datetimes on CAL-ACCESS server and latest RawDataVersion are similar.

    Confirm that the lastest RawDataVersion is returned.
    """
    fixtures = ['raw_data_versions.json']

    def test_command(self):
        """Confirm that an existing RawDataVersion is returned."""
        version, created = CalAccessCommand().get_or_create_version(
            805713742,
            datetime(2017, 4, 19, 11, 23, 29, 0, timezone.utc)
        )
        self.assertEqual(version.id, 1)
        self.assertFalse(created)
