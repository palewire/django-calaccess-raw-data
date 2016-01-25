#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


@admin.register(models.FilernameCd)
class FilernameCdAdmin(BaseAdmin):
    list_display = (
        "id",
        "xref_filer_id",
        "filer_id",
        "naml",
        "namf",
        "filer_type",
        "status",
        "effect_dt",
    )
    list_filter = ("filer_type", "status")
    search_fields = (
        "xref_filer_id",
        "filer_id",
        "naml",
        "namf",
    )
    date_hierarchy = "effect_dt"


@admin.register(models.FilerFilingsCd)
class FilerFilingsCdAdmin(BaseAdmin):
    search_fields = ("filing_id", "filer_id")
    list_display = (
        "id", "filer_id", "form_id",
        "filing_id", "filing_sequence"
    )


@admin.register(models.FilingsCd)
class FilingsCdAdmin(BaseAdmin):
    pass


@admin.register(models.SmryCd)
class SmryCdAdmin(BaseAdmin):
    list_display = (
        'filing_id',
        'amend_id',
        'form_type',
        'line_item',
        'pretty_amount_a',
        'pretty_amount_b',
        'pretty_amount_c',
    )
    list_filter = ('form_type',)
    search_fields = ('filing_id', 'form_type', 'line_item')


@admin.register(models.TextMemoCd)
class TextMemoCdAdmin(BaseAdmin):
    pass


@admin.register(models.CvrE530Cd)
class CvrE530CdAdmin(BaseAdmin):
    pass
