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

        # Get the db total
        cnt = model.objects.count()

        # Get the CSV total
        csv_path = model.objects.get_csv_path()
        infile = open(csv_path)
        csv_record_cnt = len(infile.readlines()) - 1
        infile.close()

        # Report back on how we did
        if cnt == csv_record_cnt:
            self.success("  Table record count matches CSV")
        else:
            self.failure('  Table Record count doesn\'t match CSV. \
Table: %s\tCSV: %s' % (
                cnt,
                csv_record_cnt,
            ))
