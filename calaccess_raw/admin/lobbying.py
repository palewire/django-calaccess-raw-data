#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for lobbying models.
"""
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


@admin.register(models.CvrRegistrationCd)
class CvrRegistrationCdAdmin(BaseAdmin):
    """
    Custom admin for the CvrRegistrationCd model.
    """
    list_display = (
        "filing_id",
        "rpt_date",
        "form_type",
        "filer_naml",
        "firm_name",
    )
    date_hierarchy = "rpt_date"


@admin.register(models.Cvr2RegistrationCd)
class Cvr2RegistrationCdAdmin(BaseAdmin):
    """
    Custom admin for the Cvr2RegistrationCd model.
    """
    list_display = (
        "filing_id",
        "form_type",
        "enty_naml",
    )


@admin.register(models.LobbyAmendmentsCd)
class LobbyAmendmentsCdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyAmendmentsCd model.
    """
    list_display = (
        "filing_id",
        "exec_date",
        "form_type",
    )
    date_hierarchy = "exec_date"


@admin.register(models.LobbyingChgLogCd)
class LobbyingChgLogCdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyingChgLogCd model.
    """
    list_display = (
        "filer_id",
        "entity_type",
        "log_dt",
        "filer_full_name",
    )
    date_hierarchy = "log_dt"


@admin.register(models.LempCd)
class LempCdAdmin(BaseAdmin):
    """
    Custom admin for the LempCd model.
    """
    list_display = (
        "filing_id",
        "eff_date",
        "cli_naml",
        "form_type",
    )


@admin.register(models.F690P2Cd)
class F690P2CdAdmin(BaseAdmin):
    """
    Custom admin for the F690P2Cd model.
    """
    list_display = (
        "filing_id",
        "exec_date",
        "form_type",
    )
    date_hierarchy = "exec_date"


@admin.register(models.CvrLobbyDisclosureCd)
class CvrLobbyDisclosureCdAdmin(BaseAdmin):
    """
    Custom admin for the CvrLobbyDisclosureCd model.
    """
    list_display = (
        "filing_id",
        "rpt_date",
        "filer_naml",
        "firm_name",
        "form_type",
    )
    date_hierarchy = "rpt_date"


@admin.register(models.Cvr2LobbyDisclosureCd)
class Cvr2LobbyDisclosureCdAdmin(BaseAdmin):
    """
    Custom admin for the Cvr2LobbyDisclosureCd model.
    """
    list_display = (
        "filing_id",
        "form_type",
        "entity_cd",
        "enty_naml",
    )


@admin.register(models.LattCd)
class LattCdAdmin(BaseAdmin):
    """
    Custom admin for the LattCd model.
    """
    list_display = (
        "filing_id",
        "form_type",
        "pmt_date",
        "recip_naml",
        "amount"
    )
    date_hierarchy = "pmt_date"


@admin.register(models.LexpCd)
class LexpCdAdmin(BaseAdmin):
    """
    Custom admin for the LexpCd model.
    """
    list_display = (
        "filing_id",
        "expn_date",
        "form_type",
        "payee_naml",
        "amount"
    )
    date_hierarchy = "expn_date"


@admin.register(models.LccmCd)
class LccmCdAdmin(BaseAdmin):
    """
    Custom admin for the LccmCd model.
    """
    list_display = (
        "filing_id",
        "form_type",
        "ctrib_date",
        "ctrib_naml",
        "recip_naml",
    )
    date_hierarchy = "ctrib_date"


@admin.register(models.LpayCd)
class LpayCdAdmin(BaseAdmin):
    """
    Custom admin for the LpayCd model.
    """
    list_display = (
        "filing_id",
        "form_type",
        "emplr_naml",
        "per_total"
    )


@admin.register(models.LothCd)
class LothCdAdmin(BaseAdmin):
    """
    Custom admin for the LothCd model.
    """
    list_display = (
        "filing_id",
        "pmt_date",
        "form_type",
        "firm_name",
        "amount"
    )
    date_hierarchy = "pmt_date"
