#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import apps
from django.db import router
from django.contrib.humanize.templatetags.humanize import intcomma
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.models.tracking import RawDataVersion


class Command(CalAccessCommand):
    help = "Logs row count of given model and compares against line count in cleaned CSV"

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)
        parser.add_argument('model_name', help="Name of model to verify")
        parser.add_argument(
            "-a",
            "--app-name",
            dest="app_name",
            default="calaccess_raw",
            help="Name of Django app with models into which data will "
                 "be imported (if other not calaccess_raw)"
        )

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)

        if self.verbosity > 1:
            self.log(" Verifying %s" % options['model_name'])

        model = apps.get_model(options['app_name'], options['model_name'])

        self.database = router.db_for_write(model=model)

        # Get the model total
        model_count = model.objects.count()

        try:
            version = self.raw_data_versions.latest('release_datetime')
        except RawDataVersion.DoesNotExist:
            version = None
        else:
            raw_file = self.raw_data_files.get_or_create(
                version=version,
                file_name=model._meta.db_table
            )[0]

            # add load counts to raw_file_record
            raw_file.load_columns_count = len(model._meta.fields)
            raw_file.load_records_count = model_count
            raw_file.save()

        # Get the CSV total
        try:
            csv_count = raw_file.clean_records_count
        except UnboundLocalError:
            csv_path = model.objects.get_csv_path()
            with open(csv_path) as f:
                csv_count = sum(1 for l in f) - 1

        if self.verbosity > 1:
            # Report back on how we did
            if model_count == csv_count:
                self.success("  Record count matches CSV")
                self.success("  - Model: %s" % intcomma(model_count))
                self.success("  - CSV: %s" % intcomma(csv_count))
            else:
                self.failure("  Record count does not match CSV")
                self.failure("  - Model: %s" % intcomma(model_count))
                self.failure("  - CSV: %s" % intcomma(csv_count))
