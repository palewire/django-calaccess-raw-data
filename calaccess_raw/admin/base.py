#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utilities common to all administration panels.
"""
from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    """
    Parent class with attributes common to all CAL-ACCESS data models.
    """
    save_on_top = True

    def get_readonly_fields(self, *args, **kwargs):
        """
        Make all fields read only.
        """
        return [f.name for f in self.model._meta.fields]

    def get_list_filter(self, request):
        """
        Filter all fields with `choices` configured.
        """
        return [f.name for f in self.model._meta.fields if f.choices]

    def get_search_fields(self, request):
        """
        Search all fields that aren't a ForeignKey field.
        """
        return [f.name for f in self.model._meta.fields if not f.is_relation]
