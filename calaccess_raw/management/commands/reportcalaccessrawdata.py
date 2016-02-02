#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw import get_model_list
from django.conf import settings
from django.core.management import call_command
from django.db.models import Sum
from django.forms.models import model_to_dict
from clint.textui import progress
from csv import DictWriter
from calaccess_raw.models.tracking import RawDataVersion, RawDataFile

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

        self.version=RawDataVersion.objects.latest('release_datetime')

        self.raw_file_records = RawDataFile.objects.filter(
            version=self.version
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

        self.num_download_files = self.raw_file_records.count()

        # self.num_clean_files = self.raw_file_records.filter(
        #     clean_records_count>0
        # ).count()

        # self.num_loaded_files = self.raw_file_records.filter(
        #     load_records_count>0
        # ).count()

        total_raw_records = self.sum_count_column('download_records_count')
        
        total_clean_records = self.sum_count_column('clean_records_count')
        
        total_loaded_records = self.sum_count_column('load_records_count')     

        self.log(
            '{0:.4%} of records cleaned'.format(
                float(total_clean_records) / float(total_raw_records)
            )
        )

        self.log(
            '{0:.4%} of records loaded'.format(
                float(total_loaded_records) / float(total_raw_records)
            )
        )

        self.write_csv_results()

        self.duration()

    def sum_count_column(self, column_name):
        """
        Takes the name of a RawDataFile count column.
        Returns a sum of its values
        """
        result = self.raw_file_records.aggregate(
            the_sum=Sum(column_name)
        )
        return result['the_sum']

    def write_csv_results(self):
        """
        Write .csv file to the docs directory
        """
        file_name = os.path.join(
            getattr(settings, 'REPO_DIR'), 
            'docs/calaccess_report.csv'
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

            for i in self.raw_file_records:

                row = model_to_dict(i)

                del row['id']
                del row['version']

                try:
                    row.update({
                        'pct_cleaned': '{0:.2%}'.format(
                            float(i.clean_records_count) / float(i.download_records_count)
                        )
                    })
                except ZeroDivisionError:
                    row.update({'pct_cleaned': None})
                
                try:
                    row.update({
                        'pct_loaded': '{0:.2%}'.format(
                            float(i.load_records_count) / float(i.load_records_count)
                        )
                    })
                except ZeroDivisionError:
                    row.update({'pct_loaded': None})

                writer.writerow(row)
