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
        'amount_a',
        'amount_b',
        'amount_c',
    )
    list_filter = ('form_type',)
    search_fields = ('filing_id', 'form_type', 'line_item')


@admin.register(models.SpltCd)
class SpltCdAdmin(BaseAdmin):
    pass


@admin.register(models.TextMemoCd)
class TextMemoCdAdmin(BaseAdmin):
    pass


@admin.register(models.CvrE530Cd)
class CvrE530CdAdmin(BaseAdmin):
    pass


class AcronymsCdAdmin(BaseAdmin):
    list_display = ("acronym", "stands_for", "effect_dt", "a_desc")
    date_hierarchy = 'effect_dt'
    search_fields = ("acronym", "a_desc")


class AddressCdAdmin(BaseAdmin):
    pass


class EfsFilingLogCdAdmin(BaseAdmin):
    list_display = (
        "id",
        "filing_date",
        "filingstatus",
        "filer_id",
        "vendor",
        "form_type",
    )


class FilersCdAdmin(BaseAdmin):
    pass


class FilerAcronymsCdAdmin(BaseAdmin):
    pass


class FilerAddressCdAdmin(BaseAdmin):
    list_display = (
        "filer_id",
        "adrid",
        "effect_dt",
        "add_type"
    )


class FilerEthicsClassCdAdmin(BaseAdmin):
    pass


class FilerInterestsCdAdmin(BaseAdmin):
    pass


@admin.register(models.FilerLinksCd)
class FilerLinksCdAdmin(BaseAdmin):
    list_display = (
        "filer_id_a",
        "filer_id_b",
        "link_type",
        "active_flg",
        "effect_dt",
        "termination_dt",
    )
    list_filter = (
        "active_flg",
        "link_type"
    )
    search_fields = ("filer_id_a", "filer_id_b")


class FilerStatusTypesCdAdmin(BaseAdmin):
    list_display = (
        "status_type",
        "status_desc"
    )


class FilerToFilerTypeCdAdmin(BaseAdmin):
    list_display = (
        "filer_id",
        "filer_type",
        "effect_dt",
        "active",
        "session_id",
        "race",
        "district_cd",
        "party_cd"
    )
    list_filter = (
        "active",
        "filer_type",
        "category",
        "sub_category",
        "category_type",
        "party_cd",
        "session_id"
    )
    date_hierarchy = "effect_dt"
    search_fields = (
        "filer_id",
    )


class FilerTypesCdAdmin(BaseAdmin):
    list_display = (
        "filer_type",
        "description",
        "grp_type",
        "calc_use",
        "grace_period",
    )


class FilerXrefCdAdmin(BaseAdmin):
    pass


class FilingPeriodCdAdmin(BaseAdmin):
    list_display = (
        "period_id", "start_date", "end_date", "period_desc",
    )
    search_fields = (
        "period_id",
    )


class GroupTypesCdAdmin(BaseAdmin):
    pass


class HeaderCdAdmin(BaseAdmin):
    pass


class HdrCdAdmin(BaseAdmin):
    pass


class ImageLinksCdAdmin(BaseAdmin):
    pass


class LegislativeSessionsCdAdmin(BaseAdmin):
    pass


class LookupCodeAdmin(BaseAdmin):
    list_display = (
        "code_type",
        "code_id",
        "code_desc",
    )
    list_filter = (
        "code_type",
    )
    search_fields = (
        "code_type",
        "code_id",
        "code_desc",
    )


class NamesCdAdmin(BaseAdmin):
    pass


class ReceivedFilingsCdAdmin(BaseAdmin):
    pass


class ReportsCdAdmin(BaseAdmin):
    pass


admin.site.register(models.AcronymsCd, AcronymsCdAdmin)
admin.site.register(models.AddressCd, AddressCdAdmin)
admin.site.register(models.EfsFilingLogCd, EfsFilingLogCdAdmin)
admin.site.register(models.FilersCd, FilersCdAdmin)
admin.site.register(models.FilerAcronymsCd, FilerAcronymsCdAdmin)
admin.site.register(models.FilerAddressCd, FilerAddressCdAdmin)
admin.site.register(models.FilerEthicsClassCd, FilerEthicsClassCdAdmin)
admin.site.register(models.FilerInterestsCd, FilerInterestsCdAdmin)
admin.site.register(models.FilerStatusTypesCd, FilerStatusTypesCdAdmin)
admin.site.register(models.FilerToFilerTypeCd, FilerToFilerTypeCdAdmin)
admin.site.register(models.FilerTypesCd, FilerTypesCdAdmin)
admin.site.register(models.FilerXrefCd, FilerXrefCdAdmin)
admin.site.register(models.FilingPeriodCd, FilingPeriodCdAdmin)
admin.site.register(models.GroupTypesCd, GroupTypesCdAdmin)
admin.site.register(models.HeaderCd, HeaderCdAdmin)
admin.site.register(models.HdrCd, HdrCdAdmin)
admin.site.register(models.ImageLinksCd, ImageLinksCdAdmin)
admin.site.register(models.LegislativeSessionsCd, LegislativeSessionsCdAdmin)
admin.site.register(models.LookupCodesCd, LookupCodeAdmin)
admin.site.register(models.NamesCd, NamesCdAdmin)
admin.site.register(models.ReceivedFilingsCd, ReceivedFilingsCdAdmin)
admin.site.register(models.ReportsCd, ReportsCdAdmin)
