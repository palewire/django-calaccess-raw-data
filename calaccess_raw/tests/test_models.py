#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django.test import TestCase
from calaccess_raw import models
logger = logging.getLogger(__name__)


class CommandTestCase(TestCase):
    """
    Tests related to the database models.
    """
    multi_db = True

    def test_model_methods(self):
        """
        Test the extra methods we've added to models.
        """
        models.RawDataVersion().__str__()
        models.RawDataVersion().pretty_size()
        models.RawDataVersion(size=1000).pretty_size()
        models.RawDataFile().__str__()
        models.RawDataCommand().__str__()
