from __future__ import unicode_literals
from django.db.models.loading import get_model
from django.core.management.base import LabelCommand
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.models.other import Verification


class Command(CalAccessCommand, LabelCommand):
    help = 'Compare the number of records in a model against its source CSV'
    args = '<model name>'

    def handle_label(self, label, **options):
        self.log(" Verifying %s" % label)

        # Get the model
        model = get_model("calaccess_raw", label)

        # Get the db total
        db_cnt = model.objects.count()

        # Get the CSV total, remembering not to count the header line
        csv_cnt = sum(1 for line in open(model.objects.get_csv_path())) - 1

        # Get the TSV total, remembering not to count the header line
        tsv_cnt = sum(1 for line in open(model.objects.get_tsv_path())) - 1

        if db_cnt == csv_cnt and csv_cnt == tsv_cnt:
            self.success('  Table record count matches CSV and TSV')
        else:
            self.failure('  Table Record count doesn\'t match CSV or TSV.')
            self.failure('    table # %d  CSV # %d  TSV # %d' % (
                db_cnt,
                csv_cnt,
                tsv_cnt,
            ))

            # Read the highest id value from the TSV file
            #
            highest_id = model.objects.get_highest_id()

            # Find id values that do not appear in the table
            #
            ids = range(1, highest_id + 1)

            # Does not work, so loop through the rows.
            #
            # found_ids = map(id, model.objects.all())

            found_ids = []
            for row in model.objects.all():
                found_ids.append(row.id)

            missing_ids = list(set(ids) - set(found_ids))

            if len(missing_ids) > 0:
                self.failure('    missing_ids: %s' % missing_ids)

                Verification.objects.filter(table_name=model.__name__).delete()

                for missing_id in missing_ids:
                    Verification(
                        table_name=model.__name__,
                        table_id=missing_id).save()
