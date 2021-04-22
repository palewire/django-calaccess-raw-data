#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for common models.
"""
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


@admin.register(models.FilernameCd)
class FilernameCdAdmin(BaseAdmin):
    """
    Custom admin for the FilernameCd model.
    """
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
    date_hierarchy = "effect_dt"


@admin.register(models.FilerFilingsCd)
class FilerFilingsCdAdmin(BaseAdmin):
    """
    Custom admin for the FilerFilingsCd model.
    """
    list_display = (
        "id", "filer_id", "form_id",
        "filing_id", "filing_sequence"
    )


@admin.register(models.FilingsCd)
class FilingsCdAdmin(BaseAdmin):
    """
    Custom admin for the FilingsCd model.
    """
    list_display = ("filing_id", "filing_type")


@admin.register(models.SmryCd)
class SmryCdAdmin(BaseAdmin):
    """
    Custom admin for the SmryCd model.
    """
    list_display = (
        'filing_id',
        'amend_id',
        'form_type',
        'line_item',
        'amount_a',
        'amount_b',
        'amount_c',
    )


@admin.register(models.SpltCd)
class SpltCdAdmin(BaseAdmin):
    """
    Custom admin for the SpltCd model.
    """
    list_display = (
        "filing_id",
        "amend_id",
        "line_item",
        "pform_type",
        "elec_date",
        "elec_amount",
    )
    date_hierarchy = "elec_date"


@admin.register(models.TextMemoCd)
class TextMemoCdAdmin(BaseAdmin):
    """
    Custom admin for the TextMemoCd model.
    """
    list_display = ("filing_id", "amend_id", "form_type")


@admin.register(models.CvrE530Cd)
class CvrE530CdAdmin(BaseAdmin):
    """
    Custom admin for the CvrE530Cd model.
    """
    list_display = ("filing_id", "filer_naml", "office_cd", "cand_naml", "pmnt_dt", "pmnt_amount")
    date_hierarchy = "pmnt_dt"


@admin.register(models.AcronymsCd)
class AcronymsCdAdmin(BaseAdmin):
    """
    Custom admin for the AcronymsCd model.
    """
    list_display = ("acronym", "stands_for", "effect_dt", "a_desc")
    date_hierarchy = 'effect_dt'


@admin.register(models.AddressCd)
class AddressCdAdmin(BaseAdmin):
    """
    Custom admin for the AddressCd model.
    """
    list_display = ("adrid", "city", "st", "zip4",)


@admin.register(models.FilersCd)
class FilersCdAdmin(BaseAdmin):
    """
    Custom admin for the FilersCd model.
    """
    list_display = ("filer_id",)


@admin.register(models.FilerAcronymsCd)
class FilerAcronymsCdAdmin(BaseAdmin):
    """
    Custom admin for the FilerAcronymsCd model.
    """
    list_display = ("acronym", "filer_id")


@admin.register(models.FilerAddressCd)
class FilerAddressCdAdmin(BaseAdmin):
    """
    Custom admin for the FilerAddressCd model.
    """
    list_display = (
        "filer_id",
        "adrid",
        "effect_dt",
        "add_type"
    )


@admin.register(models.FilerEthicsClassCd)
class FilerEthicsClassCdAdmin(BaseAdmin):
    """
    Custom admin for the FilerEthicsClassCd model.
    """
    list_display = ("filer_id", "session_id", "ethics_date",)
    date_hierarchy = "ethics_date"


@admin.register(models.FilerInterestsCd)
class FilerInterestsCdAdmin(BaseAdmin):
    """
    Custom admin for the FilerInterestsCd model.
    """
    list_display = (
        "filer_id",
        "session_id",
        "interest_cd",
        "effect_date"
    )
    date_hierarchy = "effect_date"


@admin.register(models.FilerLinksCd)
class FilerLinksCdAdmin(BaseAdmin):
    """
    Custom admin for the FilerLinksCd model.
    """
    list_display = (
        "filer_id_a",
        "filer_id_b",
        "link_type",
        "active_flg",
        "effect_dt",
        "termination_dt",
    )


@admin.register(models.FilerStatusTypesCd)
class FilerStatusTypesCdAdmin(BaseAdmin):
    """
    Custom admin for the FilerStatusTypesCd model.
    """
    list_display = ("status_type", "status_desc")


@admin.register(models.FilerToFilerTypeCd)
class FilerToFilerTypeCdAdmin(BaseAdmin):
    """
    Custom admin for the FilerToFilerTypeCd model.
    """
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
    date_hierarchy = "effect_dt"


@admin.register(models.FilerTypesCd)
class FilerTypesCdAdmin(BaseAdmin):
    """
    Custom admin for the FilerTypesCd model.
    """
    list_display = (
        "filer_type",
        "description",
        "grp_type",
        "calc_use",
        "grace_period",
    )


@admin.register(models.FilerXrefCd)
class FilerXrefCdAdmin(BaseAdmin):
    """
    Custom admin for the FilerXrefCd model.
    """
    list_display = ("filer_id", "xref_id", "effect_dt", "migration_source")
    date_hierarchy = "effect_dt"


@admin.register(models.FilingPeriodCd)
class FilingPeriodCdAdmin(BaseAdmin):
    """
    Custom admin for the FilingPeriodCd model.
    """
    list_display = ("period_id", "start_date", "end_date", "period_desc")


@admin.register(models.GroupTypesCd)
class GroupTypesCdAdmin(BaseAdmin):
    """
    Custom admin for the GroupTypesCd model.
    """
    list_display = ("grp_id", "grp_name", "grp_desc")


@admin.register(models.HeaderCd)
class HeaderCdAdmin(BaseAdmin):
    """
    Custom admin for the HeaderCd model.
    """
    list_display = ("line_number", "form_id", "rec_type",)


@admin.register(models.HdrCd)
class HdrCdAdmin(BaseAdmin):
    """
    Custom admin for the HdrCd model.
    """
    list_display = ("filing_id", "amend_id", "cal_ver", "soft_name", "soft_ver",)


@admin.register(models.ImageLinksCd)
class ImageLinksCdAdmin(BaseAdmin):
    """
    Custom admin for the ImageLinksCd model.
    """
    list_display = ("img_link_id", "img_link_type", "img_id", "img_type", "img_dt")
    date_hierarchy = "img_dt"


@admin.register(models.LegislativeSessionsCd)
class LegislativeSessionsCdAdmin(BaseAdmin):
    """
    Custom admin for the LegislativeSessionsCd model.
    """
    list_display = ("session_id", "begin_date", "end_date")
    date_hierarchy = "begin_date"


@admin.register(models.LookupCodesCd)
class LookupCodesCdAdmin(BaseAdmin):
    """
    Custom admin for the LookupCodesCd model.
    """
    list_display = (
        "code_type",
        "code_id",
        "code_desc",
    )


@admin.register(models.NamesCd)
class NamesCdAdmin(BaseAdmin):
    """
    Custom admin for the NamesCd model.
    """
    list_display = ("namid", "namf", "naml",)


@admin.register(models.ReceivedFilingsCd)
class ReceivedFilingsCdAdmin(BaseAdmin):
    """
    Custom admin for the ReceivedFilingsCd model.
    """
    list_display = ("filing_id", "filer_id", "form_id", "received_date",)
    date_hierarchy = "received_date"


@admin.register(models.ReportsCd)
class ReportsCdAdmin(BaseAdmin):
    """
    Custom admin for the ReportsCd model.
    """
    list_display = ("rpt_name", "rpt_id", "rpt_type")
