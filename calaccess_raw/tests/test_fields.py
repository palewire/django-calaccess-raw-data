#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for custom database fields.
"""
# Testing
from django.test import TestCase

# Stuff to test
from calaccess_raw import fields
from calaccess_raw import models

# Logging
import logging
logger = logging.getLogger(__name__)


class FieldTestCase(TestCase):
    """
    Tests related to our custom database fields.
    """
    multi_db = True

    def test_fields(self):
        """
        Creates the fields and tests their attributes.
        """
        f = fields.CharField(help_text="foo")
        self.assertEqual(f.definition(), "Foo")
        f2 = fields.CharField()
        self.assertEqual(f2.definition(), "")

        m = models.CvrCampaignDisclosureCd()
        f3 = m.get_field_list()[1]
        f3.is_unique_key()
        f4 = m.get_field_list()[2]
        f4.is_unique_key()
        f4.description()

        m2 = models.FilerToFilerTypeCd()
        f5 = m2.get_field_list()[2]
        f5.copy_type
        f5.copy_template
        f5.description()
