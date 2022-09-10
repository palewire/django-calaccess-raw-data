"""
Base management command that provides common functionality for the other commands in this app.
"""
import logging
import os
from re import sub
from datetime import datetime
from django.utils.termcolors import colorize
from django.core.management.base import BaseCommand
from calaccess_raw import get_data_directory

logger = logging.getLogger(__name__)


class CalAccessCommand(BaseCommand):
    """
    Base management command that provides common functionality for the other commands in this app.
    """

    url = "https://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip"

    def handle(self, *args, **options):
        """
        The generic handler function.

        Any command subclassing this object should implement its own
        handle method, as is standard in Django, and run this method
        via a super call to inherit its functionality.
        """
        self.set_global_options(options)

    def set_global_options(self, options):
        """
        Set options to all commands.
        """
        # Set global options
        self.verbosity = options.get("verbosity")
        self.no_color = options.get("no_color")

        # set up data directories
        self.data_dir = get_data_directory()
        self.tsv_dir = os.path.join(self.data_dir, "tsv")
        self.csv_dir = os.path.join(self.data_dir, "csv")

        os.path.exists(self.data_dir) or os.makedirs(self.data_dir)
        os.path.exists(self.tsv_dir) or os.makedirs(self.tsv_dir)
        os.path.exists(self.csv_dir) or os.makedirs(self.csv_dir)

        # set path where zip will be downloaded
        self.download_dir = os.path.join(self.data_dir, "download")
        self.zip_path = os.path.join(self.download_dir, self.url.split("/")[-1])

        # Start the clock
        self.start_datetime = datetime.now()

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
        self.stdout.write("Duration: {}".format(str(duration)))
        logger.debug("Duration: {}".format(str(duration)))

    def __str__(self):
        return sub(r"(.+\.)*", "", self.__class__.__module__)
