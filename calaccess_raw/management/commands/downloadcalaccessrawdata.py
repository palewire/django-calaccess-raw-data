#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Download the latest CAL-ACCESS database ZIP.
"""
# Files
import os
import shutil
import requests
from hurry.filesize import size

# Strings
from django.template.loader import render_to_string
from django.contrib.humanize.templatetags.humanize import naturaltime

# Time
import time
from datetime import datetime
from django.utils import timezone

# Django stuff
from django.conf import settings
from django.core.files import File
from calaccess_raw.models.tracking import RawDataVersion

# Commands
from clint.textui import progress
from django.core.management.base import CommandError
from calaccess_raw.management.commands import CalAccessCommand

# Logging
import logging
logger = logging.getLogger(__name__)


class Command(CalAccessCommand):
    """
    Download the latest CAL-ACCESS database ZIP.
    """
    help = "Download the latest CAL-ACCESS database ZIP"

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)

        # Prep
        headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }

        # flush previous download
        if os.path.exists(self.download_dir):
            shutil.rmtree(self.download_dir)
        os.mkdir(self.download_dir)

        # Stream the download
        resp = requests.get(self.url, stream=True, headers=headers, verify=False)
        logger.debug(
            'Response status {0.status_code} ({0.reason}) from GET request.'.format(resp)
        )
        if not resp.ok:
            resp.raise_for_status()

        chunk_size = 1024
        divisor = chunk_size + 1
        n_iters = float(expected_size) / divisor

        with open(self.zip_path, 'ab') as fp:
            for chunk in progress.bar(resp.iter_content(chunk_size=chunk_size), expected_size=n_iters):
                fp.write(chunk)
                fp.flush()

        logger.debug('Download zip size: %s bytes' % os.path.getsize(self.zip_path))
