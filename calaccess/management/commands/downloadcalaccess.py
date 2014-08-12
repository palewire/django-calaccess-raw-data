import os
import csv
import shutil
import zipfile
import requests
import progressbar
from cStringIO import StringIO
from hurry.filesize import size
from django.conf import settings
from optparse import make_option
from django.utils.six.moves import input
from calaccess import get_download_directory
from csvkit import CSVKitReader, CSVKitWriter
from django.db import connection, transaction
from dateutil.parser import parse as dateparse
from django.db.models import get_models, get_app
from django.template.defaultfilters import date as dateformat
from django.core.management.base import BaseCommand
from django.contrib.humanize.templatetags.humanize import naturaltime

PROMPT = """
The CalAccess snapshot was last updated %s at %s, %s.

It is %s in size.

Do you want to download the file to %s

Type 'yes' to do it, or 'no' to back out: """


custom_options = (
    make_option(
        "--skip-download",
        action="store_false",
        dest="download",
        default=True,
        help="Skip downloading of the ZIP archive"
    ),
    make_option(
        "--skip-unzip",
        action="store_false",
        dest="unzip",
        default=True,
        help="Skip unzipping of the archive"
    ),
    make_option(
        "--skip-prep",
        action="store_false",
        dest="prep",
        default=True,
        help="Skip prepping of the unzipped archive"
    ),
    make_option(
        "--skip-clear",
        action="store_false",
        dest="clear",
        default=True,
        help="Skip clearing out ZIP archive and extra files"
    ),
    make_option(
        "--skip-clean",
        action="store_false",
        dest="clean",
        default=True,
        help="Skip cleaning up the raw data files"
    ),
    make_option(
        "--skip-load",
        action="store_false",
        dest="load",
        default=True,
        help="Skip loading up the raw data files"
    ),
    make_option(
        "--noinput",
        action="store_true",
        dest="noinput",
        default=False,
        help="Download the ZIP archive without asking permission"
    ),
)


class Command(BaseCommand):
    help = 'Download the latest snapshot of the CalAccess database'
    option_list = BaseCommand.option_list + custom_options

    def set_options(self, *args, **kwargs):
        self.url = 'http://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip'
        self.data_dir = get_download_directory()
        os.path.exists(self.data_dir) or os.mkdir(self.data_dir)
        self.zip_path = os.path.join(self.data_dir, 'calaccess.zip')
        self.tsv_dir = os.path.join(self.data_dir, "tsv/")
        self.csv_dir = os.path.join(self.data_dir, "csv/")
        os.path.exists(self.csv_dir) or os.mkdir(self.csv_dir)
#        self.metadata = self.get_metadata()
#        self.prompt = PROMPT % (
#            dateformat(self.metadata['last-modified'], 'N j, Y'),
#            dateformat(self.metadata['last-modified'], 'P'),
#            naturaltime(self.metadata['last-modified']),
#            size(self.metadata['content-length']),
#            self.data_dir,
#        )
#        self.pbar = progressbar.ProgressBar(
#            widgets=[
#                progressbar.Percentage(),
#                progressbar.Bar(),
#                ' ',
#                progressbar.ETA(),
#                ' ',
#                progressbar.FileTransferSpeed()
#            ],
#            maxval=self.metadata['content-length']
#        )
        self.verbosity = int(kwargs['verbosity'])

    def handle(self, *args, **options):
        """
        If DEBUG is not set to false Django imports will fail on MySQL errors.
        This data comes with a bunch of encoding issues and malformed
        TSV files.

        The import will not be perfect. But the errors should only constitute
        a minority of the total informations.
        """
        # execute the commands if DEBUG is set to False
        if not settings.DEBUG:
            self.set_options(*args, **options)
            if options['download']:
                if options['noinput']:
                    self.download()
                else:
                    confirm = input(self.prompt.encode('utf-8'))
                    if confirm != 'yes':
                        print "Download cancelled."
                        return False
                    self.download()
            if options['unzip']:
                self.unzip()
            if options['prep']:
                self.prep()
            if options['clear']:
                self.clear()
            if options['clean']:
                self.clean()
            if options['load']:
                self.load()
        else:
            print "DEBUG is not set to False. Please change before running \
`downloadcalaccess`"

    def get_metadata(self):
        """
        Returns basic metadata about the current CalAccess snapshot,
        like its size and the last time it was updated, while stopping
        short of actually downloading it.
        """
        request = requests.head(self.url)
        return {
            'content-length': int(request.headers['content-length']),
            'last-modified': dateparse(request.headers['last-modified'])
        }

    def download(self):
        """
        Download the ZIP file in pieces.
        """
        if self.verbosity:
            print "Downloading ZIP file"
        r = requests.get(self.url, stream=True)
        bytes = 0
        self.pbar.start()
        with open(self.zip_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    bytes += len(chunk)
                    self.pbar.update(bytes)
                    f.flush()
        self.pbar.finish()

    def unzip(self):
        """
        Unzip the snapshot file.
        """
        if self.verbosity:
            print "Unzipping archive"
        with zipfile.ZipFile(self.zip_path) as zf:
            for member in zf.infolist():
                words = member.filename.split('/')
                path = self.data_dir
                for word in words[:-1]:
                    drive, word = os.path.splitdrive(word)
                    head, word = os.path.split(word)
                    if word in (os.curdir, os.pardir, ''):
                        continue
                    path = os.path.join(path, word)
                zf.extract(member, path)

    def prep(self):
        """
        Rearrange the unzipped files and get rid of the stuff we don't want.
        """
        if self.verbosity:
            print "Prepping unzipped data"
        # Move the deep down directory we want out
        shutil.move(
            os.path.join(
                self.data_dir,
                'CalAccess/DATA/CalAccess/DATA/'
            ),
            self.data_dir
        )
        # Clear out target if it exists
        if os.path.exists(self.tsv_dir):
            shutil.rmtree(self.tsv_dir)
        # Rename it to the target
        shutil.move(
            os.path.join(self.data_dir, "DATA/"),
            self.tsv_dir,
        )

    def clear(self):
        """
        Delete ZIP archive and files we don't need.
        """
        if self.verbosity:
            print "Clearing out unneeded files"
        shutil.rmtree(os.path.join(self.data_dir, 'CalAccess'))
        os.remove(self.zip_path)

    def clean(self):
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

        # Loop through all the files in the source directory
        for name in os.listdir(self.tsv_dir):
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
                continue
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

    def load(self):
        """
        Loads the cleaned up csv files into the database
        Checks record count against csv line count
        A new release of CSVKit has come out and it may
        deal with the encoding issues better.
        You might want to modify the code to use the new CSVKit release
        """
        # Get a list of tables in the database
        table_list = get_models(get_app("calaccess"))

        # load up the data
        c = connection.cursor()
        for table in table_list:
            csv_name = table.objects.get_csv_name()
            csv_path = table.objects.get_csv_path()

            c.execute('DELETE FROM %s' % table._meta.db_table)

            bulk_sql_load_part_1 = '''
                LOAD DATA LOCAL INFILE '%s'
                INTO TABLE %s
                FIELDS TERMINATED BY ','
                OPTIONALLY ENCLOSED BY '"'
                IGNORE 1 LINES
                (
            ''' % (csv_path, table._meta.db_table)

            infile = open(csv_path)
            csv_reader = CSVKitReader(infile)
            headers = csv_reader.next()
            infile.close()

            infile = open(csv_path)
            csv_record_cnt = len(infile.readlines()) - 1
            infile.close()

            sql_fields = ['`%s`' % h for h in headers]
            bulk_sql_load = bulk_sql_load_part_1 + ','.join(sql_fields) + ')'
            cnt = c.execute(bulk_sql_load)
            transaction.commit_unless_managed()

            # check load, make sure record count matches
            if self.verbosity:
                if cnt == csv_record_cnt:
                    print "record counts match\t\t\t\t%s" % csv_name
                else:
                    print 'table_cnt: %s\tcsv_lines: %s\t\t%s' % (
                        cnt,
                        csv_record_cnt,
                        csv_name
                    )
