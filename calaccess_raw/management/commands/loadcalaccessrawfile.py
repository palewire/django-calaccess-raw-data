import csv
from django.db import connection
from django.conf import settings
from django.utils import dateparse
from django.db import IntegrityError, DataError, ProgrammingError
from django.db.models.loading import get_model
from django.core.management.base import LabelCommand
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand, LabelCommand):
    help = 'Load a cleaned CalAccess file for a model into the database'
    args = '<model name>'
    # Trick for reformating date strings in source data so that they can
    # be gobbled up by MySQL. You'll see how below.
    date_sql = "DATE_FORMAT(str_to_date(@`%s`, '%%c/%%e/%%Y'), '%%Y-%%m-%%d')"

    def handle_label(self, label, **options):
        self.verbosity = options.get("verbosity")
        self.load(label)

    def _make_date_case(self, _col):
        return """
        ,CASE
            WHEN "%s" IS NOT NULL AND "%s" != ''
                THEN to_date(substring("%s" from 1 for 10), 'MM/DD/YYYY')
            WHEN "%s" = ''
                THEN to_date('01/01/1900', 'MM/DD/YYYY')
        END AS "%s"\n""" % (_col, _col, _col, _col, _col)

    def _make_int_case(self, _col):
        return """
        ,CASE
            WHEN "%s" = ''
                THEN 0
            WHEN "%s" IS NULL
                THEN 0
            WHEN "%s" IS NOT NULL
                THEN "%s"::int
        END AS "%s"\n""" % (_col, _col, _col, _col, _col)

    def load_postgresql(self, model, csv_path):
        c = connection.cursor()
        try:
            c.execute('DROP TABLE temporary_table;')
        except ProgrammingError:
            pass
        # clear our table
        c.execute('TRUNCATE TABLE "%s"' % model._meta.db_table)

        # get header names + future length
        with open(csv_path) as infile:
            reader = csv.reader(infile)
            headers = reader.next()
            csv_count = sum([1 for row in reader])

        #map column name (csv) to column name (table)
        name_to_type_map = dict([(col.db_column, col.db_type(connection))
                                for col in model._meta.fields])

        # break out special case column types
        int_columns = []
        date_columns = []
        regular_columns = []

        #fill in those column types
        for col in model._meta.fields:
            if col.db_type(connection).startswith('integer'):
                int_columns.append(col.db_column)
            elif col.db_type(connection).startswith('date'):
                date_columns.append(col.db_column)
            else:
                # if col.db_column is not None and col.db_column in headers:
                if col.db_column is not None:
                    regular_columns.append(col.db_column)

        col_w_types = []  # column with its types
        for col in headers:
            if col not in int_columns and col not in date_columns:
                col_w_types.append("\"" + col + "\"\t" + name_to_type_map[col])
            else:
                col_w_types.append("\"" + col + "\"\ttext")

        # create the temp table w/ columns with types
        c.execute("CREATE TABLE \"temporary_table\" (%s);"
                  % ',\n'.join(col_w_types))

        temp_insert = """COPY "temporary_table"
            FROM '%s'
            CSV
            HEADER;""" % (csv_path)

        c.execute(temp_insert)  # insert everything into the temp table

        # build our insert statement
        insert_statement = "INSERT INTO \"%s\" (\"" % model._meta.db_table
        r_d_i = "\", \"".join(regular_columns + date_columns + int_columns)
        insert_statement += r_d_i
        insert_statement += "\")\n"
        # add in the select part for table migration
        select_statement = "SELECT \""
        select_statement += "\", \"".join(regular_columns)
        select_statement += "\"\n"
        # add in special formatting
        for dcol in date_columns:
            select_statement += self._make_date_case(dcol)
        for icol in int_columns:
            select_statement += self._make_int_case(icol)
        # finalize from statement
        select_statement += "FROM temporary_table;"

        try:
            c.execute(insert_statement + select_statement)
        except DataError as e:
            # print insert_statement + select_statement
            # print int_columns
            print "dataerror error, ", e
        except ProgrammingError as e:
            # print insert_statement + select_statement
            # print int_columns
            print "programming error, ", e
        except IntegrityError as e:
            # print insert_statement + select_statement
            # print int_columns
            print "IntegrityError error, ", e

        c.execute('DROP TABLE temporary_table;')
        if self.verbosity:
            model_count = model.objects.count()
            if model_count == csv_count:
                self.success("  Table record count matches CSV")
            else:
                msg = '  Table Record count doesn\'t match CSV. \
Table: %s\tCSV: %s'
                self.failure(msg % (model_count, csv_count))


    def load_mysql(self, model, csv_path):
        c = connection.cursor()
        # flush
        c.execute('TRUNCATE TABLE %s' % model._meta.db_table)

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
        headers = csv_reader.next()
        infile.close()

        infile = open(csv_path)
        csv_record_cnt = len(infile.readlines()) - 1
        infile.close()

        header_sql_list = []
        date_set_list = []
        for h in headers:
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
        cnt = c.execute(bulk_sql_load)
        # Report back on how we did
        if self.verbosity:
            if cnt == csv_record_cnt:
                self.success("  Table record count matches CSV")
            else:
                msg = '  Table Record count doesn\'t match CSV. \
Table: %s\tCSV: %s'
                self.failure(msg % (
                    cnt,
                    csv_record_cnt,
                ))

    def load(self, model_name):
        """
        Loads the source CSV for the provided model.
        """
        if self.verbosity:
            self.log(" Loading %s" % model_name)

        model = get_model("calaccess_raw", model_name)
        csv_path = model.objects.get_csv_path()

        # Flush
        engine = settings.DATABASES['default']['ENGINE']
        if engine == 'django.db.backends.mysql':
            self.load_mysql(model, csv_path)
        elif engine == 'django.db.backends.postgresql_psycopg2':
            self.load_postgresql(model, csv_path)
        else:
            self.failure("Sorry that database is not supported")
