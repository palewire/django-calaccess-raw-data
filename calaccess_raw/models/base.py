#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import textwrap
import requests
import json
from django.db import models
from django.utils.deconstruct import deconstructible
from calaccess_raw import managers


class CalAccessBaseModel(models.Model):
    """
    An abstract model with some tricks we'll reuse.
    """
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

    # Default manager
    objects = managers.CalAccessManager()

    def doc(self):
        """
        Return the model's docstring as a readable string ready to print
        """
        if self.__doc__.startswith(self.klass_name):
            return ''
        return textwrap.dedent(self.__doc__).strip()

    @property
    def klass(self):
        """
        Return the model class itself.
        """
        return self.__class__

    @property
    def klass_name(self):
        """
        Return the name of the model class
        """
        return self.__class__.__name__

    @property
    def klass_group(self):
        """
        Return the name of the model's group, as determined by its submodule
        """
        return str(self.__class__).split(".")[-2]

    def get_field_list(self):
        """
        Return all the fields on the model as a list
        """
        return self._meta.fields

    def get_csv_name(self):
        """
        Return the name of the clean CSV file that contains the model's data
        """
        return self.__class__.objects.get_csv_name()

    def get_csv_path(self):
        """
        Return the path to the clean CSV file that contains the model's data
        """
        return self.__class__.objects.get_csv_path()

    def get_tsv_name(self):
        """
        Return the name of the raw TSV file that contains the model's data
        """
        return self.__class__.objects.get_tsv_name()

    def get_tsv_path(self):
        """
        Return the path to the raw TSV file that contains the model's data
        """
        return self.__class__.objects.get_tsv_path()

    def get_unique_key_list(self):
        """
        Return UNIQUE_KEY setting as a list regardless of its data type
        """
        if self.__class__.UNIQUE_KEY is None:
            return []
        elif self.__class__.UNIQUE_KEY is False:
            return []
        elif isinstance(self.__class__.UNIQUE_KEY, (list, tuple)):
            return self.__class__.UNIQUE_KEY
        else:
            return [self.__class__.UNIQUE_KEY]

    def get_documentcloud_page_urls(self):
        """
        Return canonical and thumbnail urls for each page in the DOCUMENTCLOUD_PAGES
        attribute (list of tuples).
        """
        page_url_list = []
        thumb_url_list = []
        for dc in self.DOCUMENTCLOUD_PAGES:
            if not isinstance(dc, DocumentCloud):
                raise TypeError("Values must be instances of DocumentCloud")
            page_url_list.extend(dc.get_page_urls())
            thumb_url_list.extend(dc.get_thumbnail_urls())
        return zip(page_url_list, thumb_url_list)

    class Meta:
        abstract = True


@deconstructible
class DocumentCloud(object):
    """
    A page or set of pages hosted on DocumentCloud.

    Cited in our Python code and then republished in our HTML documentation.
    """
    def __init__(self, id, start_page, end_page=None):
        self.id = id
        self.start_page = start_page
        self.end_page = end_page

    def get_pages(self):
        """
        Return a list of all the pages in the object
        """
        if self.end_page:
            return range(self.start_page, self.end_page+1)
        else:
            return [self.start_page]

    def get_doc_data(self):
        """
        Return contents of response (as dict) from request to DocumentCloud
        GET /api/documents/[id].json method.
        """
        r = requests.get('https://www.documentcloud.org/documents/{}.json'.format(self.id))
        return json.loads(r.content.decode('utf-8'))

    def get_page_urls(self):
        """
        Return a list of canonical URLs for each page in the object.
        """
        url_pattern = 'https://www.documentcloud.org/documents/%(id)s/pages/%(page)s.html'
        url_list = []
        for page in self.get_pages():
            url = url_pattern % dict(id=self.id, page=page)
            url_list.append(url)
        return url_list

    def get_thumbnail_urls(self):
        """
        Return a list of thumbnail URLs for each page in the object.
        """
        url_pattern = 'https://assets.documentcloud.org/documents/%(id)s/pages/\
%(slug)s-p%(page)s-thumbnail.gif'
        url_list = []
        for page in self.get_pages():
            split_id = self.id.split('-', 1)
            url = url_pattern % dict(id=split_id[0], slug=split_id[1], page=page)
            url_list.append(url)
        return url_list


class CalAccessForm(object):
    """
    A form used by the California Secretary of State to collection information
    which ends up in the CAL-ACCESS database
    """
    def __init__(self, id, description, group=None, document_cloud_id=None):
        self.id = id
        self.description = description
        self.group = group
        self.document_cloud_id = document_cloud_id

    def __str__(self):
        return str(self.id)
