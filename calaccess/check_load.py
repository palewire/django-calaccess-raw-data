#!/usr/bin/env python
from env_settings import data_root_dir, db_name, db_password, db_user_name
import MySQLdb
import os

conn = MySQLdb.Connection(db=db_name, host='localhost', user=db_user_name, passwd=db_password, local_infile=1)
mysql = conn.cursor()


def check_load():
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
    print 'table_name\ttable_rows\tfile_lines'
    for table_name, file_path in data_tables.items():
        try:
            mysql.execute('SELECT COUNT(*) FROM %s' % table_name)
            table_cnt = mysql.fetchall()[0][0]
            infile = open(file_path)
            file_cnt = len(infile.readlines())
            infile.close()
            print '%s\t%s\t%s' % (table_name, table_cnt, file_cnt)
        except:
            print '%s\tfailed to execute on this...' % (table_name)

if __name__ == '__main__':
    check_load()