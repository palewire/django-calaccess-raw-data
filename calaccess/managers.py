import os
from django.db import models
from calaccess import get_download_directory


class CalAccessManager(models.Manager):

    def get_csv_name(self):
        return "%s.csv" % self.model._meta.db_table.lower()

    def get_csv_path(self):
        return os.path.join(
            get_download_directory(),
            'csv',
            self.get_csv_name()
        )
