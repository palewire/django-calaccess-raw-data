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

    def add_arguments(self, parser):
        """
        Adds custom arguments that will be available to all subclasses.
        """
        parser.add_argument(
            "--d",
            "--database",
            dest="database",
            default=None,
            help="Alias of database where data will be inserted. Defaults to the "
                 "'default' in DATABASE settings."
        )

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

        self.database = options["database"] or 'default'

        self.raw_data_versions = RawDataVersion.objects.using(self.database)
        self.raw_data_files = RawDataFile.objects.using(self.database)
        self.command_logs = CalAccessCommandLog.objects.using(self.database)

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

    def get_or_copy_raw_latest_version(self):
        """
        Returns a RawDataVersion object with the most recent release_datetime.

        If the version doesn't exist in the db in the command's scope,
        look up the version in the default db and copy it to the db
        in the command's scope.

        If the default db doesn't have a version with the given release_datetime,
        return None.
        """
        # check for raw_data_version in the active db
        try:
            version = self.raw_data_versions.latest('release_datetime')
        except RawDataVersion.DoesNotExist:
            # if does not exist and we aren't using default db...
            if self.database != 'default':
                # check the default db next
                try:
                    version = self.raw_data_versions.using(
                        'default'
                    ).latest('release_datetime')
                except RawDataVersion.DoesNotExist:
                    raise
                else:
                    # if there's version in default, copy to active db
                    # use first option in Django docs http://bit.ly/1SYgWnJ
                    version.pk = None
                    version.save(using=self.database)
            else:
                raise

        return version

    def get_or_copy_raw_file(self, version, file_name):
        """
        Returns a RawDataFile object with given version and file_name.

        If the file doesn't exist in the db in the command's scope,
        look up the file in the default db and copy it to db
        in the command's scope.

        If the default db doesn't have a file with the given release_datetime,
        return None.
        """
        try:
            raw_file = self.raw_data_files.get(
                version=version,
                file_name=file_name
            )
        except RawDataFile.DoesNotExist:
            # if does not exist and we aren't using default db...
            if self.database != 'default':
                # check the default db next
                try:
                    raw_file = self.raw_data_files.using(
                        'default'
                    ).get(
                        version=version,
                        file_name=file_name
                    )
                except RawDataFile.DoesNotExist:
                    raise
                else:
                    # if there's file in default, copy to active db
                    # use first option in Django docs http://bit.ly/1SYgWnJ
                    raw_file.pk = None
                    raw_file.save(using=self.database)
            else:
                raise

        return raw_file

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
