#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django.conf import settings
from django.test import TestCase
from calaccess_raw import get_model_list
from django.test.utils import override_settings
from django.core.management import call_command
logger = logging.getLogger(__name__)


class CommandTestCase(TestCase):
    """
    Tests related to the management commands that update the database.
    """
    multi_db = True

    @classmethod
    def setUpClass(cls):
        """
        Load data into the database before running other tests.
        """
        super(CommandTestCase, cls).setUpClass()
        kwargs = dict(verbosity=3, test_data=True)
        if settings.DATABASES.get("alt", None):
            kwargs['database'] = 'alt'
            logger.debug("Loading into 'alt' database")
        call_command("updatecalaccessrawdata", **kwargs)

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
