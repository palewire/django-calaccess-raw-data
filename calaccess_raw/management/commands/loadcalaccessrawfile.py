#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Load clean CAL-ACCESS CSV file into a database model.
"""
from __future__ import unicode_literals

# Files
import os
from csvkit import reader

# Django config
from django.apps import apps
from django.conf import settings
from django.utils.timezone import now

# Database
from django.db import connections, router
from calaccess_raw.models.tracking import RawDataFile

# Commands
from django.core.management.base import CommandError
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand):
    """
    Load clean CAL-ACCESS CSV file into a database model.
    """
    help = 'Load clean CAL-ACCESS CSV file into a database model'
    # Trick for reformating date strings in source data so that they can
    # be gobbled up by MySQL. You'll see how below.
    date_sql = "DATE_FORMAT(str_to_date(@`{}`, '%%c/%%e/%%Y'), '%%Y-%%m-%%d')"
    datetime_sql = "DATE_FORMAT(str_to_date(@`{}`, '%%c/%%e/%%Y %%h:%%i:%%s %%p'), '%%Y-%%m-%%d  %%H:%%i:%%s')"

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)
        # positional (required) arg
        parser.add_argument(
            'model_name',
            help="Name of the model into which data will be loaded"
        )
        # keyword (optional) args
        parser.add_argument(
            "--c",
            "--csv",
            dest='csv',
            default=None,
            help="Path to comma-delimited file to be loaded. Defaults to one associated with model."
        )
        parser.add_argument(
            "--keep-file",
            action="store_true",
            dest="keep_file",
            default=False,
            help="Keep clean CSV file after loading"
        )
        parser.add_argument(
            "-a",
            "--app-name",
            dest="app_name",
            default="calaccess_raw",
            help="Name of Django app with models into which data will be imported (if other not calaccess_raw)"
        )

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)

        # set / compute any attributes that multiple class methods need
        self.keep_file = options["keep_file"]

        # get model based on strings of app_name and model_name
        self.model = apps.get_model(options["app_name"], options['model_name'])

        # load from provided csv or csv mapped to model
        self.csv = options["csv"] or self.model.objects.get_csv_path()

        # load into database suggested for model by router
        self.database = router.db_for_write(model=self.model)

        # get most recently cleaned RawDataFile
        try:
            raw_file = RawDataFile.objects.filter(
                file_name=self.model._meta.db_table,
                clean_start_datetime__isnull=False
            ).latest('clean_start_datetime')
        except RawDataFile.DoesNotExist:
            raise CommandError(
                'No record of cleaning {0}.TSV (run `python manage.py '
                'cleancalaccessrawfile {0}`).'.format(self.model._meta.db_table)
            )
        # raise exception if clean step did not finish
        if not raw_file.clean_finish_datetime:
            raise CommandError(
                'Previous cleaning of {0}.TSV did not finish (run `python manage.py '
                'cleancalaccessrawfile {0}`).'.format(self.model._meta.db_table)
            )

        # Get the row count from the source CSV
        with open(self.csv, 'r') as infile:
            self.csv_row_count = sum(1 for line in infile) - 1

        # Quit if the CSV is empty.
        if self.csv_row_count == 0:
            if self.verbosity > 2:
                self.failure("{} is empty.".format(self.csv))
            return

        # Get the headers from the source CSV
        with open(self.csv, 'r') as infile:
            try:
                csv_reader = reader(infile)
                self.csv_headers = next(csv_reader)
            except StopIteration:
                self.csv_headers = []

        # store the start time for the load
        raw_file.load_start_datetime = now()
        # reset the finish time for the load
        raw_file.load_finish_datetime = None
        # save here in case command doesn't finish
        raw_file.save()

        # Load table
        if self.verbosity > 2:
            self.log(" Loading {}".format(options['model_name']))
        self.load()

        # add load counts to raw_file_record
        raw_file.load_columns_count = len(self.model._meta.fields)
        raw_file.load_records_count = self.model.objects.count()

        # Log an error if the counts don't match
        if self.verbosity > 2 and raw_file.load_records_count != self.csv_row_count:
            msg = "  Table record count doesn't match CSV. {} in the table  vs. {} in the CSV."
            self.failure(msg.format(raw_file.load_records_count, self.csv_row_count))

        # if not keeping files, remove the csv file
        if not self.keep_file:
            os.remove(self.csv)

        # store the finish time for the load
        raw_file.load_finish_datetime = now()

        # and save the RawDataFile
        raw_file.save()

    def load(self):
        """
        Loads the source CSV for the provided model based on settings and database connections.
        """
        # if not using default db, make sure the database is set up in django's settings
        if self.database:
            try:
                engine = settings.DATABASES[self.database]['ENGINE']
            except KeyError:
                raise TypeError("{} not configured in DATABASES settings.".format(self.database))

        # set up database connection
        self.connection = connections[self.database]
        self.cursor = self.connection.cursor()

        # check the kind of database before calling db-specific load method
        if engine == 'django.db.backends.mysql':
            self.load_mysql()
        elif engine in (
            'django.db.backends.postgresql_psycopg2',
            'django.db.backends.postgresql',
            'django.contrib.gis.db.backends.postgis'
        ):
            self.load_postgresql()
        else:
            self.failure("Sorry your database engine is unsupported")
            raise CommandError("Only MySQL and PostgresSQL backends supported.")

    def load_mysql(self):
        """
        Load the file into a MySQL database using LOAD DATA INFILE.
        """
        import warnings
        import MySQLdb
        warnings.filterwarnings("ignore", category=MySQLdb.Warning)

        # Flush the target model
        self.cursor.execute('TRUNCATE TABLE {}'.format(self.model._meta.db_table))

        # Build the MySQL LOAD DATA INFILE command
        bulk_sql_load_part_1 = """
            LOAD DATA LOCAL INFILE '{}'
            INTO TABLE {}
            FIELDS TERMINATED BY ','
            OPTIONALLY ENCLOSED BY '"'
            LINES TERMINATED BY '\\n'
            IGNORE 1 LINES
            (
        """.format(self.csv, self.model._meta.db_table)

        header_sql_list = []
        field_types = dict(
            (f.db_column, f.db_type(self.connection)) for f in self.model._meta.fields
        )
        date_set_list = []
        char_set_list = []

        for h in self.csv_headers:
            # Pull the data type of the field
            data_type = field_types[h]
            # If it is a date field, we need to reformat the data
            # so that MySQL will properly parse it on the way in.
            if data_type == 'date':
                header_sql_list.append('@`{}`'.format(h))
                date_set = "`{}` =  {}".format(h, self.date_sql.format(h))
                date_set_list.append(date_set)
            elif data_type == 'datetime':
                header_sql_list.append('@`{}`'.format(h))
                date_set = "`{}` =  {}".format(h, self.datetime_sql.format(h))
                date_set_list.append(date_set)
            elif 'char' in data_type:
                header_sql_list.append('@`{}`'.format(h))
                date_set = r"`` = TRIM(TRAILING '\n' FROM @`{0}`)".format(h)
                char_set_list.append(date_set)
            else:
                header_sql_list.append('`{}`'.format(h))

        bulk_sql_load = bulk_sql_load_part_1 + ','.join(header_sql_list) + ')'
        if date_set_list or char_set_list:
            bulk_sql_load += " set {}".format(",".join(date_set_list + char_set_list))

        # Run the query
        self.cursor.execute(bulk_sql_load)

    def load_postgresql(self):
        """
        Load the file into a PostgreSQL database using COPY.
        """
        # Drop all the records from the target model's real table
        sql = 'TRUNCATE TABLE "{}" RESTART IDENTITY CASCADE'.format(self.model._meta.db_table)
        self.cursor.execute(sql)

        # Create a mapping between our django models and the CSV headers
        model_mapping = dict(
            (f.name, f.db_column) for f in self.model._meta.fields
            if f.db_column
        )

        # Load the data
        self.model.objects.from_csv(self.csv, model_mapping, using=self.database)
