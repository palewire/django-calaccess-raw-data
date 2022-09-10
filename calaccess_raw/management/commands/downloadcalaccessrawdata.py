"""
Download the latest CAL-ACCESS database ZIP.
"""
import os
import shutil

import requests
<<<<<<< HEAD
=======
from hurry.filesize import size

# Strings
from django.template.loader import render_to_string
from django.contrib.humanize.templatetags.humanize import naturaltime

# Time
from datetime import datetime
from django.utils import timezone

# Django stuff
from calaccess_raw.models.tracking import RawDataVersion

# Commands
from clint.textui import progress
from django.core.management.base import CommandError
>>>>>>> 1e2809770c82a7f46501cd8a16bd47d5e78850f5
from calaccess_raw.management.commands import CalAccessCommand


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

        # flush previous download
        if os.path.exists(self.download_dir):
            shutil.rmtree(self.download_dir)
        os.mkdir(self.download_dir)

        # Stream the download
        self.header("Downloading ZIP file")
        headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }
        with requests.get(self.url, stream=True, headers=headers, verify=False) as r:
            r.raise_for_status()
            chunk_size = 1024
            with open(self.zip_path, 'ab') as fp:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    fp.write(chunk)
