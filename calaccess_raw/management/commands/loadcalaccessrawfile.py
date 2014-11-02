import csv
from django.db import connection
from django.conf import settings
from django.utils import dateparse
from django.db import IntegrityError, DataError
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

    def load_postgresql(self, model, csv_path):
        c = connection.cursor()
        c.execute('TRUNCATE TABLE "%s"' % model._meta.db_table)

        headers = []

        infile = open(csv_path)
        reader = csv.reader(infile)
        headers = reader.next()
        header_enum = dict(enumerate(headers))

        date_fields = dict([(count, h) for count, h 
            in enumerate(headers)
            if h in model.DATE_FIELDS])

        integer_fields = [col.db_column for col 
            in model._meta.fields 
            if col.db_type(connection).startswith("integer")]
            
        field_col_name_map = dict([(col.db_column, col.name) for col 
            in model._meta.fields
            if col.db_column != None])

        error_reports = {
            "d":0,
            "v":0,
            "i":0
        }
        ds = []
        vs = []
        iss = []
        for row in reader:
            for z in date_fields.keys():# Take care of Date Fields
                dt = dateparse.parse_date(row[z])
                if dt:
                    row[z] = dt.strftime("%Y-%m-%d")
                else:
                    row[z] = None
            insert = {} # Get our insert dictionary ready
            for index, index_name in header_enum.items(): 
                if index_name in integer_fields:
                    try:
                        insert[field_col_name_map[index_name]] = int(row[index])
                    except ValueError as v:
                        vs.append(v.message.split('\n')[0])
                        error_reports["v"] += 1
                else:
                    insert[field_col_name_map[index_name]] = row[index]
            try: # try making the model...
                model.objects.create(**insert)
            except DataError as d:
                ds.append(d.message.split('\n')[0])
                error_reports["d"] += 1
            except ValueError as v:
                vs.append(v.message.split('\n')[0])
                error_reports["v"] += 1
            except IntegrityError as i:
                iss.append(i.message.split('\n')[0])
                error_reports["i"] += 1

        print set(ds), set(vs), set(iss)
        self.failure("Integrity Errors: %d, Data Errors: %d, Value Errors: %d" % (error_reports["i"],error_reports["d"],error_reports["v"]) )


    def load(self, model_name):
        """
        Loads the source CSV for the provided model.
        """
        if self.verbosity:
            self.log(" Loading %s" % model_name)

        model = get_model("calaccess_raw", model_name)
        csv_path = model.objects.get_csv_path()

        # Flush
        if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.mysql':
            self.load_mysql(model, csv_path)
        elif settings.DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql_psycopg2':
            self.load_postgresql(model, csv_path)
            # self.load_mysql(model, csv_path)
        else:
            self.failure("Sorry that database is not supported")
