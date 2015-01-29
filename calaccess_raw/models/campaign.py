from __future__ import unicode_literals
from django.db import models
from .base import CalAccessBaseModel


class CvrSoCd(CalAccessBaseModel):
    """
    Cover page for statement of organization

        F400 -- Statement of Organization (Slate Mailer Organization)
        F402 -- Statement of Termination (Slate Mailer Organization)
        F410 -- Statement of Organization (Recipient Committee)
    """
    acct_opendt = models.DateTimeField(db_column="ACCT_OPENDT", null=True)
    actvty_lvl = models.CharField(
        max_length=2L, db_column="ACTVTY_LVL", blank=True
    )
    amend_id = models.IntegerField(db_column="AMEND_ID")
    bank_adr1 = models.CharField(
        max_length=55L, db_column="BANK_ADR1", blank=True
    )
    bank_adr2 = models.CharField(
        max_length=55L, db_column="BANK_ADR2", blank=True
    )
    bank_city = models.CharField(
        max_length=30L, db_column="BANK_CITY", blank=True
    )
    bank_nam = models.CharField(
        max_length=200L, db_column="BANK_NAM", blank=True
    )
    bank_phon = models.CharField(
        max_length=20L, db_column="BANK_PHON", blank=True
    )
    bank_st = models.CharField(max_length=2L, db_column="BANK_ST", blank=True)
    bank_zip4 = models.CharField(
        max_length=10L, db_column="BANK_ZIP4", blank=True
    )
    brdbase_cb = models.CharField(
        max_length=1L, db_column="BRDBASE_CB", blank=True
    )
    city = models.CharField(max_length=30L, db_column="CITY", blank=True)
    cmte_email = models.CharField(
        max_length=60L, db_column="CMTE_EMAIL", blank=True
    )
    cmte_fax = models.CharField(
        max_length=20L, db_column="CMTE_FAX", blank=True
    )
    com82013id = models.CharField(
        max_length=9L, db_column="COM82013ID", blank=True
    )
    com82013nm = models.CharField(
        max_length=200L, db_column="COM82013NM", blank=True
    )
    com82013yn = models.CharField(
        max_length=1L, db_column="COM82013YN", blank=True
    )
    control_cb = models.CharField(
        max_length=1L, db_column="CONTROL_CB", blank=True
    )
    county_act = models.CharField(
        max_length=20L, db_column="COUNTY_ACT", blank=True
    )
    county_res = models.CharField(
        max_length=20L, db_column="COUNTY_RES", blank=True
    )
    entity_cd = models.CharField(
        max_length=3L, db_column="ENTITY_CD", blank=True
    )
    filer_id = models.CharField(
        max_length=9L, db_column="FILER_ID", blank=True
    )
    filer_namf = models.CharField(
        max_length=45L, db_column="FILER_NAMF", blank=True
    )
    filer_naml = models.CharField(
        max_length=200L, db_column="FILER_NAML", blank=True
    )
    filer_nams = models.CharField(
        max_length=10L, db_column="FILER_NAMS", blank=True
    )
    filer_namt = models.CharField(
        max_length=10L, db_column="FILER_NAMT", blank=True
    )
    filing_id = models.CharField(
        max_length=9L, db_column="FILING_ID", blank=True
    )
    form_type = models.CharField(
        max_length=4L, db_column="FORM_TYPE", blank=True
    )
    genpurp_cb = models.CharField(
        max_length=1L, db_column="GENPURP_CB", blank=True
    )
    gpc_descr = models.CharField(
        max_length=300L, db_column="GPC_DESCR", blank=True
    )
    mail_city = models.CharField(
        max_length=30L, db_column="MAIL_CITY", blank=True
    )
    mail_st = models.CharField(max_length=2L, db_column="MAIL_ST", blank=True)
    mail_zip4 = models.CharField(
        max_length=10L, db_column="MAIL_ZIP4", blank=True
    )
    phone = models.CharField(max_length=20L, db_column="PHONE", blank=True)
    primfc_cb = models.CharField(
        max_length=1L, db_column="PRIMFC_CB", blank=True
    )
    qualfy_dt = models.DateTimeField(db_column="QUALFY_DT", null=True)
    qual_cb = models.CharField(max_length=1L, db_column="QUAL_CB", blank=True)
    rec_type = models.CharField(
        max_length=3L, db_column="REC_TYPE", blank=True
    )
    report_num = models.CharField(
        max_length=3L, db_column="REPORT_NUM", blank=True
    )
    rpt_date = models.DateTimeField(db_column="RPT_DATE", null=True)
    smcont_qualdt = models.DateTimeField(db_column="SMCONT_QUALDT", null=True)
    sponsor_cb = models.CharField(
        max_length=1L, db_column="SPONSOR_CB", blank=True
    )
    st = models.CharField(max_length=2L, db_column="ST", blank=True)
    surplusdsp = models.CharField(
        max_length=90L, db_column="SURPLUSDSP", blank=True
    )
    term_date = models.DateTimeField(db_column="TERM_DATE", null=True)
    tres_city = models.CharField(
        max_length=30L, db_column="TRES_CITY", blank=True
    )
    tres_namf = models.CharField(
        max_length=45L, db_column="TRES_NAMF", blank=True
    )
    tres_naml = models.CharField(
        max_length=200L, db_column="TRES_NAML", blank=True
    )
    tres_nams = models.CharField(
        max_length=10L, db_column="TRES_NAMS", blank=True
    )
    tres_namt = models.CharField(
        max_length=10L, db_column="TRES_NAMT", blank=True
    )
    tres_phon = models.CharField(
        max_length=20L, db_column="TRES_PHON", blank=True
    )
    tres_st = models.CharField(
        max_length=2L, db_column="TRES_ST", blank=True
    )
    tres_zip4 = models.CharField(
        max_length=10L, db_column="TRES_ZIP4", blank=True
    )
    zip4 = models.CharField(
        max_length=10L, db_column="ZIP4", blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = "CVR_SO_CD"
        verbose_name = 'CVR_SO_CD'
        verbose_name_plural = 'CVR_SO_CD'


class Cvr2SoCd(CalAccessBaseModel):
    """
    Additional Names / Committees information for the forms 400 & 410
        F400
        F410
    """
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    rec_type = models.CharField(db_column='REC_TYPE', max_length=4)
    form_type = models.CharField(db_column='FORM_TYPE', max_length=4)
    tran_id = models.CharField(db_column='TRAN_ID', max_length=19)
    entity_cd = models.CharField(db_column='ENTITY_CD', max_length=3)
    enty_naml = models.CharField(
        db_column='ENTY_NAML', max_length=194, blank=True
    )
    enty_namf = models.CharField(
        db_column='ENTY_NAMF', max_length=34, blank=True
    )
    enty_namt = models.CharField(
        db_column='ENTY_NAMT', max_length=9, blank=True
    )
    enty_nams = models.CharField(
        db_column='ENTY_NAMS', max_length=10, blank=True
    )
    item_cd = models.CharField(db_column='ITEM_CD', max_length=4, blank=True)
    mail_city = models.CharField(
        db_column='MAIL_CITY', max_length=25, blank=True
    )
    mail_st = models.CharField(db_column='MAIL_ST', max_length=4, blank=True)
    mail_zip4 = models.CharField(
        db_column='MAIL_ZIP4', max_length=10, blank=True
    )
    day_phone = models.CharField(
        db_column='DAY_PHONE', max_length=20, blank=True
    )
    fax_phone = models.CharField(
        db_column='FAX_PHONE', max_length=20, blank=True
    )
    email_adr = models.CharField(
        db_column='EMAIL_ADR', max_length=40, blank=True
    )
    cmte_id = models.IntegerField(db_column='CMTE_ID', blank=True, null=True)
    ind_group = models.CharField(
        db_column='IND_GROUP', max_length=87, blank=True
    )
    office_cd = models.CharField(
        db_column='OFFICE_CD', max_length=4, blank=True
    )
    offic_dscr = models.CharField(
        db_column='OFFIC_DSCR', max_length=40, blank=True
    )
    juris_cd = models.CharField(db_column='JURIS_CD', max_length=4, blank=True)
    juris_dscr = models.CharField(
        db_column='JURIS_DSCR', max_length=40, blank=True
    )
    dist_no = models.CharField(db_column='DIST_NO', max_length=4, blank=True)
    off_s_h_cd = models.CharField(
        db_column='OFF_S_H_CD', max_length=4, blank=True
    )
    non_pty_cb = models.CharField(
        db_column='NON_PTY_CB', max_length=4, blank=True
    )
    party_name = models.CharField(
        db_column='PARTY_NAME', max_length=63, blank=True
    )
    bal_num = models.CharField(db_column='BAL_NUM', max_length=7, blank=True)
    bal_juris = models.CharField(
        db_column='BAL_JURIS', max_length=40, blank=True
    )
    sup_opp_cd = models.CharField(
        db_column='SUP_OPP_CD', max_length=4, blank=True
    )
    year_elect = models.CharField(
        db_column='YEAR_ELECT', max_length=4, blank=True
    )
    pof_title = models.CharField(
        db_column='POF_TITLE', max_length=44, blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR2_SO_CD'
        verbose_name = 'CVR2_SO_CD'
        verbose_name_plural = 'CVR2_SO_CD'


class CvrCampaignDisclosureCd(CalAccessBaseModel):
    """
    Cover page information for the campaign disclosure forms below.
    This data comes from the electronic filing.
    The data contained herin is "as filed" by the entity making the filing.

        F401 -- Slate Mailer Organization Campaign Statement
        F425 -- Semi-Annual Statement of No Activity
        F450 -- Recipient Committee Campaign Statement (Short Form)
        F460 -- Recipient Committee Campaign Statement
        F461 -- Independent Expenditure and Major Donor Committee
                Campaign Statement
        F465 -- Supplemental Independent Expenditure Report
        F496 -- Late Independent Expenditure Report
        F497 -- Late Contribution Report
        F498 -- Slate Mailer Late Payment Report
    """
    amend_id = models.IntegerField(db_column='AMEND_ID', db_index=True)
    amendexp_1 = models.CharField(
        max_length=100L, db_column='AMENDEXP_1', blank=True
    )
    amendexp_2 = models.CharField(
        max_length=100L, db_column='AMENDEXP_2', blank=True
    )
    amendexp_3 = models.CharField(
        max_length=100L, db_column='AMENDEXP_3', blank=True
    )
    assoc_cb = models.CharField(
        max_length=4L, db_column='ASSOC_CB', blank=True
    )
    assoc_int = models.CharField(
        max_length=90L, db_column='ASSOC_INT', blank=True
    )
    bal_id = models.CharField(max_length=9L, db_column='BAL_ID', blank=True)
    bal_juris = models.CharField(
        max_length=40L, db_column='BAL_JURIS', blank=True
    )
    bal_name = models.CharField(
        max_length=200L, db_column='BAL_NAME', blank=True
    )
    bal_num = models.CharField(
        max_length=4L, db_column='BAL_NUM', blank=True
    )
    brdbase_yn = models.CharField(
        max_length=1L, db_column='BRDBASE_YN', blank=True
    )
    bus_adr1 = models.CharField(
        max_length=55L, db_column='BUS_ADR1', blank=True
    )
    bus_adr2 = models.CharField(
        max_length=55L, db_column='BUS_ADR2', blank=True
    )
    bus_city = models.CharField(
        max_length=30L, db_column='BUS_CITY', blank=True
    )
    bus_inter = models.CharField(
        max_length=40L, db_column='BUS_INTER', blank=True
    )
    bus_name = models.CharField(
        max_length=200L, db_column='BUS_NAME', blank=True
    )
    bus_st = models.CharField(max_length=2L, db_column='BUS_ST', blank=True)
    bus_zip4 = models.CharField(
        max_length=10, db_column='BUS_ZIP4', blank=True
    )
    busact_cb = models.CharField(
        max_length=10L, db_column='BUSACT_CB', blank=True
    )
    busactvity = models.CharField(
        max_length=90L, db_column='BUSACTVITY', blank=True
    )
    cand_adr1 = models.CharField(
        max_length=55L, db_column='CAND_ADR1', blank=True
    )
    cand_adr2 = models.CharField(
        max_length=55L, db_column='CAND_ADR2', blank=True
    )
    cand_city = models.CharField(
        max_length=30L, db_column='CAND_CITY', blank=True
    )
    cand_email = models.CharField(
        max_length=60L, db_column='CAND_EMAIL', blank=True
    )
    cand_fax = models.CharField(
        max_length=20L, db_column='CAND_FAX', blank=True
    )
    cand_id = models.CharField(max_length=9L, db_column='CAND_ID', blank=True)
    cand_namf = models.CharField(
        max_length=45L, db_column='CAND_NAMF', blank=True
    )
    cand_naml = models.CharField(
        max_length=200L, db_column='CAND_NAML', blank=True
    )
    cand_nams = models.CharField(
        max_length=10L, db_column='CAND_NAMS', blank=True
    )
    cand_namt = models.CharField(
        max_length=10L, db_column='CAND_NAMT', blank=True
    )
    cand_phon = models.CharField(
        max_length=20L, db_column='CAND_PHON', blank=True
    )
    cand_st = models.CharField(
        max_length=4L, db_column='CAND_ST', blank=True
    )
    cand_zip4 = models.CharField(
        max_length=10L, db_column='CAND_ZIP4', blank=True
    )
    cmtte_id = models.CharField(
        max_length=9L, db_column='CMTTE_ID', blank=True
    )
    cmtte_type = models.CharField(
        max_length=1L, db_column='CMTTE_TYPE', blank=True
    )
    control_yn = models.IntegerField(
        null=True, db_column='CONTROL_YN', blank=True
    )
    dist_no = models.CharField(
        max_length=4L, db_column='DIST_NO', blank=True
    )
    elect_date = models.DateTimeField(
        null=True, db_column='ELECT_DATE', blank=True
    )
    emplbus_cb = models.CharField(
        max_length=4L, db_column='EMPLBUS_CB', blank=True
    )
    employer = models.CharField(
        max_length=200L, db_column='EMPLOYER', blank=True
    )
    entity_cd = models.CharField(
        max_length=4L, db_column='ENTITY_CD', blank=True
    )
    file_email = models.CharField(
        max_length=60L, db_column='FILE_EMAIL', blank=True
    )
    filer_adr1 = models.CharField(
        max_length=55L, db_column='FILER_ADR1', blank=True
    )
    filer_adr2 = models.CharField(
        max_length=55L, db_column='FILER_ADR2', blank=True
    )
    filer_city = models.CharField(
        max_length=30L, db_column='FILER_CITY', blank=True
    )
    filer_fax = models.CharField(
        max_length=20L, db_column='FILER_FAX', blank=True
    )
    filer_id = models.CharField(
        max_length=15L, db_column='FILER_ID', db_index=True
    )
    filer_namf = models.CharField(
        max_length=45L, db_column='FILER_NAMF', blank=True
    )
    filer_naml = models.CharField(max_length=200L, db_column='FILER_NAML')
    filer_nams = models.CharField(
        max_length=10L, db_column='FILER_NAMS', blank=True
    )
    filer_namt = models.CharField(
        max_length=10L, db_column='FILER_NAMT', blank=True
    )
    filer_phon = models.CharField(
        max_length=20L, db_column='FILER_PHON', blank=True
    )
    filer_st = models.CharField(
        max_length=4L, db_column='FILER_ST', blank=True
    )
    filer_zip4 = models.CharField(
        max_length=10L, db_column='FILER_ZIP4', blank=True
    )
    filing_id = models.IntegerField(db_column='FILING_ID', db_index=True)
    form_type = models.CharField(max_length=4L, db_column='FORM_TYPE')
    from_date = models.DateTimeField(
        null=True,
        db_column='FROM_DATE',
        blank=True
    )
    juris_cd = models.CharField(
        max_length=3L, db_column='JURIS_CD', blank=True
    )
    juris_dscr = models.CharField(
        max_length=40L, db_column='JURIS_DSCR', blank=True
    )
    late_rptno = models.CharField(
        max_length=30L, db_column='LATE_RPTNO', blank=True
    )
    mail_adr1 = models.CharField(
        max_length=55L, db_column='MAIL_ADR1', blank=True
    )
    mail_adr2 = models.CharField(
        max_length=55L, db_column='MAIL_ADR2', blank=True
    )
    mail_city = models.CharField(
        max_length=30L, db_column='MAIL_CITY', blank=True
    )
    mail_st = models.CharField(max_length=4L, db_column='MAIL_ST', blank=True)
    mail_zip4 = models.CharField(
        max_length=10L, db_column='MAIL_ZIP4', blank=True
    )
    occupation = models.CharField(
        max_length=60L, db_column='OCCUPATION', blank=True
    )
    off_s_h_cd = models.CharField(
        max_length=1L, db_column='OFF_S_H_CD', blank=True
    )
    offic_dscr = models.CharField(
        max_length=40L, db_column='OFFIC_DSCR', blank=True
    )
    office_cd = models.CharField(
        max_length=3L, db_column='OFFICE_CD', blank=True
    )
    other_cb = models.CharField(
        max_length=1L, db_column='OTHER_CB', blank=True
    )
    other_int = models.CharField(
        max_length=90L, db_column='OTHER_INT', blank=True
    )
    primfrm_yn = models.CharField(
        max_length=1L, db_column='PRIMFRM_YN', blank=True
    )
    rec_type = models.CharField(
        max_length=3L, db_column='REC_TYPE'
    )
    report_num = models.CharField(
        max_length=3L, db_column='REPORT_NUM'
    )
    reportname = models.CharField(
        max_length=3L, db_column='REPORTNAME', blank=True
    )
    rpt_att_cb = models.CharField(
        max_length=4L, db_column='RPT_ATT_CB', blank=True
    )
    rpt_date = models.DateTimeField(db_column='RPT_DATE', null=True)
    rptfromdt = models.DateTimeField(
        null=True, db_column='RPTFROMDT', blank=True
    )
    rptthrudt = models.DateTimeField(
        null=True, db_column='RPTTHRUDT', blank=True
    )
    selfemp_cb = models.CharField(
        max_length=1L, db_column='SELFEMP_CB', blank=True
    )
    sponsor_yn = models.IntegerField(
        null=True, db_column='SPONSOR_YN', blank=True
    )
    stmt_type = models.CharField(
        max_length=2L, db_column='STMT_TYPE', blank=True
    )
    sup_opp_cd = models.CharField(
        max_length=1L, db_column='SUP_OPP_CD', blank=True
    )
    thru_date = models.DateTimeField(
        null=True, db_column='THRU_DATE', blank=True
    )
    tres_adr1 = models.CharField(
        max_length=55L, db_column='TRES_ADR1', blank=True
    )
    tres_adr2 = models.CharField(
        max_length=55L, db_column='TRES_ADR2', blank=True
    )
    tres_city = models.CharField(
        max_length=30L, db_column='TRES_CITY', blank=True
    )
    tres_email = models.CharField(
        max_length=60L, db_column='TRES_EMAIL', blank=True
    )
    tres_fax = models.CharField(
        max_length=20L, db_column='TRES_FAX', blank=True
    )
    tres_namf = models.CharField(
        max_length=45L, db_column='TRES_NAMF', blank=True
    )
    tres_naml = models.CharField(
        max_length=200L, db_column='TRES_NAML', blank=True
    )
    tres_nams = models.CharField(
        max_length=10L, db_column='TRES_NAMS', blank=True
    )
    tres_namt = models.CharField(
        max_length=10L, db_column='TRES_NAMT', blank=True
    )
    tres_phon = models.CharField(
        max_length=20L, db_column='TRES_PHON', blank=True
    )
    tres_st = models.CharField(max_length=2L, db_column='TRES_ST', blank=True)

    tres_zip4 = models.CharField(
        max_length=10L, db_column='TRES_ZIP4', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR_CAMPAIGN_DISCLOSURE_CD'
        verbose_name = 'CVR_CAMPAIGN_DISCLOSURE_CD'
        verbose_name_plural = 'CVR_CAMPAIGN_DISCLOSURE_CD'


class Cvr2CampaignDisclosureCd(CalAccessBaseModel):
    """
    Record used to carry additional names for the campaign
    disclosure forms below.

        F401
        F450
        F460
        F461
        F425
        F465
        F496
        F497
        F498
    """
    amend_id = models.IntegerField(db_column='AMEND_ID')
    bal_juris = models.CharField(
        max_length=40L, db_column='BAL_JURIS', blank=True
    )
    bal_name = models.CharField(
        max_length=200L, db_column='BAL_NAME', blank=True
    )
    bal_num = models.CharField(max_length=7L, db_column='BAL_NUM', blank=True)
    cmte_id = models.CharField(max_length=9L, db_column='CMTE_ID', blank=True)
    control_yn = models.IntegerField(
        null=True, db_column='CONTROL_YN', blank=True
    )
    dist_no = models.CharField(
        max_length=3L, db_column='DIST_NO', blank=True
    )
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    enty_adr1 = models.CharField(
        max_length=55L, db_column='ENTY_ADR1', blank=True
    )
    enty_adr2 = models.CharField(
        max_length=55L, db_column='ENTY_ADR2', blank=True
    )
    enty_city = models.CharField(
        max_length=30L, db_column='ENTY_CITY', blank=True
    )
    enty_email = models.CharField(
        max_length=60L, db_column='ENTY_EMAIL', blank=True
    )
    enty_fax = models.CharField(
        max_length=20L, db_column='ENTY_FAX', blank=True
    )
    enty_namf = models.CharField(
        max_length=45L, db_column='ENTY_NAMF', blank=True
    )
    enty_naml = models.CharField(
        max_length=200L, db_column='ENTY_NAML', blank=True
    )
    enty_nams = models.CharField(
        max_length=10L, db_column='ENTY_NAMS', blank=True
    )
    enty_namt = models.CharField(
        max_length=10L, db_column='ENTY_NAMT', blank=True
    )
    enty_phon = models.CharField(
        max_length=20L, db_column='ENTY_PHON', blank=True
    )
    enty_st = models.CharField(max_length=2L, db_column='ENTY_ST', blank=True)
    enty_zip4 = models.CharField(
        max_length=10L, db_column='ENTY_ZIP4', blank=True
    )
    f460_part = models.CharField(
        max_length=2L, db_column='F460_PART', blank=True
    )
    filing_id = models.IntegerField(db_column='FILING_ID')
    form_type = models.CharField(max_length=4L, db_column='FORM_TYPE')
    juris_cd = models.CharField(
        max_length=3L, db_column='JURIS_CD', blank=True
    )
    juris_dscr = models.CharField(
        max_length=40L, db_column='JURIS_DSCR', blank=True
    )
    line_item = models.IntegerField(db_column='LINE_ITEM')
    mail_adr1 = models.CharField(
        max_length=55L, db_column='MAIL_ADR1', blank=True
    )
    mail_adr2 = models.CharField(
        max_length=55L, db_column='MAIL_ADR2', blank=True
    )
    mail_city = models.CharField(
        max_length=30L, db_column='MAIL_CITY', blank=True
    )
    mail_st = models.CharField(max_length=2L, db_column='MAIL_ST', blank=True)
    mail_zip4 = models.CharField(
        max_length=10L, db_column='MAIL_ZIP4', blank=True
    )
    off_s_h_cd = models.CharField(
        max_length=1L, db_column='OFF_S_H_CD', blank=True
    )
    offic_dscr = models.CharField(
        max_length=40L, db_column='OFFIC_DSCR', blank=True
    )
    office_cd = models.CharField(
        max_length=3L, db_column='OFFICE_CD', blank=True
    )
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE')
    sup_opp_cd = models.CharField(
        max_length=1L, db_column='SUP_OPP_CD', blank=True
    )
    title = models.CharField(max_length=90L, db_column='TITLE', blank=True)
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID')
    tres_namf = models.CharField(
        max_length=45L, db_column='TRES_NAMF', blank=True
    )
    tres_naml = models.CharField(
        max_length=200L, db_column='TRES_NAML', blank=True
    )
    tres_nams = models.CharField(
        max_length=10L, db_column='TRES_NAMS', blank=True
    )
    tres_namt = models.CharField(
        max_length=10L, db_column='TRES_NAMT', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR2_CAMPAIGN_DISCLOSURE_CD'
        verbose_name = 'CVR2_CAMPAIGN_DISCLOSURE_CD'
        verbose_name_plural = 'CVR2_CAMPAIGN_DISCLOSURE_CD'


class RcptCd(CalAccessBaseModel):
    """
    Receipts schedules for the following forms.

        Form 460 (Recipient Committee Campaign Statement)
        Schedules A, C, I, nd A-1.

        Form 401 (Slate Mailer Organization Campaign Statement) Schedule A.
    """
    amend_id = models.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment Identification number. A number of 0 is an \
original filing and 1 to 999 amendments."
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=14,
        db_column='AMOUNT',
        help_text="Amount Received (Monetary, Inkkind, Promise)"
    )
    bakref_tid = models.CharField(
        max_length=20L,
        db_column='BAKREF_TID',
        blank=True,
        help_text="Back Reference to a transaction identifier of a parent \
record"
    )
    bal_juris = models.CharField(
        max_length=40L,
        db_column='BAL_JURIS',
        blank=True,
        help_text="Jurisdiction of ballot measure. Used on the Form 401 \
Schedule A"
    )
    bal_name = models.CharField(
        max_length=200L,
        db_column='BAL_NAME',
        blank=True,
        help_text="Ballot measure name. Used on the Form 401 Schedule A"
    )
    bal_num = models.CharField(
        max_length=7L,
        db_column='BAL_NUM',
        blank=True,
        help_text="Ballot measure number or letter. Used on the Form 401 \
Schedule A"
    )
    cand_namf = models.CharField(
        max_length=45L,
        db_column='CAND_NAMF',
        blank=True,
        help_text="Candidate/officeholder's first name. Used on the Form \
401 Schedule A"
    )
    cand_naml = models.CharField(
        max_length=200L,
        db_column='CAND_NAML',
        blank=True,
        help_text="Candidate/officeholder's last name. Used on the Form \
401 Schedule A"
    )
    cand_nams = models.CharField(
        max_length=10L,
        db_column='CAND_NAMS',
        blank=True,
        help_text="Candidate/officeholder's name suffix. Used on the Form \
401 Schedule A"
    )
    cand_namt = models.CharField(
        max_length=10L,
        db_column='CAND_NAMT',
        blank=True,
        help_text="Candidate/officeholder's name prefix or title. Used on \
the Form 401 Schedule A"
    )
    cmte_id = models.CharField(
        max_length=9L,
        db_column='CMTE_ID',
        blank=True,
        help_text="Committee Identification number"
    )
    ctrib_adr1 = models.CharField(
        max_length=55L,
        db_column='CTRIB_ADR1',
        blank=True,
        default="",
        help_text="First line of the contributor's street address"
    )
    ctrib_adr2 = models.CharField(
        max_length=55L,
        db_column='CTRIB_ADR2',
        blank=True,
        help_text="Second line of the contributor's street address"
    )
    ctrib_city = models.CharField(
        max_length=30L,
        db_column='CTRIB_CITY',
        blank=True,
        help_text="Contributor's City"
    )
    ctrib_dscr = models.CharField(
        max_length=90L,
        db_column='CTRIB_DSCR',
        blank=True,
        help_text="Description of goods/services received"
    )
    ctrib_emp = models.CharField(
        max_length=200L,
        db_column='CTRIB_EMP',
        blank=True,
        help_text="Employer"
    )
    ctrib_namf = models.CharField(
        max_length=45L,
        db_column='CTRIB_NAMF',
        blank=True,
        help_text="Contributor's First Name"
    )
    ctrib_naml = models.CharField(
        max_length=200L,
        db_column='CTRIB_NAML',
        help_text="Contributor's last name or business name"
    )
    ctrib_nams = models.CharField(
        max_length=10L,
        db_column='CTRIB_NAMS',
        blank=True,
        help_text="Contributor's Suffix"
    )
    ctrib_namt = models.CharField(
        max_length=10L,
        db_column='CTRIB_NAMT',
        blank=True,
        help_text="Contributor's Prefix or Title"
    )
    ctrib_occ = models.CharField(
        max_length=60L,
        db_column='CTRIB_OCC',
        blank=True,
        help_text="Occupation"
    )
    ctrib_self = models.CharField(
        max_length=1L,
        db_column='CTRIB_SELF',
        blank=True,
        help_text="Self Employed Check-box"
    )
    ctrib_st = models.CharField(
        max_length=2L,
        db_column='CTRIB_ST',
        blank=True,
        help_text="Contributor's State"
    )
    ctrib_zip4 = models.CharField(
        max_length=10L,
        db_column='CTRIB_ZIP4',
        blank=True,
        help_text="Contributor's ZIP+4"
    )
    cum_oth = models.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='CUM_OTH',
        blank=True,
        help_text="Cumulative Other (Sched A, A-1)"
    )
    cum_ytd = models.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='CUM_YTD',
        blank=True,
        help_text="Cumulative year to date amount (Form 460 Schedule A \
and Form 401 Schedule A, A-1)"
    )
    date_thru = models.DateField(
        null=True,
        db_column='DATE_THRU',
        blank=True,
        help_text="End of date range for items received"
    )
    dist_no = models.CharField(
        max_length=3L,
        db_column='DIST_NO',
        blank=True,
        help_text="Office District Number (used on F401A)"
    )
    ENTITY_CODE_CHOICES = (
        ("", "None"),
        ("0", "0"),
        ("BNM", "BNM"),
        ("COM", "Recipient committee"),
        ("IND", "Individual"),
        ("OFF", "OFF"),
        ("OTH", "Other"),
        ("PTY", "Political party"),
        ("RCP", "RCP"),
        ("SCC", "Small contributor committee"),
    )
    entity_cd = models.CharField(
        max_length=3L,
        db_column='ENTITY_CD',
        blank=True,
        help_text="Entity code: Values [CMO|RCP|IND|OTH]",
        choices=ENTITY_CODE_CHOICES
    )
    filing_id = models.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        help_text="Unique filing identification number"
    )
    form_type = models.CharField(
        max_length=9L,
        db_column='FORM_TYPE',
        help_text="Schedule Name/ID: Sched A, C, I, A-1, F401A"
    )
    int_rate = models.CharField(
        max_length=9L,
        db_column='INT_RATE',
        blank=True
    )
    intr_adr1 = models.CharField(
        max_length=55L,
        db_column='INTR_ADR1',
        blank=True,
        help_text="First line of the intermediary's street address."
    )
    intr_adr2 = models.CharField(
        max_length=55L,
        db_column='INTR_ADR2',
        blank=True,
        help_text="Second line of the Intermediary's street address."
    )
    intr_city = models.CharField(
        max_length=30L,
        db_column='INTR_CITY',
        blank=True,
        help_text="Intermediary's City"
    )
    intr_cmteid = models.CharField(
        max_length=9L,
        db_column='INTR_CMTEID',
        blank=True,
        help_text=""
    )
    intr_emp = models.CharField(
        max_length=200L,
        db_column='INTR_EMP',
        blank=True,
        help_text="Intermediary's Employer"
    )
    intr_namf = models.CharField(
        max_length=45L,
        db_column='INTR_NAMF',
        blank=True,
        help_text="Intermediary's First Name"
    )
    intr_naml = models.CharField(
        max_length=200L,
        db_column='INTR_NAML',
        blank=True,
        help_text="Intermediary's Last Name"
    )
    intr_nams = models.CharField(
        max_length=10L,
        db_column='INTR_NAMS',
        blank=True,
        help_text="Intermediary's Suffix"
    )
    intr_namt = models.CharField(
        max_length=10L,
        db_column='INTR_NAMT',
        blank=True,
        help_text="Intermediary's Prefix or Title"
    )
    intr_occ = models.CharField(
        max_length=60L,
        db_column='INTR_OCC',
        blank=True,
        help_text="Intermediary's Occupation"
    )
    intr_self = models.CharField(
        max_length=1L,
        db_column='INTR_SELF',
        blank=True,
        help_text="Intermediary's self employed check box"
    )
    intr_st = models.CharField(
        max_length=2L,
        db_column='INTR_ST',
        blank=True,
        help_text="Intermediary's state"
    )
    intr_zip4 = models.CharField(
        max_length=10L,
        db_column='INTR_ZIP4',
        blank=True,
        help_text="Intermediary's zip code"
    )
    juris_cd = models.CharField(
        max_length=3L,
        db_column='JURIS_CD',
        blank=True,
        help_text="Office jurisdiction code. See the CAL document for the \
list of legal values. Used on Form 401 Schedule A"
    )
    juris_dscr = models.CharField(
        max_length=40L,
        db_column='JURIS_DSCR',
        blank=True,
        help_text="Office Jurisdiction Description (used on F401A)"
    )
    line_item = models.IntegerField(
        db_column='LINE_ITEM',
        help_text="Record line item number"
    )
    memo_code = models.CharField(
        max_length=1L,
        db_column='MEMO_CODE',
        blank=True,
        help_text="Memo amount flag (Date/Amount are informational only)"
    )
    memo_refno = models.CharField(
        max_length=20L,
        db_column='MEMO_REFNO',
        blank=True,
        help_text="Reference to text contained in a TEXT record"
    )
    off_s_h_cd = models.CharField(
        max_length=1L,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text="Office Sought/Held Code. Used on the Form 401 \
Schedule A. Legal values are 'S' for sought and 'H' for \
held"
    )
    offic_dscr = models.CharField(
        max_length=40L,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office Sought Description (used on F401A)"
    )
    office_cd = models.CharField(
        max_length=3L,
        db_column='OFFICE_CD',
        blank=True,
        help_text="Code that identifies the office being sought. See the \
CAL document for a list of valid codes. Used on the \
Form 401 Schedule A)"
    )
    rcpt_date = models.DateField(
        db_column='RCPT_DATE',
        null=True,
        help_text="Date item received"
    )
    rec_type = models.CharField(
        max_length=4L,
        db_column='REC_TYPE',
        help_text="Record Type Value: RCPT"
    )
    sup_opp_cd = models.CharField(
        max_length=1L,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text="Support/oppose code. Legal values are 'S' for support \
or 'O' for oppose. Used on Form 401 Sechedule A. \
Transaction identifier - permanent value unique to this item"
    )
    tran_id = models.CharField(
        max_length=20L,
        db_column='TRAN_ID',
        help_text="Transaction identifier - permanent value unique to this \
item"
    )
    tran_type = models.CharField(
        max_length=1L,
        db_column='TRAN_TYPE',
        blank=True,
        help_text="Transaction Type: Values T- third party | F Forgiven \
loan | R Returned (Negative amount)"
    )
    tres_adr1 = models.CharField(
        max_length=55L,
        db_column='TRES_ADR1',
        blank=True,
        help_text="First line of the treasurer or responsible officer's \
street address"
    )
    tres_adr2 = models.CharField(
        max_length=55L,
        db_column='TRES_ADR2',
        blank=True,
        help_text="Second line of the treasurer or responsible officer's \
street address"
    )
    tres_city = models.CharField(
        max_length=30L,
        db_column='TRES_CITY',
        blank=True,
        help_text="City portion of the treasurer or responsible officer's \
street address"
    )
    tres_namf = models.CharField(
        max_length=45L,
        db_column='TRES_NAMF',
        blank=True,
        help_text="Treasurer or responsible officer's first name"
    )
    tres_naml = models.CharField(
        max_length=200L,
        db_column='TRES_NAML',
        blank=True,
        help_text="Treasurer or responsible officer's last name"
    )
    tres_nams = models.CharField(
        max_length=10L,
        db_column='TRES_NAMS',
        blank=True,
        help_text="Treasurer or responsible officer's suffix"
    )
    tres_namt = models.CharField(
        max_length=10L,
        db_column='TRES_NAMT',
        blank=True,
        help_text="Treasurer or responsible officer's prefix or title"
    )
    tres_st = models.CharField(
        max_length=2L,
        db_column='TRES_ST',
        blank=True,
        help_text="State portion of the treasurer or responsible officer's \
address"
    )
    tres_zip4 = models.CharField(
        null=True,
        max_length=10L,
        blank=True,
        db_column='TRES_ZIP4',
        help_text="Zip code portion of the treasurer or responsible officer's \
address"
    )
    xref_match = models.CharField(
        max_length=1L,
        db_column='XREF_MATCH',
        blank=True,
        help_text="Related item on other schedule has same transaction \
identifier. 'X' indicates this condition is true"
    )
    xref_schnm = models.CharField(
        max_length=2L,
        db_column='XREF_SCHNM',
        blank=True,
        help_text="Related record is included on Sched 'B2' or 'F'"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'RCPT_CD'
        verbose_name = 'RCPT_CD'
        verbose_name_plural = 'RCPT_CD'


class Cvr3VerificationInfoCd(CalAccessBaseModel):
    """
    Cover Page Verification Information for the Campaign Forms below.

        F400
        F402
        F410
        F425
        F450
        F460
        F461
        F465
        F470
    """
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    rec_type = models.CharField(db_column='REC_TYPE', max_length=4)
    form_type = models.CharField(db_column='FORM_TYPE', max_length=4)
    tran_id = models.CharField(db_column='TRAN_ID', max_length=20)
    entity_cd = models.CharField(db_column='ENTITY_CD', max_length=3)
    sig_date = models.DateField(db_column='SIG_DATE', blank=True, null=True)
    sig_loc = models.CharField(db_column='SIG_LOC', max_length=39, blank=True)
    sig_naml = models.CharField(
        db_column='SIG_NAML', max_length=56, blank=True
    )
    sig_namf = models.CharField(
        db_column='SIG_NAMF', max_length=45, blank=True
    )
    sig_namt = models.CharField(
        db_column='SIG_NAMT', max_length=10, blank=True
    )
    sig_nams = models.CharField(
        db_column='SIG_NAMS', max_length=8, blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR3_VERIFICATION_INFO_CD'
        verbose_name = 'CVR3_VERIFICATION_INFO_CD'
        verbose_name_plural = 'CVR3_VERIFICATION_INFO_CD'


class LoanCd(CalAccessBaseModel):
    amend_id = models.IntegerField(db_column='AMEND_ID')
    bakref_tid = models.CharField(
        max_length=20L, db_column='BAKREF_TID', blank=True
    )
    cmte_id = models.CharField(max_length=9L, db_column='CMTE_ID', blank=True)
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    filing_id = models.IntegerField(db_column='FILING_ID')
    form_type = models.CharField(max_length=2L, db_column='FORM_TYPE')
    intr_adr1 = models.CharField(
        max_length=55L, db_column='INTR_ADR1', blank=True
    )
    intr_adr2 = models.CharField(
        max_length=55L, db_column='INTR_ADR2', blank=True
    )
    intr_city = models.CharField(
        max_length=30L, db_column='INTR_CITY', blank=True
    )
    intr_namf = models.CharField(
        max_length=45L, db_column='INTR_NAMF', blank=True
    )
    intr_naml = models.CharField(
        max_length=200L, db_column='INTR_NAML', blank=True
    )
    intr_nams = models.CharField(
        max_length=10L, db_column='INTR_NAMS', blank=True
    )
    intr_namt = models.CharField(
        max_length=10L, db_column='INTR_NAMT', blank=True
    )
    intr_st = models.CharField(max_length=2L, db_column='INTR_ST', blank=True)
    intr_zip4 = models.CharField(
        max_length=10L, db_column='INTR_ZIP4', blank=True
    )
    line_item = models.IntegerField(db_column='LINE_ITEM')
    lndr_namf = models.CharField(
        max_length=45L, db_column='LNDR_NAMF', blank=True
    )
    lndr_naml = models.CharField(
        max_length=200L, db_column='LNDR_NAML'
    )
    lndr_nams = models.CharField(
        max_length=10L, db_column='LNDR_NAMS', blank=True
    )
    lndr_namt = models.CharField(
        max_length=10L, db_column='LNDR_NAMT', blank=True
    )
    loan_adr1 = models.CharField(
        max_length=55L, db_column='LOAN_ADR1', blank=True
    )
    loan_adr2 = models.CharField(
        max_length=55L, db_column='LOAN_ADR2', blank=True
    )
    loan_amt1 = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='LOAN_AMT1', blank=True
    )
    loan_amt2 = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='LOAN_AMT2', blank=True
    )
    loan_amt3 = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='LOAN_AMT3', blank=True
    )
    loan_amt4 = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='LOAN_AMT4', blank=True
    )
    loan_amt5 = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='LOAN_AMT5', blank=True
    )
    loan_amt6 = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='LOAN_AMT6', blank=True
    )
    loan_amt7 = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='LOAN_AMT7', blank=True
    )
    loan_amt8 = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='LOAN_AMT8', blank=True
    )
    loan_city = models.CharField(
        max_length=30L, db_column='LOAN_CITY', blank=True
    )
    loan_date1 = models.DateField(db_column='LOAN_DATE1', null=True)
    loan_date2 = models.DateField(
        null=True, db_column='LOAN_DATE2', blank=True
    )
    loan_emp = models.CharField(
        max_length=200L, db_column='LOAN_EMP', blank=True
    )
    loan_occ = models.CharField(
        max_length=60L, db_column='LOAN_OCC', blank=True
    )
    loan_rate = models.CharField(
        max_length=30L, db_column='LOAN_RATE', blank=True
    )
    loan_self = models.CharField(
        max_length=1L, db_column='LOAN_SELF', blank=True
    )
    loan_st = models.CharField(max_length=2L, db_column='LOAN_ST', blank=True)
    loan_type = models.CharField(
        max_length=3L, db_column='LOAN_TYPE', blank=True
    )
    loan_zip4 = models.CharField(
        max_length=10L, db_column='LOAN_ZIP4', blank=True
    )
    memo_code = models.CharField(
        max_length=1L, db_column='MEMO_CODE', blank=True
    )
    memo_refno = models.CharField(
        max_length=20L, db_column='MEMO_REFNO', blank=True
    )
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE')
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID')
    tres_adr1 = models.CharField(
        max_length=55L, db_column='TRES_ADR1', blank=True
    )
    tres_adr2 = models.CharField(
        max_length=55L, db_column='TRES_ADR2', blank=True
    )
    tres_city = models.CharField(
        max_length=30L, db_column='TRES_CITY', blank=True
    )
    tres_namf = models.CharField(
        max_length=45L, db_column='TRES_NAMF', blank=True
    )
    tres_naml = models.CharField(
        max_length=200L, db_column='TRES_NAML', blank=True
    )
    tres_nams = models.CharField(
        max_length=10L, db_column='TRES_NAMS', blank=True
    )
    tres_namt = models.CharField(
        max_length=10L, db_column='TRES_NAMT', blank=True
    )
    tres_st = models.CharField(
        max_length=2L, db_column='TRES_ST', blank=True
    )
    tres_zip4 = models.CharField(
        max_length=10L, db_column='TRES_ZIP4', blank=True
    )
    xref_match = models.CharField(
        max_length=1L, db_column='XREF_MATCH', blank=True
    )
    xref_schnm = models.CharField(
        max_length=2L, db_column='XREF_SCHNM', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOAN_CD'
        verbose_name = 'LOAN_CD'
        verbose_name_plural = 'LOAN_CD'


class S401Cd(CalAccessBaseModel):
    """
    This table contains Form 401 (Slate Mailer Organization) payment and other
    disclosure schedule (F401B, F401B-1, F401C, F401D) information.
    """
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    rec_type = models.CharField(
        max_length=4L, db_column='REC_TYPE', blank=True
    )
    form_type = models.CharField(
        max_length=7L, db_column='FORM_TYPE', blank=True
    )
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID', blank=True)
    agent_naml = models.CharField(
        max_length=200l, db_column='AGENT_NAML', blank=True
    )
    agent_namf = models.CharField(
        max_length=45L, db_column='AGENT_NAMF', blank=True
    )
    agent_namt = models.CharField(
        max_length=200L, db_column='AGENT_NAMT', blank=True
    )
    agent_nams = models.CharField(
        max_length=10L, db_column='AGENT_NAMS', blank=True
    )
    payee_naml = models.CharField(
        max_length=200L, db_column='PAYEE_NAML', blank=True
    )
    payee_namf = models.CharField(
        max_length=45L, db_column='PAYEE_NAMF', blank=True
    )
    payee_namt = models.CharField(
        max_length=10L, db_column='PAYEE_NAMT', blank=True
    )
    payee_nams = models.CharField(
        max_length=10L, db_column='PAYEE_NAMS', blank=True
    )
    payee_city = models.CharField(
        max_length=30L, db_column='PAYEE_CITY', blank=True
    )
    payee_st = models.CharField(
        max_length=2L, db_column='PAYEE_ST', blank=True
    )
    payee_zip4 = models.CharField(
        max_length=10L, db_column='PAYEE_ZIP4', blank=True
    )
    amount = models.DecimalField(
        max_digits=16L, decimal_places=2, db_column='AMOUNT'
    )
    aggregate = models.DecimalField(
        max_digits=16L, decimal_places=2, db_column='AGGREGATE'
    )
    expn_dscr = models.CharField(
        max_length=90L, db_column='EXPN_DSCR', blank=True
    )
    cand_naml = models.CharField(
        max_length=200L, db_column='CAND_NAML', blank=True
    )
    cand_namf = models.CharField(
        max_length=45L, db_column='CAND_NAMF', blank=True
    )
    cand_namt = models.CharField(
        max_length=10L, db_column='CAND_NAMT', blank=True
    )
    cand_nams = models.CharField(
        max_length=10L, db_column='CAND_NAMS', blank=True
    )
    office_cd = models.CharField(
        max_length=3L, db_column='OFFICE_CD', blank=True
    )
    offic_dscr = models.CharField(
        max_length=40L, db_column='OFFIC_DSCR', blank=True
    )
    juris_cd = models.CharField(
        max_length=3L, db_column='JURIS_CD', blank=True
    )
    juris_dscr = models.CharField(
        max_length=40L, db_column='JURIS_DSCR', blank=True
    )
    dist_no = models.CharField(max_length=3L, db_column='DIST_NO', blank=True)
    off_s_h_cd = models.CharField(
        max_length=1L, db_column='OFF_S_H_CD', blank=True
    )
    bal_name = models.CharField(
        max_length=200L, db_column='BAL_NAME', blank=True
    )
    bal_num = models.CharField(max_length=7L, db_column='BAL_NUM', blank=True)
    bal_juris = models.CharField(
        max_length=40L, db_column='BAL_JURIS', blank=True
    )
    sup_opp_cd = models.CharField(
        max_length=1L, db_column='SUP_OPP_CD', blank=True
    )
    memo_code = models.CharField(
        max_length=1L, db_column='MEMO_CODE', blank=True
    )
    memo_refno = models.CharField(
        max_length=20L, db_column='MEMO_REFNO', blank=True
    )
    bakref_tid = models.CharField(
        max_length=20L, db_column='BAKREF_TID', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'S401_CD'
        verbose_name = 'S401_CD'
        verbose_name_plural = 'S401_CD'


class ExpnCd(CalAccessBaseModel):
    """
    Expenditure records for the following forms:
        * Form 460 (Recipient Committee Campaign Statement): Schedule D
        * Form 460 (Recipient Committee Campaign Statement): Schedule E
        * Form 460 (Recipient Committee Campaign Statement): Schedule G
        * Form 450 (Recipient Committee Campaign Statement Short Form): Part 5
        * Form 461 (Independent Expenditure and Major Donor Committee
            Campaign Statement): Part 5
        * Form 465 (Supplemental Independent Expenditure Report) Part 3
        * Form 900 (Public Employee's Retirement Board Candidate
            Campaign Statement)
    """
    agent_namf = models.CharField(
        max_length=45L, db_column='AGENT_NAMF', blank=True
    )
    agent_naml = models.CharField(
        max_length=200L, db_column='AGENT_NAML', blank=True
    )
    agent_nams = models.CharField(
        max_length=10L, db_column='AGENT_NAMS', blank=True
    )
    agent_namt = models.CharField(
        max_length=10L, db_column='AGENT_NAMT', blank=True
    )
    amend_id = models.IntegerField(db_column='AMEND_ID', db_index=True)
    amount = models.DecimalField(
        decimal_places=2, max_digits=14, db_column='AMOUNT'
    )
    bakref_tid = models.CharField(
        max_length=20L, db_column='BAKREF_TID', blank=True
    )
    bal_juris = models.CharField(
        max_length=40L, db_column='BAL_JURIS', blank=True
    )
    bal_name = models.CharField(
        max_length=200L, db_column='BAL_NAME', blank=True
    )
    bal_num = models.CharField(
        max_length=7L, db_column='BAL_NUM', blank=True
    )
    cand_namf = models.CharField(
        max_length=45L, db_column='CAND_NAMF', blank=True
    )
    cand_naml = models.CharField(
        max_length=200L, db_column='CAND_NAML', blank=True
    )
    cand_nams = models.CharField(
        max_length=10L, db_column='CAND_NAMS', blank=True
    )
    cand_namt = models.CharField(
        max_length=10L, db_column='CAND_NAMT', blank=True
    )
    cmte_id = models.CharField(max_length=9L, db_column='CMTE_ID', blank=True)
    cum_oth = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='CUM_OTH', blank=True
    )
    cum_ytd = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='CUM_YTD', blank=True
    )
    dist_no = models.CharField(max_length=3L, db_column='DIST_NO', blank=True)
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    expn_chkno = models.CharField(
        max_length=20L, db_column='EXPN_CHKNO', blank=True
    )
    expn_code = models.CharField(
        max_length=3L, db_column='EXPN_CODE', blank=True
    )
    expn_date = models.DateField(null=True, db_column='EXPN_DATE', blank=True)
    expn_dscr = models.CharField(
        max_length=400L, db_column='EXPN_DSCR', blank=True
    )
    filing_id = models.IntegerField(db_column='FILING_ID', db_index=True)
    FORM_TYPE_CHOICES = (
        ('D', 'Form 460 (Recipient Committee Campaign Statement): Schedule D'),
        ('E', 'Form 460 (Recipient Committee Campaign Statement): Schedule E'),
        ('G', 'Form 460 (Recipient Committee Campaign Statement): Schedule G'),
        ('F450P5', 'Form 450 (Recipient Committee Campaign Statement \
Short Form): Part 5'),
        ('F461P5', 'Form 461 (Independent Expenditure and Major Donor \
Committee Campaign Statement): Part 5'),
        ('F465P3', 'Form 465 (Supplemental Independent Expenditure \
Report) Part 3'),
        ('F900', 'Form 900 (Public Employee\'s Retirement Board Candidate \
Campaign Statement)'),
    )
    form_type = models.CharField(
        choices=FORM_TYPE_CHOICES,
        max_length=6L,
        db_column='FORM_TYPE'
    )
    g_from_e_f = models.CharField(
        max_length=1L, db_column='G_FROM_E_F', blank=True
    )
    juris_cd = models.CharField(
        max_length=3L, db_column='JURIS_CD', blank=True
    )
    juris_dscr = models.CharField(
        max_length=40L, db_column='JURIS_DSCR', blank=True
    )
    line_item = models.IntegerField(db_column='LINE_ITEM')
    memo_code = models.CharField(
        max_length=1L, db_column='MEMO_CODE', blank=True
    )
    memo_refno = models.CharField(
        max_length=20L, db_column='MEMO_REFNO', blank=True
    )
    off_s_h_cd = models.CharField(
        max_length=1L, db_column='OFF_S_H_CD', blank=True
    )
    offic_dscr = models.CharField(
        max_length=40L, db_column='OFFIC_DSCR', blank=True
    )
    office_cd = models.CharField(
        max_length=3L, db_column='OFFICE_CD', blank=True
    )
    payee_adr1 = models.CharField(
        max_length=55L, db_column='PAYEE_ADR1', blank=True
    )
    payee_adr2 = models.CharField(
        max_length=55L, db_column='PAYEE_ADR2', blank=True
    )
    payee_city = models.CharField(
        max_length=30L, db_column='PAYEE_CITY', blank=True
    )
    payee_namf = models.CharField(
        max_length=45L, db_column='PAYEE_NAMF', blank=True
    )
    payee_naml = models.CharField(
        max_length=200L, db_column='PAYEE_NAML', blank=True
    )
    payee_nams = models.CharField(
        max_length=10L, db_column='PAYEE_NAMS', blank=True
    )
    payee_namt = models.CharField(
        max_length=10L, db_column='PAYEE_NAMT', blank=True
    )
    payee_st = models.CharField(
        max_length=2L, db_column='PAYEE_ST', blank=True
    )
    payee_zip4 = models.CharField(
        max_length=10L, db_column='PAYEE_ZIP4', blank=True
    )
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE')
    sup_opp_cd = models.CharField(
        max_length=1L, db_column='SUP_OPP_CD', blank=True
    )
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID')
    tres_adr1 = models.CharField(
        max_length=55L, db_column='TRES_ADR1', blank=True
    )
    tres_adr2 = models.CharField(
        max_length=55L, db_column='TRES_ADR2', blank=True
    )
    tres_city = models.CharField(
        max_length=30L, db_column='TRES_CITY', blank=True
    )
    tres_namf = models.CharField(
        max_length=45L, db_column='TRES_NAMF', blank=True
    )
    tres_naml = models.CharField(
        max_length=200L, db_column='TRES_NAML', blank=True
    )
    tres_nams = models.CharField(
        max_length=10L, db_column='TRES_NAMS', blank=True
    )
    tres_namt = models.CharField(
        max_length=10L, db_column='TRES_NAMT', blank=True
    )
    tres_st = models.CharField(max_length=2L, db_column='TRES_ST', blank=True)
    tres_zip4 = models.CharField(
        max_length=10L, db_column='TRES_ZIP4', blank=True
    )
    xref_match = models.CharField(
        max_length=1L, db_column='XREF_MATCH', blank=True
    )
    xref_schnm = models.CharField(
        max_length=2L, db_column='XREF_SCHNM', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'EXPN_CD'
        verbose_name = 'EXPN_CD'
        verbose_name_plural = 'EXPN_CD'


class F495P2Cd(CalAccessBaseModel):
    """
    F495 Supplemental Preelection Campaign Statement

    It's attatchment to the forms below

        F450 Recipient Committee Campaign Statement Short Form
        F460 Recipient Committee Campaign Statement

    Form 495 is for use by a recipient committee that
    makes contributions totaling $10,000 or more in
    connection with an election for which the committee
    is not required to file regular preelection reports.
    Form 495 is filed as an attachment to a campaign
    disclosure statement (Form 450 or 460). On the
    Form 450 or 460, the committee will report all
    contributions received and expenditures made since
    its last report.
    """
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    rec_type = models.CharField(db_column='REC_TYPE', max_length=4)
    form_type = models.CharField(db_column='FORM_TYPE', max_length=4)
    elect_date = models.DateField(
        db_column='ELECT_DATE', blank=True, null=True
    )
    electjuris = models.CharField(db_column='ELECTJURIS', max_length=40)
    contribamt = models.FloatField(db_column='CONTRIBAMT')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'F495P2_CD'
        verbose_name = 'F495P2_CD'
        verbose_name_plural = 'F495P2_CD'


class DebtCd(CalAccessBaseModel):
    """
    Form 460 (Recipient Committee Campaign Statement)
    Schedule (F) Accrued Expenses (Unpaid Bills) records
    """
    amend_id = models.IntegerField(db_column='AMEND_ID', db_index=True)
    amt_incur = models.DecimalField(
        decimal_places=2, max_digits=14, db_column='AMT_INCUR'
    )
    amt_paid = models.DecimalField(
        decimal_places=2, max_digits=14, db_column='AMT_PAID'
    )
    bakref_tid = models.CharField(
        max_length=20L, db_column='BAKREF_TID', blank=True
    )
    beg_bal = models.DecimalField(
        decimal_places=2, max_digits=14, db_column='BEG_BAL'
    )
    cmte_id = models.CharField(
        max_length=9L, db_column='CMTE_ID', blank=True
    )
    end_bal = models.DecimalField(
        decimal_places=2, max_digits=14, db_column='END_BAL'
    )
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    expn_code = models.CharField(
        max_length=3L, db_column='EXPN_CODE', blank=True
    )
    expn_dscr = models.CharField(
        max_length=400L, db_column='EXPN_DSCR', blank=True
    )
    filing_id = models.IntegerField(db_column='FILING_ID', db_index=True)
    form_type = models.CharField(max_length=1L, db_column='FORM_TYPE')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    memo_code = models.CharField(
        max_length=1L, db_column='MEMO_CODE', blank=True
    )
    memo_refno = models.CharField(
        max_length=20L, db_column='MEMO_REFNO', blank=True
    )
    payee_adr1 = models.CharField(
        max_length=55L, db_column='PAYEE_ADR1', blank=True
    )
    payee_adr2 = models.CharField(
        max_length=55L, db_column='PAYEE_ADR2', blank=True
    )
    payee_city = models.CharField(
        max_length=30L, db_column='PAYEE_CITY', blank=True
    )
    payee_namf = models.CharField(
        max_length=45L, db_column='PAYEE_NAMF', blank=True
    )
    payee_naml = models.CharField(max_length=200L, db_column='PAYEE_NAML')
    payee_nams = models.CharField(
        max_length=10L, db_column='PAYEE_NAMS', blank=True
    )
    payee_namt = models.CharField(
        max_length=100L, db_column='PAYEE_NAMT', blank=True
    )
    payee_st = models.CharField(
        max_length=2L, db_column='PAYEE_ST', blank=True
    )
    payee_zip4 = models.CharField(
        max_length=10L, db_column='PAYEE_ZIP4', blank=True
    )
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE')
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID')
    tres_adr1 = models.CharField(
        max_length=55L, db_column='TRES_ADR1', blank=True
    )
    tres_adr2 = models.CharField(
        max_length=55L, db_column='TRES_ADR2', blank=True
    )
    tres_city = models.CharField(
        max_length=30L, db_column='TRES_CITY', blank=True
    )
    tres_namf = models.CharField(
        max_length=45L, db_column='TRES_NAMF', blank=True
    )
    tres_naml = models.CharField(
        max_length=200L, db_column='TRES_NAML', blank=True
    )
    tres_nams = models.CharField(
        max_length=10L, db_column='TRES_NAMS', blank=True
    )
    tres_namt = models.CharField(
        max_length=100L, db_column='TRES_NAMT', blank=True
    )
    tres_st = models.CharField(max_length=2L, db_column='TRES_ST', blank=True)
    tres_zip4 = models.CharField(
        max_length=10L, db_column='TRES_ZIP4', blank=True
    )
    xref_match = models.CharField(
        max_length=1L, db_column='XREF_MATCH', blank=True
    )
    xref_schnm = models.CharField(
        max_length=2L, db_column='XREF_SCHNM', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'DEBT_CD'
        verbose_name = 'DEBT_CD'
        verbose_name_plural = 'DEBT_CD'


class S496Cd(CalAccessBaseModel):
    """
    Form 496 Late Independent Expenditures
    """
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    rec_type = models.CharField(
        max_length=4L, db_column='REC_TYPE', blank=True
    )
    form_type = models.CharField(
        max_length=4L, db_column='FORM_TYPE', blank=True
    )
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID', blank=True)
    amount = models.DecimalField(
        max_digits=16, decimal_places=2, db_column='AMOUNT'
    )
    exp_date = models.DateField(db_column='EXP_DATE', null=True)
    expn_dscr = models.CharField(
        max_length=90L, db_column='EXPN_DSCR', blank=True
    )
    memo_code = models.CharField(
        max_length=1L, db_column='MEMO_CODE', blank=True
    )
    memo_refno = models.CharField(
        max_length=20L, db_column='MEMO_REFNO', blank=True
    )
    date_thru = models.DateField(db_column='DATE_THRU', null=True)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'S496_CD'
        verbose_name = 'S496_CD'
        verbose_name_plural = 'S496_CD'


class SpltCd(CalAccessBaseModel):
    """
    Split Records

        -- F450P5
        -- F460 (A-B1-B2-C-D-H)
    """
    amend_id = models.IntegerField(db_column='AMEND_ID')
    elec_amount = models.DecimalField(
        max_digits=16, decimal_places=2, db_column='ELEC_AMOUNT'
    )
    elec_code = models.CharField(
        max_length=2L, db_column='ELEC_CODE', blank=True
    )
    elec_date = models.DateField(db_column='ELEC_DATE', null=True)
    filing_id = models.IntegerField(db_column='FILING_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    pform_type = models.CharField(
        max_length=7L, db_column='PFORM_TYPE', blank=True
    )
    ptran_id = models.CharField(
        max_length=32L, db_column='PTRAN_ID', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'SPLT_CD'
        verbose_name = 'SPLT_CD'
        verbose_name_plural = 'SPLT_CD'


class S497Cd(CalAccessBaseModel):
    """
    Form 497 Late Contributions Received/Made
    """
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    rec_type = models.CharField(
        max_length=4L, db_column='REC_TYPE', blank=True
    )
    form_type = models.CharField(
        max_length=6L, db_column='FORM_TYPE', blank=True
    )
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID', blank=True)
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    enty_naml = models.CharField(
        max_length=200L, db_column='ENTY_NAML', blank=True
    )
    enty_namf = models.CharField(
        max_length=45L, db_column='ENTY_NAMF', blank=True
    )
    enty_namt = models.CharField(
        max_length=10L, db_column='ENTY_NAMT', blank=True
    )
    enty_nams = models.CharField(
        max_length=10L, db_column='ENTY_NAMS', blank=True
    )
    enty_city = models.CharField(
        max_length=30L, db_column='ENTY_CITY', blank=True
    )
    enty_st = models.CharField(max_length=2L, db_column='ENTY_ST', blank=True)
    enty_zip4 = models.CharField(
        max_length=10L, db_column='ENTY_ZIP4', blank=True
    )
    ctrib_emp = models.CharField(
        max_length=200L, db_column='CTRIB_EMP', blank=True
    )
    ctrib_occ = models.CharField(
        max_length=60L, db_column='CTRIB_OCC', blank=True
    )
    ctrib_self = models.CharField(
        max_length=1L, db_column='CTRIB_SELF', blank=True
    )
    elec_date = models.DateField(db_column='ELEC_DATE', null=True)
    ctrib_date = models.DateField(db_column='CTRIB_DATE', null=True)
    date_thru = models.DateField(db_column='DATE_THRU', null=True)
    amount = models.DecimalField(
        max_digits=16, decimal_places=2, db_column='AMOUNT'
    )
    cmte_id = models.CharField(max_length=9L, db_column='CMTE_ID', blank=True)
    cand_naml = models.CharField(
        max_length=200L, db_column='CAND_NAML', blank=True
    )
    cand_namf = models.CharField(
        max_length=45L, db_column='CAND_NAMF', blank=True
    )
    cand_namt = models.CharField(
        max_length=10L, db_column='CAND_NAMT', blank=True
    )
    cand_nams = models.CharField(
        max_length=10L, db_column='CAND_NAMS', blank=True
    )
    office_cd = models.CharField(
        max_length=3L, db_column='OFFICE_CD', blank=True
    )
    offic_dscr = models.CharField(
        max_length=40L, db_column='OFFIC_DSCR', blank=True
    )
    juris_cd = models.CharField(
        max_length=3L, db_column='JURIS_CD', blank=True
    )
    juris_dscr = models.CharField(
        max_length=40L, db_column='JURIS_DSCR', blank=True
    )
    dist_no = models.CharField(max_length=3L, db_column='DIST_NO', blank=True)
    off_s_h_cd = models.CharField(
        max_length=1L, db_column='OFF_S_H_CD', blank=True
    )
    bal_name = models.CharField(
        max_length=200L, db_column='BAL_NAME', blank=True
    )
    bal_num = models.CharField(max_length=7L, db_column='BAL_NUM', blank=True)
    bal_juris = models.CharField(
        max_length=40L, db_column='BAL_JURIS', blank=True
    )
    memo_code = models.CharField(
        max_length=1L, db_column='MEMO_CODE', blank=True
    )
    memo_refno = models.CharField(
        max_length=20L, db_column='MEMO_REFNO', blank=True
    )
    bal_id = models.CharField(max_length=9L, db_column='BAL_ID', blank=True)
    cand_id = models.CharField(max_length=9L, db_column='CAND_ID', blank=True)
    sup_off_cd = models.CharField(
        max_length=1L, db_column='SUP_OFF_CD', blank=True
    )
    sup_opp_cd = models.CharField(
        max_length=1L, db_column='SUP_OPP_CD', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'S497_CD'
        verbose_name = 'S497_CD'
        verbose_name_plural = 'S497_CD'


class F501502Cd(CalAccessBaseModel):
    """
    Candidate Intention Statement

        -- F501
        -- F502
    """
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    rec_type = models.CharField(db_column='REC_TYPE', max_length=3)
    form_type = models.CharField(db_column='FORM_TYPE', max_length=4)
    filer_id = models.CharField(db_column='FILER_ID', max_length=8, blank=True)
    committee_id = models.CharField(
        db_column='COMMITTEE_ID', max_length=8, blank=True
    )
    entity_cd = models.IntegerField(
        db_column='ENTITY_CD', blank=True, null=True
    )
    report_num = models.IntegerField(
        db_column='REPORT_NUM', blank=True, null=True
    )
    rpt_date = models.DateTimeField(
        db_column='RPT_DATE', blank=True, null=True
    )
    stmt_type = models.IntegerField(db_column='STMT_TYPE')
    from_date = models.CharField(
        db_column='FROM_DATE', max_length=32, blank=True
    )
    thru_date = models.CharField(
        db_column='THRU_DATE', max_length=32, blank=True
    )
    elect_date = models.CharField(
        db_column='ELECT_DATE', max_length=32, blank=True
    )
    cand_naml = models.CharField(
        db_column='CAND_NAML', max_length=81, blank=True
    )
    cand_namf = models.CharField(
        db_column='CAND_NAMF', max_length=25, blank=True
    )
    can_namm = models.CharField(
        db_column='CAN_NAMM', max_length=10, blank=True
    )
    cand_namt = models.CharField(
        db_column='CAND_NAMT', max_length=7, blank=True
    )
    cand_nams = models.CharField(
        db_column='CAND_NAMS', max_length=7, blank=True
    )
    moniker_pos = models.CharField(
        db_column='MONIKER_POS', max_length=32, blank=True
    )
    moniker = models.CharField(
        db_column='MONIKER', max_length=4, blank=True
    )
    cand_city = models.CharField(
        db_column='CAND_CITY', max_length=22, blank=True
    )
    cand_st = models.CharField(
        db_column='CAND_ST', max_length=4, blank=True
    )
    cand_zip4 = models.CharField(
        db_column='CAND_ZIP4', max_length=10, blank=True
    )
    cand_phon = models.CharField(
        db_column='CAND_PHON', max_length=14, blank=True
    )
    cand_fax = models.CharField(
        db_column='CAND_FAX', max_length=14, blank=True
    )
    cand_email = models.CharField(
        db_column='CAND_EMAIL', max_length=37, blank=True
    )
    fin_naml = models.CharField(
        db_column='FIN_NAML', max_length=53, blank=True
    )
    fin_namf = models.CharField(
        db_column='FIN_NAMF', max_length=32, blank=True
    )
    fin_namt = models.CharField(
        db_column='FIN_NAMT', max_length=32, blank=True
    )
    fin_nams = models.CharField(
        db_column='FIN_NAMS', max_length=32, blank=True
    )
    fin_city = models.CharField(
        db_column='FIN_CITY', max_length=20, blank=True
    )
    fin_st = models.CharField(
        db_column='FIN_ST', max_length=4, blank=True
    )
    fin_zip4 = models.CharField(
        db_column='FIN_ZIP4', max_length=9, blank=True
    )
    fin_phon = models.CharField(
        db_column='FIN_PHON', max_length=14, blank=True
    )
    fin_fax = models.CharField(
        db_column='FIN_FAX', max_length=10, blank=True
    )
    fin_email = models.CharField(
        db_column='FIN_EMAIL', max_length=15, blank=True
    )
    office_cd = models.IntegerField(db_column='OFFICE_CD')
    offic_dscr = models.CharField(
        db_column='OFFIC_DSCR', max_length=50, blank=True
    )
    agency_nam = models.CharField(
        db_column='AGENCY_NAM', max_length=63, blank=True
    )
    juris_cd = models.IntegerField(
        db_column='JURIS_CD', blank=True, null=True
    )
    juris_dscr = models.CharField(
        db_column='JURIS_DSCR', max_length=14, blank=True
    )
    dist_no = models.CharField(db_column='DIST_NO', max_length=4, blank=True)
    party = models.CharField(db_column='PARTY', max_length=20, blank=True)
    yr_of_elec = models.IntegerField(
        db_column='YR_OF_ELEC', blank=True, null=True
    )
    elec_type = models.IntegerField(
        db_column='ELEC_TYPE', blank=True, null=True
    )
    execute_dt = models.DateTimeField(
        db_column='EXECUTE_DT', blank=True, null=True
    )
    can_sig = models.CharField(
        db_column='CAN_SIG', max_length=13, blank=True
    )
    account_no = models.CharField(
        db_column='ACCOUNT_NO', max_length=22, blank=True
    )
    acct_op_dt = models.DateField(
        db_column='ACCT_OP_DT', blank=True, null=True
    )
    party_cd = models.IntegerField(
        db_column='PARTY_CD', blank=True, null=True
    )
    district_cd = models.IntegerField(
        db_column='DISTRICT_CD', blank=True, null=True
    )
    accept_limit_yn = models.IntegerField(
        db_column='ACCEPT_LIMIT_YN', blank=True, null=True
    )
    did_exceed_dt = models.DateField(
        db_column='DID_EXCEED_DT', blank=True, null=True
    )
    cntrb_prsnl_fnds_dt = models.DateField(
        db_column='CNTRB_PRSNL_FNDS_DT', blank=True, null=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'F501_502_CD'
        verbose_name = 'F501_502_CD'
        verbose_name_plural = 'F501_502_CD'


class S498Cd(CalAccessBaseModel):
    """
    Form 498 Slate Mailer Late Independent Expenditures Made
    """
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    rec_type = models.CharField(
        max_length=4L, db_column='REC_TYPE', blank=True
    )
    form_type = models.CharField(
        max_length=9L, db_column='FORM_TYPE', blank=True
    )
    tran_id = models.CharField(
        max_length=20L, db_column='TRAN_ID', blank=True
    )
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    cmte_id = models.CharField(
        max_length=9L, db_column='CMTE_ID', blank=True
    )
    payor_naml = models.CharField(
        max_length=200L, db_column='PAYOR_NAML', blank=True
    )
    payor_namf = models.CharField(
        max_length=45L, db_column='PAYOR_NAMF', blank=True
    )
    payor_namt = models.CharField(
        max_length=10L, db_column='PAYOR_NAMT', blank=True
    )
    payor_nams = models.CharField(
        max_length=10L, db_column='PAYOR_NAMS', blank=True
    )
    payor_city = models.CharField(
        max_length=30L, db_column='PAYOR_CITY', blank=True
    )
    payor_st = models.CharField(
        max_length=2L, db_column='PAYOR_ST', blank=True
    )
    payor_zip4 = models.CharField(
        max_length=10L, db_column='PAYOR_ZIP4', blank=True
    )
    date_rcvd = models.DateField(db_column='DATE_RCVD', null=True)
    amt_rcvd = models.DecimalField(
        max_digits=16, decimal_places=2, db_column='AMT_RCVD'
    )
    cand_naml = models.CharField(
        max_length=200L, db_column='CAND_NAML', blank=True
    )
    cand_namf = models.CharField(
        max_length=45L, db_column='CAND_NAMF', blank=True
    )
    cand_namt = models.CharField(
        max_length=10L, db_column='CAND_NAMT', blank=True
    )
    cand_nams = models.CharField(
        max_length=10L, db_column='CAND_NAMS', blank=True
    )
    office_cd = models.CharField(
        max_length=3L, db_column='OFFICE_CD', blank=True
    )
    offic_dscr = models.CharField(
        max_length=40L, db_column='OFFIC_DSCR', blank=True
    )
    juris_cd = models.CharField(
        max_length=3L, db_column='JURIS_CD', blank=True
    )
    juris_dscr = models.CharField(
        max_length=40L, db_column='JURIS_DSCR', blank=True
    )
    dist_no = models.CharField(max_length=3L, db_column='DIST_NO', blank=True)
    off_s_h_cd = models.CharField(
        max_length=1L, db_column='OFF_S_H_CD', blank=True
    )
    bal_name = models.CharField(
        max_length=200L, db_column='BAL_NAME', blank=True
    )
    bal_num = models.CharField(max_length=7L, db_column='BAL_NUM', blank=True)
    bal_juris = models.CharField(
        max_length=40L, db_column='BAL_JURIS', blank=True
    )
    sup_opp_cd = models.CharField(
        max_length=1L, db_column='SUP_OPP_CD', blank=True
    )
    amt_attrib = models.DecimalField(
        max_digits=16, decimal_places=2, db_column='AMT_ATTRIB'
    )
    memo_code = models.CharField(
        max_length=1L, db_column='MEMO_CODE', blank=True
    )
    memo_refno = models.CharField(
        max_length=20L, db_column='MEMO_REFNO', blank=True
    )
    employer = models.CharField(
        max_length=200L, db_column='EMPLOYER', blank=True
    )
    occupation = models.CharField(
        max_length=60L, db_column='OCCUPATION', blank=True
    )
    selfemp_cb = models.CharField(
        max_length=1L, db_column='SELFEMP_CB', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'S498_CD'
        verbose_name = 'S498_CD'
        verbose_name_plural = 'S498_CD'
