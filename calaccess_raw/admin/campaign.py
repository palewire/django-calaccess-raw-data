#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


@admin.register(models.CvrSoCd)
class CvrSoCdAdmin(BaseAdmin):
    list_display = ("filing_id", "amend_id", "rpt_date", "filer_naml", "form_type")
    list_filter = ("form_type",)
    search_fields = ("filing_id", "filer_naml", "filer_namf")
    date_hierarchy = "rpt_date"


@admin.register(models.Cvr2SoCd)
class Cvr2SoCdAdmin(BaseAdmin):
    list_display = ("filing_id",  "item_cd", "entity_cd", "enty_naml", "form_type",)
    list_filter = ("form_type", "entity_cd", "off_s_h_cd", "item_cd")
    search_fields = ("filing_id", "enty_naml", "enty_namf", "cmte_id")


@admin.register(models.CvrCampaignDisclosureCd)
class CvrCampaignDisclosureCdAdmin(BaseAdmin):
    list_display = ("filing_id", "rpt_date", "filer_naml", "cmtte_type", "form_type")
    list_filter = ("cmtte_type", "form_type", "entity_cd",)
    search_fields = (
        "filing_id",
        "filer_id",
        "cand_namf",
        "cand_naml",
        "filer_namf",
        "filer_naml",
    )
    date_hierarchy = "rpt_date"


@admin.register(models.Cvr2CampaignDisclosureCd)
class Cvr2CampaignDisclosureCdAdmin(BaseAdmin):
    list_display = ("filing_id", "enty_naml", "form_type")
    list_filter = ("form_type", "entity_cd",)
    search_fields = (
        "filing_id",
        "enty_namf",
        "enty_naml",
        "filer_namf",
        "filer_naml",
    )


@admin.register(models.Cvr3VerificationInfoCd)
class Cvr3VerificationInfoCdAdmin(BaseAdmin):
    list_display = ("filing_id", "sig_date", "sig_naml", "form_type")
    list_filter = ("form_type",)
    search_fields = (
        "filing_id",
        "sig_naml",
        "sign_namf",
    )
    date_hierarchy = "sig_date"


@admin.register(models.DebtCd)
class DebtCdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "expn_code",
        "payee_naml",
        "amt_incur",
        "amt_paid",
    )
    list_filter = ("entity_cd", "expn_code",)
    search_fields = (
        "filing_id",
        "cmte_id",
        "payee_naml",
        "payee_namf",
    )


@admin.register(models.ExpnCd)
class ExpnCdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "expn_date",
        "cand_naml",
        "payee_naml",
        "form_type",
        "amount",
    )
    list_filter = ("expn_code", "entity_cd", "form_type",)
    search_fields = (
        "filing_id",
        "cand_naml",
        "cand_namf",
        "payee_naml",
        "payee_namf",
    )
    date_hierarchy = "expn_date"


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
