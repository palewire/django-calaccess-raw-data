from __future__ import unicode_literals
#from postgres_copy import Copy
from csvkit import CSVKitReader, reader
from django.db import connection
from django.conf import settings
from django.db.models.loading import get_model
from calaccess_raw.management.commands import CalAccessCommand
from django.core.management.base import LabelCommand, CommandError


class Command(CalAccessCommand, LabelCommand):
    help = 'Load clean CAL-ACCESS file into its corresponding database model'
    args = '<model name>'
    # Trick for reformating date strings in source data so that they can
    # be gobbled up by MySQL. You'll see how below.
    date_sql = "DATE_FORMAT(str_to_date(@`%s`, '%%c/%%e/%%Y'), '%%Y-%%m-%%d')"
    datetime_sql = "DATE_FORMAT(str_to_date(@`%s`, '%%c/%%e/%%Y \
%%h:%%i:%%s %%p'), '%%Y-%%m-%%d  %%H:%%i:%%s')"

    def handle_label(self, label, **options):
        self.verbosity = options.get("verbosity")
        self.cursor = connection.cursor()
        self.load(label)

    def load(self, model_name):
        """
        Loads the source CSV for the provided model.
        """
        if self.verbosity > 2:
            self.log(" Loading %s" % model_name)

        model = get_model("calaccess_raw", model_name)
        csv_path = model.objects.get_csv_path()

        engine = settings.DATABASES['default']['ENGINE']
        if engine == 'django.db.backends.mysql':
            self.load_mysql(model, csv_path)
        elif engine in (
            'django.db.backends.postgresql_psycopg2'
            'django.contrib.gis.db.backends.postgis'
                ):
            self.load_postgresql(model, csv_path)
        elif engine == 'django.db.backends.sqlite3':
            self.load_sqlite(model, csv_path)
        else:
            self.failure("Sorry your database engine is unsupported")
            raise CommandError(
                "Only MySQL,PostgresSQL, SQLite3 backends supported."
            )

    def load_mysql(self, model, csv_path):
        import warnings
        import MySQLdb
        warnings.filterwarnings("ignore", category=MySQLdb.Warning)

        # Flush the target model
        self.cursor.execute('TRUNCATE TABLE %s' % model._meta.db_table)

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
            csv_path,
            model._meta.db_table
        )

        # Get the headers and the row count from the source CSV
        csv_headers = self.get_headers(csv_path)
        csv_record_cnt = self.get_row_count(csv_path)

        header_sql_list = []
        field_types = dict(
            (f.db_column, f.db_type(connection))
            for f in model._meta.fields
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

    def load_postgresql(self, model, csv_path):
        """
        Takes a model and a csv_path and loads it into postgresql
        """
        # Drop all the records from the target model's real table
        self.cursor.execute('TRUNCATE TABLE "%s" CASCADE' % (
            model._meta.db_table
        ))

        c = Copy(
            model,
            csv_path,
            dict((f.db_column, f.name) for f in model._meta.fields),
        )
        c.save(silent=True)

        # Print out the results
        csv_count = self.get_row_count(csv_path)
        model_count = model.objects.count()
        self.finish_load_message(model_count, csv_count)

    def load_sqlite(self, model, csv_path):
        """
        Takes a model and csv_path and loads in sqlite.
        """
        import sqlite3
        import pandas as pd
        #drop all records from target
        self.cursor.execute('DELETE FROM "%s"' % model._meta.db_table)

        # insert using sqlite executemany
        csv_headers = self.get_headers(csv_path)
        csv_record_cn = self.get_row_count(csv_path)

        header_sql_list = []
        field_types = dict(
                (f.db_column, f.db_type(connection))
                for f in model._meta.fields
            )
        date_fields = []
        datetime_fields = []
        for idx, h in enumerate(csv_headers):
            # pull datatype
            data_type = field_types[h]
            if data_type == 'date':
                date_fields.append(idx)
            elif data_type == 'datetime':
                datetime_fields.append(idx)
        
        with open(csv_path, 'r') as infile:
            csv_reader = reader(infile)
            header = csv_reader.next()
            for idx, row in enumerate(csv_reader):
                # grab the rows that have things in them 
                # populated rows
                pop_rows = []
                for item_loc, item in enumerate(row): 
                    if item:
                        pop_rows.append((item_loc, item))
                subset_header_string = ""
                for item in pop_rows:
                    subset_header_string = subset_header_string + header[item[0]] + ","
                subset_header_string = subset_header_string[:-1] # drop last comma
                values = [p[1] for p in pop_rows]
                values_insert_string = ""
                for val in values:
                    values_insert_string = values_insert_string + val + ","
                values_insert_string = values_insert_string[:-1]
                print values_insert_string
                _insert_tmpl = 'INSERT INTO %s (%s) VALUES (%s)' %  (model._meta.db_table, subset_header_string,
                                join(['?']*len(pop_rows)))
                self.cursor.execute(_insert_tmpl, values)


    def get_headers(self, csv_path):
        """
        Returns the column headers from the csv as a list.
        """
        with open(csv_path, 'r') as infile:
            csv_reader = CSVKitReader(infile)
            headers = next(csv_reader)
        return headers

    def get_row_count(self, csv_path):
        """
        Returns the number of rows in the file, not counting headers.
        """
        with open(csv_path) as infile:
            row_count = len(infile.readlines()) - 1
        return row_count

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
