#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Load clean CAL-ACCESS CSV file into a database model.
"""
from __future__ import unicode_literals
import os
import six
from django.apps import apps
from csvkit import CSVKitReader
from django.conf import settings
from postgres_copy import CopyMapping
from django.db import connections, router
from django.core.management.base import CommandError
from django.utils.timezone import now
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.models.tracking import RawDataFile


class Command(CalAccessCommand):
    """
    Load clean CAL-ACCESS CSV file into a database model.
    """
    help = 'Load clean CAL-ACCESS CSV file into a database model'
    # Trick for reformating date strings in source data so that they can
    # be gobbled up by MySQL. You'll see how below.
    date_sql = "DATE_FORMAT(str_to_date(@`%s`, '%%c/%%e/%%Y'), '%%Y-%%m-%%d')"
    datetime_sql = "DATE_FORMAT(str_to_date(@`%s`, '%%c/%%e/%%Y \
%%h:%%i:%%s %%p'), '%%Y-%%m-%%d  %%H:%%i:%%s')"

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
            help="Name of Django app with models into which data will "
                 "be imported (if other not calaccess_raw)"
        )

    # all BaseCommand subclasses require a handle() method that includes
    #   the actual logic of the command
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

        # get the row count
        row_count = self.get_row_count()

        if row_count == 0:
            if self.verbosity > 2:
                self.failure("%s is empty." % self.csv)
        else:
            # store the start time for the load
            raw_file.load_start_datetime = now()
            # reset the finish time for the load
            raw_file.load_finish_datetime = None
            # save here in case command doesn't finish
            raw_file.save()

            if self.verbosity > 2:
                self.log(" Loading %s" % options['model_name'])
            self.load()

            # add load counts to raw_file_record
            raw_file.load_columns_count = len(self.model._meta.fields)
            raw_file.load_records_count = self.model.objects.count()

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
        # check if can load into dat
        if getattr(settings, 'CALACCESS_DAT_SOURCE', None) and six.PY2:
            self.load_dat()

        # if not using default db, make sure the database is set up in django's settings
        if self.database:
            try:
                engine = settings.DATABASES[self.database]['ENGINE']
            except KeyError:
                raise TypeError(
                    "{} not configured in DATABASES settings.".format(self.database)
                )

        # temporarily drop model and field constraints and indexes
        self.model.objects.drop_constraints_and_indexes()

        # set up database connection
        self.connection = connections[self.database]
        self.cursor = self.connection.cursor()

        # check the kind of database before calling db-specific load method
        if engine == 'django.db.backends.mysql':
            self.load_mysql()
        elif engine in (
            'django.db.backends.postgresql_psycopg2'
            'django.contrib.gis.db.backends.postgis'
        ):
            self.load_postgresql()
        else:
            self.failure("Sorry your database engine is unsupported")
            raise CommandError(
                "Only MySQL and PostgresSQL backends supported."
            )

        # re-add model and field constraints and indexes
        self.model.objects.add_constraints_and_indexes()

    def load_dat(self):
        """
        Takes a model and a csv file and loads it into dat.
        """
        import datpy
        dat_source = settings.CALACCESS_DAT_SOURCE
        self.dat = datpy.Dat(dat_source['source'])
        dataset = self.dat.dataset(self.model._meta.db_table)
        try:
            dataset.import_file(self.csv, format='csv')
            if self.verbosity > 2:
                dat_status = self.dat.status()
                model_count = dat_status['rows']
                csv_count = self.get_row_count(self.csv)
                self.finish_load_message(model_count, csv_count)
        except datpy.DatException:
            raise CommandError(
                'Failed to load dat for %s, %s' % (
                    self.model._meta.db_table,
                    self.csv
                )
            )

    def load_mysql(self):
        """
        Load the file into a MySQL database using LOAD DATA INFILE.
        """
        import warnings
        import MySQLdb
        warnings.filterwarnings("ignore", category=MySQLdb.Warning)

        # Flush the target model
        self.cursor.execute('TRUNCATE TABLE %s' % self.model._meta.db_table)

        # Build the MySQL LOAD DATA INFILE command
        bulk_sql_load_part_1 = """
            LOAD DATA LOCAL INFILE '%s'
            INTO TABLE %s
            FIELDS TERMINATED BY ','
            OPTIONALLY ENCLOSED BY '"'
            LINES TERMINATED BY '\\n'
            IGNORE 1 LINES
            (
        """ % (
            self.csv,
            self.model._meta.db_table
        )

        # Get the headers and the row count from the source CSV
        csv_headers = self.get_headers()
        csv_record_cnt = self.get_row_count()

        header_sql_list = []
        field_types = dict(
            (f.db_column, f.db_type(self.connection))
            for f in self.model._meta.fields
        )
        date_set_list = []
        char_set_list = []

        for h in csv_headers:
            # Pull the data type of the field
            data_type = field_types[h]
            # If it is a date field, we need to reformat the data
            # so that MySQL will properly parse it on the way in.
            if data_type == 'date':
                header_sql_list.append('@`%s`' % h)
                date_set_list.append(
                    "`%s` =  %s" % (h, self.date_sql % h)
                )
            elif data_type == 'datetime':
                header_sql_list.append('@`%s`' % h)
                date_set_list.append(
                    "`%s` =  %s" % (h, self.datetime_sql % h)
                )
            elif 'char' in data_type:
                header_sql_list.append('@`%s`' % h)
                char_set_list.append(
                    r"`{0}` = TRIM(TRAILING '\n' FROM @`{0}`)".format(h)
                )
            else:
                header_sql_list.append('`%s`' % h)

        bulk_sql_load = bulk_sql_load_part_1 + ','.join(header_sql_list) + ')'
        if date_set_list or char_set_list:
            bulk_sql_load += " set %s" % ",".join(date_set_list + char_set_list)

        # Run the query
        cnt = self.cursor.execute(bulk_sql_load)

        # Report back on how we did
        if self.verbosity > 2:
            self.finish_load_message(cnt, csv_record_cnt)

    def load_postgresql(self):
        """
        Load the file into a PostgreSQL database using COPY.
        """
        # Drop all the records from the target model's real table
        self.cursor.execute('TRUNCATE TABLE "%s" CASCADE' % (
            self.model._meta.db_table
        ))

        # Create a mapping between our django models and the CSV headers
        model_mapping = dict(
            (f.name, f.db_column) for f in self.model._meta.fields
            if f.db_column
        )

        # Load the data
        c = CopyMapping(
            self.model,
            self.csv,
            model_mapping,
            using=self.database,
        )
        c.save(silent=True)

        # Print out the results
        if self.verbosity > 2:
            csv_count = self.get_row_count()
            model_count = self.model.objects.count()
            self.finish_load_message(model_count, csv_count)

    def get_headers(self):
        """
        Returns the column headers from the csv as a list.
        """
        with open(self.csv, 'r') as infile:
            csv_reader = CSVKitReader(infile)
            try:
                headers = next(csv_reader)
            except StopIteration:
                headers = []
        return headers

    def get_row_count(self):
        """
        Returns the number of rows in the file, not counting headers.
        """
        with open(self.csv) as infile:
            row_count = sum(1 for line in infile) - 1

        if row_count < 0:
            row_count = 0

        return row_count

    def finish_load_message(self, model_count, csv_count):
        """
        The message displayed about whether or not a load finished successfully.
        """
        if model_count != csv_count:
            msg = '  Table record count doesn\'t match CSV. \
Table: %s\tCSV: %s'
            self.failure(msg % (
                model_count,
                csv_count,
            ))
