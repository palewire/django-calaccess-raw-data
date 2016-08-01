#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate report outlining the number / proportion of files / records cleaned and loaded.
"""
from __future__ import unicode_literals
from __future__ import division
import os
from csv import DictWriter
from clint.textui import progress
from django.core.management import call_command
from django.core.management.base import CommandError
from django.db.models import Sum
from django.forms.models import model_to_dict
from calaccess_raw import get_model_list, get_download_directory
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.models.tracking import RawDataVersion


def calc_percent(whole, total):
    """
    Calculate percentage of the total.
    """
    try:
        pct = whole / total
    except ZeroDivisionError:
        pct = 0
    else:
        pct * 100

    return pct


class Command(CalAccessCommand):
    """
    Generate report outlining the number / proportion of files / records cleaned and loaded.
    """
    help = 'Generate report outlining the number / proportion of files / records cleaned and loaded'

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

        self.missing_raw_files = []
        self.empty_raw_files = []
        self.unknown_raw_files = []

        # get the latest version
        try:
            self.version = RawDataVersion.objects.latest('release_datetime')
        except RawDataVersion.DoesNotExist:
            raise CommandError('No CAL-ACCESS versions tracked.')
        # quit if version update not complete
        if not self.version.update_completed:
            raise CommandError(
                'Update to {:%c} version is not complete. (run `python manage.py '
                'updatecalaccessrawdata`).'.format(self.version.release_datetime)
            )

        self.log("Analyzing loaded models")

        if self.verbosity == 1:
            model_list = progress.bar(get_model_list())
        else:
            model_list = get_model_list()

        for model in model_list:

            call_command(
                'verifycalaccessrawfile',
                model.__name__,
                verbosity=self.verbosity
            )

        self.num_download_files = self.version.files.count()

        self.num_clean_files = self.version.files.filter(
            clean_records_count__gt=0
        ).count()

        self.num_loaded_files = self.version.files.filter(
            load_records_count__gt=0
        ).count()

        total_raw_records = self.sum_count_column('download_records_count')

        total_clean_records = self.sum_count_column('clean_records_count')

        total_loaded_records = self.sum_count_column('load_records_count')

        self.log(
            '{0:.4%} of records cleaned'.format(
                calc_percent(total_clean_records, total_raw_records)
            )
        )

        self.log(
            '{0:.4%} of records loaded'.format(
                calc_percent(total_loaded_records, total_raw_records)
            )
        )

        self.write_csv_results()

        self.duration()

    def sum_count_column(self, column_name):
        """
        Takes the name of a RawDataFile count column. Returns a sum of its values.
        """
        result = self.version.files.aggregate(
            the_sum=Sum(column_name)
        )
        return result['the_sum']

    def write_csv_results(self):
        """
        Write .csv file to the docs directory.
        """
        file_name = os.path.join(
            get_download_directory(),
            'calaccess_raw_files_report.csv'
        )

        with open(file_name, 'w') as f:
            fieldnames = [
                'file_name',
                'download_columns_count',
                'clean_columns_count',
                'load_columns_count',
                'download_records_count',
                'clean_records_count',
                'load_records_count',
                'error_count',
                'pct_cleaned',
                'pct_loaded'
            ]
            writer = DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for i in self.version.files.all():

                row = model_to_dict(i)

                for k in row.keys():
                    if k not in fieldnames:
                        del row[k]

                row.update({
                    'pct_cleaned': '{0:.2%}'.format(
                        calc_percent(i.clean_records_count, i.download_records_count)
                    )
                })

                row.update({
                    'pct_loaded': '{0:.2%}'.format(
                        calc_percent(i.load_records_count, i.download_records_count)
                    )
                })

                writer.writerow(row)
