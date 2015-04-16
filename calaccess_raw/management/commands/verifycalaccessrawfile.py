from __future__ import unicode_literals
from django.db import connection
from optparse import make_option
from django.db.models.loading import get_model
from django.core.management.base import LabelCommand
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand, LabelCommand):

    option_list = LabelCommand.option_list + (
        make_option(
            '--create-diff',
            action="store_true",
            dest="create_diff",
            help="Create a difference file for the TSV and the database."
        ),
    )

    help = 'Compare the number of records in a model \
against its source CSV and TSV and show the missing ids. \
\
Using -create-diff will generate a new copy of the \
TSV file from the database table, thus showing what \
was missed.'
    args = '<model name>'

    def handle_label(self, label, **options):
        self.log(" Verifying %s" % label)

        create_diff = options['create_diff']

        # Get the model
        model = get_model("calaccess_raw", label)

        # Get the counts of id values in the files and the database
        tsv_cnt = sum(1 for line in open(model.objects.get_tsv_path())) - 1
        csv_cnt = sum(1 for line in open(model.objects.get_csv_path())) - 1
        db_cnt = model.objects.count()

        if tsv_cnt == csv_cnt == db_cnt:
            self.success('  Table record counts match in CSV, TSV, and db')
        else:
            self.failure('  Table Record counts NOT match in TSV, CSV or db.')
            self.failure('    table # %d, CSV # %d, TSV # %d' %
                         (db_cnt, csv_cnt, tsv_cnt))

            # If the -create-diff option is set, create a new version of the
            # TSV file from the database table.
            #
            # If not, just get the ids from the table and check against the
            # TSV file to find the missing ids.
            #
            next_ids = []

            if create_diff:

                with open(model.objects.get_tsv_path()) as f:
                    col_names = f.readline().replace('\r\n', '')

                next_file_name = model.objects.get_tsv_path().replace(
                    '.TSV',
                    '_DERIVED.TSV')

                next_file = open(next_file_name, 'w')
                next_file.write(col_names + '\r\n')

            for row in model.objects.all():
                next_ids.append(str(row.id))

                if create_diff:

                    next_row = []

                    for col_name in col_names.split('\t'):

                        field_name = col_name.lower()
                        if field_name == 'hdrcomment':
                            field_name = 'hdr_comment'

                        next_row.append(str(getattr(row, field_name)))

                    next_file.write('\t'.join(next_row) + '\r\n')

            if create_diff:
                next_file.close()
                self.failure('    compare: %s %s' %
                             (model.objects.get_tsv_path(), next_file_name))

            # Find the ids that are missing from the database
            #
            with open(model.objects.get_tsv_path()) as f:
                f.readline()
                original_ids = []
                for line in f:
                    try:
                        original_ids.append(str(line.split('\t')[0]))
                    except UnicodeDecodeError:
                        self.failure('    UnicodeDecodeError: "%s"' %
                                     unicode(line, 'utf-8'))

            missing_ids = list(set(original_ids) - set(next_ids))
            self.failure('    missing_ids: %s' % missing_ids)
