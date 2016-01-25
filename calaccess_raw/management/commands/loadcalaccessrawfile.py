from __future__ import unicode_literals
import os
import six
from django.apps import apps
from csvkit import CSVKitReader
from django.conf import settings
from postgres_copy import CopyMapping
from django.db import connections, router
from django.core.management.base import CommandError
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand):
    help = 'Load clean CAL-ACCESS CSV file into database model'
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
            "--d",
            "--database",
            dest="database",
            default=None,
            help="Alias of database where data will be inserted. Defaults to the "
                 "'default' in DATABASE settings."
        )
        parser.add_argument(
            "-a",
            "--app-name",
            dest="app_name",
            default="calaccess_raw",
            help="Name of Django app where model will be imported from"
        )

    # all BaseCommand subclasses require a handle() method that includes
    #   the actual logic of the command
    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)

        # set / compute any attributes that multiple class methods need
        self.keep_files = options["keep_files"]
        self.model = apps.get_model(options["app_name"], options['model_name'])
        self.database = options["database"] or router.db_for_write(self.model)
        self.csv = options["csv"] or self.model.objects.get_csv_path()

        if self.verbosity > 2:
            self.log(" Loading %s" % options['model_name'])

        if getattr(settings, 'CALACCESS_DAT_SOURCE', None) and six.PY2:
            self.load_dat()

        # make sure the database is set up in django's settings
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

        # if not keeping files, remove the csv file
        if not self.keep_files:
            os.remove(self.csv)

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
            else:
                header_sql_list.append('`%s`' % h)

        bulk_sql_load = bulk_sql_load_part_1 + ','.join(header_sql_list) + ')'
        if date_set_list:
            bulk_sql_load += " set %s" % ",".join(date_set_list)

        # Run the query
        cnt = self.cursor.execute(bulk_sql_load)

        # Report back on how we did
        self.finish_load_message(cnt, csv_record_cnt)

    def load_postgresql(self):
        """
        Takes a model and a csv file and loads it into postgresql
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
        csv_count = self.get_row_count()
        model_count = self.model.objects.count()
        self.finish_load_message(model_count, csv_count)

    def get_headers(self):
        """
        Returns the column headers from the csv as a list.
        """
        with open(self.csv, 'r') as infile:
            csv_reader = CSVKitReader(infile)
            headers = next(csv_reader)
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
        if self.verbosity:
            if model_count != csv_count and self.verbosity > 2:
                msg = '  Table record count doesn\'t match CSV. \
Table: %s\tCSV: %s'
                self.failure(msg % (
                    model_count,
                    csv_count,
                ))
