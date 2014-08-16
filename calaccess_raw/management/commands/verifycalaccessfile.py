import csv
from django.db.models.loading import get_model
from django.core.management.base import LabelCommand


class Command(LabelCommand):
    help = 'Compare the number of records in a model against its source CSV'
    args = '<model name>'

    def handle_label(self, label, **options):
        print "- Verifying %s" % label

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
            print "-- Record counts match"
        else:
            print '-- Records don\'t match. Table: %s\tCSV: %s' % (
                cnt,
                csv_record_cnt,
            )
