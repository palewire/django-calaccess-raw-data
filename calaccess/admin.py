from calaccess import models
from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    save_on_top = True


class CvrSoAdmin(BaseAdmin):
    pass


class Cvr2CampaignDisclosureCdAdmin(BaseAdmin):
    pass


class CvrCampaignDisclosureCdAdmin(BaseAdmin):
    pass


class CvrLobbyDisclosureCdAdmin(BaseAdmin):
    pass


class Cvr2LobbyDisclosureCdAdmin(BaseAdmin):
    pass


class CvrRegistrationCdAdmin(BaseAdmin):
    pass


class Cvr2RegistrationCdAdmin(BaseAdmin):
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


class FilerFilingsCdAdmin(BaseAdmin):
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


class FilingsCdAdmin(BaseAdmin):
    pass


class FilingPeriodCdAdmin(BaseAdmin):
    pass


class HdrCdAdmin(BaseAdmin):
    pass


class LattCdAdmin(BaseAdmin):
    pass


class LccmCdAdmin(BaseAdmin):
    pass


class LempCdAdmin(BaseAdmin):
    pass


class LexpCdAdmin(BaseAdmin):
    pass


class LoanCdAdmin(BaseAdmin):
    pass


class LobbyAmendmentsCdAdmin(BaseAdmin):
    pass


class LookupCodeAdmin(BaseAdmin):
    pass


class LothCdAdmin(BaseAdmin):
    pass


class LpayCdAdmin(BaseAdmin):
    pass


class NamesCdAdmin(BaseAdmin):
    pass


class RcptCdAdmin(BaseAdmin):
    pass


class SmryCdAdmin(BaseAdmin):
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


admin.site.register(models.CvrSo, CvrSoAdmin)
admin.site.register(
    models.Cvr2CampaignDisclosureCd,
    Cvr2CampaignDisclosureCdAdmin
)
admin.site.register(
    models.CvrCampaignDisclosureCd,
    CvrCampaignDisclosureCdAdmin
)
admin.site.register(models.CvrLobbyDisclosureCd, CvrLobbyDisclosureCdAdmin)
admin.site.register(models.Cvr2LobbyDisclosureCd, Cvr2LobbyDisclosureCdAdmin)
admin.site.register(models.CvrRegistrationCd, CvrRegistrationCdAdmin)
admin.site.register(models.Cvr2RegistrationCd, Cvr2RegistrationCdAdmin)
admin.site.register(models.DebtCd, DebtCdAdmin)
admin.site.register(models.ExpnCd, ExpnCdAdmin)
admin.site.register(models.FilernameCd, FilernameCdAdmin)
admin.site.register(models.FilersCd, FilersCdAdmin)
admin.site.register(models.FilerAcronymsCd, FilerAcronymsCdAdmin)
admin.site.register(models.FilerFilingsCd, FilerFilingsCdAdmin)
admin.site.register(models.FilerInterestsCd, FilerInterestsCdAdmin)
admin.site.register(models.FilerLinksCd, FilerLinksCdAdmin)
admin.site.register(models.FilerStatusTypesCd, FilerStatusTypesCdAdmin)
admin.site.register(models.FilerToFilerTypeCd, FilerToFilerTypeCdAdmin)
admin.site.register(models.FilerTypesCd, FilerTypesCdAdmin)
admin.site.register(models.FilerXrefCd, FilerXrefCdAdmin)
admin.site.register(models.FilingsCd, FilingsCdAdmin)
admin.site.register(models.FilingPeriodCd, FilingPeriodCdAdmin)
admin.site.register(models.HdrCd, HdrCdAdmin)
admin.site.register(models.LattCd, LattCdAdmin)
admin.site.register(models.LccmCd, LccmCdAdmin)
admin.site.register(models.LempCd, LempCdAdmin)
admin.site.register(models.LexpCd, LexpCdAdmin)
admin.site.register(models.LoanCd, LoanCdAdmin)
admin.site.register(models.LobbyAmendmentsCd, LobbyAmendmentsCdAdmin)
admin.site.register(models.LookupCode, LookupCodeAdmin)
admin.site.register(models.LothCd, LothCdAdmin)
admin.site.register(models.LpayCd, LpayCdAdmin)
admin.site.register(models.NamesCd, NamesCdAdmin)
admin.site.register(models.RcptCd, RcptCdAdmin)
admin.site.register(models.SmryCd, SmryCdAdmin)
admin.site.register(models.SpltCd, SpltCdAdmin)
admin.site.register(models.S401Cd, S401CdAdmin)
admin.site.register(models.S496Cd, S496CdAdmin)
admin.site.register(models.S497Cd, S497CdAdmin)
admin.site.register(models.S498Cd, S498CdAdmin)
