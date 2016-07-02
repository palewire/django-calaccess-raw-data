#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


@admin.register(models.RawDataVersion)
class RawDataVersionAdmin(BaseAdmin):
    list_display = (
        "id",
        "release_datetime",
        "pretty_size",
    )
    list_display_links = ('release_datetime',)
    list_filter = ("release_datetime",)


@admin.register(models.RawDataFile)
class RawDataFileAdmin(BaseAdmin):
    list_display = (
        "id",
        "version",
        "file_name",
        "download_records_count",
        "clean_records_count",
        "load_records_count",
        "download_columns_count",
        "clean_columns_count",
        "load_columns_count",
    )
    list_display_links = ('id', 'file_name',)
    list_filter = ("version__release_datetime",)


@admin.register(models.RawDataCommand)
class RawDataCommandAdmin(BaseAdmin):
    list_display = (
        "id",
        "version",
        "command",
        "file_name",
        "start_datetime",
        "finish_datetime",
    )
    list_display_links = ("id", "command",)
    list_filter = (
        "start_datetime",
        "finish_datetime",
        "version__release_datetime",
        "command",
    )
