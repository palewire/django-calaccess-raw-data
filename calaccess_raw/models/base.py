from __future__ import unicode_literals
from django.db import models
from calaccess_raw import managers


class CalAccessBaseModel(models.Model):
    """
    An abstract model with some tricks we'll reuse below.
    """
    objects = managers.CalAccessManager()

    def doc(self):
        if self.__doc__.startswith(self.klass_name()):
            return ''
        return self.__doc__

    def klass(self):
        return self.__class__

    def klass_name(self):
        return self.__class__.__name__

    def get_csv_name(self):
        return self.__class__.objects.get_csv_name()

    def get_csv_path(self):
        return self.__class__.objects.get_csv_path()

    class Meta:
        abstract = True
