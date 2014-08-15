class CvrSo(CalAccessBaseModel):
    DATE_FIELDS = [
        'ACCT_OPENDT',
        'QUALFY_DT',
    ]
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


class Cvr2SoCd(CalAccessBaseModel):
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
        db_table = 'CVR2_SO_CD'


class Cvr3VerificationInfoCd(CalAccessBaseModel):
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
        db_table = 'CVR3_VERIFICATION_INFO_CD'


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
    DATE_FIELDS = [
        'ELECT_DATE',
        'FROM_DATE',
        'RPT_DATE',
        'RPTFROMDT',
        'RPTTHRUDT',
        'THRU_DATE'
    ]
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
    DATE_FIELDS = ['EXPN_DATE', ]
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


class F495P2Cd(CalAccessBaseModel):
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
        db_table = 'F495P2_CD'


class S496Cd(CalAccessBaseModel):
    DATE_FIELDS = [
        'EXP_DATE',
        'DATE_THRU',
    ]
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
    DATE_FIELDS = [
        'ELEC_DATE',
        'CTRIB_DATE',
        'DATE_THRU',
    ]
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
    DATE_FIELDS = [
        'DATE_RCVD',
    ]
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
