#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import textwrap
import requests
import json
from django.db import models
from django.utils.deconstruct import deconstructible
from calaccess_raw import managers, get_model_list


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

    def get_documentcloud_pages(self):
        """
        Return a list of tuples for each page or each document in the DOCUMENTCLOUD_PAGES attr

        Each tuple contains a DocumentCloud and DocPage object.
        """
        page_list = []
        for dc in self.DOCUMENTCLOUD_PAGES:
            if not isinstance(dc, DocumentCloud):
                raise TypeError("Values must be instances of DocumentCloud")

            page_list.extend([(dc, page) for page in dc.pages])

        return page_list

    class Meta:
        abstract = True


@deconstructible
class DocumentCloud(object):
    """
    A document hosted on DocumentCloud.

    Cited in our Python code and then republished in our HTML documentation.
    """
    def __init__(self, id, start_page=None, end_page=None):
        self.id = id
        self.start_page = start_page
        self.end_page = end_page

    def _lazy_load(self):
        """
        Makes a GET /api/documents/[id].json method and assigns data in response to attrs
        """
        r = requests.get(
            'https://www.documentcloud.org/documents/{id}.json'.format(id=self.id)
        )
        self._metadata = json.loads(r.content.decode('utf-8'))
        self._title = self._metadata['title']

    @property
    def metadata(self):
        try:
            self._metadata
        except AttributeError:
            self._lazy_load()

        return self._metadata

    @property
    def title(self):
        try:
            self._title
        except AttributeError:
            self._lazy_load()

        return self._title

    @property
    def canonical_url(self):
        try:
            self._metadata
        except AttributeError:
            self._lazy_load()

        if self.start_page:
            canonical_url = (
                self._metadata['canonical_url'] +
                '#document/p{}'.format(self.start_page)
            )
        else:
            canonical_url = self._metadata['canonical_url']

        return canonical_url

    @property
    def thumbnail_url(self):
        try:
            self._metadata
        except AttributeError:
            self._lazy_load()

        page = self.start_page or 1

        return self._metadata['resources']['page']['image'].format(
                size='thumbnail',
                page=page
            )

    @property
    def pdf_url(self):
        try:
            self._metadata
        except AttributeError:
            self._lazy_load()

        return self._metadata['resources']['pdf']

    @property
    def text_url(self):
        try:
            self._metadata
        except AttributeError:
            self._lazy_load()

        return self._metadata['resources']['text']

    @property
    def num_pages(self):
        if self.start_page and self.end_page:
            num_pages = self.end_page - self.start_page + 1
        elif self.end_page:
            num_pages = self.end_page
        elif self.start_page:
            num_pages = 1
        # ignored case: User wants to specify and start page and
        # expects to include all subsequent pages in doc
        else:
            try:
                num_pages = self._metadata['pages']
            except AttributeError:
                self._lazy_load()
                num_pages = self._metadata['pages']

        return num_pages

    @property
    def pages(self):

        class DocPage(object):
            def __init__(self, num, canonical_url, thumbnail_url):
                self.num = num
                self.canonical_url = canonical_url
                self.thumbnail_url = thumbnail_url

        canonical_url = 'https://www.documentcloud.org/documents/{id}/pages/{page}.html'

        try:
            image_url = self._metadata['resources']['page']['image']
        except AttributeError:
            self._lazy_load()
            image_url = self._metadata['resources']['page']['image']

        start = self.start_page or 1

        return [
            DocPage(
                x,
                canonical_url.format(id=self.id, page=x),
                image_url.format(size='thumbnail', page=x)
            ) for x in range(start, start+self.num_pages)
        ]


class FilingForm(object):
    """
    A form used by the California Secretary of State to collection information
    which ends up in the CAL-ACCESS database
    """
    def __init__(
            self, id, title, description=None, group=None,
            documentcloud=None, sections=None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.group = group
        self.documentcloud = documentcloud
        self.raw_sections = sections

        if self.documentcloud:
            if not isinstance(documentcloud, DocumentCloud):
                raise TypeError("documentcloud must be instance of DocumentCloud")

    def get_models(self):
        models = []
        for model in get_model_list():
            try:
                model.CALACCESS_FORMS
            except AttributeError:
                pass
            else:
                if self in model.CALACCESS_FORMS:
                    models.append(model)

        return models

    @property
    def sections(self):
        class FilingFormSection(object):
            def __init__(self, id, title, documentcloud=None):
                self.id = id
                self.title = title
                self.documentcloud = documentcloud

                if documentcloud:
                    if not isinstance(documentcloud, DocumentCloud):
                        raise TypeError("documentcloud must be instance of DocumentCloud")

            def __str__(self):
                return str(self.id)

        objs = []

        for i in self.raw_sections:
            if len(i) == 4:
                doc = DocumentCloud(self.documentcloud.id, i[2], i[3])
            elif len(i) == 3:
                doc = DocumentCloud(self.documentcloud.id, i[2])
            else:
                doc = None

            objs.append(FilingFormSection(i[0], i[1], doc))

        return objs

    def get_section(self, id):
        section_dict = {i.id: i for i in self.sections}
        return section_dict[id]

    def __str__(self):
        return str(self.id)
