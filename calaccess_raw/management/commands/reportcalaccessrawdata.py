#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw import get_download_directory, get_model_list
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import intcomma
from clint.textui import progress
from csv import DictWriter


class Command(CalAccessCommand):
    help = 'Generate report outlining the number / proportion of files / records cleaned and loaded'

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)

        self.num_source_files = 0
        self.total_source_records = 0
        self.num_clean_files = 0
        self.total_clean_records = 0
        self.incomplete_loads = 0
        self.total_loaded_records = 0
        self.results = {}
        self.missing_source_files = []
        self.data_dir = get_download_directory()

        self.log("Analyzing source files")

        tsv_dir = os.path.join(self.data_dir, "tsv/")

        tsv_list = []

        # ignore any file that isn't a .TSV file (e.g., .DS_Store)
        for i in os.listdir(tsv_dir):
            if '.TSV' in i.upper():
                tsv_list.append(i)

        # iterate through tsv files
        for file_name in progress.bar(tsv_list):

            # add each to the total count of source files
            self.num_source_files += 1

            # get the count of original records
            with open(os.path.join(tsv_dir, file_name)) as f:
                row_count = sum(1 for l in f)

            # subtract header row as long as file is not empty
            if row_count > 0:
                row_count -= 1

            # add the source file name to results with the record count
            self.results[file_name.replace('.TSV', '')] = {'orig_records_count': row_count}

        self.log("Analyzing cleaned files")

        csv_dir = os.path.join(self.data_dir, "csv/")

        csv_list = []

        # ignore any file that isn't a .TSV file (e.g., .DS_Store)
        for i in os.listdir(csv_dir):
            if '.CSV' in i.upper():
                csv_list.append(i)

        # iterate through the cleaned csv files
        for file_name in progress.bar(csv_list):

            # add each to the total count of clean files
            self.num_clean_files += 1

            # get the count of clean records
            with open(os.path.join(csv_dir, file_name)) as f:
                row_count = sum(1 for l in f)

            # subtract header row as long as file is not empty
            if row_count > 0:
                row_count -= 1

            source_file = file_name.upper().replace('.CSV', '') 
            
            # store count of clean records for each source file
            self.results[source_file]['clean_records_count'] = row_count
            self.results[source_file]['model_records_count'] = 0

        self.log("Analyzing models")

        # iterate through all the models
        for model in progress.bar(get_model_list()):

            # get the count of records loaded
            row_count = model.objects.count()

            try:
                self.results[model._meta.db_table]['model_records_count'] = row_count
            except IndexError:
                self.missing_source_files.append(model._meta.db_table)

        self.write_csv_results()

        self.duration()

    def write_csv_results(self):
        """
        Write .csv file to the docs directory
        """
        file_name = os.path.join(getattr(settings, 'REPO_DIR'), 'docs/calaccess_report.csv')
        # os.path.exists(file_name) or os.makedirs(file_name)

        with open(file_name, 'w') as f:

            fieldnames = [
                    'source',
                    'orig_records_count',
                    'clean_records_count',
                    'model_records_count'
                ]
            writer = DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for source, data in self.results.iteritems():

                data.update({'source':source})

                writer.writerow(data)


