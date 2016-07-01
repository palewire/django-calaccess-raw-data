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
    list_display = ("filing_id", "filer_naml", "office_cd", "cand_naml", "pmnt_dt", "pmnt_amount")
    list_filter = ("office_cd",)
    search_fields = ("filer_namf", "filer_naml", "cand_naml", "cand_namf")
    date_hierarchy = "pmnt_dt"


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
    list_display = ("acronym", "filer_id")
    search_fields = ("acronym",)


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
    list_display = ("filer_id", "session_id", "ethics_date",)
    search_fields = ("filer_id",)
    date_hierarchy = "ethics_date"


@admin.register(models.FilerInterestsCd)
class FilerInterestsCdAdmin(BaseAdmin):
    list_display = (
        "filer_id",
        "session_id",
        "interest_cd",
        "effect_date"
    )
    list_filter = ("interest_cd",)
    search_fields = ("filter_id",)
    date_hierarchy = "effect_date"


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
    list_display = ("filer_id", "xref_id", "effect_dt", "migration_source")
    list_filter = ("migration_source",)
    search_fields = ("filer_id", "xref_id",)
    date_hierarchy = "effect_dt"


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
    list_display = ("grp_id", "grp_name", "grp_desc")
    search_fields = ("grp_id", "grp_name", "grp_desc")


@admin.register(models.HeaderCd)
class HeaderCdAdmin(BaseAdmin):
    list_display = ("line_number", "form_id", "rec_type",)
    list_filter = ("rec_type",)


@admin.register(models.HdrCd)
class HdrCdAdmin(BaseAdmin):
    list_display = ("filing_id", "amend_id", "cal_ver", "soft_name", "soft_ver",)
    list_filter = ("cal_ver", "soft_name",)
    search_fields = ("filing_id",)


@admin.register(models.ImageLinksCd)
class ImageLinksCdAdmin(BaseAdmin):
    list_display = ("img_link_id", "img_link_type", "img_id", "img_type", "img_dt")
    list_filter = ("img_link_type", "img_type")
    search_fields = ("img_link_id", "img_id")
    date_hierarchy = "img_dt"


@admin.register(models.LegislativeSessionsCd)
class LegislativeSessionsCdAdmin(BaseAdmin):
    list_display = ("session_id", "begin_date", "end_date")
    search_fields = ("session_id",)
    date_hierarchy = "begin_date"


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
    list_display = ("namid", "namf", "naml",)
    search_fields = ("namid", "namt", "namf", "naml", "nams", "moniker")


@admin.register(models.ReceivedFilingsCd)
class ReceivedFilingsCdAdmin(BaseAdmin):
    list_display = ("filing_id", "filer_id", "form_id", "received_date",)
    list_filter = ("form_id",)
    search_fields = ("filing_id", "filer_id", "form_id",)
    date_hierarchy = "received_date"


@admin.register(models.ReportsCd)
class ReportsCdAdmin(BaseAdmin):
    list_display = ("rpt_name", "rpt_id", "rpt_type")
    list_filter = ("rpt_type",)
    search_fields = ("rpt_id", "rpt_name")
