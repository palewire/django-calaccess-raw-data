#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base management command that provides common functionality for the other commands in this app.
"""
import codecs
import locale
import logging
import os
import requests
import sys
from re import sub
from email.utils import parsedate_tz, mktime_tz
from datetime import datetime
from django.utils import timezone
from django.utils.termcolors import colorize
from django.core.management.base import BaseCommand
from calaccess_raw import get_data_directory
from calaccess_raw.models import RawDataVersion
logger = logging.getLogger(__name__)


class CalAccessCommand(BaseCommand):
    """
    Base management command that provides common functionality for the other commands in this app.
    """
    url = 'https://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip'

    def handle(self, *args, **options):
        """
        Sets options common to all commands.

        Any command subclassing this object should implement its own
        handle method, as is standard in Django, and run this method
        via a super call to inherit its functionality.
        """
        # Set global options
        self.verbosity = options.get("verbosity")
        self.no_color = options.get("no_color")

        # set up data directories
        self.data_dir = get_data_directory()
        self.tsv_dir = os.path.join(self.data_dir, 'tsv')
        self.csv_dir = os.path.join(self.data_dir, 'csv')

        os.path.exists(self.data_dir) or os.makedirs(self.data_dir)
        os.path.exists(self.tsv_dir) or os.makedirs(self.tsv_dir)
        os.path.exists(self.csv_dir) or os.makedirs(self.csv_dir)

        # set path where zip will be downloaded
        self.download_dir = os.path.join(self.data_dir, 'download')
        self.zip_path = os.path.join(
            self.download_dir,
            self.url.split('/')[-1]
        )

        # Start the clock
        self.start_datetime = datetime.now()

    def parse_imf_datetime_str(self, datetime_str):
        """
        Parse a string containing a datetime value in Internet Message Format.

        See Section 7.1.1.1 of RFC 7231:
        https://tools.ietf.org/html/rfc7231.html#section-7.1.1.1

        Return a utc datetime object.
        """
        datetime_tuple = parsedate_tz(datetime_str)
        timestamp = mktime_tz(datetime_tuple)
        datetime_obj = datetime.fromtimestamp(timestamp, timezone.utc)
        return datetime_obj

    def get_download_metadata(self):
        """
        Returns a dict with metadata about the current CAL-ACCESS snapshot.
        """
        response = requests.head(self.url)
        logger.debug(
            'Response status {0.status_code} ({0.reason}) from HEAD request.'.format(response)
        )
        if not response.ok:
            response.raise_for_status()
        # content length is a string, need to convert
        try:
            # long int type is big enough for double the current size of the zip
            length = long(response.headers['content-length'])
        except NameError:
            # in py3, no long(), instead int will suffice
            length = int(response.headers['content-length'])
        return {
            # should prob not call int here, can this remain a string until writing to db?
            'content-length': length,
            'last-modified': response.headers['last-modified'],
            'etag': response.headers['etag'],
            'server': response.headers['server'],
        }

    def get_or_create_version(self, expected_size, release_datetime):
        """
        Get or create a RawDataVersion.

        Create a new one only if:
        * expected_size is different from the latest version; or
        * release_datetime is five minutes later than latest_version's.

        Return a tuple of (object, created), where created is a boolean
        specifying whether an object was created.
        """
        obj = None
        try:
            latest = RawDataVersion.objects.latest('release_datetime')
        except RawDataVersion.DoesNotExist:
            obj = RawDataVersion.objects.create(
                release_datetime=release_datetime,
                expected_size=expected_size
            )
            created = True
        else:
            diff = release_datetime - latest.release_datetime
            if latest.expected_size == expected_size and diff.total_seconds() < 300:
                obj = latest
                created = False
            else:
                obj = RawDataVersion.objects.create(
                    release_datetime=release_datetime,
                    expected_size=expected_size,
                )
                created = True
        return obj, created

    #
    # Logging methods
    #

    def header(self, string):
        """
        Writes out a string to stdout formatted to look like a header.
        """
        logger.debug(string)
        if not self.no_color:
            string = colorize(string, fg="cyan", opts=("bold",))
        self.stdout.write(string)

    def log(self, string):
        """
        Writes out a string to stdout formatted to look like a standard line.
        """
        logger.debug(string)
        if not self.no_color:
            string = colorize("%s" % string, fg="white")
        self.stdout.write(string)

    def success(self, string):
        """
        Writes out a string to stdout formatted green to communicate success.
        """
        logger.debug(string)
        if not self.no_color:
            string = colorize(string, fg="green")
        self.stdout.write(string)

    def failure(self, string):
        """
        Writes out a string to stdout formatted red to communicate failure.
        """
        logger.debug(string)
        if not self.no_color:
            string = colorize(string, fg="red")
        self.stdout.write(string)

    def duration(self):
        """
        Calculates how long the command has been running and writes it to stdout.
        """
        duration = datetime.now() - self.start_datetime
        self.stdout.write('Duration: {}'.format(str(duration)))
        logger.debug('Duration: {}'.format(str(duration)))

    def confirm_proceed(self, prompt):
        """
        Prompts the user for yes/no confirmation to proceed.
        """
        # Ensure stdout can handle Unicode data: http://bit.ly/1C3l4eV
        locale_encoding = locale.getpreferredencoding()
        old_stdout = sys.stdout
        sys.stdout = codecs.getwriter(locale_encoding)(sys.stdout)

        # Send the confirmation prompt out to the user
        user_input = input(prompt)

        confirm = None

        while confirm is None:
            if user_input.lower() in ['y', 'yes']:
                confirm = True
            elif user_input.lower() in ['n', 'no']:
                confirm = False
            else:
                user_input = input("Invalid input. Please type 'yes', 'no', 'y' or 'n':\n")

        # Set things back to the way they were before continuing.
        sys.stdout = old_stdout

        # Pass back what the user typed
        return confirm

    def __str__(self):
        return sub(r'(.+\.)*', '', self.__class__.__module__)
