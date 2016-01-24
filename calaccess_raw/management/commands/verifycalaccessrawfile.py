from __future__ import unicode_literals
from django.apps import apps
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand):
    help = 'Compare the number of records in a model against its source CSV'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            'model_name',
            help="Name of the model to verify"
        )

    def handle(self, **options):
        self.log(" Verifying %s" % options['model_name'])

        # Get the model
        model = apps.get_model(options['app_name'], options['model_name'])

        # Get the db total
        model_count = model.objects.count()

        # Get the CSV total
        csv_path = model.objects.get_csv_path()

        with open(csv_path) as f:
            csv_count = sum(1 for l in f) - 1

        # Report back on how we did
        if model_count == csv_count:
            self.success("  Table record count matches CSV")
        else:
            self.failure('  Table Record count doesn\'t match CSV. \
Table: %s\tCSV: %s' % (
                model_count,
                csv_count,
            ))
