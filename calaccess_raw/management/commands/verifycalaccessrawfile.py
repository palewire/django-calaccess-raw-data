from __future__ import unicode_literals
from django.apps import apps
from django.core.management.base import LabelCommand
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand, LabelCommand):
    help = 'Compare the number of records in a model against its source CSV'
    args = '<model name>'

    def handle_label(self, label, **options):
        self.log(" Verifying %s" % label)

        # Get the model
        app = apps.get_app_config("calaccess_raw")
        model = app.get_model(label)

        # Get the db total
        cnt = model.objects.count()

        # Get the CSV total
        csv_path = model.objects.get_csv_path()

        with open(csv_path) as f:
            csv_record_cnt = sum(1 for l in f) - 1

        # Report back on how we did
        if cnt == csv_record_cnt:
            self.success("  Table record count matches CSV")
        else:
            self.failure('  Table Record count doesn\'t match CSV. \
Table: %s\tCSV: %s' % (
                cnt,
                csv_record_cnt,
            ))
