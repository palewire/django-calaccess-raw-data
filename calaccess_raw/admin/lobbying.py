from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


class CvrRegistrationCdAdmin(BaseAdmin):
    pass


class Cvr2RegistrationCdAdmin(BaseAdmin):
    pass


class CvrLobbyDisclosureCdAdmin(BaseAdmin):
    pass


class Cvr2LobbyDisclosureCdAdmin(BaseAdmin):
    pass


class LobbyAmendmentsCdAdmin(BaseAdmin):
    pass


class F690P2CdAdmin(BaseAdmin):
    pass


class LattCdAdmin(BaseAdmin):
    pass


class LexpCdAdmin(BaseAdmin):
    pass


class LccmCdAdmin(BaseAdmin):
    pass


class LothCdAdmin(BaseAdmin):
    pass


class LempCdAdmin(BaseAdmin):
    pass


class LpayCdAdmin(BaseAdmin):
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
