#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from re import sub
from datetime import datetime
from dateutil.parser import parse as datetime_parse
import requests
from django.utils.termcolors import colorize
from django.core.management.base import BaseCommand
from calaccess_raw.models.tracking import (
    RawDataVersion,
    RawDataFile,
    CalAccessCommandLog
)


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

        self.raw_data_versions = RawDataVersion.objects
        self.raw_data_files = RawDataFile.objects
        self.command_logs = CalAccessCommandLog.objects

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

    def get_last_log(self, file_name=None, finished=False):
        """
        Execute query for the given command most recently started CalAccessCommandLog,
        unless finished=True, in which case query for the most recently finished.

        Commands that require a file / model as a positional argument should
        pass the file_name keyword argument.

        Returns a CalAccessCommandLog object or None, if no results.
        """
        if file_name:
            q = self.command_logs.filter(file_name=file_name)
        else:
            q = self.command_logs

        if finished:
            order_by_field = '-finish_datetime'
            q = q.filter(finish_datetime__isnull=False)
        else:
            order_by_field = '-start_datetime'

        try:
            last_log = q.filter(
                command=self
            ).order_by(order_by_field)[0]
        except IndexError:
            last_log = None

        return last_log

    def get_caller(self):
        """
        If the command was called by another command, return the caller's
        RawDataCommandLog object. Else, return None.
        """
        caller = None

        if not self._called_from_command_line:
            # TODO: see if there's another way to identify caller
            # in (edge) case when update is not called from command line

            # for now, assume the caller is the arg passed to manage.py
            # try getting the most recent log of this command for the version
            try:
                caller = self.command_logs.filter(
                    command=sys.argv[1]
                ).order_by('-start_datetime')[0]
            except IndexError:
                pass

        return caller

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

    def __str__(self):
        return sub(r'(.+\.)*', '', self.__class__.__module__)
