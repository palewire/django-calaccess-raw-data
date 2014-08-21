from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


class AcronymsCdAdmin(BaseAdmin):
    pass


class AddressCdAdmin(BaseAdmin):
    pass


class BallotMeasuresCdAdmin(BaseAdmin):
    pass


class EfsFilingLogCdAdmin(BaseAdmin):
    pass


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
    list_filter = ("filer_type",)


class FilersCdAdmin(BaseAdmin):
    pass


class FilerAcronymsCdAdmin(BaseAdmin):
    pass


class FilerAddressCdAdmin(BaseAdmin):
    pass


class FilerEthicsClassCdAdmin(BaseAdmin):
    pass


class FilerInterestsCdAdmin(BaseAdmin):
    pass


class FilerLinksCdAdmin(BaseAdmin):
    pass


class FilerStatusTypesCdAdmin(BaseAdmin):
    pass


class FilerToFilerTypeCdAdmin(BaseAdmin):
    pass


class FilerTypesCdAdmin(BaseAdmin):
    pass


class FilerXrefCdAdmin(BaseAdmin):
    pass


class FilingPeriodCdAdmin(BaseAdmin):
    pass


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


class LobbyingChgLogCdAdmin(BaseAdmin):
    pass


class LobbyistContributions1CdAdmin(BaseAdmin):
    pass


class LobbyistContributions2CdAdmin(BaseAdmin):
    pass


class LobbyistContributions3CdAdmin(BaseAdmin):
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


class LookupCodeAdmin(BaseAdmin):
    pass


class NamesCdAdmin(BaseAdmin):
    pass


class ReceivedFilingsCdAdmin(BaseAdmin):
    pass


class ReportsCdAdmin(BaseAdmin):
    pass


admin.site.register(models.AcronymsCd, AcronymsCdAdmin)
admin.site.register(models.AddressCd, AddressCdAdmin)
admin.site.register(models.BallotMeasuresCd, BallotMeasuresCdAdmin)
admin.site.register(models.EfsFilingLogCd, BaseAdmin)
admin.site.register(models.FilernameCd, FilernameCdAdmin)
admin.site.register(models.FilersCd, FilersCdAdmin)
admin.site.register(models.FilerAcronymsCd, FilerAcronymsCdAdmin)
admin.site.register(models.FilerAddressCd, FilerAddressCdAdmin)
admin.site.register(models.FilerEthicsClassCd, FilerEthicsClassCdAdmin)
admin.site.register(models.FilerInterestsCd, FilerInterestsCdAdmin)
admin.site.register(models.FilerLinksCd, FilerLinksCdAdmin)
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
admin.site.register(models.LookupCode, LookupCodeAdmin)
admin.site.register(models.NamesCd, NamesCdAdmin)
admin.site.register(models.ReceivedFilingsCd, ReceivedFilingsCdAdmin)
admin.site.register(models.ReportsCd, ReportsCdAdmin)
