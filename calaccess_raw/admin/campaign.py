#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_raw import models
from .base import BaseAdmin


@admin.register(models.CvrSoCd)
class CvrSoCdAdmin(BaseAdmin):
    list_display = ("filing_id", "amend_id", "rpt_date", "filer_naml", "form_type")
    date_hierarchy = "rpt_date"


@admin.register(models.Cvr2SoCd)
class Cvr2SoCdAdmin(BaseAdmin):
    list_display = ("filing_id",  "item_cd", "entity_cd", "enty_naml", "form_type",)


@admin.register(models.CvrCampaignDisclosureCd)
class CvrCampaignDisclosureCdAdmin(BaseAdmin):
    list_display = ("filing_id", "rpt_date", "filer_naml", "cmtte_type", "form_type")
    date_hierarchy = "rpt_date"


@admin.register(models.Cvr2CampaignDisclosureCd)
class Cvr2CampaignDisclosureCdAdmin(BaseAdmin):
    list_display = ("filing_id", "enty_naml", "form_type")


@admin.register(models.Cvr3VerificationInfoCd)
class Cvr3VerificationInfoCdAdmin(BaseAdmin):
    list_display = ("filing_id", "sig_date", "sig_naml", "form_type")
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
    date_hierarchy = "expn_date"


@admin.register(models.LoanCd)
class LoanCdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "form_type",
        "loan_date1",
        "loan_type",
        "lndr_naml",
        "loan_amt1",
        "loan_amt2",
        "loan_amt3",
        "loan_amt4"
    )
    date_hierarchy = "loan_date1"


@admin.register(models.RcptCd)
class RcptCdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "form_type",
        "rcpt_date",
        "ctrib_naml",
        "ctrib_emp",
        "ctrib_occ",
        "amount"
    )
    date_hierarchy = "rcpt_date"


@admin.register(models.S401Cd)
class S401CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "form_type",
        "cand_naml",
        "payee_naml",
        "amount",
    )


@admin.register(models.F495P2Cd)
class F495P2CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "form_type",
        "elect_date",
        "contribamt"
    )
    date_hierarchy = "elect_date"


@admin.register(models.S496Cd)
class S496CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "exp_date",
        "expn_dscr",
        "amount"
    )
    date_hierarchy = "exp_date"


@admin.register(models.S497Cd)
class S497CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "ctrib_date",
        "cand_naml",
        "enty_naml",
        "amount",
    )
    date_hierarchy = "ctrib_date"


@admin.register(models.S498Cd)
class S498CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "date_rcvd",
        "payor_naml",
        "cand_naml",
        "amt_rcvd",
    )
    date_hierarchy = "date_rcvd"


@admin.register(models.F501502Cd)
class F501502CdAdmin(BaseAdmin):
    list_display = (
        "filing_id",
        "rpt_date",
        "cand_naml",
        "office_cd",
        "elec_type",
    )
    date_hierarchy = "rpt_date"


@admin.register(models.BallotMeasuresCd)
class BallotMeasuresCdAdmin(BaseAdmin):
    list_display = ("measure_name", "election_date", "jurisdiction")


@admin.register(models.CvrF470Cd)
class CvrF470CdAdmin(BaseAdmin):
    list_display = ("filing_id", "filer_naml",)
