from __future__ import unicode_literals
from django.db import models
from calaccess_raw import managers


class CalAccessBaseModel(models.Model):
    """
    An abstract model with some tricks we'll reuse below.
    """
    DATE_FIELDS = ()
    DATETIME_FIELDS = ()
    objects = managers.CalAccessManager()

    def get_csv_name(self):
        return self.__class__.objects.get_csv_name()

    def get_csv_path(self):
        return self.__class__.objects.get_csv_path()

    class Meta:
        abstract = True
