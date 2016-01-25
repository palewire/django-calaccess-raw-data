#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.termcolors import colorize
from django.core.management.base import BaseCommand


class CalAccessCommand(BaseCommand):
    """
    A base management command that provides common functionality
    for the other commands in this application.
    """
    def handle(self, *args, **options):
        """
        Sets options common to all commands.

        Any command subclassing this object should implement its own
        handle method, as is standard in Django, and run this method
        via a super call to inherit its functionality.
        """
        self.verbosity = int(options.get("verbosity"))
        self.no_color = options.get("no_color")

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
