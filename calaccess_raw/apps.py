#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Configuration of the Django app.
"""
from __future__ import unicode_literals
from django.apps import AppConfig


class CalAccessRawConfig(AppConfig):
    """
    Configuration of the `calaccess_raw` Django app.
    """
    name = 'calaccess_raw'
    verbose_name = "CAL-ACCESS raw data"
