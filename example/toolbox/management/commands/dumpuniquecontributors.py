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
            SELECT DISTINCT
                ctrib_namt,
                ctrib_namf,
                ctrib_naml,
                ctrib_nams,
                ctrib_occ,
                ctrib_emp,
                ctrib_adr1,
                ctrib_adr2,
                ctrib_city,
                ctrib_st,
                ctrib_zip4
            FROM %(rcpt)s

            UNION

            SELECT DISTINCT
                lndr_namt,
                lndr_namf,
                lndr_naml,
                lndr_nams,
                loan_occ,
                loan_emp,
                loan_adr1,
                loan_adr2,
                loan_city,
                loan_st,
                loan_zip4
            FROM %(loan)s

            UNION

            SELECT DISTINCT
                enty_namt,
                enty_namf,
                enty_naml,
                enty_nams,
                ctrib_occ,
                ctrib_emp,
                '',
                '',
                enty_city,
                enty_st,
                enty_zip4
            FROM %(s497)s
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
            'zipcode'
        ])
        [writer.writerow(row) for row in self.cursor.fetchall()]