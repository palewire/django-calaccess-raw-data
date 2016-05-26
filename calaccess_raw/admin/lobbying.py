#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


class CvrRegistrationCdAdmin(BaseAdmin):
    pass


class Cvr2RegistrationCdAdmin(BaseAdmin):
    pass


class LobbyAmendmentsCdAdmin(BaseAdmin):
    pass


class LobbyingChgLogCdAdmin(BaseAdmin):
    pass


class LempCdAdmin(BaseAdmin):
    pass


class LobbyistEmployer1CdAdmin(BaseAdmin):
    pass


class LobbyistEmployer2CdAdmin(BaseAdmin):
    pass


class LobbyistEmployer3CdAdmin(BaseAdmin):
    pass


class LobbyistEmployerFirms1CdAdmin(BaseAdmin):
    pass


class LobbyistEmployerFirms2CdAdmin(BaseAdmin):
    pass


class LobbyistEmpLobbyist1CdAdmin(BaseAdmin):
    pass


class LobbyistEmpLobbyist2CdAdmin(BaseAdmin):
    pass


class LobbyistFirm1CdAdmin(BaseAdmin):
    pass


class LobbyistFirm2CdAdmin(BaseAdmin):
    pass


class LobbyistFirm3CdAdmin(BaseAdmin):
    pass


class LobbyistFirmEmployer1CdAdmin(BaseAdmin):
    pass


class LobbyistFirmEmployer2CdAdmin(BaseAdmin):
    pass


class LobbyistFirmLobbyist1CdAdmin(BaseAdmin):
    pass


class LobbyistFirmLobbyist2CdAdmin(BaseAdmin):
    pass


class F690P2CdAdmin(BaseAdmin):
    pass


class CvrLobbyDisclosureCdAdmin(BaseAdmin):
    pass


class Cvr2LobbyDisclosureCdAdmin(BaseAdmin):
    pass


class LattCdAdmin(BaseAdmin):
    pass


class LexpCdAdmin(BaseAdmin):
    pass


class LccmCdAdmin(BaseAdmin):
    pass


class LobbyistContributions1CdAdmin(BaseAdmin):
    pass


class LobbyistContributions2CdAdmin(BaseAdmin):
    pass


class LobbyistContributions3CdAdmin(BaseAdmin):
    pass


class LpayCdAdmin(BaseAdmin):
    pass


class LothCdAdmin(BaseAdmin):
    pass


admin.site.register(models.CvrRegistrationCd, CvrRegistrationCdAdmin)
admin.site.register(models.Cvr2RegistrationCd, Cvr2RegistrationCdAdmin)
admin.site.register(models.CvrLobbyDisclosureCd, CvrLobbyDisclosureCdAdmin)
admin.site.register(models.Cvr2LobbyDisclosureCd, Cvr2LobbyDisclosureCdAdmin)
admin.site.register(models.LobbyAmendmentsCd, LobbyAmendmentsCdAdmin)
admin.site.register(models.F690P2Cd, F690P2CdAdmin)
admin.site.register(models.LattCd, LattCdAdmin)
admin.site.register(models.LexpCd, LexpCdAdmin)
admin.site.register(models.LccmCd, LccmCdAdmin)
admin.site.register(models.LothCd, LothCdAdmin)
admin.site.register(models.LempCd, LempCdAdmin)
admin.site.register(models.LpayCd, LpayCdAdmin)
admin.site.register(models.LobbyingChgLogCd, LobbyingChgLogCdAdmin)
admin.site.register(
    models.LobbyistContributions1Cd,
    LobbyistContributions1CdAdmin
)
admin.site.register(
    models.LobbyistContributions2Cd,
    LobbyistContributions2CdAdmin
)
admin.site.register(
    models.LobbyistContributions3Cd,
    LobbyistContributions3CdAdmin
)
admin.site.register(models.LobbyistEmployer1Cd, LobbyistEmployer1CdAdmin)
admin.site.register(models.LobbyistEmployer2Cd, LobbyistEmployer2CdAdmin)
admin.site.register(models.LobbyistEmployer3Cd, LobbyistEmployer3CdAdmin)
admin.site.register(
    models.LobbyistEmployerFirms1Cd,
    LobbyistEmployerFirms1CdAdmin
)
admin.site.register(
    models.LobbyistEmployerFirms2Cd,
    LobbyistEmployerFirms2CdAdmin
)
admin.site.register(
    models.LobbyistEmpLobbyist1Cd,
    LobbyistEmpLobbyist1CdAdmin
)
admin.site.register(
    models.LobbyistEmpLobbyist2Cd,
    LobbyistEmpLobbyist2CdAdmin
)
admin.site.register(models.LobbyistFirm1Cd, LobbyistFirm1CdAdmin)
admin.site.register(models.LobbyistFirm2Cd, LobbyistFirm2CdAdmin)
admin.site.register(models.LobbyistFirm3Cd, LobbyistFirm3CdAdmin)
admin.site.register(
    models.LobbyistFirmEmployer1Cd,
    LobbyistFirmEmployer1CdAdmin
)
admin.site.register(
    models.LobbyistFirmEmployer2Cd,
    LobbyistFirmEmployer2CdAdmin
)
admin.site.register(
    models.LobbyistFirmLobbyist1Cd,
    LobbyistFirmLobbyist1CdAdmin
)
admin.site.register(
    models.LobbyistFirmLobbyist2Cd,
    LobbyistFirmLobbyist2CdAdmin
)
