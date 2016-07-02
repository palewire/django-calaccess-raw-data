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
    pass


@admin.register(models.LobbyistEmployer1Cd)
class LobbyistEmployer1CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistEmployer2Cd)
class LobbyistEmployer2CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistEmployer3Cd)
class LobbyistEmployer3CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistEmployerFirms1Cd)
class LobbyistEmployerFirms1CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistEmployerFirms2Cd)
class LobbyistEmployerFirms2CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistEmpLobbyist1Cd)
class LobbyistEmpLobbyist1CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistEmpLobbyist2Cd)
class LobbyistEmpLobbyist2CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistFirm1Cd)
class LobbyistFirm1CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistFirm2Cd)
class LobbyistFirm2CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistFirm3Cd)
class LobbyistFirm3CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistFirmEmployer1Cd)
class LobbyistFirmEmployer1CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistFirmEmployer2Cd)
class LobbyistFirmEmployer2CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistFirmLobbyist1Cd)
class LobbyistFirmLobbyist1CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistFirmLobbyist2Cd)
class LobbyistFirmLobbyist2CdAdmin(BaseAdmin):
    pass


@admin.register(models.F690P2Cd)
class F690P2CdAdmin(BaseAdmin):
    pass


@admin.register(models.CvrLobbyDisclosureCd)
class CvrLobbyDisclosureCdAdmin(BaseAdmin):
    pass


@admin.register(models.Cvr2LobbyDisclosureCd)
class Cvr2LobbyDisclosureCdAdmin(BaseAdmin):
    pass


@admin.register(models.LattCd)
class LattCdAdmin(BaseAdmin):
    pass


@admin.register(models.LexpCd)
class LexpCdAdmin(BaseAdmin):
    pass


@admin.register(models.LccmCd)
class LccmCdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistContributions1Cd)
class LobbyistContributions1CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistContributions2Cd)
class LobbyistContributions2CdAdmin(BaseAdmin):
    pass


@admin.register(models.LobbyistContributions3Cd)
class LobbyistContributions3CdAdmin(BaseAdmin):
    pass


@admin.register(models.LpayCd)
class LpayCdAdmin(BaseAdmin):
    pass


@admin.register(models.LothCd)
class LothCdAdmin(BaseAdmin):
    pass
