import os
import csv
from cStringIO import StringIO
from calaccess import get_download_directory
from csvkit import CSVKitReader, CSVKitWriter
from dateutil.parser import parse as dateparse
from django.core.management.base import LabelCommand
from django.template.defaultfilters import date as dateformat


class Command(LabelCommand):
    help = 'Clean a source CalAccess file and reformat it as a CSV'
    args = '<file path>'

    def handle_label(self, label, **options):
        self.verbosity = options.get("verbosity")
        self.data_dir = get_download_directory()
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        self.csv_dir = os.path.join(self.data_dir, "csv/")
        self.clean(label)

    def clean(self, name):
        """
        Clean up the raw data files from the state so they are
        ready to get loaded into the database.
        Keep track of the date fields manually in the date_field_dict
        so we can parse them into a format that works for import.
        """
        if self.verbosity:
            print "Cleaning data files"
        csv.field_size_limit(1000000000)  # Up the CSV data limit

        date_field_dict = {
            'CVR_SO': [
                'ACCT_OPENDT',
                'QUALFY_DT',
            ],
            'CVR_CAMPAIGN_DISCLOSURE_CD': [
                'ELECT_DATE',
                'FROM_DATE',
                'RPT_DATE',
                'RPTFROMDT',
                'RPTTHRUDT',
                'THRU_DATE'
            ],
            'CVR_LOBBY_DISCLOSURE_CD': [
                'CUM_BEG_DT',
                'FROM_DATE',
                'RPT_DATE',
                'SIG_DATE',
                'THRU_DATE'
            ],
            'CVR_REGISTRATION_CD': [
                'COMPLET_DT',
                'EFF_DATE',
                'QUAL_DATE',
                'RPT_DATE',
                'SIG_DATE'
            ],
            'EXPN_CD': [
                'EXPN_DATE'
            ],
            'FILERNAME_CD': [
                'EFFECT_DT'
            ],
            'FILER_FILINGS_CD': [
                'FILING_DATE',
                'RPT_START',
                'RPT_END',
                'RPT_DATE'
            ],
            'FILER_INTERESTS_CD': [
                'EFFECT_DATE'
            ],
            'FILER_LINKS_CD': [
                'EFFECT_DT',
                'TERMINATION_DT'
            ],
            'FILER_TO_FILER_TYPE_CD': [
                'EFFECT_DT',
                'NYQ_DT'
            ],
            'FILER_XREF_CD': [
                'EFFECT_DT'
            ],
            'FILING_PERIOD_CD': [
                'START_DATE',
                'END_DATE',
                'DEADLINE'
            ],
            'LATT_CD': [
                'CUMBEG_DT',
                'PMT_DATE',
            ],
            'LCCM_CD': [
                'CTRIB_DATE',
            ],
            'LEMP_CD': [
                'EFF_DATE'
            ],
            'LEXP_CD': [
                'EXPN_DATE'
            ],
            'LOAN_CD': [
                'LOAN_DATE1',
                'LOAN_DATE2'
            ],
            'LOBBY_AMENDMENTS_CD': [
                'ADD_L_EFF',
                'ADD_LE_EFF',
                'ADD_LF_EFF',
                'DEL_LF_EFF',
                'OTHER_EFF'
            ],
            'LOTH_CD': [
                'PMT_DATE',
            ],
            'RCPT_CD': [
                'DATE_THRU',
                'RCPT_DATE'
            ],
            'SMRY_CD': [
                'ELEC_DT'
            ],
            'S496_CD': [
                'EXP_DATE',
                'DATE_THRU',
            ],
            'S497_CD': [
                'ELEC_DATE',
                'CTRIB_DATE',
                'DATE_THRU',
            ],
            'S498_CD': [
                'DATE_RCVD',
            ],
        }

        if self.verbosity:
            print "- %s" % name

        # Pull the data into memory
        tsv_path = os.path.join(self.tsv_dir, name)
        tsv_data = open(tsv_path, 'rb').read()

        # Nuke any null bytes
        null_bytes = tsv_data.count('\x00')
        if null_bytes:
            tsv_data = tsv_data.replace('\x00', ' ')

        # Nuke ASCII 26 char, the "substitute character"
        # or chr(26) in python
        sub_char = tsv_data.count('\x1a')
        if sub_char:
            tsv_data = tsv_data.replace('\x1a', '')

        # Convert the file to a CSV line by line.
        csv_path = os.path.join(
            self.csv_dir,
            name.lower().replace("tsv", "csv")
        )
        csv_file = open(csv_path, 'wb')
        csv_writer = CSVKitWriter(csv_file, quoting=csv.QUOTE_ALL)
        if tsv_data == '':
            if self.verbosity:
                print 'no data in %s' % name
            return
        else:
            tsv_reader = StringIO(tsv_data)

        headers = tsv_reader.next()
        headers = headers.decode("ascii", "replace").encode('utf-8')
        headers_csv = CSVKitReader(StringIO(headers), delimiter='\t')
        headers_list = headers_csv.next()
        csv_writer.writerow(headers_list)

        line_number = 1
        for tsv_line in tsv_reader:
            # Goofing around with the encoding while we're in there.
            tsv_line = tsv_line.decode("ascii", "replace").encode('utf-8')
            # choking on fields with bad quoting again
            # eg. '"HEIGHT AIN\'T RIGHT DOWNTOWN\'',
            # quotes aren't closed
            try:
                csv_line = CSVKitReader(StringIO(tsv_line), delimiter='\t')
                # csv_line_date_cleaned = date_clean_csv_line(
                #    csv_line.next()
                # )
                # csv_writer.writerow(csv_line_date_cleaned)
                csv_field_list = csv_line.next()
            except:
                tsv_clean_line = ''.join(
                    c for c in tsv_line if c not in ('"', "'")
                )  # so strip all quotes for now
                csv_line = CSVKitReader(
                    StringIO(tsv_clean_line),
                    delimiter='\t'
                )
                # csv_line_date_cleaned = date_clean_csv_line(
                #     csv_line.next()
                # )
                # csv_writer.writerow(csv_line_date_cleaned)
                csv_field_list = csv_line.next()

            if len(csv_field_list) == len(headers_list):
                if name.replace('.TSV', '') in date_field_dict:
                    date_field_list = date_field_dict[name.replace(
                        '.TSV', ''
                    )]
                    for f in date_field_list:
                        if csv_field_list[headers_list.index(f)] != '':
                            try:
                                k = headers_list.index(f)
                                csv_field_list[k] = dateformat(
                                    dateparse(csv_field_list[k]), 'Y-m-d')
                            except:
                                if self.verbosity:
                                    print '+ INVALID DATE: %s\t%s\t%s' % (
                                        name,
                                        f,
                                        csv_field_list[k]
                                    )
                                    csv_field_list[k] = ''
            else:
                if self.verbosity:
                    print '+ %s bad parse of %s headers=%s & line=%s' % (
                        name,
                        line_number,
                        len(headers_list),
                        len(csv_field_list)
                    )
            csv_writer.writerow(csv_field_list)
            line_number += 1

        # Shut it down
        tsv_reader.close()
        csv_file.close()
