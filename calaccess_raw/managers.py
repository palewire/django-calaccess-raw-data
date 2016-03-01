#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.db import models
from calaccess_raw import get_download_directory
import requests
import json


class CalAccessManager(models.Manager):

    def get_csv_name(self):
        return "%s.csv" % self.model._meta.db_table.lower()

    def get_csv_path(self):
        return os.path.join(
            get_download_directory(),
            'csv',
            self.get_csv_name()
        )

    def get_tsv_name(self):
        return "%s.TSV" % self.model._meta.db_table

    def get_tsv_path(self):
        return os.path.join(
            get_download_directory(),
            'tsv',
            self.get_tsv_name()
        )


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
        return json.loads(r.content)

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
        title = self.get_doc_data()['id'].split('-', 1)[1]
        url_pattern = 'https://assets.documentcloud.org/documents/%(id)s/pages/\
%(title)s-p%(page)s-thumbnail.gif'
        url_list = []
        for page in self.get_pages():
            url = url_pattern % dict(id=self.id, title=title, page=page)
            url_list.append(url)
        return url_list
