#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests the management commands that interact with the database.
"""
# Files
import io
import os

# Testing
import warnings
import requests_mock
from requests import HTTPError
from django.test import TransactionTestCase
from django.test.utils import override_settings
# from django.utils.crypto import get_random_string

# Times
from datetime import datetime
from django.utils import timezone

# Django etc.
from django.conf import settings
from calaccess_raw import get_model_list
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.management.commands.loadcalaccessrawfile import Command as LoadCommand
from calaccess_raw.management.commands.cleancalaccessrawfile import Command as CleanCommand
from calaccess_raw.management.commands.updatecalaccessrawdata import Command as UpdateCommand
from calaccess_raw.management.commands.extractcalaccessrawfiles import Command as ExtractCommand
from calaccess_raw.management.commands.downloadcalaccessrawdata import Command as DownloadCommand

# Logging
import logging
logger = logging.getLogger(__name__)


@override_settings(
    CALACCESS_DATA_DIR=os.path.join(settings.BASE_DIR, 'test-data'),
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'test-data', '.media'),
    CALACCESS_STORE_ARCHIVE=False
)
class CommandTestCase(TransactionTestCase):
    """
    Tests the management commands that interact with the database.
    """
    multi_db = True
    test_archiving = False

    @classmethod
    def setUpClass(cls):
        """
        Load data into the database before running other tests.
        """
        super(CommandTestCase, cls).setUpClass()
        with requests_mock.Mocker() as m:
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
            dcmd = DownloadCommand()
            dcmd.handle(**kwargs)

        # Now archive the download
        suffix = "-test"  # f"-test-{get_random_string()}"
        print(f"Suffix: {suffix}")
        if cls.test_archiving:
            dcmd.archive(suffix=suffix)

        # Extract the data
        ecmd = ExtractCommand()
        ecmd.handle(verbosity=3, keep_files=True)
        if cls.test_archiving:
            ecmd.archive(suffix=suffix)

        # Clean the data
        tsv_list = [f for f in os.listdir(ecmd.tsv_dir) if '.TSV' in f.upper()]
        for i, name in enumerate(tsv_list):
            ccmd = CleanCommand()
            ccmd.handle(file_name=name, verbosity=3, keep_file=True)
            # Archive every 10th one. Don't need to do them all.
            if i % 10 == 0 and cls.test_archiving:
                ccmd.archive(suffix=suffix)

        model_list = [x for x in get_model_list() if os.path.exists(x.objects.get_csv_path())]
        for model in model_list:
            lcmd = LoadCommand()
            lcmd.handle(
                model_name=model.__name__,
                csv=model.objects.get_csv_path(),
                verbosity=3,
                keep_file=True,
                app_name='calaccess_raw'
            )

        ucmd = UpdateCommand()
        ucmd.set_global_options(dict(verbosity=3, no_color=False))
        ucmd.version = ecmd.version
        if cls.test_archiving:
            ucmd.archive(suffix=suffix)

    def test_download_metadata(self):
        """
        Test the bit that downloads metadata about the latest dump.
        """
        try:
            CalAccessCommand().get_download_metadata()
        except HTTPError as e:
            warnings.warn(f"Could not verify download metadata: {e}")

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
