#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for inactive models.
"""
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


@admin.register(models.BallotMeasuresCd)
class BallotMeasuresCdAdmin(BaseAdmin):
    """
    Custom admin for the BallotMeasuresCd model.
    """
    list_display = ("measure_name", "election_date", "jurisdiction")


@admin.register(models.CvrF470Cd)
class CvrF470CdAdmin(BaseAdmin):
    """
    Custom admin for the CvrF470Cd model.
    """
    list_display = ("filing_id", "filer_naml",)


@admin.register(models.FilerTypePeriodsCd)
class FilerTypePeriodsCd(BaseAdmin):
    """
    Custom admin for the FilerTypePeriodsCd model.
    """
    list_display = ("election_type", "filer_type", "period_id")


@admin.register(models.LobbyistContributions1Cd)
class LobbyistContributions1CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistContributions1Cd model.
    """
    list_display = (
        "filer_id",
        "filing_period_start_dt",
        "recipient_name",
        "amount"
    )
    date_hierarchy = "filing_period_start_dt"


@admin.register(models.LobbyistContributions2Cd)
class LobbyistContributions2CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistContributions2Cd model.
    """
    list_display = (
        "filer_id",
        "filing_period_start_dt",
        "recipient_name",
        "amount"
    )
    date_hierarchy = "filing_period_start_dt"


@admin.register(models.LobbyistContributions3Cd)
class LobbyistContributions3CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistContributions3Cd model.
    """
    list_display = (
        "filer_id",
        "filing_period_start_dt",
        "recipient_name",
        "amount"
    )
    date_hierarchy = "filing_period_start_dt"


@admin.register(models.LobbyistEmpLobbyist1Cd)
class LobbyistEmpLobbyist1CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistEmpLobbyist1Cd model.
    """
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
    """
    Custom admin for the LobbyistEmpLobbyist2Cd model.
    """
    list_display = (
        "lobbyist_id",
        "employer_id",
        "session_id",
        "lobbyist_first_name",
        "lobbyist_last_name",
        "employer_name",
    )


@admin.register(models.LobbyistEmployer1Cd)
class LobbyistEmployer1CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistEmployer1Cd model.
    """
    list_display = (
        "employer_id",
        "session_id",
        "employer_name",
        "session_total_amt",
    )


@admin.register(models.LobbyistEmployer2Cd)
class LobbyistEmployer2CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistEmployer2Cd model.
    """
    list_display = (
        "employer_id",
        "session_id",
        "employer_name",
        "session_total_amt",
    )


@admin.register(models.LobbyistEmployer3Cd)
class LobbyistEmployer3CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistEmployer3Cd model.
    """
    list_display = (
        "employer_id",
        "session_id",
        "employer_name",
        "session_total_amt",
    )


@admin.register(models.LobbyistEmployerFirms1Cd)
class LobbyistEmployerFirms1CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistEmployerFirms1Cd model.
    """
    list_display = (
        "firm_id",
        "employer_id",
        "session_id",
        "firm_name",
        "termination_dt",
    )


@admin.register(models.LobbyistEmployerFirms2Cd)
class LobbyistEmployerFirms2CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistEmployerFirms2Cd model.
    """
    list_display = (
        "firm_id",
        "employer_id",
        "session_id",
        "firm_name",
        "termination_dt",
    )


@admin.register(models.LobbyistEmployerHistoryCd)
class LobbyistEmployerHistoryCdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistEmployerHistoryCd model.
    """
    list_display = ("employer_id", "employer_name")


@admin.register(models.LobbyistFirm1Cd)
class LobbyistFirm1CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistFirm1Cd model.
    """
    list_display = (
        "firm_id",
        "firm_name",
        "session_id",
        "contributor_id",
        "current_qtr_amt",
    )


@admin.register(models.LobbyistFirm2Cd)
class LobbyistFirm2CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistFirm2Cd model.
    """
    list_display = (
        "firm_id",
        "firm_name",
        "session_id",
        "contributor_id",
        "current_qtr_amt",
    )


@admin.register(models.LobbyistFirm3Cd)
class LobbyistFirm3CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistFirm3Cd model.
    """
    list_display = (
        "firm_id",
        "firm_name",
        "session_id",
        "contributor_id",
        "current_qtr_amt",
    )


@admin.register(models.LobbyistFirmEmployer1Cd)
class LobbyistFirmEmployer1CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistFirm2Cd model.
    """
    list_display = (
        "filing_id",
        "firm_name",
        "employer_name",
        "rpt_start",
        "per_total",
    )


@admin.register(models.LobbyistFirmEmployer2Cd)
class LobbyistFirmEmployer2CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistFirmEmployer2Cd model.
    """
    list_display = (
        "filing_id",
        "firm_name",
        "employer_name",
        "rpt_start",
        "per_total",
    )


@admin.register(models.LobbyistFirmHistoryCd)
class LobbyistFirmHistoryCdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistFirm2Cd model.
    """
    list_display = ("contributor_id", "firm_id", "session_id")


@admin.register(models.LobbyistFirmLobbyist1Cd)
class LobbyistFirmLobbyist1CdAdmin(BaseAdmin):
    """
    Custom admin for the LobbyistFirm2Cd model.
    """
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
    """
    Custom admin for the LobbyistFirm2Cd model.
    """
    list_display = (
        "lobbyist_id",
        "firm_id",
        "session_id",
        "lobbyist_first_name",
        "lobbyist_last_name",
        "firm_name"
    )


@admin.register(models.EfsFilingLogCd)
class EfsFilingLogCdAdmin(BaseAdmin):
    """
    Custom admin for the EfsFilingLogCd model.
    """
    list_display = (
        "id",
        "vendor",
        "filing_date",
        "filingstatus",
        "form_type",
    )
    date_hierarchy = "filing_date"
