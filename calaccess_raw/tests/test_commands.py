#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests the management commands that interact with the database.
"""
from __future__ import unicode_literals
import logging
import warnings
from requests import HTTPError
from django.test import TestCase
from calaccess_raw import get_model_list
from django.test.utils import override_settings
from django.core.management import call_command
from calaccess_raw.management.commands import CalAccessCommand
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
