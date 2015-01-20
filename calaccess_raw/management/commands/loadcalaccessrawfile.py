import csv
from django.db import connection
from django.conf import settings
from django.db import ProgrammingError
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
        if self.verbosity:
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
        else:
            self.failure("Sorry your database engine is unsupported")
            raise CommandError(
                "Only MySQL and PostgresSQL backends supported."
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
            LINES TERMINATED BY '\\r\\n'
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
        # Drop the temporary table if it already exists
        try:
            self.cursor.execute('DROP TABLE temporary_table;')
        except ProgrammingError:
            pass

        # Drop all the records from the target model's real table
        self.cursor.execute('TRUNCATE TABLE "%s"' % model._meta.db_table)

        # Get the headers and the count from source CSV
        csv_headers = self.get_headers(csv_path)
        csv_count = self.get_row_count(csv_path)

        # Get the pg data type expected for each field on the target model
        name2type = {}
        for col in model._meta.fields:
            name2type[col.db_column] = col.db_type(connection)

        # Work out what data type we're actually going to use when we
        # ram it into the database via the temporary table
        column_types = self._get_pg_column_types(model, csv_headers)
        regular_cols = column_types.pop('regular_cols')
        empty_cols = column_types['empty_cols']

        # Build pg-ready SQL field declarations to put into the
        # CREATE TABLE statement for the temporary table
        create_field_list = []
        for col in csv_headers:
            if col in regular_cols:
                create_field_list.append("\"" + col + "\"\t" + name2type[col])
            else:
                create_field_list.append("\"" + col + "\"\ttext")
        create_field_sql = ',\n'.join(create_field_list)

        # Create the temporary table
        create_table_sql = "CREATE TABLE \"temporary_table\" (%s);" % (
            create_field_sql
        )
        self.cursor.execute(create_table_sql)

        # Insert CSV data into the temporary table
        temp_insert = """
            COPY "temporary_table"
            FROM '%s'
            CSV
            HEADER;
        """ % (csv_path)
        self.cursor.execute(temp_insert)

        # For tables where we create cases for every column and
        # we need a dummy column in order to migrate from table to table
        for col in empty_cols:
            sql = "ALTER TABLE temporary_table ADD COLUMN \"%s\" text" % col
            self.cursor.execute(sql)

        # Make a big flat list for insertion into target model's table
        flat_special_cols = [
            itm for sl in column_types.values() for itm in sl
        ]

        # Build the top half of that INSERT statement
        insert_statement = "INSERT INTO \"%s\" (\"" % model._meta.db_table

        if not regular_cols:
            self.cursor.execute("ALTER TABLE temporary_table \
                 ADD COLUMN \"DUMMY_COLUMN\" text")
            self.cursor.execute(
                "ALTER TABLE \"%s\" ADD COLUMN \"%s\" text" % (
                    model._meta.db_table,
                    "DUMMY_COLUMN"
                )
            )
            insert_col_list = "\", \"".join(
                ["DUMMY_COLUMN"] + flat_special_cols
            )
        else:
            insert_col_list = "\", \"".join(
                regular_cols + flat_special_cols
            )

        insert_statement += insert_col_list
        insert_statement += "\")\n"

        # Build SELECT statement for table migration that comes after
        # the INSERT
        select_statement = self._make_pg_select(regular_cols, column_types)

        # Mash them together and run it
        self.cursor.execute(insert_statement + select_statement)

        # Drop the temporary table
        self.cursor.execute('DROP TABLE temporary_table;')

        # Drop any dummy columns we put on the target model
        if not regular_cols:
            self.cursor.execute(
                "ALTER TABLE \"%s\" DROP COLUMN \"%s\""
                % (model._meta.db_table, "DUMMY_COLUMN")
            )

        # Print out the results
        model_count = model.objects.count()
        self.finish_load_message(model_count, csv_count)

    def get_headers(self, csv_path):
        """
        Returns the column headers from the csv as a list.
        """
        with open(csv_path) as infile:
            csv_reader = csv.reader(infile)
            headers = csv_reader.next()
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
            if model_count != csv_count:
                msg = '  Table Record count doesn\'t match CSV. \
Table: %s\tCSV: %s'
                self.failure(msg % (
                    model_count,
                    csv_count,
                ))

    def _get_pg_column_types(self, model, csv_headers):
        """
        Get the columns postgresql will have to treate
        differently on a case by base basis on insert
        """
        int_cols = []
        numeric_cols = []
        date_cols = []
        time_cols = []
        regular_cols = []
        double_cols = []
        empty_cols = []

        # fill in those column types
        for col in model._meta.fields:
            if col.db_type(connection).startswith('integer'):
                int_cols.append(col.db_column)
            elif col.db_type(connection).startswith('numeric'):
                numeric_cols.append(col.db_column)
            elif col.db_type(connection).startswith('date'):
                date_cols.append(col.db_column)
            elif col.db_type(connection).startswith('timestamp'):
                time_cols.append(col.db_column)
            elif col.db_type(connection).startswith('double'):
                double_cols.append(col.db_column)
            else:
                if col.db_column is not None and col.db_column in csv_headers:
                    regular_cols.append(col.db_column)

        extra_cols = set([col.db_column for col in
                          model._meta.fields]).difference(set(csv_headers))

        for col in extra_cols:
            if col is not None:
                empty_cols.append(col)

        return {
            "int_cols": int_cols,
            "numeric_cols": numeric_cols,
            "date_cols": date_cols,
            "time_cols": time_cols,
            "regular_cols": regular_cols,
            "double_cols": double_cols,
            "empty_cols": empty_cols
        }

    def _make_date_case(self, _col):
        """
        This method takes in a column name and generates a
        PostgreSQL "case" for correct insertion into the primary table.
        It cleans "date" types to be properly formatted for postgresql
        -----
        it takes in format 'MM/DD/YYYY' or longer timestamps and strips
        the first 10 characters
        if empty it enters '01/01/1900'
        """
        return """
        ,CASE
            WHEN "%(col)s" IS NOT NULL AND "%(col)s" != ''
                THEN to_date(substring("%(col)s" from 1 for 10), 'MM/DD/YYYY')
            ELSE null
        END AS "%(col)s"\n""" % dict(col=_col)

    def _make_int_case(self, _col):
        """
        This method takes in a column name and generates a
        PostgreSQL "case" for correct insertion into the primary table.
        It cleans "int" types to be properly formatted for postgresql
        (and helps to clean up incorrectly entered data)
        """
        return """
        ,CASE
            WHEN "%s" = ''
                THEN NULL
            WHEN "%s" = '          '
                THEN NULL
            WHEN "%s" = '         '
                THEN NULL
            WHEN "%s" = 'Y'
                THEN 1
            WHEN "%s" = 'y'
                THEN 1
            WHEN "%s" = 'X'
                THEN 1
            WHEN "%s" = 'x'
                THEN 1
            WHEN "%s" = 'N'
                THEN 0
            WHEN "%s" = 'n'
                THEN 0
            WHEN "%s" IS NOT NULL
                THEN "%s"::int
        END AS "%s"\n""" % (
            _col, _col, _col, _col, _col, _col,
            _col, _col, _col, _col, _col, _col)

    def _make_numeric_case(self, _col):
        """
        This method takes in a column name and generates a
        PostgreSQL "case" for correct insertion into the primary table.
        It cleans "numeric" types to be properly
        formatted for postgresql (and clean up incorrectly entered data)
        ----
        If the data is blank or Null 0.0 will be inserted
        """
        return """
        ,CASE
            WHEN "%s" = ''
                THEN 0.0
            WHEN "%s" IS NULL
                THEN 0.0
            WHEN "%s" IS NOT NULL
                THEN "%s"::numeric
        END AS "%s"\n""" % (_col, _col, _col, _col, _col)

    def _make_float_case(self, _col):
        """
        This method takes in a column name and generates a
        PostgreSQL "case" for correct insertion into the primary table.
        It cleans "numeric" types to be properly
        formatted for postgresql (and clean up incorrectly entered data)
        ----
        If the data is blank or Null 0.0 will be inserted
        """
        return """
        ,CASE
            WHEN "%s" = ''
                THEN 0.0
            WHEN "%s" IS NULL
                THEN 0.0
            WHEN "%s" IS NOT NULL
                THEN "%s"::double precision
        END AS "%s"\n""" % (_col, _col, _col, _col, _col)

    def _make_timestamp_case(self, _col):
        """
        This method takes in a column name and generates a
        PostgreSQL "case" for correct insertion into the primary table.

        It cleans "timestamp" from a form "7/9/2014 12:00:00 AM" or
        enters it as null if empty
        """
        return """
        ,CASE
            WHEN "%(col)s" IS NOT NULL AND "%(col)s" != ''
                THEN to_timestamp("%(col)s", 'MM/DD/YYYY HH12:MI:SS AM')
            ELSE null
        END AS "%(col)s"\n""" % dict(col=_col)

    def _make_special_not_null_case(self, _col):
        """
        This method takes in a column name and generates a
        PostgreSQL "case" for correct insertion into the primary table.

        It takes in empty columns that are in the csv and formats
        then to be inserted correctly
        """
        return """
        ,CASE
            WHEN "%s" IS NULL
                THEN ''
        END AS "%s"\n""" % (_col, _col)

    def _make_pg_select(self, regular_cols, special_cols):
        """
        Returns a SELECT statement that will pull data from our temporary
        table and transform data types where necessary.
        """
        select_statement = "SELECT \""
        if not regular_cols:
            select_statement += "\", \"".join(["DUMMY_COLUMN"])
        else:
            select_statement += "\", \"".join(regular_cols)
        select_statement += "\"\n"

        # Add in special formatting
        for col_type, ls in special_cols.items():
            if col_type == "int_cols":
                select_statement += '\n'.join(
                    [self._make_int_case(col) for col in ls]
                )
            elif col_type == "numeric_cols":
                select_statement += '\n'.join(
                    [self._make_numeric_case(col) for col in ls]
                )
            elif col_type == "date_cols":
                select_statement += '\n'.join(
                    [self._make_date_case(col) for col in ls]
                )
            elif col_type == "time_cols":
                select_statement += '\n'.join(
                    [self._make_timestamp_case(col) for col in ls]
                )
            elif col_type == "double_cols":
                select_statement += '\n'.join(
                    [self._make_float_case(col) for col in ls]
                )
            elif col_type == "empty_cols":
                select_statement += '\n'.join(
                    [self._make_special_not_null_case(col) for col in ls]
                )

        # Finalize from statement
        select_statement += "FROM temporary_table;"
        return select_statement
