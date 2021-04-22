#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utilities for representing DocumentCloud documents.
"""
import os
import json
import requests
from django.conf import settings
from django.utils.deconstruct import deconstructible


@deconstructible
class DocumentCloudPage(object):
    """
    A page in a DocumentCloud document.
    """
    def __init__(self, num, canonical_url, thumbnail_url):
        """
        Create a page.
        """
        self.num = num
        self.canonical_url = canonical_url
        self.thumbnail_url = thumbnail_url


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
        self.metadata_filename = os.path.join(self.metadata_cache_dir, '{}.json'.format(self.id))

    def _request_metadata(self):
        """
        Returns contents of GET request to /api/documents/[id].json method.
        """
        url = f'https://api.www.documentcloud.org/api/documents/{self.id}'
        r = requests.get(url)
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
        with open(self.metadata_filename, 'r') as f:
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
    def slug(self):
        """
        Returns the slug of the document.
        """
        self._slug = self.metadata['slug']
        return self._slug

    @property
    def canonical_url(self):
        """
        Returns the URL where the document can be found on DocumentCloud.
        """
        if self.start_page:
            canonical_url = (
                self.metadata['canonical_url']
                + '#document/p{}'.format(self.start_page)
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
        url = f'https://assets.documentcloud.org/documents/{self.id}/pages/{self.slug}-p{page}-thumbnail.gif'
        self._thumbnail_url = url
        return self._thumbnail_url

    @property
    def pdf_url(self):
        """
        Returns a URL to the full PDF of the document.
        """
        self._pdf_url = f"https://assets.documentcloud.org/documents/{self.id}/{self.slug}.pdf"
        return self._pdf_url

    @property
    def text_url(self):
        """
        Returns a URL to the full text of the document.
        """
        self._text_url = f"https://assets.documentcloud.org/documents/{self.id}/{self.slug}.txt"
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
            self._num_pages = self.metadata['page_count']
        return self._num_pages

    @property
    def pages(self):
        """
        Returns a list of the pages in this form as DocPage objects.
        """
        canonical_url = 'https://www.documentcloud.org/documents/{id}/pages/{page}.html'
        start = self.start_page or 1
        return [
            DocumentCloudPage(
                x,
                canonical_url.format(id=self.id, page=x),
                f'https://assets.documentcloud.org/documents/{self.id}/pages/{self.slug}-p{x}-thumbnail.gif'
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
