"""Test commands."""
# Files
import io
import os

# Testing
import requests_mock
from django.test import TransactionTestCase
from django.test.utils import override_settings

# Django etc.
from django.conf import settings
from calaccess_raw import get_model_list
from calaccess_raw.management.commands.loadcalaccessrawfile import (
    Command as LoadCommand,
)
from calaccess_raw.management.commands.cleancalaccessrawfile import (
    Command as CleanCommand,
)
from calaccess_raw.management.commands.extractcalaccessrawfiles import (
    Command as ExtractCommand,
)
from calaccess_raw.management.commands.downloadcalaccessrawdata import (
    Command as DownloadCommand,
)

# Logging
import logging

logger = logging.getLogger(__name__)


@override_settings(
    CALACCESS_DATA_DIR=os.path.join(settings.BASE_DIR, "test-data"),
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, "test-data", ".media"),
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
                "dbwebexport.zip",
            )
            headers = {
                "Content-Length": str(os.stat(test_zip_path).st_size),
                "Accept-Ranges": "bytes",
                "Last-Modified": "Mon, 11 Jul 2017 11:20:31 GMT",
                "Connection": "keep-alive",
                "Date": "Mon, 10 Jul 2017 21:25:40 GMT",
                "Content-Type": "application/zip",
                "ETag": "2320c8-30619331-c54f7dc0",
                "Server": "Apache/2.2.3 (Red Hat)",
            }
            m.register_uri(
                "HEAD",
                "https://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip",
                headers=headers,
            )
            m.register_uri(
                "GET",
                "https://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip",
                headers=headers,
                content=io.open(test_zip_path, mode="rb").read(),
            )
            kwargs = dict(verbosity=3)
            dcmd = DownloadCommand()
            dcmd.handle(**kwargs)

        # Now archive the download
        suffix = "-test"  # f"-test-{get_random_string()}"
        print(f"Suffix: {suffix}")

        # Extract the data
        ecmd = ExtractCommand()
        ecmd.handle(verbosity=3, keep_files=True)

        # Clean the data
        tsv_list = [f for f in os.listdir(ecmd.tsv_dir) if ".TSV" in f.upper()]
        for i, name in enumerate(tsv_list):
            ccmd = CleanCommand()
            ccmd.handle(file_name=name, verbosity=3, keep_file=True)

        model_list = [
            x for x in get_model_list() if os.path.exists(x.objects.get_csv_path())
        ]
        for model in model_list:
            lcmd = LoadCommand()
            lcmd.handle(
                model_name=model.__name__,
                csv=model.objects.get_csv_path(),
                verbosity=3,
                keep_file=True,
            )

    def test_csv_gettrs(self):
        """
        Verify that get_csv_name methods work for all models.
        """
        for m in get_model_list():
            self.assertEqual(m.objects.get_csv_name(), m().get_csv_name())
            self.assertEqual(m.objects.get_csv_path(), m().get_csv_path())
