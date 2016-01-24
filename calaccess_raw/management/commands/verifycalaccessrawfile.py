from __future__ import unicode_literals
from django.apps import apps
from calaccess_raw.management.commands import CalAccessCommand
from django.contrib.humanize.templatetags.humanize import intcomma


class Command(CalAccessCommand):
    help = 'Compare the number of records in a model against its source CSV'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('model_name', help="Name of model to verify")
        parser.add_argument(
            "-a",
            "--app-name",
            dest="app_name",
            default="calaccess_raw",
            help="Name of Django app where model will be imported from"
        )

    def handle(self, **options):
        self.log(" Verifying %s" % options['model_name'])

        # Get the model total
        model = apps.get_model(options['app_name'], options['model_name'])
        model_count = model.objects.count()

        # Get the CSV total
        csv_path = model.objects.get_csv_path()
        with open(csv_path) as f:
            csv_count = sum(1 for l in f) - 1

        # Report back on how we did
        if model_count == csv_count:
            self.success("  Record count matches CSV")
        else:
            self.failure("  Record count does not match CSV")
            self.failure("  - Model: %s" % intcomma(model_count))
            self.failure("  - CSV: %s" % intcomma(csv_count))
