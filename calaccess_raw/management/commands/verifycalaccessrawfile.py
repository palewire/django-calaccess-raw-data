from __future__ import unicode_literals
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

            # Take out ids we find in the table.
            #
            # (I bet there is a better way to do this. -rrk)
            #
            for row in model.objects.all():
                foundId = row.id
                ids.remove(foundId)

            if len(ids) > 0:
                self.failure('    ids: %s' % ids)

                # Read the bad lines from the TSV file
                #
                # Is there a way to ignore the first line in the for-loop?
                # Then I would not need check on the if, which seems smelly.
                #
                with open(model.objects.get_tsv_path()) as tsv_lines:
                    for line in tsv_lines:
                        line_id = line.split('\t')[0]
                        line = line.encode('string_escape')
                        line = line.encode('ascii', 'ignore')
                        if line_id == 'id':
                            self.failure('\n    hdr: %s' % line)
                        else:
                            # Show the line above and the line below
                            # the problem line, also.
                            #
                            # Why 3 times? Because using 'or' gives too long
                            # a line, just like this line....
                            #
                            if (int(line_id) + 1) in ids:
                                self.failure('\n    tsv: %s' % line)
                            if int(line_id) in ids:
                                self.failure('    tsv: %s' % line)
                            if (int(line_id) - 1) in ids:
                                self.failure('    tsv: %s' % line)


                # Read the bad lines from the CSV file.
                # Recall that the number is surrounded by double-quotes.
                #
                # A bunch of this string "fixing" here and above is probably
                # I keep getting this error from one of the 'encode's.
                #
                #   TypeError: must be string, not unicode
                #
                #with open(model.objects.get_csv_path()) as csv_lines:
                #    for line in csv_lines:
                #        line_id = line.split(',')[0].replace('"', '')
                #        line = line.encode('ascii','ignore')
                #        line = line.encode(encoding='string_escape')
                #        line = line.replace('\r', '').replace('\n', '')
                #        if line_id == 'id':
                #            self.failure('    hdr: %s' % line)
                #        if line_id != 'id' and int(line_id) in ids:
                #            self.failure('    csv: %s' % line)
