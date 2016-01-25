#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


class CvrSoCdAdmin(BaseAdmin):
    pass


class Cvr2SoCdAdmin(BaseAdmin):
    pass


class Cvr2CampaignDisclosureCdAdmin(BaseAdmin):
    pass


class CvrCampaignDisclosureCdAdmin(BaseAdmin):
    pass


class Cvr3VerificationInfoCdAdmin(BaseAdmin):
    pass


class DebtCdAdmin(BaseAdmin):
    pass


class ExpnCdAdmin(BaseAdmin):
    pass


class LoanCdAdmin(BaseAdmin):
    pass


class RcptCdAdmin(BaseAdmin):
    list_display = (
        "id",
        "filing_id",
        "amend_id",
        "form_type",
        "rcpt_date",
        "ctrib_namf",
        "ctrib_naml",
        "amount"
    )
    search_fields = ("ctrib_namf", "ctrib_naml",)


class F495P2CdAdmin(BaseAdmin):
    pass


class SpltCdAdmin(BaseAdmin):
    pass


class S496CdAdmin(BaseAdmin):
    pass


class S497CdAdmin(BaseAdmin):
    pass


class S498CdAdmin(BaseAdmin):
    pass


class S401CdAdmin(BaseAdmin):
    pass


class F501502CdAdmin(BaseAdmin):
    pass


admin.site.register(models.CvrSoCd, CvrSoCdAdmin)
admin.site.register(models.Cvr2SoCd, Cvr2SoCdAdmin)
admin.site.register(models.Cvr3VerificationInfoCd, Cvr3VerificationInfoCdAdmin)
admin.site.register(
    models.CvrCampaignDisclosureCd,
    CvrCampaignDisclosureCdAdmin
)
admin.site.register(
    models.Cvr2CampaignDisclosureCd,
    Cvr2CampaignDisclosureCdAdmin
)
admin.site.register(models.DebtCd, DebtCdAdmin)
admin.site.register(models.ExpnCd, ExpnCdAdmin)
admin.site.register(models.F495P2Cd, F495P2CdAdmin)
admin.site.register(models.LoanCd, LoanCdAdmin)
admin.site.register(models.RcptCd, RcptCdAdmin)
admin.site.register(models.SpltCd, SpltCdAdmin)
admin.site.register(models.S496Cd, S496CdAdmin)
admin.site.register(models.S497Cd, S497CdAdmin)
admin.site.register(models.S498Cd, S498CdAdmin)
admin.site.register(models.S401Cd, S401CdAdmin)
admin.site.register(models.F501502Cd, F501502CdAdmin)
