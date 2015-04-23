from __future__ import unicode_literals
import textwrap
from django.db import models
from calaccess_raw import managers


class CalAccessBaseModel(models.Model):
    """
    An abstract model with some tricks we'll reuse below.
    """
    objects = managers.CalAccessManager()

    def doc(self):
        if self.__doc__.startswith(self.klass_name):
            return ''
        return textwrap.dedent(self.__doc__).strip()

    @property
    def klass(self):
        return self.__class__

    @property
    def klass_name(self):
        return self.__class__.__name__

    @property
    def klass_group(self):
        return str(self.__class__).split(".")[-2]

    def get_field_list(self):
        return self._meta.fields

    def get_csv_name(self):
        return self.__class__.objects.get_csv_name()

    def get_csv_path(self):
        return self.__class__.objects.get_csv_path()

    def get_tsv_name(self):
        return self.__class__.objects.get_tsv_name()

    def get_tsv_path(self):
        return self.__class__.objects.get_tsv_path()

    class Meta:
        abstract = True
