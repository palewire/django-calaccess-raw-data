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
    list_display = ("filing_id", "filing_type")
    list_filter = ("filing_type",)
    search_fields = ("filing_id",)


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
    list_display = (
        "filing_id",
        "amend_id",
        "line_item",
        "pform_type",
        "elec_date",
        "elec_amount",
    )
    list_filter = ("pform_type",)
    search_fields = ("filing_id",)
    date_hierarchy = "elec_date"


@admin.register(models.TextMemoCd)
class TextMemoCdAdmin(BaseAdmin):
    list_display = ("filing_id", "amend_id", "form_type")
    list_filter = ("form_type",)
    search_fields = ("filing_id", "rec_no", "text4000")


@admin.register(models.CvrE530Cd)
class CvrE530CdAdmin(BaseAdmin):
    pass


@admin.register(models.AcronymsCd)
class AcronymsCdAdmin(BaseAdmin):
    list_display = ("acronym", "stands_for", "effect_dt", "a_desc")
    date_hierarchy = 'effect_dt'
    search_fields = ("acronym", "a_desc")


@admin.register(models.AddressCd)
class AddressCdAdmin(BaseAdmin):
    list_display = ("adrid", "city", "st", "zip4",)
    list_filter = ("st",)
    search_fields = ("adrid", "city", "st", "zip4")


@admin.register(models.EfsFilingLogCd)
class EfsFilingLogCdAdmin(BaseAdmin):
    list_display = (
        "id",
        "vendor",
        "filing_date",
        "filingstatus",
        "form_type",
    )
    list_filter = (
        "filingstatus",
        "vendor",
        "form_type",
    )
    date_hierarchy = "filing_date"
    search_fields = ("vendor",)


@admin.register(models.FilersCd)
class FilersCdAdmin(BaseAdmin):
    list_display = ("filer_id",)
    search_fields = ("filer_id",)


@admin.register(models.FilerAcronymsCd)
class FilerAcronymsCdAdmin(BaseAdmin):
    pass


@admin.register(models.FilerAddressCd)
class FilerAddressCdAdmin(BaseAdmin):
    list_display = (
        "filer_id",
        "adrid",
        "effect_dt",
        "add_type"
    )


@admin.register(models.FilerEthicsClassCd)
class FilerEthicsClassCdAdmin(BaseAdmin):
    pass


@admin.register(models.FilerInterestsCd)
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


@admin.register(models.FilerStatusTypesCd)
class FilerStatusTypesCdAdmin(BaseAdmin):
    list_display = (
        "status_type",
        "status_desc"
    )


@admin.register(models.FilerToFilerTypeCd)
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


@admin.register(models.FilerTypesCd)
class FilerTypesCdAdmin(BaseAdmin):
    list_display = (
        "filer_type",
        "description",
        "grp_type",
        "calc_use",
        "grace_period",
    )


@admin.register(models.FilerXrefCd)
class FilerXrefCdAdmin(BaseAdmin):
    pass


@admin.register(models.FilingPeriodCd)
class FilingPeriodCdAdmin(BaseAdmin):
    list_display = (
        "period_id", "start_date", "end_date", "period_desc",
    )
    search_fields = (
        "period_id",
    )


@admin.register(models.GroupTypesCd)
class GroupTypesCdAdmin(BaseAdmin):
    pass


@admin.register(models.HeaderCd)
class HeaderCdAdmin(BaseAdmin):
    pass


@admin.register(models.HdrCd)
class HdrCdAdmin(BaseAdmin):
    pass


@admin.register(models.ImageLinksCd)
class ImageLinksCdAdmin(BaseAdmin):
    pass


@admin.register(models.LegislativeSessionsCd)
class LegislativeSessionsCdAdmin(BaseAdmin):
    pass


@admin.register(models.LookupCodesCd)
class LookupCodesCdAdmin(BaseAdmin):
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


@admin.register(models.NamesCd)
class NamesCdAdmin(BaseAdmin):
    pass


@admin.register(models.ReceivedFilingsCd)
class ReceivedFilingsCdAdmin(BaseAdmin):
    pass


@admin.register(models.ReportsCd)
class ReportsCdAdmin(BaseAdmin):
    pass
