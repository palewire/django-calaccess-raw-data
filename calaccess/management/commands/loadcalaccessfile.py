import os
import csv
from django.db import connection, transaction
from django.db.models.loading import get_model
from calaccess import get_download_directory
from django.core.management.base import LabelCommand


class Command(LabelCommand):
    help = 'Load a cleaned CalAccess file into the database'
    args = '<file path>'

    def handle_label(self, label, **options):
        # Set options
        self.verbosity = options.get("verbosity")
        # Do it
        self.load(label)

    def load(self, model_name):
        """
        Loads the cleaned up csv files into the database
        Checks record count against csv line count
        A new release of CSVKit has come out and it may
        deal with the encoding issues better.
        You might want to modify the code to use the new CSVKit release
        """
        model = get_model("calaccess", model_name)

        # load up the data
        c = connection.cursor()

        csv_name = model.objects.get_csv_name()
        csv_path = model.objects.get_csv_path()

        c.execute('DELETE FROM %s' % model._meta.db_table)

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

        sql_fields = ['`%s`' % h for h in headers]
        bulk_sql_load = bulk_sql_load_part_1 + ','.join(sql_fields) + ')'

        cnt = c.execute(bulk_sql_load)
        transaction.commit_unless_managed()

        # check load, make sure record count matches
        if self.verbosity:
            if cnt == csv_record_cnt:
                print "record counts match\t\t\t\t%s" % csv_name
            else:
                print 'table_cnt: %s\tcsv_lines: %s\t\t%s' % (
                    cnt,
                    csv_record_cnt,
                    csv_name
                )
