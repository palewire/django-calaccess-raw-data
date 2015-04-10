from __future__ import unicode_literals
import os
from django.db import models
from calaccess_raw import get_download_directory


class CalAccessManager(models.Manager):

    def get_csv_name(self):
        return "%s.csv" % self.model._meta.db_table.lower()

    def get_csv_path(self):
        return os.path.join(
            get_download_directory(),
            'csv',
            self.get_csv_name()
        )

    def get_tsv_name(self):
        return "%s.TSV" % self.model._meta.db_table.upper()

    def get_tsv_path(self):
        return os.path.join(
            get_download_directory(),
            'tsv',
            self.get_tsv_name()
        )

    def get_highest_id(self):
        stdin,stdout = os.popen2("tail --lines=1 %s" % self.get_tsv_path())
        stdin.close()
        lines = stdout.readlines(); stdout.close()
        # words = lines[0].split('\t')
        # self.success(" lines # %d" % int(lines[0].split('\t')[0]))
        return int(lines[0].split('\t')[0])


