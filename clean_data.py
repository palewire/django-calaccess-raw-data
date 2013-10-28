#!/usr/bin/env python
from env_settings import clean_data_dir, data_root_dir, db_name, db_password, db_user_name
try:
    from csvkit import CSVKitReader, CSVKitWriter
except:
    print 'need to install csvkit for this script to work'
from cStringIO import StringIO
import csv
import os
import sys



'''

To find null bytes

data = open(file_path, 'rb').read()
print data.find('\x00')
print data.count('\x00')

'''

csv.field_size_limit(1000000000)

def remove_quotes(s):
    return ''.join(c for c in s if c not in ('"', "'"))

def process_clean_data(clean_data, file_name):
    print 'working on %s' % file_name
    #infile = open(file_path, 'rb')
    new_csv_name = file_name.lower() + '.csv'
    new_csv_path = os.path.join(clean_data_dir, new_csv_name)
    outfile = open(new_csv_path, 'wb')
    reader = CSVKitReader(StringIO(clean_data))
    writer = CSVKitWriter(outfile, quoting=csv.QUOTE_ALL)
    try:
        for line in reader:
                writer.writerow([remove_quotes(elem) for elem in line])
    except csv.Error, e:
        sys.exit('file %s, line %d: %s' % (new_csv_name, reader.line_num, e))
    outfile.close()

def fix_null_bytes(file_path):
    #print repr(open(file_path, 'rb').read(200)) # dump 1st 200 bytes of file
    data = open(file_path, 'rb').read()
    print data.find('\x00')
    cnt = data.count('\x00')
    print cnt
    if cnt > 0:
        clean_data = data.replace('\x00', ' ')
    else:
        clean_data = data
    return clean_data

def car_wash(clean_data, file_name):
    new_csv_name = file_name.lower() + '.csv'
    new_csv_path = os.path.join(clean_data_dir, new_csv_name)
    outfile = open(new_csv_path, 'wb')
    writer = CSVKitWriter(outfile, quoting=csv.QUOTE_ALL)
    infile = StringIO(clean_data)
    for line in infile:
        l = line.decode("ascii", "replace").encode('utf-8')
        reader = CSVKitReader(StringIO(l), delimiter='\t')
        writer.writerow(reader.next())
    outfile.close()
    infile.close()
    

def fix_all_csv_quoting():
    data_tables = {
        'CVR_CAMPAIGN_DISCLOSURE_CD' : os.path.join(data_root_dir, 'CVR_CAMPAIGN_DISCLOSURE_CD.TSV'),
        'CVR_LOBBY_DISCLOSURE_CD': os.path.join(data_root_dir, 'CVR_LOBBY_DISCLOSURE_CD.TSV'),
        'CVR_REGISTRATION_CD': os.path.join(data_root_dir, 'CVR_REGISTRATION_CD.TSV'),
        'CVR2_CAMPAIGN_DISCLOSURE_CD': os.path.join(data_root_dir, 'CVR2_CAMPAIGN_DISCLOSURE_CD.TSV'),
        'DEBT_CD': os.path.join(data_root_dir, 'DEBT_CD.TSV'),
        'EXPN_CD': os.path.join(data_root_dir, 'EXPN_CD.TSV'),
        'FILER_ACRONYMS_CD': os.path.join(data_root_dir, 'FILER_ACRONYMS_CD.TSV'),
        'FILER_FILINGS_CD': os.path.join(data_root_dir, 'FILER_FILINGS_CD.TSV'),
        'FILER_INTERESTS_CD': os.path.join(data_root_dir, 'FILER_INTERESTS_CD.TSV'),
        'FILER_LINKS_CD': os.path.join(data_root_dir, 'FILER_LINKS_CD.TSV'),
        'FILER_STATUS_TYPES_CD': os.path.join(data_root_dir, 'FILER_STATUS_TYPES_CD.TSV'),
        'FILER_TO_FILER_TYPE_CD': os.path.join(data_root_dir, 'FILER_TO_FILER_TYPE_CD.TSV'),
        'FILER_TYPE_PERIODS_CD': os.path.join(data_root_dir, 'FILER_TYPE_PERIODS_CD.TSV'),
        'FILER_TYPES_CD': os.path.join(data_root_dir, 'FILER_TYPES_CD.TSV'),
        'FILER_XREF_CD': os.path.join(data_root_dir, 'FILER_XREF_CD.TSV'),
        'FILERNAME_CD': os.path.join(data_root_dir, 'FILERNAME_CD.TSV'),
        'FILERS_CD': os.path.join(data_root_dir, 'FILERS_CD.TSV'),
        'FILING_PERIOD_CD': os.path.join(data_root_dir, 'FILING_PERIOD_CD.TSV'),
        'FILINGS': os.path.join(data_root_dir, 'FILINGS_CD.TSV'),
        'LEMP_CD': os.path.join(data_root_dir, 'LEMP_CD.TSV'),
        'LEXP_CD': os.path.join(data_root_dir, 'LEXP_CD.TSV'),
        'LOAN_CD': os.path.join(data_root_dir, 'LOAN_CD.TSV'),
        'LOBBY_AMENDMENTS_CD': os.path.join(data_root_dir, 'LOBBY_AMENDMENTS_CD.TSV'),
        'LOTH_CD': os.path.join(data_root_dir, 'LOTH_CD.TSV'),
        'LPAY_CD': os.path.join(data_root_dir, 'LPAY_CD.TSV'),
        'NAMES': os.path.join(data_root_dir, 'NAMES_CD.TSV'),
        'RCPT_CD': os.path.join(data_root_dir, 'RCPT_CD.TSV'),
        'SMRY_CD': os.path.join(data_root_dir, 'SMRY_CD.TSV'),
    }
    for file_name, file_path in data_tables.items():
        print 'processing %s' % file_name
        clean_data = fix_null_bytes(file_path)
        #process_clean_data(clean_data, file_name)
        car_wash(clean_data, file_name)

if __name__ == '__main__':
    fix_all_csv_quoting()
