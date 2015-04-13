from __future__ import unicode_literals
from django.db import connection
from django.db.models import Max
from django.db.models.loading import get_model
from django.core.management.base import LabelCommand
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand, LabelCommand):
    help = 'Compare the number of records in a model against its source CSV'
    args = '<model name>'

    def handle_label(self, label, **options):
        self.log(" Verifying %s" % label)

        # Get the model
        model = get_model("calaccess_raw", label)

        # Get the counts of id values in the files and the database
        tsv_cnt = sum(1 for line in open(model.objects.get_tsv_path())) - 1
        csv_cnt = sum(1 for line in open(model.objects.get_csv_path())) - 1
        db_cnt = model.objects.count()

        # Read the highest id value from the files and the database
        high_tsv_id = model.objects.get_highest_tsv_id()
        high_csv_id = model.objects.get_highest_csv_id()
        high_db_id = int(model.objects.all().aggregate(Max('id'))['id__max'])

        if tsv_cnt == csv_cnt == db_cnt == high_tsv_id == high_csv_id == high_db_id:
            self.success('  Table record counts and high id values matches in CSV, TSV, and database')
        else:
            self.failure('  Table Record counts or high id values in TSV, CSV or database.')
            self.failure('    table # %d, CSV # %d, TSV # %d' % (db_cnt, csv_cnt, tsv_cnt))

            # Regenerate the TSV file. Since there was a problem, one should see differences.
            #
            with open(model.objects.get_tsv_path()) as f:
                col_names = f.readline().replace('\r\n', '')

            next_file_name = model.objects.get_tsv_path().replace('.TSV', '_DERIVED.TSV')

            next_file = open(next_file_name, 'w')
            next_file.write(col_names + '\r\n')

            # I need to do this because I need the values in the same order as the TSV.
            #
            # The field name is the lower-case version of the column key. Except
            # when it is not.
            #
            for row in model.objects.all():

                next_row = []

                for col_name in col_names.split('\t'):

                    field_name = col_name.lower()
                    if field_name == 'hdrcomment':
                        field_name = 'hdr_comment'

                    next_row.append(str(getattr(row, field_name)))

                next_file.write('\t'.join(next_row) + '\r\n')

            next_file.close()
            self.failure('    compare: %s %s' % (model.objects.get_tsv_path(), next_file_name))
