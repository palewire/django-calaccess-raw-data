import csv
from django.db import connection
from django.conf import settings
from django.db import IntegrityError, DataError, ProgrammingError
from django.db.models.loading import get_model
from django.core.management.base import LabelCommand
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand, LabelCommand):
    help = 'Load clean CAL-ACCESS file into its corresponding database model'
    args = '<model name>'
    # Trick for reformating date strings in source data so that they can
    # be gobbled up by MySQL. You'll see how below.
    date_sql = "DATE_FORMAT(str_to_date(@`%s`, '%%c/%%e/%%Y'), '%%Y-%%m-%%d')"

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

        # Flush
        self.cursor.execute('TRUNCATE TABLE %s' % model._meta.db_table)

        engine = settings.DATABASES['default']['ENGINE']
        if engine == 'django.db.backends.mysql':
            self.load_mysql(model, csv_path)
        elif engine in (
            'django.db.backends.postgresql_psycopg2'
            'django.contrib.gis.db.backends.postgis'
                ):
            self.load_postgresql(model, csv_path)
        else:
            self.failure("Sorry that database is not supported")

    def get_hdrs_and_cnt(self, csv_path):
        """
        Get the headers and the line count
        from a specified csv file
        """
        with open(csv_path) as infile:
            csv_reader = csv.reader(infile)
            hdrs = csv_reader.next()

        with open(csv_path) as infile:
            csv_count = len(infile.readlines()) - 1

        return hdrs, csv_count

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
            WHEN "%s" IS NOT NULL AND "%s" != ''
                THEN to_date(substring("%s" from 1 for 10), 'MM/DD/YYYY')
            WHEN "%s" = ''
                THEN to_date('01/01/1900', 'MM/DD/YYYY')
        END AS "%s"\n""" % (_col, _col, _col, _col, _col)

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
        ---
        It cleans "timestamp" from a form "7/9/2014 12:00:00 AM" or
        enters it as '01/01/1900 1:00:00 AM' if null or empty
        """
        return """
        ,CASE
            WHEN "%s" IS NOT NULL AND "%s" != ''
                THEN to_timestamp("%s", 'MM/DD/YYYY HH12:MI:SS AM')
            WHEN "%s" = ''
                THEN to_timestamp('01/01/1900 1:00:00 AM', \
                    'MM/DD/YYYY HH12:MI:SS AM')
        END AS "%s"\n""" % (_col, _col, _col, _col, _col)

    def _make_special_not_null_case(self, _col):
        """
        This method takes in a column name and generates a
        PostgreSQL "case" for correct insertion into the primary table.
        ---
        it takes it empty columns that are in the csv and formats
        then to be inserted correctly
        """
        return """
        ,CASE
            WHEN "%s" IS NULL
                THEN ''
        END AS "%s"\n""" % (_col, _col)

    def _get_col_types(self, model, csv_headers, n_2_t_map):
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

        csv_col_types = []  # column with its types
        for col in csv_headers:
            if col in regular_cols:
                csv_col_types.append("\"" + col + "\"\t" + n_2_t_map[col])
            else:
                csv_col_types.append("\"" + col + "\"\ttext")

        extra_cols = set([col.db_column for col in
                          model._meta.fields]).difference(set(csv_headers))

        for col in extra_cols:
            if col is not None:
                empty_cols.append(col)

        return csv_col_types, {
            "int_cols": int_cols,
            "numeric_cols": numeric_cols,
            "date_cols": date_cols,
            "time_cols": time_cols,
            "regular_cols": regular_cols,
            "double_cols": double_cols,
            "empty_cols": empty_cols
            }

    def _make_pg_select(self, regular_cols, special_cols):
        select_statement = "SELECT \""
        if not regular_cols:
            select_statement += "\", \"".join(["DUMMY_COLUMN"])
        else:
            select_statement += "\", \"".join(regular_cols)
        select_statement += "\"\n"
        # add in special formatting

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
        # finalize from statement
        select_statement += "FROM temporary_table;"

        return select_statement

    def load_postgresql(self, model, csv_path):
        """
        Takes a model and a csv_path and loads it into postgresql
        """
        c = connection.cursor()
        try:
            c.execute('DROP TABLE temporary_table;')
        except ProgrammingError:
            pass

        c.execute('TRUNCATE TABLE "%s"' % model._meta.db_table)

        # get the headers and the count
        hdrs, csv_count = self.get_hdrs_and_cnt(csv_path)

        n_2_t_map = {}  # name to type map for columns
        for col in model._meta.fields:
            n_2_t_map[col.db_column] = col.db_type(connection)

        csv_col_types, special_cols = self._get_col_types(
            model, hdrs, n_2_t_map
        )
        regular_cols = special_cols.pop('regular_cols')
        empty_cols = special_cols['empty_cols']

        # make a big flat list for later insertion into the true table
        flat_special_cols = [itm for sl in special_cols.values() for itm in sl]

        # create the temp table w/ columns with types
        try:
            c.execute("CREATE TABLE \"temporary_table\" (%s);"
                      % ',\n'.join(csv_col_types))
        except ProgrammingError:
            self.failure("Temporary table already exists")

        temp_insert = """COPY "temporary_table"
            FROM '%s'
            CSV
            HEADER;""" % (csv_path)

        try:
            c.execute(temp_insert)  # insert everything into the temp table
        except DataError as e:
            print "initial insert dataerror error, ", e

        for col in empty_cols:
            # for tables where we create cases for every column and
            # we need a dummy column in order to migrate from table to table
            c.execute("ALTER TABLE temporary_table \
                ADD COLUMN \"%s\" text" % col)

        # build our insert statement
        insert_statement = "INSERT INTO \"%s\" (\"" % model._meta.db_table
        if not regular_cols:
            try:
                c.execute("ALTER TABLE temporary_table \
                    ADD COLUMN \"DUMMY_COLUMN\" text")
                c.execute("ALTER TABLE \"%s\" ADD COLUMN \"%s\" text"
                          % (model._meta.db_table, "DUMMY_COLUMN"))
                insert_col_list = "\", \"".join(
                    ["DUMMY_COLUMN"] + flat_special_cols
                )
            except ProgrammingError as e:
                self.failure("Error Altering Table: %s" % e)
        else:
            insert_col_list = "\", \"".join(
                regular_cols + flat_special_cols
            )

        insert_statement += insert_col_list
        insert_statement += "\")\n"
        # add in the select part for table migration

        select_statement = self._make_pg_select(regular_cols, special_cols)

        try:
            # print insert_statement + select_statement
            c.execute(insert_statement + select_statement)
        except DataError as e:
                self.failure(
                    "Data Error Inserting Data Into Table: %s" % e)
        except ProgrammingError as e:
                self.failure(
                    "Programming Error Inserting Data Into Table: %s" % e)
        except IntegrityError as e:
                self.failure(
                    "Integrity Error Inserting Data Into Table: %s" % e)

        # c.execute('DROP TABLE temporary_table;')
        if not regular_cols:
            c.execute(
                "ALTER TABLE \"%s\" DROP COLUMN \"%s\""
                % (model._meta.db_table, "DUMMY_COLUMN")
            )

        model_count = model.objects.count()
        self.finish_load_message(model_count, csv_count)

    def load_mysql(self, model, csv_path):
        # flush
        self.cursor.execute('TRUNCATE TABLE %s' % model._meta.db_table)

        # Build the MySQL LOAD DATA INFILE command
        bulk_sql_load_part_1 = '''
            LOAD DATA LOCAL INFILE '%s'
            INTO TABLE %s
            FIELDS TERMINATED BY ','
            OPTIONALLY ENCLOSED BY '"'
            LINES TERMINATED BY '\\r\\n'
            IGNORE 1 LINES
            (
        ''' % (csv_path, model._meta.db_table)

        infile = open(csv_path)
        csv_reader = csv.reader(infile)
        hdrs = csv_reader.next()
        infile.close()

        infile = open(csv_path)
        csv_record_cnt = len(infile.readlines()) - 1
        infile.close()

        header_sql_list = []
        date_set_list = []
        for h in hdrs:
            # If it is a date field, we need to reformat the data
            # so that MySQL will properly parse it on the way in.
            if h in model.DATE_FIELDS:
                header_sql_list.append('@`%s`' % h)
                date_set_list.append(
                    "`%s` =  %s" % (h, self.date_sql % h)
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
