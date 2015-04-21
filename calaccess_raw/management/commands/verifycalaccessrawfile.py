from __future__ import unicode_literals
from optparse import make_option
from django.db.models.loading import get_model
from django.core.management.base import LabelCommand
from calaccess_raw.management.commands import CalAccessCommand
import os


class Command(CalAccessCommand, LabelCommand):

    option_list = LabelCommand.option_list + (
        make_option(
            '--create-diff',
            action="store_true",
            dest="create_diff",
            help="Create a difference file for the TSV and the database."
        ),
        make_option(
            '--missing-ids',
            action="store_true",
            dest="missing_ids",
            default=False,
            help="List the id values which are found in the \
TSV file but not the database."
        ),
    )

    help = """
Compare the number of records in a model
against its source CSV and TSV and show the missing ids.

Using --create-diff will generate a new copy of the
TSV file from the database table, thus showing what
was missed.

Using --missing-ids will generate a list of the ids that
are found in the TSV file but missing from the database.
"""
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

                for row in model.objects.all().order_by('id'):
                    next_ids.append(int(row.id))

                    next_row = []

                    for col_name in col_names.split('\t'):

                        field_name = col_name.lower()
                        if field_name == 'hdrcomment':
                            field_name = 'hdr_comment'

                        next_row.append(str(getattr(row, field_name)))

                    next_file.write('\t'.join(next_row) + '\r\n')

                next_file.close()
                self.failure('    compare: %s %s' %
                             (model.objects.get_tsv_path(), next_file_name))

            # Find the ids that are missing from the database
            #
            if options['missing_ids']:

                # if we did create_diffs, we already created this list.
                #
                if not create_diff:
                    for row in model.objects.all().order_by('id'):
                        next_ids.append(int(row.id))

                with open(model.objects.get_tsv_path()) as f:
                    last_line = tail(f)

                highest_id = int(last_line[0].split('\t')[0])

                missing_ids = list(set(range(1, highest_id + 1)) -
                                   set(next_ids))
                self.failure('    missing_ids: %s' % missing_ids)


def tail(f, lines=1, _buffer=4098):
    """Tail a file and get X lines from the end"""
    # place holder for the lines found
    lines_found = []

    # block counter will be multiplied by buffer
    # to get the block size from the end
    block_counter = -1

    # loop until we find X lines
    while len(lines_found) < lines:
        try:
            f.seek(block_counter * _buffer, os.SEEK_END)
        except IOError:  # file is too small, or too many lines requested
            f.seek(0)
            lines_found = f.readlines()
            break

        lines_found = f.readlines()

        # we found enough lines, get out
        if len(lines_found) > lines:
            break

        # decrement the block counter to get the
        # next X bytes
        block_counter -= 1

    return lines_found[-lines:]
