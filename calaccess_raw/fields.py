#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom field overrides.

Allow for cleaning and transforming the data when it is loaded into the database with PostgreSQL's COPY command.
"""
from django.db.models import fields
from django.db.models import ForeignKey
from django.template.defaultfilters import capfirst


class CalAccessFieldMixin(fields.Field):
    """
    A set of common helpers for all of our custom fields.
    """
    def definition(self):
        """
        A humanized definition of what's the in field for documentation.
        """
        if self.help_text:
            return capfirst(self.help_text)
        else:
            return ''

    def is_unique_key(self):
        """
        Tests if the column is part of its model's unique key.

        Returns True or False
        """
        if self.__dict__['db_column'] in self.model().get_unique_key_list():
            return True
        return False


class DocumentCloudMixin(fields.Field):
    """
    Adds a documentcloud_pages keyword argument to the Field.

    Allows it to link to documents that explain the contents of the data.
    """
    def __init__(self, documentcloud_pages=[], *args, **kwargs):
        """
        Overrides the standard __init__ to add our documentcloud_page_urls option.
        """
        self.documentcloud_pages = documentcloud_pages
        super(DocumentCloudMixin, self).__init__(*args, **kwargs)

    def deconstruct(self):
        """
        Overrides the standard deconstruct method to add our documentcloud_page_urls option.
        """
        name, path, args, kwargs = super(
            DocumentCloudMixin,
            self
        ).deconstruct()
        # Only include kwarg if it's not the default
        if self.documentcloud_pages != []:
            kwargs['documentcloud_pages'] = self.documentcloud_pages
        return name, path, args, kwargs


class CharField(fields.CharField, CalAccessFieldMixin, DocumentCloudMixin):
    """
    A custom character field.
    """
    copy_type = "text"
    copy_template = """
    CASE
        WHEN "%(name)s" IS NULL
            THEN ''
        ELSE regexp_replace(TRIM("%(name)s"), '\r|\n', '', 'g')
    END"""

    def description(self):
        """
        Returns a custom description for documentation that includes the max length.
        """
        return super(CharField, self).description % dict(
            max_length=self.max_length
        )


class DateField(fields.DateField, CalAccessFieldMixin):
    """
    A custom date field.
    """
    copy_type = "text"
    copy_template = """
    CASE
        WHEN "%(name)s" IS NOT NULL AND TRIM("%(name)s") != ''
            THEN to_date(substring("%(name)s" from 1 for 10), 'MM/DD/YYYY')
        ELSE null
    END"""


class DateTimeField(fields.DateTimeField, CalAccessFieldMixin):
    """
    A custom datetime field.
    """
    copy_type = "text"
    copy_template = """
    CASE
        WHEN "%(name)s" IS NOT NULL AND TRIM("%(name)s") != ''
            THEN to_timestamp("%(name)s", 'MM/DD/YYYY HH12:MI:SS AM')
        ELSE null
    END"""


class DecimalField(fields.DecimalField, CalAccessFieldMixin):
    """
    A custom decimal field.
    """
    copy_type = "text"
    copy_template = """
    CASE
        WHEN "%(name)s" = ''
            THEN 0.0
        WHEN "%(name)s" IS NULL
            THEN 0.0
        WHEN "%(name)s" IS NOT NULL
            THEN "%(name)s"::numeric
    END"""


class FloatField(fields.FloatField, CalAccessFieldMixin):
    """
    A custom float field.
    """
    copy_type = "text"
    copy_template = """
    CASE
        WHEN TRIM("%(name)s") = ''
            THEN 0.0
        WHEN TRIM("%(name)s") IS NULL
            THEN 0.0
        WHEN TRIM("%(name)s") IS NOT NULL
            THEN "%(name)s"::double precision
    END"""


class IntegerField(fields.IntegerField, CalAccessFieldMixin, DocumentCloudMixin):
    """
    A custom integer field.
    """
    copy_type = "text"
    copy_template = """
    CASE
        WHEN TRIM("%(name)s") = ''
            THEN NULL
        WHEN "%(name)s" = '          '
            THEN NULL
        WHEN "%(name)s" = '         '
            THEN NULL
        WHEN "%(name)s" = 'Y'
            THEN 1
        WHEN "%(name)s" = 'y'
            THEN 1
        WHEN "%(name)s" = 'X'
            THEN 1
        WHEN "%(name)s" = 'x'
            THEN 1
        WHEN "%(name)s" = 'N'
            THEN 0
        WHEN "%(name)s" = 'n'
            THEN 0
        WHEN "%(name)s" IS NOT NULL
            THEN "%(name)s"::int
        ELSE NULL
    END"""


class ForeignKeyField(ForeignKey, CalAccessFieldMixin, DocumentCloudMixin):
    """
    A custom foreign key field.
    """
    @property
    def copy_type(self):
        """
        Returns the copy_type of the related foreign key field.
        """
        return self.foreign_related_fields[0].copy_type

    @property
    def copy_template(self):
        """
        Returns the copy_template of the related foreign key field.
        """
        return self.foreign_related_fields[0].copy_template

    def description(self):
        """
        Returns a description for documentation from the related foreign key field.
        """
        return self.foreign_related_fields[0].description
