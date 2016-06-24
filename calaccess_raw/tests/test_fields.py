#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from calaccess_raw import fields
from django.test import TestCase
logger = logging.getLogger(__name__)


class FieldTestCase(TestCase):
    """
    Tests related to our custom database fields.
    """
    multi_db = True
    
    def test_fields(self):
        f = fields.CharField(help_text="foo")
        self.assertEqual(f.definition(), "Foo")
        f2 = fields.CharField()
        self.assertEqual(f2.definition(), "")

