#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests the adminstration panel configuration.
"""
# Testing
from django.test import TestCase

# Stuff to test
from calaccess_raw import admin
from calaccess_raw import models
from calaccess_raw import get_model_list

# Logging
import logging
logger = logging.getLogger(__name__)


class AdminTestCase(TestCase):
    """
    Tests the adminstration panel configuration.
    """
    def test_models(self):
        """
        Make sure all the models have admins.
        """
        model_list = [m.__name__ for m in get_model_list()]
        admin_list = [a.replace("Admin", "") for a in admin.__all__]
        missing = set(model_list).difference(admin_list)
        self.assertEqual(missing, set([]))

    def test_methods(self):
        """
        Make sure our custom methods work.
        """
        a = admin.CvrSoCdAdmin(models.CvrSoCd(), None)
        a.get_readonly_fields()
        a.get_list_filter({})
        a.get_search_fields({})
