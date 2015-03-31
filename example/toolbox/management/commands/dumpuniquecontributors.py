from __future__ import unicode_literals
from csvkit import CSVKitWriter
from calaccess_raw import models
from django.db import connection
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand):
    help = 'Dump all of the unique campaign contributor names'

    def handle(self, *args, **options):
        self.cursor = connection.cursor()
        sql = """
        SELECT
            title,
            first_name,
            last_name,
            suffix,
            occupation,
            employer,
            address1,
            address2,
            city,
            state,
            zipcode,
            committee_id,
            COUNT(*)
        FROM (
            SELECT
                ctrib_namt as title,
                ctrib_namf as first_name,
                ctrib_naml as last_name,
                ctrib_nams as suffix,
                ctrib_occ as occupation,
                ctrib_emp as employer,
                ctrib_adr1 as address1,
                ctrib_adr2 as address2,
                ctrib_city as city,
                ctrib_st as state,
                ctrib_zip4 as zipcode,
                cmte_id as committee_id
            FROM %(rcpt)s

            UNION ALL

            SELECT
                lndr_namt as title,
                lndr_namf as first_name,
                lndr_naml as last_name,
                lndr_nams as suffix,
                loan_occ as occupation,
                loan_emp as employer,
                loan_adr1 as address1,
                loan_adr2 as address2,
                loan_city as city,
                loan_st as state,
                loan_zip4 as zipcode,
                cmte_id as committee_id
            FROM %(loan)s

            UNION ALL

            SELECT
                enty_namt as title,
                enty_namf as first_name,
                enty_naml as last_name,
                enty_nams as suffix,
                ctrib_occ as occupation,
                ctrib_emp as employer,
                '' as address1,
                '' as address2,
                enty_city as city,
                enty_st as state,
                enty_zip4 as zipcode,
                cmte_id as committee_id
            FROM %(s497)s
        ) as t
        GROUP BY
            title,
            first_name,
            last_name,
            suffix,
            occupation,
            employer,
            address1,
            address2,
            city,
            state,
            zipcode,
            committee_id
        ORDER BY
            last_name,
            first_name,
            suffix,
            title,
            city,
            state,
            occupation,
            employer
        """ % dict(
            rcpt=models.RcptCd._meta.db_table,
            loan=models.LoanCd._meta.db_table,
            s497=models.S497Cd._meta.db_table,
        )
        self.cursor.execute(sql)
        writer = CSVKitWriter(open("./contributors.csv", 'wb'))
        writer.writerow([
            'title',
            'first_name',
            'last_name',
            'suffix',
            'occupation',
            'employer',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
            'committee_id',
            'count'
        ])
        writer.writerows(self.cursor.fetchall())
