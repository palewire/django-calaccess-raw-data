from __future__ import unicode_literals
from django.db import models
from calaccess import managers


class CalAccessBaseModel(models.Model):
    """
    An abstract model with some tricks we'll reuse below.
    """
    objects = managers.CalAccessManager()

    def get_csv_name(self):
        return self.__class__.objects.get_csv_name()

    def get_csv_path(self):
        return self.__class__.objects.get_csv_path()

    class Meta:
        abstract = True


class CvrSo(CalAccessBaseModel):
    acct_opendt = models.DateField(db_column="ACCT_OPENDT")
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
    qualfy_dt = models.DateField(db_column="QUALFY_DT")
    qual_cb = models.CharField(max_length=1L, db_column="QUAL_CB", blank=True)
    rec_type = models.CharField(
        max_length=3L, db_column="REC_TYPE", blank=True
    )
    report_num = models.CharField(
        max_length=3L, db_column="REPORT_NUM", blank=True
    )
    rpt_date = models.DateField(db_column="RPT_DATE")
    smcont_qualdt = models.DateField(db_column="SMCONT_QUALDT")
    sponsor_cb = models.CharField(
        max_length=1L, db_column="SPONSOR_CB", blank=True
    )
    st = models.CharField(max_length=2L, db_column="ST", blank=True)
    surplusdsp = models.CharField(
        max_length=90L, db_column="SURPLUSDSP", blank=True
    )
    term_date = models.DateField(db_column="TERM_DATE")
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
        db_table = "CVR_SO_CD"


class Cvr2CampaignDisclosureCd(CalAccessBaseModel):
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
        db_table = 'CVR2_CAMPAIGN_DISCLOSURE_CD'


class CvrCampaignDisclosureCd(CalAccessBaseModel):
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
    elect_date = models.DateField(
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
    filer_id = models.IntegerField(db_column='FILER_ID', db_index=True)
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
    from_date = models.DateField(null=True, db_column='FROM_DATE', blank=True)
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
    rpt_date = models.DateField(db_column='RPT_DATE')
    rptfromdt = models.DateField(
        null=True, db_column='RPTFROMDT', blank=True
    )
    rptthrudt = models.DateField(
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
    thru_date = models.DateField(
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
        db_table = 'CVR_CAMPAIGN_DISCLOSURE_CD'


class CvrLobbyDisclosureCd(CalAccessBaseModel):
    amend_id = models.IntegerField(db_column='AMEND_ID')
    ctrib_n_cb = models.CharField(
        max_length=1L, db_column='CTRIB_N_CB', blank=True
    )
    ctrib_y_cb = models.CharField(
        max_length=1L, db_column='CTRIB_Y_CB', blank=True
    )
    cum_beg_dt = models.DateField(
        null=True, db_column='CUM_BEG_DT', blank=True
    )
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    filer_id = models.CharField(max_length=9L, db_column='FILER_ID')
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
    filing_id = models.IntegerField(db_column='FILING_ID')
    firm_adr1 = models.CharField(
        max_length=55L, db_column='FIRM_ADR1', blank=True
    )
    firm_adr2 = models.CharField(
        max_length=55L, db_column='FIRM_ADR2', blank=True
    )
    firm_city = models.CharField(
        max_length=30L, db_column='FIRM_CITY', blank=True
    )
    firm_id = models.CharField(max_length=9L, db_column='FIRM_ID', blank=True)
    firm_name = models.CharField(
        max_length=200L, db_column='FIRM_NAME', blank=True
    )
    firm_phon = models.CharField(
        max_length=20L, db_column='FIRM_PHON', blank=True
    )
    firm_st = models.CharField(max_length=2L, db_column='FIRM_ST', blank=True)
    firm_zip4 = models.CharField(
        max_length=10L, db_column='FIRM_ZIP4', blank=True
    )
    form_type = models.CharField(max_length=4L, db_column='FORM_TYPE')
    from_date = models.DateField(db_column='FROM_DATE')
    lby_actvty = models.CharField(
        max_length=400L, db_column='LBY_ACTVTY', blank=True
    )
    lobby_n_cb = models.CharField(
        max_length=1L, db_column='LOBBY_N_CB', blank=True
    )
    lobby_y_cb = models.CharField(
        max_length=1L, db_column='LOBBY_Y_CB', blank=True
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
    mail_phon = models.CharField(
        max_length=20L, db_column='MAIL_PHON', blank=True
    )
    mail_st = models.CharField(
        max_length=2L, db_column='MAIL_ST', blank=True
    )
    mail_zip4 = models.CharField(
        max_length=10L, db_column='MAIL_ZIP4', blank=True
    )
    major_namf = models.CharField(
        max_length=45L, db_column='MAJOR_NAMF', blank=True
    )
    major_naml = models.CharField(
        max_length=200L, db_column='MAJOR_NAML', blank=True
    )
    major_nams = models.CharField(
        max_length=10L, db_column='MAJOR_NAMS', blank=True
    )
    major_namt = models.CharField(
        max_length=10L, db_column='MAJOR_NAMT', blank=True
    )
    nopart1_cb = models.CharField(
        max_length=1L, db_column='NOPART1_CB', blank=True
    )
    nopart2_cb = models.CharField(
        max_length=1L, db_column='NOPART2_CB', blank=True
    )
    part1_1_cb = models.CharField(
        max_length=1L, db_column='PART1_1_CB', blank=True
    )
    part1_2_cb = models.CharField(
        max_length=1L, db_column='PART1_2_CB', blank=True
    )
    prn_namf = models.CharField(
        max_length=45L, db_column='PRN_NAMF', blank=True
    )
    prn_naml = models.CharField(
        max_length=200L, db_column='PRN_NAML', blank=True
    )
    prn_nams = models.CharField(
        max_length=10L, db_column='PRN_NAMS', blank=True
    )
    prn_namt = models.CharField(
        max_length=10L, db_column='PRN_NAMT', blank=True
    )
    rcpcmte_id = models.CharField(
        max_length=9L, db_column='RCPCMTE_ID', blank=True
    )
    rcpcmte_nm = models.CharField(
        max_length=200L, db_column='RCPCMTE_NM', blank=True
    )
    rec_type = models.CharField(max_length=3L, db_column='REC_TYPE')
    report_num = models.CharField(max_length=3L, db_column='REPORT_NUM')
    rpt_date = models.DateField(db_column='RPT_DATE')
    sender_id = models.CharField(max_length=9L, db_column='SENDER_ID')
    sig_date = models.DateField(db_column='SIG_DATE')
    sig_loc = models.CharField(max_length=45L, db_column='SIG_LOC', blank=True)
    sig_namf = models.CharField(
        max_length=45L, db_column='SIG_NAMF', blank=True
    )
    sig_naml = models.CharField(
        max_length=200L, db_column='SIG_NAML', blank=True
    )
    sig_nams = models.CharField(
        max_length=10L, db_column='SIG_NAMS', blank=True
    )
    sig_namt = models.CharField(
        max_length=10L, db_column='SIG_NAMT', blank=True
    )
    sig_title = models.CharField(
        max_length=45L, db_column='SIG_TITLE', blank=True
    )
    thru_date = models.DateField(db_column='THRU_DATE')

    class Meta:
        db_table = 'CVR_LOBBY_DISCLOSURE_CD'


class Cvr2LobbyDisclosureCd(CalAccessBaseModel):
    amend_id = models.IntegerField(db_column='AMEND_ID')
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    entity_id = models.CharField(
        max_length=9L, db_column='ENTITY_ID', blank=True
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
    enty_title = models.CharField(
        max_length=45L, db_column='ENTY_TITLE', blank=True
    )
    filing_id = models.IntegerField(db_column='FILING_ID')
    form_type = models.CharField(
        max_length=4L, db_column='FORM_TYPE', blank=True
    )
    line_item = models.IntegerField(db_column='LINE_ITEM')
    rec_type = models.CharField(
        max_length=4L, db_column='REC_TYPE', blank=True
    )
    tran_id = models.CharField(
        max_length=20L, db_column='TRAN_ID', blank=True
    )

    class Meta:
        db_table = 'CVR2_LOBBY_DISCLOSURE_CD'


class CvrRegistrationCd(CalAccessBaseModel):
    a_b_adr1 = models.CharField(
        max_length=55L, db_column='A_B_ADR1', blank=True
    )
    a_b_adr2 = models.CharField(
        max_length=55L, db_column='A_B_ADR2', blank=True
    )
    a_b_city = models.CharField(
        max_length=30L, db_column='A_B_CITY', blank=True
    )
    a_b_name = models.CharField(
        max_length=200L, db_column='A_B_NAME', blank=True
    )
    a_b_st = models.CharField(max_length=2L, db_column='A_B_ST', blank=True)
    a_b_zip4 = models.CharField(
        max_length=10L, db_column='A_B_ZIP4', blank=True
    )
    amend_id = models.IntegerField(db_column='AMEND_ID')
    auth_adr1 = models.CharField(
        max_length=55L, db_column='AUTH_ADR1', blank=True
    )
    auth_adr2 = models.CharField(
        max_length=55L, db_column='AUTH_ADR2', blank=True
    )
    auth_city = models.CharField(
        max_length=30L, db_column='AUTH_CITY', blank=True
    )
    auth_name = models.CharField(
        max_length=200L, db_column='AUTH_NAME', blank=True
    )
    auth_st = models.CharField(max_length=2L, db_column='AUTH_ST', blank=True)
    auth_zip4 = models.CharField(
        max_length=10L, db_column='AUTH_ZIP4', blank=True
    )
    bus_adr1 = models.CharField(
        max_length=55L, db_column='BUS_ADR1', blank=True
    )
    bus_adr2 = models.CharField(
        max_length=55L, db_column='BUS_ADR2', blank=True
    )
    bus_cb = models.CharField(max_length=1L, db_column='BUS_CB', blank=True)
    bus_city = models.CharField(max_length=30L, db_column='BUS_CITY')
    bus_class = models.CharField(
        max_length=3L, db_column='BUS_CLASS', blank=True
    )
    bus_descr = models.CharField(
        max_length=100L, db_column='BUS_DESCR', blank=True
    )
    bus_email = models.CharField(
        max_length=60L, db_column='BUS_EMAIL', blank=True
    )
    bus_fax = models.CharField(max_length=20L, db_column='BUS_FAX', blank=True)
    bus_phon = models.CharField(
        max_length=20L, db_column='BUS_PHON', blank=True
    )
    bus_st = models.CharField(max_length=2L, db_column='BUS_ST', blank=True)
    bus_zip4 = models.CharField(
        max_length=10L, db_column='BUS_ZIP4', blank=True
    )
    c_less50 = models.CharField(
        max_length=1L, db_column='C_LESS50', blank=True
    )
    c_more50 = models.CharField(
        max_length=1L, db_column='C_MORE50', blank=True
    )
    complet_dt = models.DateField(
        null=True, db_column='COMPLET_DT', blank=True
    )
    descrip_1 = models.CharField(
        max_length=300L, db_column='DESCRIP_1', blank=True
    )
    descrip_2 = models.CharField(
        max_length=300L, db_column='DESCRIP_2', blank=True
    )
    eff_date = models.DateField(null=True, db_column='EFF_DATE', blank=True)
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    filer_id = models.CharField(max_length=9L, db_column='FILER_ID')
    filer_namf = models.CharField(
        max_length=45L, db_column='FILER_NAMF', blank=True
    )
    filer_naml = models.CharField(
        max_length=200L, db_column='FILER_NAML', blank=True
    )
    filer_nams = models.CharField(
        max_length=10L, db_column='FILER_NAMS', blank=True
    )
    filer_namt = models.CharField(
        max_length=10L, db_column='FILER_NAMT', blank=True
    )
    filing_id = models.IntegerField(
        null=True, db_column='FILING_ID', blank=True
    )
    firm_name = models.CharField(
        max_length=200L, db_column='FIRM_NAME', blank=True
    )
    form_type = models.CharField(
        max_length=4L, db_column='FORM_TYPE', blank=True
    )
    ind_cb = models.CharField(max_length=1L, db_column='IND_CB', blank=True)
    ind_class = models.CharField(
        max_length=3L, db_column='IND_CLASS', blank=True
    )
    ind_descr = models.CharField(
        max_length=100L, db_column='IND_DESCR', blank=True
    )
    influen_yn = models.IntegerField(
        null=True, db_column='INFLUEN_YN', blank=True
    )
    l_firm_cb = models.CharField(
        max_length=1L, db_column='L_FIRM_CB', blank=True
    )
    lby_604_cb = models.CharField(
        max_length=1L, db_column='LBY_604_CB', blank=True
    )
    lby_reg_cb = models.CharField(
        max_length=1L, db_column='LBY_REG_CB', blank=True
    )
    lobby_cb = models.CharField(
        max_length=1L, db_column='LOBBY_CB', blank=True
    )
    lobby_int = models.CharField(
        max_length=300L, db_column='LOBBY_INT', blank=True
    )
    ls_beg_yr = models.IntegerField(
        null=True, db_column='LS_BEG_YR', blank=True
    )
    ls_end_yr = models.IntegerField(db_column='LS_END_YR')
    mail_adr1 = models.CharField(
        max_length=55L, db_column='MAIL_ADR1', blank=True
    )
    mail_adr2 = models.CharField(
        max_length=55L, db_column='MAIL_ADR2', blank=True
    )
    mail_city = models.CharField(
        max_length=30L, db_column='MAIL_CITY', blank=True
    )
    mail_phon = models.CharField(
        max_length=20L, db_column='MAIL_PHON', blank=True
    )
    mail_st = models.CharField(max_length=2L, db_column='MAIL_ST', blank=True)
    mail_zip4 = models.CharField(
        max_length=10L, db_column='MAIL_ZIP4', blank=True
    )
    newcert_cb = models.CharField(
        max_length=1L, db_column='NEWCERT_CB', blank=True
    )
    oth_cb = models.CharField(max_length=1L, db_column='OTH_CB', blank=True)
    prn_namf = models.CharField(
        max_length=45L, db_column='PRN_NAMF', blank=True
    )
    prn_naml = models.CharField(
        max_length=200L, db_column='PRN_NAML', blank=True
    )
    prn_nams = models.CharField(
        max_length=10L, db_column='PRN_NAMS', blank=True
    )
    prn_namt = models.CharField(
        max_length=10L, db_column='PRN_NAMT', blank=True
    )
    qual_date = models.DateField(
        null=True, db_column='QUAL_DATE', blank=True
    )
    rec_type = models.CharField(
        max_length=4L, db_column='REC_TYPE', blank=True
    )
    rencert_cb = models.CharField(
        max_length=1L, db_column='RENCERT_CB', blank=True
    )
    report_num = models.CharField(
        max_length=3L, db_column='REPORT_NUM', blank=True
    )
    rpt_date = models.DateField(db_column='RPT_DATE')
    sender_id = models.CharField(max_length=9L, db_column='SENDER_ID')
    sig_date = models.DateField(
        null=True, db_column='SIG_DATE', blank=True
    )
    sig_loc = models.CharField(
        max_length=45L, db_column='SIG_LOC', blank=True
    )
    sig_namf = models.CharField(
        max_length=45L, db_column='SIG_NAMF', blank=True
    )
    sig_naml = models.CharField(
        max_length=200L, db_column='SIG_NAML', blank=True
    )
    sig_nams = models.CharField(
        max_length=10L, db_column='SIG_NAMS', blank=True
    )
    sig_namt = models.CharField(
        max_length=10L, db_column='SIG_NAMT', blank=True
    )
    sig_title = models.CharField(
        max_length=45L, db_column='SIG_TITLE', blank=True
    )
    st_agency = models.CharField(
        max_length=100L, db_column='ST_AGENCY', blank=True
    )
    st_leg_yn = models.IntegerField(
        null=True, db_column='ST_LEG_YN', blank=True
    )
    stmt_firm = models.CharField(
        max_length=90L, db_column='STMT_FIRM', blank=True
    )
    trade_cb = models.CharField(
        max_length=1L, db_column='TRADE_CB', blank=True
    )

    class Meta:
        db_table = 'CVR_REGISTRATION_CD'


class Cvr2RegistrationCd(CalAccessBaseModel):
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    line_item = models.CharField(
        max_length=9L, db_column='LINE_ITEM', blank=True
    )
    rec_type = models.CharField(
        max_length=4L, db_column='REC_TYPE', blank=True
    )
    form_type = models.CharField(
        max_length=10L, db_column='FORM_TYPE', blank=True
    )
    tran_id = models.CharField(
        max_length=20L, db_column='TRAN_ID', blank=True
    )
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    entity_id = models.CharField(
        max_length=9L, db_column='ENTITY_ID', blank=True
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

    class Meta:
        db_table = 'CVR2_REGISTRATION_CD'


class DebtCd(CalAccessBaseModel):
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
        db_table = 'DEBT_CD'


class ExpnCd(CalAccessBaseModel):
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
    form_type = models.CharField(max_length=6L, db_column='FORM_TYPE')
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
    current_filing = models.CharField(max_length=1L, blank=True)

    class Meta:
        db_table = 'EXPN_CD'


class FilernameCd(CalAccessBaseModel):
    xref_filer_id = models.CharField(
        max_length=7L, db_column='XREF_FILER_ID', db_index=True
    )
    filer_id = models.IntegerField(db_column='FILER_ID', db_index=True)
    filer_type = models.CharField(max_length=45L, db_column='FILER_TYPE')
    status = models.CharField(max_length=10L, db_column='STATUS')
    effect_dt = models.DateField(db_column='EFFECT_DT')
    naml = models.CharField(max_length=200L, db_column='NAML')
    namf = models.CharField(max_length=55L, db_column='NAMF', blank=True)
    namt = models.CharField(max_length=28L, db_column='NAMT', blank=True)
    nams = models.CharField(max_length=32L, db_column='NAMS', blank=True)
    adr1 = models.CharField(max_length=200L, db_column='ADR1', blank=True)
    adr2 = models.CharField(max_length=200L, db_column='ADR2', blank=True)
    city = models.CharField(max_length=55L, db_column='CITY', blank=True)
    st = models.CharField(max_length=4L, db_column='ST', blank=True)
    zip4 = models.CharField(max_length=10L, db_column='ZIP4', blank=True)
    phon = models.CharField(max_length=60L, db_column='PHON', blank=True)
    fax = models.CharField(max_length=60L, db_column='FAX', blank=True)
    email = models.CharField(max_length=60L, db_column='EMAIL', blank=True)

    class Meta:
        db_table = 'FILERNAME_CD'


class FilersCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID', db_index=True)

    class Meta:
        db_table = 'FILERS_CD'


class FilerAcronymsCd(CalAccessBaseModel):
    acronym = models.CharField(max_length=32L)
    filer_id = models.IntegerField()

    class Meta:
        db_table = 'FILER_ACRONYMS_CD'


class FilerFilingsCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID', db_index=True)
    filing_id = models.IntegerField(db_column='FILING_ID', db_index=True)
    period_id = models.IntegerField(
        null=True, db_column='PERIOD_ID', blank=True
    )
    form_id = models.CharField(max_length=7L, db_column='FORM_ID')
    filing_sequence = models.IntegerField(
        db_column='FILING_SEQUENCE', db_index=True
    )
    filing_date = models.DateField(db_column='FILING_DATE')
    stmnt_type = models.IntegerField(db_column='STMNT_TYPE')
    stmnt_status = models.IntegerField(db_column='STMNT_STATUS')
    session_id = models.IntegerField(db_column='SESSION_ID')
    user_id = models.CharField(max_length=12L, db_column='USER_ID')
    special_audit = models.IntegerField(
        null=True, db_column='SPECIAL_AUDIT', blank=True
    )
    fine_audit = models.IntegerField(
        null=True, db_column='FINE_AUDIT', blank=True
    )
    rpt_start = models.DateField(null=True, db_column='RPT_START', blank=True)
    rpt_end = models.DateField(null=True, db_column='RPT_END', blank=True)
    rpt_date = models.DateField(null=True, db_column='RPT_DATE', blank=True)
    filing_type = models.IntegerField(
        null=True, db_column='FILING_TYPE', blank=True
    )

    class Meta:
        db_table = 'FILER_FILINGS_CD'


class FilerInterestsCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    interest_cd = models.IntegerField(db_column='INTEREST_CD')
    effect_date = models.DateTimeField(db_column='EFFECT_DATE')

    class Meta:
        db_table = 'FILER_INTERESTS_CD'


class FilerLinksCd(CalAccessBaseModel):
    filer_id_a = models.IntegerField(db_column='FILER_ID_A', db_index=True)
    filer_id_b = models.IntegerField(db_column='FILER_ID_B', db_index=True)
    active_flg = models.CharField(max_length=1L, db_column='ACTIVE_FLG')
    session_id = models.IntegerField(db_column='SESSION_ID')
    link_type = models.IntegerField(db_column='LINK_TYPE')
    link_desc = models.CharField(
        max_length=255L, db_column='LINK_DESC', blank=True
    )
    effect_dt = models.DateField(db_column='EFFECT_DT')
    dominate_filer = models.CharField(
        max_length=1L, db_column='DOMINATE_FILER', blank=True
    )
    termination_dt = models.DateField(
        null=True, db_column='TERMINATION_DT', blank=True
    )

    class Meta:
        db_table = 'FILER_LINKS_CD'


class FilerStatusTypesCd(CalAccessBaseModel):
    status_type = models.CharField(max_length=11L, db_column='STATUS_TYPE')
    status_desc = models.CharField(max_length=11L, db_column='STATUS_DESC')

    class Meta:
        db_table = 'FILER_STATUS_TYPES_CD'


class FilerToFilerTypeCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    filer_type = models.IntegerField(db_column='FILER_TYPE')
    active = models.CharField(max_length=1L, db_column='ACTIVE')
    race = models.IntegerField(null=True, db_column='RACE', blank=True)
    session_id = models.IntegerField(db_column='SESSION_ID')
    category = models.IntegerField(
        null=True, db_column='CATEGORY', blank=True
    )
    category_type = models.IntegerField(
        null=True, db_column='CATEGORY_TYPE', blank=True
    )
    sub_category = models.IntegerField(
        null=True, db_column='SUB_CATEGORY', blank=True
    )
    effect_dt = models.DateField(db_column='EFFECT_DT')
    sub_category_type = models.IntegerField(
        null=True, db_column='SUB_CATEGORY_TYPE', blank=True
    )
    election_type = models.IntegerField(
        null=True, db_column='ELECTION_TYPE', blank=True
    )
    sub_category_a = models.CharField(
        max_length=1L, db_column='SUB_CATEGORY_A', blank=True
    )
    nyq_dt = models.DateField(null=True, db_column='NYQ_DT', blank=True)
    party_cd = models.IntegerField(
        null=True, db_column='PARTY_CD', blank=True
    )
    county_cd = models.IntegerField(
        null=True, db_column='COUNTY_CD', blank=True
    )
    district_cd = models.IntegerField(
        null=True, db_column='DISTRICT_CD', blank=True
    )

    class Meta:
        db_table = 'FILER_TO_FILER_TYPE_CD'


class FilerTypesCd(CalAccessBaseModel):
    filer_type = models.IntegerField(db_column='FILER_TYPE')
    description = models.CharField(max_length=255L, db_column='DESCRIPTION')
    grp_type = models.IntegerField(null=True, db_column='GRP_TYPE', blank=True)
    calc_use = models.CharField(
        max_length=1L, db_column='CALC_USE', blank=True
    )
    grace_period = models.CharField(
        max_length=12L, db_column='GRACE_PERIOD', blank=True
    )

    class Meta:
        db_table = 'FILER_TYPES_CD'


class FilerXrefCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    xref_id = models.CharField(max_length=32L, db_column='XREF_ID')
    effect_dt = models.DateField(db_column='EFFECT_DT')
    migration_source = models.CharField(
        max_length=50L, db_column='MIGRATION_SOURCE'
    )

    class Meta:
        db_table = 'FILER_XREF_CD'


class FilingsCd(CalAccessBaseModel):
    filing_id = models.IntegerField(db_column='FILING_ID', db_index=True)
    filing_type = models.IntegerField(db_column='FILING_TYPE')

    class Meta:
        db_table = 'FILINGS_CD'


class FilingPeriodCd(CalAccessBaseModel):
    period_id = models.IntegerField(db_column='PERIOD_ID')
    start_date = models.DateField(db_column='START_DATE')
    end_date = models.DateField(db_column='END_DATE')
    period_type = models.IntegerField(db_column='PERIOD_TYPE')
    per_grp_type = models.IntegerField(db_column='PER_GRP_TYPE')
    period_desc = models.CharField(max_length=255L, db_column='PERIOD_DESC')
    deadline = models.DateField(db_column='DEADLINE')

    class Meta:
        db_table = 'FILING_PERIOD_CD'


class HdrCd(CalAccessBaseModel):
    amend_id = models.IntegerField(db_column='AMEND_ID')
    cal_ver = models.CharField(max_length=4L, db_column='CAL_VER', blank=True)
    ef_type = models.CharField(max_length=3L, db_column='EF_TYPE', blank=True)
    filing_id = models.IntegerField(db_column='FILING_ID')
    hdr_comment = models.CharField(
        max_length=200L, db_column='HDRCOMMENT', blank=True
    )
    rec_type = models.CharField(
        max_length=3L, db_column='REC_TYPE', blank=True
    )
    soft_name = models.CharField(
        max_length=90L, db_column='SOFT_NAME', blank=True
    )
    soft_ver = models.CharField(
        max_length=16L, db_column='SOFT_VER', blank=True
    )
    state_cd = models.CharField(
        max_length=2L, db_column='STATE_CD', blank=True
    )

    class Meta:
        db_table = 'HDR_CD'


class LattCd(CalAccessBaseModel):
    amend_id = models.IntegerField(db_column='AMEND_ID')
    amount = models.DecimalField(
        max_digits=16, decimal_places=2, db_column='AMOUNT'
    )
    cum_amt = models.DecimalField(
        max_digits=16, decimal_places=2, db_column='CUM_AMT'
    )
    cumbeg_dt = models.DateField(db_column='CUMBEG_DT')
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    filing_id = models.IntegerField(db_column='FILING_ID')
    form_type = models.CharField(max_length=6L, db_column='FORM_TYPE')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    memo_code = models.CharField(
        max_length=1L, db_column='MEMO_CODE', blank=True
    )
    memo_refno = models.CharField(
        max_length=20L, db_column='MEMO_REFNO', blank=True
    )
    pmt_date = models.DateField(db_column='PMT_DATE')
    rec_type = models.CharField(
        max_length=4L, db_column='REC_TYPE', blank=True
    )
    recip_adr1 = models.CharField(
        max_length=55L, db_column='RECIP_ADR1', blank=True
    )
    recip_adr2 = models.CharField(
        max_length=55L, db_column='RECIP_ADR2', blank=True
    )
    recip_city = models.CharField(
        max_length=30L, db_column='RECIP_CITY', blank=True
    )
    recip_namf = models.CharField(
        max_length=45L, db_column='RECIP_NAMF', blank=True
    )
    recip_naml = models.CharField(
        max_length=200L, db_column='RECIP_NAML', blank=True
    )
    recip_nams = models.CharField(
        max_length=10L, db_column='RECIP_NAMS', blank=True
    )
    recip_namt = models.CharField(
        max_length=10L, db_column='RECIP_NAMT', blank=True
    )
    recip_st = models.CharField(
        max_length=2L, db_column='RECIP_ST', blank=True
    )
    recip_zip4 = models.CharField(
        max_length=10L, db_column='RECIP_ZIP4', blank=True
    )
    tran_id = models.CharField(
        max_length=20L, db_column='TRAN_ID', blank=True
    )

    class Meta:
        db_table = 'LATT_CD'


class LccmCd(CalAccessBaseModel):
    acct_name = models.CharField(
        max_length=90L, db_column='ACCT_NAME', blank=True
    )
    amend_id = models.IntegerField(db_column='AMEND_ID', db_index=True)
    amount = models.DecimalField(
        max_digits=16, decimal_places=2, db_column='AMOUNT'
    )
    bakref_tid = models.CharField(
        max_length=20L, db_column='BAKREF_TID', blank=True
    )
    ctrib_date = models.DateField(db_column='CTRIB_DATE')
    ctrib_namf = models.CharField(
        max_length=45L, db_column='CTRIB_NAMF', blank=True
    )
    ctrib_naml = models.CharField(
        max_length=45L, db_column='CTRIB_NAML', blank=True
    )
    ctrib_nams = models.CharField(
        max_length=10L, db_column='CTRIB_NAMS', blank=True
    )
    ctrib_namt = models.CharField(
        max_length=10L, db_column='CTRIB_NAMT', blank=True
    )
    entity_cd = models.CharField(
        max_length=3, db_column='ENTITY_CD', blank=True
    )
    filing_id = models.IntegerField(db_column='FILING_ID', db_index=True)
    form_type = models.CharField(
        max_length=7L, db_column='FORM_TYPE', blank=True
    )
    line_item = models.IntegerField(db_column='LINE_ITEM')
    memo_code = models.CharField(
        max_length=1L, db_column='MEMO_CODE', blank=True
    )
    memo_refno = models.CharField(
        max_length=20L, db_column='MEMO_REFNO', blank=True
    )
    rec_type = models.CharField(
        max_length=4L, db_column='REC_TYPE', blank=True
    )
    recip_adr1 = models.CharField(
        max_length=55L, db_column='RECIP_ADR1', blank=True
    )
    recip_adr2 = models.CharField(
        max_length=55L, db_column='RECIP_ADR2', blank=True
    )
    recip_city = models.CharField(
        max_length=30L, db_column='RECIP_CITY', blank=True
    )
    recip_id = models.CharField(
        max_length=9L, db_column='RECIP_ID', blank=True
    )
    recip_namf = models.CharField(
        max_length=45L, db_column='RECIP_NAMF', blank=True
    )
    recip_naml = models.CharField(
        max_length=200L, db_column='RECIP_NAML', blank=True
    )
    recip_nams = models.CharField(
        max_length=10L, db_column='RECIP_NAMS', blank=True
    )
    recip_namt = models.CharField(
        max_length=10L, db_column='RECIP_NAMT', blank=True
    )
    recip_st = models.CharField(
        max_length=2L, db_column='RECIP_ST', blank=True
    )
    recip_zip4 = models.CharField(
        max_length=10L, db_column='RECIP_ZIP4', blank=True
    )
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID', blank=True)

    class Meta:
        db_table = 'LCCM_CD'


class LempCd(CalAccessBaseModel):
    agencylist = models.CharField(
        max_length=200L, db_column='AGENCYLIST', blank=True
    )
    amend_id = models.IntegerField(db_column='AMEND_ID')
    cli_adr1 = models.CharField(
        max_length=55L, db_column='CLI_ADR1', blank=True
    )
    cli_adr2 = models.CharField(
        max_length=55L, db_column='CLI_ADR2', blank=True
    )
    cli_city = models.CharField(max_length=30L, db_column='CLI_CITY')
    cli_namf = models.CharField(
        max_length=45L, db_column='CLI_NAMF', blank=True
    )
    cli_naml = models.CharField(max_length=200L, db_column='CLI_NAML')
    cli_nams = models.CharField(
        max_length=10L, db_column='CLI_NAMS', blank=True
    )
    cli_namt = models.CharField(
        max_length=10L, db_column='CLI_NAMT', blank=True
    )
    cli_phon = models.CharField(
        max_length=20L, db_column='CLI_PHON', blank=True
    )
    cli_st = models.CharField(max_length=2L, db_column='CLI_ST', blank=True)
    cli_zip4 = models.CharField(max_length=10L, db_column='CLI_ZIP4')
    client_id = models.CharField(
        max_length=9L, db_column='CLIENT_ID', blank=True
    )
    con_period = models.CharField(
        max_length=30L, db_column='CON_PERIOD', blank=True
    )
    descrip = models.CharField(
        max_length=100L, db_column='DESCRIP', blank=True
    )
    eff_date = models.DateField(null=True, db_column='EFF_DATE', blank=True)
    filing_id = models.IntegerField(db_column='FILING_ID')
    form_type = models.CharField(max_length=7L, db_column='FORM_TYPE')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE')
    sub_adr1 = models.CharField(
        max_length=55L, db_column='SUB_ADR1', blank=True
    )
    sub_adr2 = models.CharField(
        max_length=55L, db_column='SUB_ADR2', blank=True
    )
    sub_city = models.CharField(
        max_length=30L, db_column='SUB_CITY', blank=True
    )
    sub_name = models.CharField(
        max_length=200L, db_column='SUB_NAME', blank=True
    )
    sub_phon = models.CharField(
        max_length=20L, db_column='SUB_PHON', blank=True
    )
    sub_st = models.CharField(max_length=2L, db_column='SUB_ST', blank=True)
    sub_zip4 = models.CharField(
        max_length=10L, db_column='SUB_ZIP4', blank=True
    )
    subfirm_id = models.CharField(
        max_length=9L, db_column='SUBFIRM_ID', blank=True
    )

    class Meta:
        db_table = 'LEMP_CD'


class LexpCd(CalAccessBaseModel):
    amend_id = models.IntegerField(db_column='AMEND_ID', db_index=True)
    amount = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='AMOUNT', blank=True
    )
    bakref_tid = models.CharField(
        max_length=20L, db_column='BAKREF_TID', blank=True
    )
    bene_amt = models.CharField(
        max_length=12L, db_column='BENE_AMT', blank=True
    )
    bene_name = models.CharField(
        max_length=90L, db_column='BENE_NAME', blank=True
    )
    bene_posit = models.CharField(
        max_length=90L, db_column='BENE_POSIT', blank=True
    )
    credcardco = models.CharField(
        max_length=200L, db_column='CREDCARDCO', blank=True
    )
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD')
    expn_date = models.DateField(null=True, db_column='EXPN_DATE', blank=True)
    expn_dscr = models.CharField(
        max_length=90L, db_column='EXPN_DSCR', blank=True
    )
    filing_id = models.IntegerField(db_column='FILING_ID', db_index=True)
    form_type = models.CharField(max_length=7L, db_column='FORM_TYPE')
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
    recsubtype = models.CharField(max_length=1L, db_column='RECSUBTYPE')
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID')

    class Meta:
        db_table = 'LEXP_CD'


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
    loan_date1 = models.DateField(db_column='LOAN_DATE1')
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
        db_table = 'LOAN_CD'


class LobbyAmendmentsCd(CalAccessBaseModel):
    filing_id = models.CharField(max_length=9L, db_column='FILING_ID')
    amend_id = models.CharField(max_length=8L, db_column='AMEND_ID')
    rec_type = models.CharField(max_length=8L, db_column='REC_TYPE')
    form_type = models.CharField(max_length=9L, db_column='FORM_TYPE')
    exec_date = models.CharField(max_length=22L, db_column='EXEC_DATE')
    from_date = models.CharField(max_length=22L, db_column='FROM_DATE')
    thru_date = models.CharField(max_length=22L, db_column='THRU_DATE')
    add_l_cb = models.CharField(
        max_length=1L, db_column='ADD_L_CB', blank=True
    )
    add_l_eff = models.DateField(null=True, db_column='ADD_L_EFF', blank=True)
    a_l_naml = models.CharField(
        max_length=200L, db_column='A_L_NAML', blank=True
    )
    a_l_namf = models.CharField(
        max_length=45L, db_column='A_L_NAMF', blank=True
    )
    a_l_namt = models.CharField(
        max_length=10L, db_column='A_L_NAMT', blank=True
    )
    a_l_nams = models.CharField(
        max_length=10L, db_column='A_L_NAMS', blank=True
    )
    del_l_cb = models.CharField(
        max_length=8L, db_column='DEL_L_CB', blank=True
    )
    del_l_eff = models.CharField(
        max_length=22L, db_column='DEL_L_EFF', blank=True
    )
    d_l_naml = models.CharField(
        max_length=56L, db_column='D_L_NAML', blank=True
    )
    d_l_namf = models.CharField(
        max_length=35L, db_column='D_L_NAMF', blank=True
    )
    d_l_namt = models.CharField(
        max_length=10L, db_column='D_L_NAMT', blank=True
    )
    d_l_nams = models.CharField(
        max_length=8L, db_column='D_L_NAMS', blank=True
    )
    add_le_cb = models.CharField(
        max_length=1L, db_column='ADD_LE_CB', blank=True
    )
    add_le_eff = models.DateField(
        null=True, db_column='ADD_LE_EFF', blank=True
    )
    a_le_naml = models.CharField(
        max_length=200L, db_column='A_LE_NAML', blank=True
    )
    a_le_namf = models.CharField(
        max_length=45L, db_column='A_LE_NAMF', blank=True
    )
    a_le_namt = models.CharField(
        max_length=10L, db_column='A_LE_NAMT', blank=True
    )
    a_le_nams = models.CharField(
        max_length=10L, db_column='A_LE_NAMS', blank=True
    )
    del_le_cb = models.CharField(
        max_length=9L, db_column='DEL_LE_CB', blank=True
    )
    del_le_eff = models.CharField(
        max_length=22L, db_column='DEL_LE_EFF', blank=True
    )
    d_le_naml = models.CharField(
        max_length=160L, db_column='D_LE_NAML', blank=True
    )
    d_le_namf = models.CharField(
        max_length=45L, db_column='D_LE_NAMF', blank=True
    )
    d_le_namt = models.CharField(
        max_length=9L, db_column='D_LE_NAMT', blank=True
    )
    d_le_nams = models.CharField(
        max_length=9L, db_column='D_LE_NAMS', blank=True
    )
    add_lf_cb = models.CharField(
        max_length=1L, db_column='ADD_LF_CB', blank=True
    )
    add_lf_eff = models.DateField(
        null=True, db_column='ADD_LF_EFF', blank=True
    )
    a_lf_name = models.CharField(
        max_length=200L, db_column='A_LF_NAME', blank=True
    )
    del_lf_cb = models.CharField(
        max_length=1L, db_column='DEL_LF_CB', blank=True
    )
    del_lf_eff = models.DateField(
        null=True, db_column='DEL_LF_EFF', blank=True
    )
    d_lf_name = models.CharField(
        max_length=200L, db_column='D_LF_NAME', blank=True
    )
    other_cb = models.CharField(
        max_length=1L, db_column='OTHER_CB', blank=True
    )
    other_eff = models.DateField(
        null=True, db_column='OTHER_EFF', blank=True
    )
    other_desc = models.CharField(
        max_length=100L, db_column='OTHER_DESC', blank=True
    )
    f606_yes = models.CharField(
        max_length=1L, db_column='F606_YES', blank=True
    )
    f606_no = models.CharField(
        max_length=1L, db_column='F606_NO', blank=True
    )

    class Meta:
        db_table = 'LOBBY_AMENDMENTS_CD'


class LookupCode(CalAccessBaseModel):
    code_type = models.IntegerField()
    code_id = models.IntegerField()
    code_desc = models.CharField(max_length=100)

    class Meta:
        db_table = 'LOOKUP_CODES_CD'


class LothCd(CalAccessBaseModel):
    amend_id = models.IntegerField(db_column='AMEND_ID')
    amount = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='AMOUNT', blank=True
    )
    cum_amt = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='CUM_AMT', blank=True
    )
    filing_id = models.IntegerField(db_column='FILING_ID')
    firm_adr1 = models.CharField(
        max_length=55L, db_column='FIRM_ADR1', blank=True
    )
    firm_adr2 = models.CharField(
        max_length=55L, db_column='FIRM_ADR2', blank=True
    )
    firm_city = models.CharField(
        max_length=30L, db_column='FIRM_CITY', blank=True
    )
    firm_name = models.CharField(
        max_length=200L, db_column='FIRM_NAME', blank=True
    )
    firm_phon = models.CharField(
        max_length=20L, db_column='FIRM_PHON', blank=True
    )
    firm_st = models.CharField(
        max_length=2L, db_column='FIRM_ST', blank=True
    )
    firm_zip4 = models.CharField(
        max_length=10L, db_column='FIRM_ZIP4', blank=True
    )
    form_type = models.CharField(max_length=7L, db_column='FORM_TYPE')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    memo_code = models.CharField(
        max_length=1L, db_column='MEMO_CODE', blank=True
    )
    memo_refno = models.CharField(
        max_length=20L, db_column='MEMO_REFNO', blank=True
    )
    pmt_date = models.DateField(
        null=True, db_column='PMT_DATE', blank=True
    )
    rec_type = models.CharField(
        max_length=4L, db_column='REC_TYPE'
    )
    subj_namf = models.CharField(
        max_length=45L, db_column='SUBJ_NAMF', blank=True
    )
    subj_naml = models.CharField(
        max_length=200L, db_column='SUBJ_NAML', blank=True
    )
    subj_nams = models.CharField(
        max_length=45L, db_column='SUBJ_NAMS', blank=True
    )
    subj_namt = models.CharField(
        max_length=45L, db_column='SUBJ_NAMT', blank=True
    )
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID')

    class Meta:
        db_table = 'LOTH_CD'


class LpayCd(CalAccessBaseModel):
    advan_amt = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='ADVAN_AMT', blank=True
    )
    advan_dscr = models.CharField(
        max_length=100L, db_column='ADVAN_DSCR', blank=True
    )
    amend_id = models.IntegerField(db_column='AMEND_ID')
    bakref_tid = models.CharField(
        max_length=20L, db_column='BAKREF_TID', blank=True
    )
    cum_total = models.DecimalField(
        decimal_places=2, max_digits=14, db_column='CUM_TOTAL'
    )
    emplr_adr1 = models.CharField(
        max_length=55L, db_column='EMPLR_ADR1', blank=True
    )
    emplr_adr2 = models.CharField(
        max_length=55L, db_column='EMPLR_ADR2', blank=True
    )
    emplr_city = models.CharField(
        max_length=30L, db_column='EMPLR_CITY', blank=True
    )
    emplr_id = models.CharField(
        max_length=9L, db_column='EMPLR_ID', blank=True
    )
    emplr_namf = models.CharField(
        max_length=45L, db_column='EMPLR_NAMF', blank=True
    )
    emplr_naml = models.CharField(max_length=200L, db_column='EMPLR_NAML')
    emplr_nams = models.CharField(
        max_length=10L, db_column='EMPLR_NAMS', blank=True
    )
    emplr_namt = models.CharField(
        max_length=10L, db_column='EMPLR_NAMT', blank=True
    )
    emplr_phon = models.CharField(
        max_length=20L, db_column='EMPLR_PHON', blank=True
    )
    emplr_st = models.CharField(
        max_length=2L, db_column='EMPLR_ST', blank=True
    )
    emplr_zip4 = models.CharField(
        max_length=10L, db_column='EMPLR_ZIP4', blank=True
    )
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    fees_amt = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='FEES_AMT', blank=True
    )
    filing_id = models.IntegerField(db_column='FILING_ID')
    form_type = models.CharField(max_length=7L, db_column='FORM_TYPE')
    lby_actvty = models.CharField(
        max_length=200L, db_column='LBY_ACTVTY', blank=True
    )
    line_item = models.IntegerField(db_column='LINE_ITEM')
    memo_code = models.CharField(
        max_length=1L, db_column='MEMO_CODE', blank=True
    )
    memo_refno = models.CharField(
        max_length=20L, db_column='MEMO_REFNO', blank=True
    )
    per_total = models.DecimalField(
        decimal_places=2, max_digits=14, db_column='PER_TOTAL'
    )
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE')
    reimb_amt = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='REIMB_AMT', blank=True
    )
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID')

    class Meta:
        db_table = 'LPAY_CD'


class NamesCd(CalAccessBaseModel):
    namid = models.IntegerField(db_column='NAMID')
    naml = models.CharField(max_length=200L, db_column='NAML')
    namf = models.CharField(max_length=50L, db_column='NAMF')
    namt = models.CharField(max_length=100L, db_column='NAMT', blank=True)
    nams = models.CharField(max_length=30L, db_column='NAMS', blank=True)
    moniker = models.CharField(max_length=30L, db_column='MONIKER', blank=True)
    moniker_pos = models.CharField(
        max_length=9L, db_column='MONIKER_POS', blank=True
    )
    namm = models.CharField(max_length=20L, db_column='NAMM', blank=True)
    fullname = models.CharField(max_length=200L, db_column='FULLNAME')
    naml_search = models.CharField(max_length=200L, db_column='NAML_SEARCH')

    class Meta:
        db_table = 'NAMES_CD'


class RcptCd(CalAccessBaseModel):
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
    ctrib_adr1 = models.CharField(
        max_length=55L, db_column='CTRIB_ADR1', blank=True
    )
    ctrib_adr2 = models.CharField(
        max_length=55L, db_column='CTRIB_ADR2', blank=True
    )
    ctrib_city = models.CharField(
        max_length=30L, db_column='CTRIB_CITY', blank=True
    )
    ctrib_dscr = models.CharField(
        max_length=90L, db_column='CTRIB_DSCR', blank=True
    )
    ctrib_emp = models.CharField(
        max_length=200L, db_column='CTRIB_EMP', blank=True
    )
    ctrib_namf = models.CharField(
        max_length=45L, db_column='CTRIB_NAMF', blank=True
    )
    ctrib_naml = models.CharField(max_length=200L, db_column='CTRIB_NAML')
    ctrib_nams = models.CharField(
        max_length=10L, db_column='CTRIB_NAMS', blank=True
    )
    ctrib_namt = models.CharField(
        max_length=10L, db_column='CTRIB_NAMT', blank=True
    )
    ctrib_occ = models.CharField(
        max_length=60L, db_column='CTRIB_OCC', blank=True
    )
    ctrib_self = models.CharField(
        max_length=1L, db_column='CTRIB_SELF', blank=True
    )
    ctrib_st = models.CharField(
        max_length=2L, db_column='CTRIB_ST', blank=True
    )
    ctrib_zip4 = models.CharField(
        max_length=10L, db_column='CTRIB_ZIP4', blank=True
    )
    cum_oth = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='CUM_OTH', blank=True
    )
    cum_ytd = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='CUM_YTD', blank=True
    )
    date_thru = models.DateField(null=True, db_column='DATE_THRU', blank=True)
    dist_no = models.CharField(max_length=3L, db_column='DIST_NO', blank=True)
    entity_cd = models.CharField(
        max_length=3L, db_column='ENTITY_CD', blank=True
    )
    filing_id = models.IntegerField(db_column='FILING_ID', db_index=True)
    form_type = models.CharField(max_length=9L, db_column='FORM_TYPE')
    int_rate = models.CharField(
        max_length=9L, db_column='INT_RATE', blank=True
    )
    intr_adr1 = models.CharField(
        max_length=55L, db_column='INTR_ADR1', blank=True
    )
    intr_adr2 = models.CharField(
        max_length=55L, db_column='INTR_ADR2', blank=True
    )
    intr_city = models.CharField(
        max_length=30L, db_column='INTR_CITY', blank=True
    )
    intr_cmteid = models.CharField(
        max_length=9L, db_column='INTR_CMTEID', blank=True
    )
    intr_emp = models.CharField(
        max_length=200L, db_column='INTR_EMP', blank=True
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
    intr_occ = models.CharField(
        max_length=60L, db_column='INTR_OCC', blank=True
    )
    intr_self = models.CharField(
        max_length=1L, db_column='INTR_SELF', blank=True
    )
    intr_st = models.CharField(max_length=2L, db_column='INTR_ST', blank=True)
    intr_zip4 = models.CharField(
        max_length=10L, db_column='INTR_ZIP4', blank=True
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
    rcpt_date = models.DateField(db_column='RCPT_DATE')
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE')
    sup_opp_cd = models.CharField(
        max_length=1L, db_column='SUP_OPP_CD', blank=True
    )
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID')
    tran_type = models.CharField(
        max_length=1L, db_column='TRAN_TYPE', blank=True
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
    tres_zip4 = models.IntegerField(
        null=True, db_column='TRES_ZIP4', blank=True
    )
    xref_match = models.CharField(
        max_length=1L, db_column='XREF_MATCH', blank=True
    )
    xref_schnm = models.CharField(
        max_length=2L, db_column='XREF_SCHNM', blank=True
    )

    class Meta:
        db_table = 'RCPT_CD'


class SmryCd(CalAccessBaseModel):
    filing_id = models.IntegerField(db_column='FILING_ID', db_index=True)
    amend_id = models.IntegerField(db_column='AMEND_ID', db_index=True)
    line_item = models.CharField(max_length=8L, db_column='LINE_ITEM')
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE')
    form_type = models.CharField(max_length=8L, db_column='FORM_TYPE')
    amount_a = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='AMOUNT_A', blank=True
    )
    amount_b = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='AMOUNT_B', blank=True
    )
    amount_c = models.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='AMOUNT_C', blank=True
    )
    elec_dt = models.DateField(null=True, db_column='ELEC_DT', blank=True)
    current_filing = models.CharField(max_length=1L, blank=True)

    class Meta:
        db_table = 'SMRY_CD'


class SpltCd(CalAccessBaseModel):
    amend_id = models.IntegerField(db_column='AMEND_ID')
    elec_amount = models.DecimalField(
        max_digits=16, decimal_places=2, db_column='ELEC_AMOUNT'
    )
    elec_code = models.CharField(
        max_length=2L, db_column='ELEC_CODE', blank=True
    )
    elec_date = models.DateField(db_column='ELEC_DATE')
    filing_id = models.IntegerField(db_column='FILING_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    pform_type = models.CharField(
        max_length=7L, db_column='PFORM_TYPE', blank=True
    )
    ptran_id = models.CharField(
        max_length=32L, db_column='PTRAN_ID', blank=True
    )

    class Meta:
        db_table = 'SPLT_CD'


class S401Cd(CalAccessBaseModel):
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
    # payee_adr1 = models.CharField(
    #   max_length=55L, db_column='PAYEE_ADR1', blank=True
    # )
    # payee_adr2 = models.CharField(
    #   max_length=55L, db_column='PAYEE_ADR2', blank=True
    # )
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
        db_table = 'S401_CD'


class S496Cd(CalAccessBaseModel):
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
    exp_date = models.DateField(db_column='EXP_DATE')
    expn_dscr = models.CharField(
        max_length=90L, db_column='EXPN_DSCR', blank=True
    )
    memo_code = models.CharField(
        max_length=1L, db_column='MEMO_CODE', blank=True
    )
    memo_refno = models.CharField(
        max_length=20L, db_column='MEMO_REFNO', blank=True
    )
    date_thru = models.DateField(db_column='DATE_THRU')

    class Meta:
        db_table = 'S496_CD'


class S497Cd(CalAccessBaseModel):
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
    # enty_adr1 = models.CharField(
    #   max_length=55L, db_column='ENTY_ADR1', blank=True
    # )
    # enty_adr2 = models.CharField(
    #    max_length=55L, db_column='ENTY_ADR2', blank=True
    # )
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
    elec_date = models.DateField(db_column='ELEC_DATE')
    ctrib_date = models.DateField(db_column='CTRIB_DATE')
    date_thru = models.DateField(db_column='DATE_THRU')
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
        db_table = 'S497_CD'


class S498Cd(CalAccessBaseModel):
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
    # payor_adr1 = models.CharField(
    #    max_length='', db_column='PAYOR_ADR1', blank=True
    # )
    # payor_adr2 = models.CharField(
    #    max_length='', db_column='PAYOR_ADR2', blank=True
    # )
    payor_city = models.CharField(
        max_length=30L, db_column='PAYOR_CITY', blank=True
    )
    payor_st = models.CharField(
        max_length=2L, db_column='PAYOR_ST', blank=True
    )
    payor_zip4 = models.CharField(
        max_length=10L, db_column='PAYOR_ZIP4', blank=True
    )
    date_rcvd = models.DateField(db_column='DATE_RCVD')
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
        db_table = 'S498_CD'
