#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from calaccess_raw.models.tracking import RawDataVersion


class Command(CalAccessCommand):
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
            "--keep-files",
            action="store_true",
            dest="keep_files",
            default=False,
            help="Keep CSV file after loading"
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
        super(Command, self).handle(*args, **options)

        # set / compute any attributes that multiple class methods need
        self.keep_files = options["keep_files"]
        # get model based on strings of app_name and model_name
        self.model = apps.get_model(options["app_name"], options['model_name'])

        # load from provided csv or csv mapped to model
        self.csv = options["csv"] or self.model.objects.get_csv_path()

        # load into database suggested for model by router
        self.database = router.db_for_write(model=self.model)

        if self.verbosity > 2:
            self.log(" Loading %s" % options['model_name'])

        # set up version and log records
        caller = self.get_caller_log()

        if caller:
            # if called by another command, use it's version
            self.version = caller.version
            self.log_record = self.command_logs.create(
                version=self.version,
                command=self,
                called_by=caller,
                file_name=self.model._meta.db_table
            )
        else:
            # try getting the most recent version
            try:
                self.version = self.raw_data_versions.latest('release_datetime')
            except RawDataVersion.DoesNotExist:
                # if there's no version, assume this is a test and do not log
                # TODO: Figure out a more direct way to handle this
                self.version = None
            else:
                self.log_record = self.command_logs.create(
                    # if called by another command, use it's version
                    version=self.version,
                    command=self,
                    file_name=self.model._meta.db_table
                )

        row_count = self.get_row_count()

        if row_count > 0:
            self.load()
        else:
            if self.verbosity > 2:
                self.failure("File is empty.")

        # handle tracking data
        raw_file = self.raw_data_files.get_or_create(
            version=self.version,
            file_name=self.log_record.file_name
        )[0]

        # add clean counts to raw_file_record
        raw_file.clean_columns_count = len(self.get_headers())
        raw_file.clean_records_count = self.get_row_count()
        raw_file.save()

        # save the log record
        self.log_record.finish_datetime = now()
        self.log_record.save()

        # if not keeping files, remove the csv file
        if not self.keep_files:
            os.remove(self.csv)

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

    def load_dat(self):
        """
        Takes a model and a csv file and loads it into dat
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
        Load the file into a MySQL database using LOAD DATA INFILE
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
        Load the file into a PostgreSQL database using COPY
        """
        # Drop all the records from the target model's real table
        self.cursor.execute('TRUNCATE TABLE "%s" CASCADE' % (
            self.model._meta.db_table
        ))

        c = CopyMapping(
            self.model,
            self.csv,
            dict((f.name, f.db_column) for f in self.model._meta.fields),
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
            return sum(1 for line in infile) - 1

    def finish_load_message(self, model_count, csv_count):
        """
        The message displayed about whether or not a load finished
        successfully.
        """
        if model_count != csv_count:
            msg = '  Table record count doesn\'t match CSV. \
Table: %s\tCSV: %s'
            self.failure(msg % (
                model_count,
                csv_count,
            ))
