from calaccess import models
from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    save_on_top = True


class AcronymsCdAdmin(BaseAdmin):
    pass


class AddressCdAdmin(BaseAdmin):
    pass


class BallotMeasuresCdAdmin(BaseAdmin):
    pass


class CvrSoAdmin(BaseAdmin):
    pass


class Cvr2CampaignDisclosureCdAdmin(BaseAdmin):
    pass


class CvrCampaignDisclosureCdAdmin(BaseAdmin):
    pass


class DebtCdAdmin(BaseAdmin):
    pass


class ExpnCdAdmin(BaseAdmin):
    pass


class FilernameCdAdmin(BaseAdmin):
    pass


class FilersCdAdmin(BaseAdmin):
    pass


class FilerAcronymsCdAdmin(BaseAdmin):
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


class HdrCdAdmin(BaseAdmin):
    pass


class LoanCdAdmin(BaseAdmin):
    pass


class LobbyingChgLogCdAdmin(BaseAdmin):
    pass


class LookupCodeAdmin(BaseAdmin):
    pass


class NamesCdAdmin(BaseAdmin):
    pass


class RcptCdAdmin(BaseAdmin):
    pass


class SpltCdAdmin(BaseAdmin):
    pass


class S401CdAdmin(BaseAdmin):
    pass


class S496CdAdmin(BaseAdmin):
    pass


class S497CdAdmin(BaseAdmin):
    pass


class S498CdAdmin(BaseAdmin):
    pass


admin.site.register(models.AcronymsCd, AcronymsCdAdmin)
admin.site.register(models.AddressCd, AddressCdAdmin)
admin.site.register(models.BallotMeasuresCd, BallotMeasuresCdAdmin)
admin.site.register(models.CvrSo, CvrSoAdmin)
admin.site.register(models.Cvr2SoCd, BaseAdmin)
admin.site.register(models.Cvr3VerificationInfoCd, BaseAdmin)
admin.site.register(
    models.Cvr2CampaignDisclosureCd,
    Cvr2CampaignDisclosureCdAdmin
)
admin.site.register(
    models.CvrCampaignDisclosureCd,
    CvrCampaignDisclosureCdAdmin
)
admin.site.register(models.DebtCd, DebtCdAdmin)
admin.site.register(models.ExpnCd, ExpnCdAdmin)
admin.site.register(models.EfsFilingLogCd, BaseAdmin)
admin.site.register(models.F495P2Cd, BaseAdmin)
admin.site.register(models.FilernameCd, FilernameCdAdmin)
admin.site.register(models.FilersCd, FilersCdAdmin)
admin.site.register(models.FilerAcronymsCd, FilerAcronymsCdAdmin)
admin.site.register(models.FilerAddressCd, BaseAdmin)
admin.site.register(models.FilerEthicsClassCd, BaseAdmin)
admin.site.register(models.FilerInterestsCd, FilerInterestsCdAdmin)
admin.site.register(models.FilerLinksCd, FilerLinksCdAdmin)
admin.site.register(models.FilerStatusTypesCd, FilerStatusTypesCdAdmin)
admin.site.register(models.FilerToFilerTypeCd, FilerToFilerTypeCdAdmin)
admin.site.register(models.FilerTypesCd, FilerTypesCdAdmin)
admin.site.register(models.FilerXrefCd, FilerXrefCdAdmin)
admin.site.register(models.FilingPeriodCd, FilingPeriodCdAdmin)
admin.site.register(models.GroupTypesCd, BaseAdmin)
admin.site.register(models.HeaderCd, BaseAdmin)
admin.site.register(models.HdrCd, HdrCdAdmin)
admin.site.register(models.ImageLinksCd, BaseAdmin)
admin.site.register(models.LegislativeSessionsCd, BaseAdmin)
admin.site.register(models.LobbyingChgLogCd, BaseAdmin)
admin.site.register(models.LoanCd, LoanCdAdmin)
admin.site.register(models.LobbyingChgLogCd, LobbyingChgLogCdAdmin)
admin.site.register(models.LookupCode, LookupCodeAdmin)
admin.site.register(models.NamesCd, NamesCdAdmin)
admin.site.register(models.RcptCd, RcptCdAdmin)
admin.site.register(models.SpltCd, SpltCdAdmin)
admin.site.register(models.S401Cd, S401CdAdmin)
admin.site.register(models.S496Cd, S496CdAdmin)
admin.site.register(models.S497Cd, S497CdAdmin)
admin.site.register(models.S498Cd, S498CdAdmin)
