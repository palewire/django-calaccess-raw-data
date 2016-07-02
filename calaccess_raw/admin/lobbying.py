#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


@admin.register(models.LobbyistEmployer1Cd)
class LobbyistEmployer1CdAdmin(BaseAdmin):
    list_display = (
        "employer_id",
        "session_id",
        "employer_name",
        "session_total_amt",
    )


@admin.register(models.LobbyistEmployer2Cd)
class LobbyistEmployer2CdAdmin(BaseAdmin):
    list_display = (
        "employer_id",
        "session_id",
        "employer_name",
        "session_total_amt",
    )


@admin.register(models.LobbyistEmployer3Cd)
class LobbyistEmployer3CdAdmin(BaseAdmin):
    list_display = (
        "employer_id",
        "session_id",
        "employer_name",
        "session_total_amt",
    )


@admin.register(models.LobbyistEmployerFirms1Cd)
class LobbyistEmployerFirms1CdAdmin(BaseAdmin):
    list_display = (
        "firm_id",
        "employer_id",
        "session_id",
        "firm_name",
        "termination_dt",
    )


@admin.register(models.LobbyistEmployerFirms2Cd)
class LobbyistEmployerFirms2CdAdmin(BaseAdmin):
    list_display = (
        "firm_id",
        "employer_id",
        "session_id",
        "firm_name",
        "termination_dt",
    )


@admin.register(models.LobbyistEmpLobbyist1Cd)
class LobbyistEmpLobbyist1CdAdmin(BaseAdmin):
    list_display = (
        "lobbyist_id",
        "employer_id",
        "session_id",
        "lobbyist_first_name",
        "lobbyist_last_name",
        "employer_name",
    )


@admin.register(models.LobbyistEmpLobbyist2Cd)
class LobbyistEmpLobbyist2CdAdmin(BaseAdmin):
    list_display = (
        "lobbyist_id",
        "employer_id",
        "session_id",
        "lobbyist_first_name",
        "lobbyist_last_name",
        "employer_name",
    )


@admin.register(models.LobbyistFirm1Cd)
class LobbyistFirm1CdAdmin(BaseAdmin):
    list_display = (
        "firm_id",
        "firm_name",
        "session_id",
        "contributor_id",
        "current_qtr_amt",
    )


@admin.register(models.LobbyistFirm2Cd)
class LobbyistFirm2CdAdmin(BaseAdmin):
    list_display = (
        "firm_id",
        "firm_name",
        "session_id",
        "contributor_id",
        "current_qtr_amt",
    )


@admin.register(models.LobbyistFirm3Cd)
class LobbyistFirm3CdAdmin(BaseAdmin):
    list_display = (
        "firm_id",
        "firm_name",
        "session_id",
        "contributor_id",
        "current_qtr_amt",
    )


@admin.register(models.LobbyistFirmEmployer1Cd)
class LobbyistFirmEmployer1CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "firm_name",
        "employer_name",
        "rpt_start",
        "per_total",
    )


@admin.register(models.LobbyistFirmEmployer2Cd)
class LobbyistFirmEmployer2CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "firm_name",
        "employer_name",
        "rpt_start",
        "per_total",
    )


@admin.register(models.LobbyistFirmLobbyist1Cd)
class LobbyistFirmLobbyist1CdAdmin(BaseAdmin):
    list_display = (
        "lobbyist_id",
        "firm_id",
        "session_id",
        "lobbyist_first_name",
        "lobbyist_last_name",
        "firm_name"
    )


@admin.register(models.LobbyistFirmLobbyist2Cd)
class LobbyistFirmLobbyist2CdAdmin(BaseAdmin):
    list_display = (
        "lobbyist_id",
        "firm_id",
        "session_id",
        "lobbyist_first_name",
        "lobbyist_last_name",
        "firm_name"
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


@admin.register(models.LobbyistContributions1Cd)
class LobbyistContributions1CdAdmin(BaseAdmin):
    list_display = (
        "filer_id",
        "filing_period_start_dt",
        "recipient_name",
        "amount"
    )
    date_hierarchy = "filing_period_start_dt"


@admin.register(models.LobbyistContributions2Cd)
class LobbyistContributions2CdAdmin(BaseAdmin):
    list_display = (
        "filer_id",
        "filing_period_start_dt",
        "recipient_name",
        "amount"
    )
    date_hierarchy = "filing_period_start_dt"


@admin.register(models.LobbyistContributions3Cd)
class LobbyistContributions3CdAdmin(BaseAdmin):
    list_display = (
        "filer_id",
        "filing_period_start_dt",
        "recipient_name",
        "amount"
    )
    date_hierarchy = "filing_period_start_dt"


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


@admin.register(models.LobbyistFirmHistoryCd)
class LobbyistFirmHistoryCdAdmin(BaseAdmin):
    list_display = (
        "contributor_id",
        "firm_id",
        "session_id",
    )


@admin.register(models.LobbyistEmployerHistoryCd)
class LobbyistEmployerHistoryCdAdmin(BaseAdmin):
    list_display = (
        "employer_id",
        "employer_name",
    )
