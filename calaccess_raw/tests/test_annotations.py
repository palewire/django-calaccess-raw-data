#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests annotations of the data.
"""
from __future__ import unicode_literals
import os
import logging
from django.test import TestCase
from calaccess_raw import annotations
from calaccess_raw.annotations.filing_forms import get_filing_form
logger = logging.getLogger(__name__)


class AnnotationTestCase(TestCase):
    """
    Tests annotations of the data.
    """
    multi_db = True

    def test_filingform(self):
        """
        Test attributes of the FilingForm object.
        """
        ff = get_filing_form('F400')
        ff.get_models()
        ff.__str__()
        s = ff.get_section("P1")
        s.__str__()

    def test_documentcloud(self):
        """
        Test attributes of the DocumentCloud object.
        """
        dc = annotations.DocumentCloud('2753585', 1, 1)
        if os.path.exists(dc.metadata_filename):
            os.remove(dc.metadata_filename)
        dc.metadata
        dc.metadata
        dc.title
        dc.canonical_url
        dc.thumbnail_url
        dc.pdf_url
        dc.text_url
        dc.num_pages
        dc.pages
        dc.formatted_page_nums
        dc2 = annotations.DocumentCloud('2753585')
        dc2.canonical_url
        dc2.num_pages
        dc2.formatted_page_nums
        dc3 = annotations.DocumentCloud('2753585', None, 1)
        dc3.num_pages
        dc3.formatted_page_nums
        dc4 = annotations.DocumentCloud('2753585', 1, None)
        dc4.num_pages
        dc4.formatted_page_nums
