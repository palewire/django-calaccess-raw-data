#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.conf import settings
from calaccess_raw import get_test_download_directory
from calaccess_raw.management.commands import downloadcalaccessrawdata
from calaccess_raw.models.tracking import RawDataVersion, RawDataFile


class Command(downloadcalaccessrawdata.Command):
    help = "Simulates downloading and unzipping of CAL-ACCESS raw data \
for the purposes of unit testing."

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        self.verbosity = options.get("verbosity")
        self.no_color = options.get("no_color")
        self.raw_data_files = RawDataFile.objects
        self.data_dir = get_test_download_directory()
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        self.zip_path = os.path.join(self.data_dir, self.url.split('/')[-1])

        print self.tsv_dir

        with open(self.data_dir + "/sampled_version.txt", "r") as f:
            release_datetime = f.readline()
            size = f.readline()

        try:
            self.version = RawDataVersion.objects.get(
                release_datetime=release_datetime
            )
        except RawDataVersion.DoesNotExist:
            self.version = RawDataVersion.objects.create(
                release_datetime=release_datetime,
                size=size
            )

        self.unzip()
        self.prep()
        self.track_files()

        if getattr(settings, 'CALACCESS_STORE_ARCHIVE', False):
            self.archive()
