#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base models for tables from the CAL-ACCESS database.
"""
# Text
import textwrap

# Models
from django.db import models
from calaccess_raw import managers
from django.db.models.base import ModelBase


class CalAccessMetaClass(ModelBase):
    """
    A custom metaclass for our base model.

    Automatically configures Meta attributes common to all models.
    """
    def __new__(cls, name, bases, attrs):
        """
        Override the default __new__ behavior.
        """
        klass = super(CalAccessMetaClass, cls).__new__(cls, name, bases, attrs)

        # Cook up an automated verbose name for each model
        klass_group = str(klass).split(".")[-2].upper()
        klass_table = klass._meta.db_table
        klass_name = "{0}: {1}".format(klass_group, klass_table)

        # Insert the verbose name into each model's configuration
        klass._meta.verbose_name = klass_name
        klass._meta.verbose_name_plural = klass_name

        # Set the app_label too
        klass._meta.app_label = "calaccess_raw"

        # Finish up
        return klass


class CalAccessBaseModel(models.Model):
    """
    An abstract model with some tricks we'll reuse.
    """
    __metaclass__ = CalAccessMetaClass

    # The UNIQUE_KEY is one or more fields that, taken together, are unique
    # within the database. https://en.wikipedia.org/wiki/Unique_key

    # Because the CAL-ACCESS database is released without unique keys specified
    # we determine these on our own and list them with each model.

    # If a single field is believed to be unique, it can be set as a simple
    # string variable, like:

    #   UNIQUE_KEY = 'field_name'

    # If multiple fields must be combined to guarantee uniqueness, they
    # should be listed as tuple like:

    #   UNIQUE_KEY = ('field_one', 'field_two')

    # If the unique key does not exist or cannot be determined it will be
    # set to False

    #   UNIQUE_KEY = False
    UNIQUE_KEY = None

    # A list of URL strings that point to pages hosted on DocumentCloud.org
    # that contain documentation for this model. Once assembled they can be
    # embedded in our user-facing documentation as images.

    # Should be filled with instances of our DocumentCloud class below
    # which accepts a unique DocumentCloud id along with start and/or end
    # page numbers
    DOCUMENTCLOUD_PAGES = []
    FILING_FORMS = []

    # Default manager
    objects = managers.CalAccessManager()

    def doc(self):
        """
        Return the model's docstring as a readable string ready to print.
        """
        if self.__doc__.startswith(self.klass_name):
            return ''
        return textwrap.dedent(self.__doc__).strip()

    @property
    def db_table(self):
        """
        Return the model's database table name as a string.
        """
        return self._meta.db_table

    @property
    def klass(self):
        """
        Return the model class itself.
        """
        return self.__class__

    @property
    def klass_name(self):
        """
        Return the name of the model class.
        """
        return self.__class__.__name__

    @property
    def klass_group(self):
        """
        Return the name of the model's group, as determined by its submodule.
        """
        return str(self.__class__).split(".")[-2]

    def get_field_list(self):
        """
        Return all the fields on the model as a list.
        """
        return self._meta.fields

    def get_csv_name(self):
        """
        Return the name of the clean CSV file that contains the model's data.
        """
        return self.__class__.objects.get_csv_name()

    def get_csv_path(self):
        """
        Return the path to the clean CSV file that contains the model's data.
        """
        return self.__class__.objects.get_csv_path()

    def get_tsv_name(self):
        """
        Return the name of the raw TSV file that contains the model's data.
        """
        return self.__class__.objects.get_tsv_name()

    def get_tsv_path(self):
        """
        Return the path to the raw TSV file that contains the model's data.
        """
        return self.__class__.objects.get_tsv_path()

    def get_unique_key_list(self):
        """
        Return UNIQUE_KEY setting as a list regardless of its data type.
        """
        if self.__class__.UNIQUE_KEY is None:
            return []
        elif self.__class__.UNIQUE_KEY is False:
            return []
        elif isinstance(self.__class__.UNIQUE_KEY, (list, tuple)):
            return self.__class__.UNIQUE_KEY
        else:
            return [self.__class__.UNIQUE_KEY]

    def get_documentcloud_pages(self):
        """
        Return a list of tuples for each page or each document in the DOCUMENTCLOUD_PAGES attr.

        Each tuple contains a DocumentCloud and DocPage object.
        """
        page_list = []
        for dc in self.DOCUMENTCLOUD_PAGES:
            page_list.extend([(dc, page) for page in dc.pages])
        return page_list

    def get_filing_forms_w_sections(self):
        """
        Returns a list of tuples, each containing a FilingForm object and list of FilingFormSection objects.
        """
        from calaccess_raw.annotations import FilingForm
        forms_dict = {}
        for i in self.FILING_FORMS:
            if isinstance(i, FilingForm):
                try:
                    forms_dict[i]
                except KeyError:
                    forms_dict[i] = []
            else:
                try:
                    forms_dict[i.form].append(i)
                except KeyError:
                    forms_dict[i.form] = [i]
        return sorted(forms_dict.items(), key=lambda x: x[0].id)

    class Meta:
        """
        Meta model options.
        """
        abstract = True
        app_label = 'calaccess_raw'
