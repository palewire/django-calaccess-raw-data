#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


@admin.register(models.CvrSoCd)
class CvrSoCdAdmin(BaseAdmin):
    pass


@admin.register(models.Cvr2SoCd)
class Cvr2SoCdAdmin(BaseAdmin):
    pass


@admin.register(models.Cvr2CampaignDisclosureCd)
class Cvr2CampaignDisclosureCdAdmin(BaseAdmin):
    pass


@admin.register(models.CvrCampaignDisclosureCd)
class CvrCampaignDisclosureCdAdmin(BaseAdmin):
    pass


@admin.register(models.Cvr3VerificationInfoCd)
class Cvr3VerificationInfoCdAdmin(BaseAdmin):
    pass


@admin.register(models.DebtCd)
class DebtCdAdmin(BaseAdmin):
    pass


@admin.register(models.ExpnCd)
class ExpnCdAdmin(BaseAdmin):
    pass


@admin.register(models.LoanCd)
class LoanCdAdmin(BaseAdmin):
    pass


@admin.register(models.RcptCd)
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


@admin.register(models.S401Cd)
class S401CdAdmin(BaseAdmin):
    pass


@admin.register(models.F495P2Cd)
class F495P2CdAdmin(BaseAdmin):
    pass


@admin.register(models.S496Cd)
class S496CdAdmin(BaseAdmin):
    pass


@admin.register(models.S497Cd)
class S497CdAdmin(BaseAdmin):
    pass


@admin.register(models.S498Cd)
class S498CdAdmin(BaseAdmin):
    pass


@admin.register(models.F501502Cd)
class F501502CdAdmin(BaseAdmin):
    pass


@admin.register(models.BallotMeasuresCd)
class BallotMeasuresCdAdmin(BaseAdmin):
    list_display = ("measure_name", "election_date", "jurisdiction")
    list_filter = ("jurisdiction",)
    search_fields = ("measure_name",)
