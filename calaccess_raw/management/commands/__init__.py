#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from re import sub
from datetime import datetime
from dateutil.parser import parse as datetime_parse
import requests
from django.utils.termcolors import colorize
from django.core.management.base import BaseCommand


class CalAccessCommand(BaseCommand):
    """
    A base management command that provides common functionality
    for the other commands in this application.
    """
    url = 'http://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip'

    def handle(self, *args, **options):
        """
        Sets options common to all commands.

        Any command subclassing this object should implement its own
        handle method, as is standard in Django, and run this method
        via a super call to inherit its functionality.
        """
        self.verbosity = options.get("verbosity")
        self.no_color = options.get("no_color")

        self.start_datetime = datetime.now()

        # TODO: see if there's another way to identify caller
        # in (edge) case when update is not called from command line
        # if called from command line
        if self._called_from_command_line:
            # use the arg passed to manage.py as command name
            self.command_name = sys.argv[1]
        else:
            # or take the end of the command's full module name
            self.command_name = sub(r'(.+\.)*', '', self.__class__.__module__)

    def get_download_metadata(self):
        """
        Returns basic metadata about the current CAL-ACCESS snapshot,
        like its size and the last time it was updated while stopping
        short of actually downloading it.
        """
        request = requests.head(self.url)
        return {
            'content-length': int(request.headers['content-length']),
            'last-modified': datetime_parse(request.headers['last-modified'])
        }

    #
    # Logging methods
    #

    def header(self, string):
        """
        Writes out a string to stdout formatted to look like a header
        that stands out among the other lines.
        """
        if not self.no_color:
            string = colorize(string, fg="cyan", opts=("bold",))
        self.stdout.write(string)

    def log(self, string):
        """
        Writes out a string to stdout formatted to look like a standard line.
        """
        if not self.no_color:
            string = colorize("%s" % string, fg="white")
        self.stdout.write(string)

    def success(self, string):
        """
        Writes out a string to stdout formatted green to communicate success.
        """
        if not self.no_color:
            string = colorize(string, fg="green")
        self.stdout.write(string)

    def failure(self, string):
        """
        Writes out a string to stdout formatted red to communicate failure.
        """
        if not self.no_color:
            string = colorize(string, fg="red")
        self.stdout.write(string)

    def duration(self):
        """
        Calculates how long the command has been running and writes a readable duration to stdout.
        """
        duration = datetime.now() - self.start_datetime
        self.stdout.write('Duration: {}'.format(str(duration)))
