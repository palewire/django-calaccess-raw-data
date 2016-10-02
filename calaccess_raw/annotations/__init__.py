#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utilities for representing and interacting with CAL-ACCESS reference documents and forms.
"""
import os
import json
import requests
from django.conf import settings
from calaccess_raw import get_model_list
from django.utils.deconstruct import deconstructible


@deconstructible
class DocumentCloud(object):
    """
    A document hosted on DocumentCloud.

    Cited in our Python code and then republished in our HTML documentation.
    """
    def __init__(self, id, start_page=None, end_page=None):
        """
        Create a new object by submitting a unique ID from DocumentCloud.org.
        """
        self.id = id
        self.start_page = start_page
        self.end_page = end_page
        self.metadata_cache_dir = os.path.join(
            settings.BASE_DIR,
            ".documentcloud_metadata"
        )
        self.metadata_filename = os.path.join(
            self.metadata_cache_dir,
            '{id}.json'.format(id=self.id)
        )

    def _request_metadata(self):
        """
        Returns contents of GET request to /api/documents/[id].json method.
        """
        r = requests.get(
            'https://www.documentcloud.org/documents/{id}.json'.format(id=self.id)
        )
        return r.content.decode('utf-8')

    def _cache_metadata(self):
        """
        Requests metadata and stores in .json file in .documentcloud_cache dir.

        Creates .documentcloud_cache dir if it doesn't already exist.
        """
        os.path.exists(self.metadata_cache_dir) or os.makedirs(self.metadata_cache_dir)

        with open(self.metadata_filename, 'w') as f:
            f.write(self._request_metadata())

    @property
    def metadata(self):
        """
        Returns a dictionary with the document's metadata retrieved from DocumentCould.
        """
        if not os.path.exists(self.metadata_filename):
            self._cache_metadata()

        with open(self.metadata_filename) as f:
            self._metadata = json.loads(f.read())

        return self._metadata

    @property
    def title(self):
        """
        Returns the title of the document.
        """
        self._title = self.metadata['title']
        return self._title

    @property
    def canonical_url(self):
        """
        Returns the URL where the document can be found on DocumentCloud.
        """
        if self.start_page:
            canonical_url = (
                self.metadata['canonical_url'] +
                '#document/p{}'.format(self.start_page)
            )
        else:
            canonical_url = self.metadata['canonical_url']
        return canonical_url

    @property
    def thumbnail_url(self):
        """
        Returns a URL to the thumbnail image of the document's first page.
        """
        page = self.start_page or 1
        self._thumbnail_url = self.metadata['resources']['page']['image'].format(
            size='thumbnail',
            page=page
        )
        return self._thumbnail_url

    @property
    def pdf_url(self):
        """
        Returns a URL to the full PDF of the document.
        """
        self._pdf_url = self.metadata['resources']['pdf']
        return self._pdf_url

    @property
    def text_url(self):
        """
        Returns a URL to the full text of the document.
        """
        self._text_url = self.metadata['resources']['text']
        return self._text_url

    @property
    def num_pages(self):
        """
        Returns the number of pages in this document.
        """
        if self.start_page and self.end_page:
            self._num_pages = self.end_page - self.start_page + 1
        elif self.end_page:
            self._num_pages = self.end_page
        elif self.start_page:
            self._num_pages = 1
        # ignored case: User wants to specify and start page and
        # expects to include all subsequent pages in doc
        else:
            self._num_pages = self.metadata['pages']

        return self._num_pages

    @property
    def pages(self):
        """
        Returns a list of the pages in this form as DocPage objects.
        """
        class DocPage(object):
            def __init__(self, num, canonical_url, thumbnail_url):
                self.num = num
                self.canonical_url = canonical_url
                self.thumbnail_url = thumbnail_url

        canonical_url = 'https://www.documentcloud.org/documents/{id}/pages/{page}.html'

        image_url = self.metadata['resources']['page']['image']

        start = self.start_page or 1

        return [
            DocPage(
                x,
                canonical_url.format(id=self.id, page=x),
                image_url.format(size='thumbnail', page=x)
            ) for x in range(start, start + self.num_pages)
        ]

    @property
    def formatted_page_nums(self):
        """
        Returns the page range as a pretty string.
        """
        if self.end_page:
            formatted_str = '{0}-{1}'.format(self.start_page, self.end_page)
        else:
            formatted_str = str(self.start_page)
        return formatted_str


@deconstructible
class FilingForm(object):
    """
    A form used to collect information for the CAL-ACCESS database.
    """
    def __init__(self, id, title, **kwargs):
        """
        Create a new object by submitting a unique ID and title.
        """
        self.id = id
        self.title = title
        self.description = kwargs.get('description')
        self.group = kwargs.get('group')
        self.documentcloud_id = kwargs.get('documentcloud_id')
        self.db_value = kwargs.get('db_value', self.id)
        self.sections = []
        if self.documentcloud_id:
            self.documentcloud = DocumentCloud(self.documentcloud_id)
        else:
            self.documentcloud = None

    @property
    def type_and_num(self):
        """
        Returns a short title for the form that includes its type and number.
        """
        if self.id[0] == 'E':
            self._type_and_num = 'Electronic Form {}'.format(self.id[1:])
        elif self.id[0] == 'S':
            self._type_and_num = 'Schedule {}'.format(self.id[1:])
        else:
            self._type_and_num = 'Form {}'.format(self.id[1:])

        return self._type_and_num

    @property
    def full_title(self):
        """
        Returns the full title of the form.
        """
        self._full_title = '{0}: {1}'.format(self.type_and_num, self.title)
        return self._full_title

    def add_section(self, id, title, **kwargs):
        """
        Adds a Section with the provided title and options to this object.
        """
        new_section = FilingFormSection(
            form=self,
            id=id,
            title=title,
            db_value=kwargs.get('db_value', self.db_value),
            start_page=kwargs.get('start_page'),
            end_page=kwargs.get('end_page'),
            documentcloud_id=kwargs.get('documentcloud_id'),
        )
        self.sections.append(new_section)
        return new_section

    def get_section(self, id):
        """
        Returns the Section object with the given id.
        """
        section_dict = {i.id: i for i in self.sections}
        return section_dict[id]

    def get_models(self):
        """
        Returns all the CAL-ACCESS models connected with this form.
        """
        models = []
        for model in get_model_list():
            if self in [x[0] for x in model().get_filing_forms_w_sections()]:
                models.append(model)

        return models

    def __str__(self):
        return str(self.id)


@deconstructible
class FilingFormSection(object):
    """
    A section of a FilingForm (e.g., a cover page, summary sheet, schedule or part).
    """
    def __init__(self, form, id, title, **kwargs):
        """
        Create a new object by submitting a FilingForm parent with an ID and title.
        """
        self.form = form
        self.id = id
        self.title = title
        self.db_value = kwargs.get('db_value', form.db_value)
        self.start_page = kwargs.get('start_page')
        self.end_page = kwargs.get('end_page')
        self.documentcloud = DocumentCloud(
            self.form.documentcloud_id,
            self.start_page,
            self.end_page
        )

    @property
    def full_title(self):
        """
        Returns full title of the section, including the parent form's name.
        """
        self._full_title = '{0} ({1}): {2}'.format(
            self.form.type_and_num,
            self.form.title,
            self.title,
        )
        return self._full_title

    def __str__(self):
        return str(self.id)


def get_sorted_choices(codes_dict):
    """
    Returns a tuple of tuples, sorted by the given codes_dict's key.
    """
    return tuple(sorted(codes_dict.items(), key=lambda x: x[0]))
