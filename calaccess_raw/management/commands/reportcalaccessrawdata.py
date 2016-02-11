#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import os
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw import get_model_list
from django.conf import settings
from django.core.management import call_command
from django.db.models import Sum
from django.forms.models import model_to_dict
from django.contrib.humanize.templatetags.humanize import naturaltime
from clint.textui import progress
from csv import DictWriter


def calc_percent(whole, total):
    """
    """
    try:
        pct = whole / total
    except ZeroDivisionError:
        pct = 0
    else:
        pct * 100

    return pct


class Command(CalAccessCommand):
    help = 'Generate report outlining the number / proportion of files / records cleaned and loaded'

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)

        self.missing_raw_files = []
        self.empty_raw_files = []
        self.unknown_raw_files = []

        try:
            last_complete_download = self.command_logs.filter(
                command='downloadcalaccessrawdata',
                finish_datetime__isnull=False
            ).order_by('-finish_datetime')[0]
        except IndexError:
            self.failure("No complete downloads yet.")
            self.log("Try: python manage.py updatecalaccessrawdata")
            return
        else:
            self.raw_data_files = self.raw_data_files.filter(
                version=last_complete_download.version
            )

            downloaded_release_datetime = last_complete_download.version.release_datetime
            current_release_datetime = self.get_download_metadata()['last-modified']

            if current_release_datetime != downloaded_release_datetime:
                since_new_release = naturaltime(current_release_datetime)
                self.failure("A new version of CAL-ACCESS was "
                             "released {}.".format(since_new_release))
                self.log("Try: python manage.py updatecalaccessrawdata")

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

        self.num_download_files = self.raw_data_files.count()

        self.num_clean_files = self.raw_data_files.filter(
            clean_records_count__gt=0
        ).count()

        self.num_loaded_files = self.raw_data_files.filter(
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
        Takes the name of a RawDataFile count column.
        Returns a sum of its values
        """
        result = self.raw_data_files.aggregate(
            the_sum=Sum(column_name)
        )
        return result['the_sum']

    def write_csv_results(self):
        """
        Write .csv file to the docs directory
        """
        file_name = os.path.join(
            getattr(settings, 'REPO_DIR'),
            'docs/calaccess_raw_files_report.csv'
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
                    'pct_cleaned',
                    'pct_loaded'
                ]
            writer = DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for i in self.raw_data_files:

                row = model_to_dict(i)

                del row['id']
                del row['version']

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
