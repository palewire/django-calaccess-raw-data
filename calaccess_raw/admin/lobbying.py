#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for lobbying models.
"""
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


@admin.register(models.CvrRegistrationCd)
class CvrRegistrationCdAdmin(BaseAdmin):
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
    list_display = (
        "filing_id",
        "form_type",
        "enty_naml",
    )


@admin.register(models.LobbyAmendmentsCd)
class LobbyAmendmentsCdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "exec_date",
        "form_type",
    )
    date_hierarchy = "exec_date"


@admin.register(models.LobbyingChgLogCd)
class LobbyingChgLogCdAdmin(BaseAdmin):
    list_display = (
        "filer_id",
        "log_dt",
        "filer_full_name",
    )
    date_hierarchy = "log_dt"


@admin.register(models.LempCd)
class LempCdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "eff_date",
        "cli_naml",
        "form_type",
    )


@admin.register(models.F690P2Cd)
class F690P2CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "exec_date",
        "form_type",
    )
    date_hierarchy = "exec_date"


@admin.register(models.CvrLobbyDisclosureCd)
class CvrLobbyDisclosureCdAdmin(BaseAdmin):
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
    list_display = (
        "filing_id",
        "form_type",
        "entity_cd",
        "enty_naml",
    )


@admin.register(models.LattCd)
class LattCdAdmin(BaseAdmin):
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
    list_display = (
        "filing_id",
        "form_type",
        "emplr_naml",
        "per_total"
    )


@admin.register(models.LothCd)
class LothCdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "pmt_date",
        "form_type",
        "firm_name",
        "amount"
    )
    date_hierarchy = "pmt_date"
