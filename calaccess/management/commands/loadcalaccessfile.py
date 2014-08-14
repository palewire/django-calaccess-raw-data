import csv
from django.db import connection, transaction
from django.db.models.loading import get_model
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
        if self.verbosity:
            print "- Loading %s" % model_name

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

        header_sql_list = []
        date_set_list = []
        for h in headers:
            if h in model.DATE_FIELDS:
                header_sql_list.append('@`%s`' % h)
                date_set_list.append("`%s` = DATE_FORMAT(str_to_date(@`%s`, '%%c/%%e/%%Y'), '%%Y-%%m-%%d')" % (h, h))
            else:
                header_sql_list.append('`%s`' % h)

        bulk_sql_load = bulk_sql_load_part_1 + ','.join(header_sql_list) + ')'
        if date_set_list:
            bulk_sql_load += " set %s" % ",".join(date_set_list)

        cnt = c.execute(bulk_sql_load)
        transaction.commit_unless_managed()

        # check load, make sure record count matches
        if self.verbosity:
            if cnt == csv_record_cnt:
                print "-- record counts match"
            else:
                print '-- Records don\'t match. Table: %s\tCSV: %s' % (
                    cnt,
                    csv_record_cnt,
                )
