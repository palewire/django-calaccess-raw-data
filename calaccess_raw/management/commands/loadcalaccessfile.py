import csv
from django.db import connection, transaction
from django.db.models.loading import get_model
from django.core.management.base import LabelCommand


class Command(LabelCommand):
    help = 'Load a cleaned CalAccess file for a model into the database'
    args = '<model name>'
    # Trick for reformating date strings in source data so that they can
    # be gobbled up by MySQL. You'll see how below.
    date_sql = "DATE_FORMAT(str_to_date(@`%s`, '%%c/%%e/%%Y'), '%%Y-%%m-%%d')"

    def handle_label(self, label, **options):
        self.verbosity = options.get("verbosity")
        self.load(label)

    def load(self, model_name):
        """
        Loads the source CSV for the provided model.
        """
        if self.verbosity:
            print "- Loading %s" % model_name

        model = get_model("calaccess_raw", model_name)
        csv_path = model.objects.get_csv_path()

        # Flush
        c = connection.cursor()
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
                print "-- Record counts match"
            else:
                print '-- Records don\'t match. Table: %s\tCSV: %s' % (
                    cnt,
                    csv_record_cnt,
                )
