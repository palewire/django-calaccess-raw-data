#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import os
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
        Returns contents of GET request to /api/documents/[id].json method
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
        if not os.path.exists(self.metadata_filename):
            self._cache_metadata()

        with open(self.metadata_filename) as f:
            self._metadata = json.loads(f.read())

        return self._metadata

    @property
    def title(self):
        self._title = self.metadata['title']
        return self._title

    @property
    def canonical_url(self):
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
        page = self.start_page or 1

        self._thumbnail_url = self.metadata['resources']['page']['image'].format(
                size='thumbnail',
                page=page
            )

        return self._thumbnail_url

    @property
    def pdf_url(self):
        self._pdf_url = self.metadata['resources']['pdf']
        return self._pdf_url

    @property
    def text_url(self):
        self._text_url = self.metadata['resources']['text']
        return self._text_url

    @property
    def num_pages(self):
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
            ) for x in range(start, start+self.num_pages)
        ]


@deconstructible
class FilingForm(object):
    """
    A form used by the California Secretary of State to collection information
    which ends up in the CAL-ACCESS database
    """
    def __init__(
            self, id, title, description=None, group=None,
            documentcloud_id=None, sections=None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.group = group
        self.documentcloud_id = documentcloud_id
        self.raw_sections = sections

        if self.documentcloud_id:
            self.documentcloud = DocumentCloud(self.documentcloud_id)
        else:
            self.documentcloud = None

    @property
    def type_and_num(self):

        if self.id[0] == 'E':
            self._type_and_num = 'Electronic Form {}'.format(self.id[1:])
        elif self.id[0] == 'S':
            self._type_and_num = 'Schedule {}'.format(self.id[1:])
        else:
            self._type_and_num = 'Form {}'.format(self.id[1:])

        return self._type_and_num

    @property
    def full_title(self):

        self._full_title = '{0}: {1}'.format(self.type_and_num, self.title)

        return self._full_title

    @property
    def sections(self):
        return [FilingFormSection(self, *x) for x in self.raw_sections]

    def get_section(self, id):
        section_dict = {i.id: i for i in self.sections}
        return section_dict[id]

    def get_models(self):
        models = []
        for model in get_model_list():
            try:
                model.FILING_FORMS
            except AttributeError:
                pass
            else:
                if self in model.FILING_FORMS:
                    models.append(model)

        return models

    def __str__(self):
        return str(self.id)


class FilingFormSection(object):
    """
    A section of a FilingForm (e.g., a cover page, summary sheet, schedule or part).
    """
    def __init__(self, form, id, title, start_page=None, end_page=None):
        self.id = id
        self.title = title
        self.form = form
        self.start_page = start_page
        self.end_page = end_page

        self.documentcloud = DocumentCloud(
            self.form.documentcloud_id,
            self.start_page,
            self.end_page
        )

    @property
    def full_title(self):
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
    Returns a tuple of tuples, sorted by the given codes_dict's key
    """
    return tuple(sorted(codes_dict.items(), key=lambda x: x[0]))
