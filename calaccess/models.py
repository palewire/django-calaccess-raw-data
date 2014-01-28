from __future__ import unicode_literals
from django.contrib.gis.db import models


class Cvr2CampaignDisclosureCd(models.Model):
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    bal_juris = models.CharField(max_length=40L, db_column='BAL_JURIS', blank=True) # Field name made lowercase.
    bal_name = models.CharField(max_length=200L, db_column='BAL_NAME', blank=True) # Field name made lowercase.
    bal_num = models.CharField(max_length=7L, db_column='BAL_NUM', blank=True) # Field name made lowercase.
    cmte_id = models.CharField(max_length=9L, db_column='CMTE_ID', blank=True) # Field name made lowercase.
    control_yn = models.IntegerField(null=True, db_column='CONTROL_YN', blank=True) # Field name made lowercase.
    dist_no = models.CharField(max_length=3L, db_column='DIST_NO', blank=True) # Field name made lowercase.
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD', blank=True) # Field name made lowercase.
    enty_adr1 = models.CharField(max_length=55L, db_column='ENTY_ADR1', blank=True) # Field name made lowercase.
    enty_adr2 = models.CharField(max_length=55L, db_column='ENTY_ADR2', blank=True) # Field name made lowercase.
    enty_city = models.CharField(max_length=30L, db_column='ENTY_CITY', blank=True) # Field name made lowercase.
    enty_email = models.CharField(max_length=60L, db_column='ENTY_EMAIL', blank=True) # Field name made lowercase.
    enty_fax = models.CharField(max_length=20L, db_column='ENTY_FAX', blank=True) # Field name made lowercase.
    enty_namf = models.CharField(max_length=45L, db_column='ENTY_NAMF', blank=True) # Field name made lowercase.
    enty_naml = models.CharField(max_length=200L, db_column='ENTY_NAML', blank=True) # Field name made lowercase.
    enty_nams = models.CharField(max_length=10L, db_column='ENTY_NAMS', blank=True) # Field name made lowercase.
    enty_namt = models.CharField(max_length=10L, db_column='ENTY_NAMT', blank=True) # Field name made lowercase.
    enty_phon = models.CharField(max_length=20L, db_column='ENTY_PHON', blank=True) # Field name made lowercase.
    enty_st = models.CharField(max_length=2L, db_column='ENTY_ST', blank=True) # Field name made lowercase.
    enty_zip4 = models.CharField(max_length=10L, db_column='ENTY_ZIP4', blank=True) # Field name made lowercase.
    f460_part = models.CharField(max_length=2L, db_column='F460_PART', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    form_type = models.CharField(max_length=4L, db_column='FORM_TYPE') # Field name made lowercase.
    juris_cd = models.CharField(max_length=3L, db_column='JURIS_CD', blank=True) # Field name made lowercase.
    juris_dscr = models.CharField(max_length=40L, db_column='JURIS_DSCR', blank=True) # Field name made lowercase.
    line_item = models.IntegerField(db_column='LINE_ITEM') # Field name made lowercase.
    mail_adr1 = models.CharField(max_length=55L, db_column='MAIL_ADR1', blank=True) # Field name made lowercase.
    mail_adr2 = models.CharField(max_length=55L, db_column='MAIL_ADR2', blank=True) # Field name made lowercase.
    mail_city = models.CharField(max_length=30L, db_column='MAIL_CITY', blank=True) # Field name made lowercase.
    mail_st = models.CharField(max_length=2L, db_column='MAIL_ST', blank=True) # Field name made lowercase.
    mail_zip4 = models.CharField(max_length=10L, db_column='MAIL_ZIP4', blank=True) # Field name made lowercase.
    off_s_h_cd = models.CharField(max_length=1L, db_column='OFF_S_H_CD', blank=True) # Field name made lowercase.
    offic_dscr = models.CharField(max_length=40L, db_column='OFFIC_DSCR', blank=True) # Field name made lowercase.
    office_cd = models.CharField(max_length=3L, db_column='OFFICE_CD', blank=True) # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE') # Field name made lowercase.
    sup_opp_cd = models.CharField(max_length=1L, db_column='SUP_OPP_CD', blank=True) # Field name made lowercase.
    title = models.CharField(max_length=90L, db_column='TITLE', blank=True) # Field name made lowercase.
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID') # Field name made lowercase.
    tres_namf = models.CharField(max_length=45L, db_column='TRES_NAMF', blank=True) # Field name made lowercase.
    tres_naml = models.CharField(max_length=200L, db_column='TRES_NAML', blank=True) # Field name made lowercase.
    tres_nams = models.CharField(max_length=10L, db_column='TRES_NAMS', blank=True) # Field name made lowercase.
    tres_namt = models.CharField(max_length=10L, db_column='TRES_NAMT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'CVR2_CAMPAIGN_DISCLOSURE_CD'

class CvrCampaignDisclosureCd(models.Model):
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    amendexp_1 = models.CharField(max_length=100L, db_column='AMENDEXP_1', blank=True) # Field name made lowercase.
    amendexp_2 = models.CharField(max_length=100L, db_column='AMENDEXP_2', blank=True) # Field name made lowercase.
    amendexp_3 = models.CharField(max_length=100L, db_column='AMENDEXP_3', blank=True) # Field name made lowercase.
    assoc_cb = models.CharField(max_length=4L, db_column='ASSOC_CB', blank=True) # Field name made lowercase.
    assoc_int = models.CharField(max_length=90L, db_column='ASSOC_INT', blank=True) # Field name made lowercase.
    bal_id = models.CharField(max_length=9L, db_column='BAL_ID', blank=True) # Field name made lowercase.
    bal_juris = models.CharField(max_length=40L, db_column='BAL_JURIS', blank=True) # Field name made lowercase.
    bal_name = models.CharField(max_length=200L, db_column='BAL_NAME', blank=True) # Field name made lowercase.
    bal_num = models.CharField(max_length=4L, db_column='BAL_NUM', blank=True) # Field name made lowercase.
    brdbase_yn = models.CharField(max_length=1L, db_column='BRDBASE_YN', blank=True) # Field name made lowercase.
    bus_adr1 = models.CharField(max_length=55L, db_column='BUS_ADR1', blank=True) # Field name made lowercase.
    bus_adr2 = models.CharField(max_length=55L, db_column='BUS_ADR2', blank=True) # Field name made lowercase.
    bus_city = models.CharField(max_length=30L, db_column='BUS_CITY', blank=True) # Field name made lowercase.
    bus_inter = models.CharField(max_length=40L, db_column='BUS_INTER', blank=True) # Field name made lowercase.
    bus_name = models.CharField(max_length=200L, db_column='BUS_NAME', blank=True) # Field name made lowercase.
    bus_st = models.CharField(max_length=2L, db_column='BUS_ST', blank=True) # Field name made lowercase.
    bus_zip4 = models.CharField(max_length=10, db_column='BUS_ZIP4', blank=True) # Field name made lowercase
    busact_cb = models.CharField(max_length=10L, db_column='BUSACT_CB', blank=True) # Field name made lowercase.
    busactvity = models.CharField(max_length=90L, db_column='BUSACTVITY', blank=True) # Field name made lowercase.
    cand_adr1 = models.CharField(max_length=55L, db_column='CAND_ADR1', blank=True) # Field name made lowercase.
    cand_adr2 = models.CharField(max_length=55L, db_column='CAND_ADR2', blank=True) # Field name made lowercase.
    cand_city = models.CharField(max_length=30L, db_column='CAND_CITY', blank=True) # Field name made lowercase.
    cand_email = models.CharField(max_length=60L, db_column='CAND_EMAIL', blank=True) # Field name made lowercase.
    cand_fax = models.CharField(max_length=20L, db_column='CAND_FAX', blank=True) # Field name made lowercase.
    cand_id = models.CharField(max_length=9L, db_column='CAND_ID', blank=True) # Field name made lowercase.
    cand_namf = models.CharField(max_length=45L, db_column='CAND_NAMF', blank=True) # Field name made lowercase.
    cand_naml = models.CharField(max_length=200L, db_column='CAND_NAML', blank=True) # Field name made lowercase.
    cand_nams = models.CharField(max_length=10L, db_column='CAND_NAMS', blank=True) # Field name made lowercase.
    cand_namt = models.CharField(max_length=10L, db_column='CAND_NAMT', blank=True) # Field name made lowercase.
    cand_phon = models.CharField(max_length=20L, db_column='CAND_PHON', blank=True) # Field name made lowercase.
    cand_st = models.CharField(max_length=4L, db_column='CAND_ST', blank=True) # Field name made lowercase.
    cand_zip4 = models.CharField(max_length=10L, db_column='CAND_ZIP4', blank=True) # Field name made lowercase.
    cmtte_id = models.CharField(max_length=9L, db_column='CMTTE_ID', blank=True) # Field name made lowercase.
    cmtte_type = models.CharField(max_length=1L, db_column='CMTTE_TYPE', blank=True) # Field name made lowercase.
    control_yn = models.IntegerField(null=True, db_column='CONTROL_YN', blank=True) # Field name made lowercase.
    dist_no = models.CharField(max_length=4L, db_column='DIST_NO', blank=True) # Field name made lowercase.
    elect_date = models.DateField(null=True, db_column='ELECT_DATE', blank=True) # Field name made lowercase.
    emplbus_cb = models.CharField(max_length=4L, db_column='EMPLBUS_CB', blank=True) # Field name made lowercase.
    employer = models.CharField(max_length=200L, db_column='EMPLOYER', blank=True) # Field name made lowercase.
    entity_cd = models.CharField(max_length=4L, db_column='ENTITY_CD', blank=True) # Field name made lowercase.
    file_email = models.CharField(max_length=60L, db_column='FILE_EMAIL', blank=True) # Field name made lowercase.
    filer_adr1 = models.CharField(max_length=55L, db_column='FILER_ADR1', blank=True) # Field name made lowercase.
    filer_adr2 = models.CharField(max_length=55L, db_column='FILER_ADR2', blank=True) # Field name made lowercase.
    filer_city = models.CharField(max_length=30L, db_column='FILER_CITY', blank=True) # Field name made lowercase.
    filer_fax = models.CharField(max_length=20L, db_column='FILER_FAX', blank=True) # Field name made lowercase.
    filer_id = models.IntegerField(db_column='FILER_ID') # Field name made lowercase.
    filer_namf = models.CharField(max_length=45L, db_column='FILER_NAMF', blank=True) # Field name made lowercase.
    filer_naml = models.CharField(max_length=200L, db_column='FILER_NAML') # Field name made lowercase.
    filer_nams = models.CharField(max_length=10L, db_column='FILER_NAMS', blank=True) # Field name made lowercase.
    filer_namt = models.CharField(max_length=10L, db_column='FILER_NAMT', blank=True) # Field name made lowercase.
    filer_phon = models.CharField(max_length=20L, db_column='FILER_PHON', blank=True) # Field name made lowercase.
    filer_st = models.CharField(max_length=4L, db_column='FILER_ST', blank=True) # Field name made lowercase.
    filer_zip4 = models.CharField(max_length=10L, db_column='FILER_ZIP4', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    form_type = models.CharField(max_length=4L, db_column='FORM_TYPE') # Field name made lowercase.
    from_date = models.DateField(null=True, db_column='FROM_DATE', blank=True) # Field name made lowercase.
    juris_cd = models.CharField(max_length=3L, db_column='JURIS_CD', blank=True) # Field name made lowercase.
    juris_dscr = models.CharField(max_length=40L, db_column='JURIS_DSCR', blank=True) # Field name made lowercase.
    late_rptno = models.CharField(max_length=30L, db_column='LATE_RPTNO', blank=True) # Field name made lowercase.
    mail_adr1 = models.CharField(max_length=55L, db_column='MAIL_ADR1', blank=True) # Field name made lowercase.
    mail_adr2 = models.CharField(max_length=55L, db_column='MAIL_ADR2', blank=True) # Field name made lowercase.
    mail_city = models.CharField(max_length=30L, db_column='MAIL_CITY', blank=True) # Field name made lowercase.
    mail_st = models.CharField(max_length=4L, db_column='MAIL_ST', blank=True) # Field name made lowercase.
    mail_zip4 = models.CharField(max_length=10L, db_column='MAIL_ZIP4', blank=True) # Field name made lowercase.
    occupation = models.CharField(max_length=60L, db_column='OCCUPATION', blank=True) # Field name made lowercase.
    off_s_h_cd = models.CharField(max_length=1L, db_column='OFF_S_H_CD', blank=True) # Field name made lowercase.
    offic_dscr = models.CharField(max_length=40L, db_column='OFFIC_DSCR', blank=True) # Field name made lowercase.
    office_cd = models.CharField(max_length=3L, db_column='OFFICE_CD', blank=True) # Field name made lowercase.
    other_cb = models.CharField(max_length=1L, db_column='OTHER_CB', blank=True) # Field name made lowercase.
    other_int = models.CharField(max_length=90L, db_column='OTHER_INT', blank=True) # Field name made lowercase.
    primfrm_yn = models.CharField(max_length=1L, db_column='PRIMFRM_YN', blank=True) # Field name made lowercase.
    rec_type = models.CharField(max_length=3L, db_column='REC_TYPE') # Field name made lowercase.
    report_num = models.CharField(max_length=3L, db_column='REPORT_NUM') # Field name made lowercase.
    reportname = models.CharField(max_length=3L, db_column='REPORTNAME', blank=True) # Field name made lowercase.
    rpt_att_cb = models.CharField(max_length=4L, db_column='RPT_ATT_CB', blank=True) # Field name made lowercase.
    rpt_date = models.DateField(db_column='RPT_DATE') # Field name made lowercase.
    rptfromdt = models.DateField(null=True, db_column='RPTFROMDT', blank=True) # Field name made lowercase.
    rptthrudt = models.DateField(null=True, db_column='RPTTHRUDT', blank=True) # Field name made lowercase.
    selfemp_cb = models.CharField(max_length=1L, db_column='SELFEMP_CB', blank=True) # Field name made lowercase.
    sponsor_yn = models.IntegerField(null=True, db_column='SPONSOR_YN', blank=True) # Field name made lowercase.
    stmt_type = models.CharField(max_length=2L, db_column='STMT_TYPE', blank=True) # Field name made lowercase.
    sup_opp_cd = models.CharField(max_length=1L, db_column='SUP_OPP_CD', blank=True) # Field name made lowercase.
    thru_date = models.DateField(null=True, db_column='THRU_DATE', blank=True) # Field name made lowercase.
    tres_adr1 = models.CharField(max_length=55L, db_column='TRES_ADR1', blank=True) # Field name made lowercase.
    tres_adr2 = models.CharField(max_length=55L, db_column='TRES_ADR2', blank=True) # Field name made lowercase.
    tres_city = models.CharField(max_length=30L, db_column='TRES_CITY', blank=True) # Field name made lowercase.
    tres_email = models.CharField(max_length=60L, db_column='TRES_EMAIL', blank=True) # Field name made lowercase.
    tres_fax = models.CharField(max_length=20L, db_column='TRES_FAX', blank=True) # Field name made lowercase.
    tres_namf = models.CharField(max_length=45L, db_column='TRES_NAMF', blank=True) # Field name made lowercase.
    tres_naml = models.CharField(max_length=200L, db_column='TRES_NAML', blank=True) # Field name made lowercase.
    tres_nams = models.CharField(max_length=10L, db_column='TRES_NAMS', blank=True) # Field name made lowercase.
    tres_namt = models.CharField(max_length=10L, db_column='TRES_NAMT', blank=True) # Field name made lowercase.
    tres_phon = models.CharField(max_length=20L, db_column='TRES_PHON', blank=True) # Field name made lowercase.
    tres_st = models.CharField(max_length=2L, db_column='TRES_ST', blank=True) # Field name made lowercase.
    tres_zip4 = models.CharField(max_length=10L, db_column='TRES_ZIP4', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'CVR_CAMPAIGN_DISCLOSURE_CD'

class CvrLobbyDisclosureCd(models.Model):
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    ctrib_n_cb = models.CharField(max_length=1L, db_column='CTRIB_N_CB', blank=True) # Field name made lowercase.
    ctrib_y_cb = models.CharField(max_length=1L, db_column='CTRIB_Y_CB', blank=True) # Field name made lowercase.
    cum_beg_dt = models.DateField(null=True, db_column='CUM_BEG_DT', blank=True) # Field name made lowercase.
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD', blank=True) # Field name made lowercase.
    filer_id = models.CharField(max_length=9L, db_column='FILER_ID') # Field name made lowercase.
    filer_namf = models.CharField(max_length=45L, db_column='FILER_NAMF', blank=True) # Field name made lowercase.
    filer_naml = models.CharField(max_length=200L, db_column='FILER_NAML') # Field name made lowercase.
    filer_nams = models.CharField(max_length=10L, db_column='FILER_NAMS', blank=True) # Field name made lowercase.
    filer_namt = models.CharField(max_length=10L, db_column='FILER_NAMT', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    firm_adr1 = models.CharField(max_length=55L, db_column='FIRM_ADR1', blank=True) # Field name made lowercase.
    firm_adr2 = models.CharField(max_length=55L, db_column='FIRM_ADR2', blank=True) # Field name made lowercase.
    firm_city = models.CharField(max_length=30L, db_column='FIRM_CITY', blank=True) # Field name made lowercase.
    firm_id = models.CharField(max_length=9L, db_column='FIRM_ID', blank=True) # Field name made lowercase.
    firm_name = models.CharField(max_length=200L, db_column='FIRM_NAME', blank=True) # Field name made lowercase.
    firm_phon = models.CharField(max_length=20L, db_column='FIRM_PHON', blank=True) # Field name made lowercase.
    firm_st = models.CharField(max_length=2L, db_column='FIRM_ST', blank=True) # Field name made lowercase.
    firm_zip4 = models.CharField(max_length=10L, db_column='FIRM_ZIP4', blank=True) # Field name made lowercase.
    form_type = models.CharField(max_length=4L, db_column='FORM_TYPE') # Field name made lowercase.
    from_date = models.DateField(db_column='FROM_DATE') # Field name made lowercase.
    lby_actvty = models.CharField(max_length=400L, db_column='LBY_ACTVTY', blank=True) # Field name made lowercase.
    lobby_n_cb = models.CharField(max_length=1L, db_column='LOBBY_N_CB', blank=True) # Field name made lowercase.
    lobby_y_cb = models.CharField(max_length=1L, db_column='LOBBY_Y_CB', blank=True) # Field name made lowercase.
    mail_adr1 = models.CharField(max_length=55L, db_column='MAIL_ADR1', blank=True) # Field name made lowercase.
    mail_adr2 = models.CharField(max_length=55L, db_column='MAIL_ADR2', blank=True) # Field name made lowercase.
    mail_city = models.CharField(max_length=30L, db_column='MAIL_CITY', blank=True) # Field name made lowercase.
    mail_phon = models.CharField(max_length=20L, db_column='MAIL_PHON', blank=True) # Field name made lowercase.
    mail_st = models.CharField(max_length=2L, db_column='MAIL_ST', blank=True) # Field name made lowercase.
    mail_zip4 = models.CharField(max_length=10L, db_column='MAIL_ZIP4', blank=True) # Field name made lowercase.
    major_namf = models.CharField(max_length=45L, db_column='MAJOR_NAMF', blank=True) # Field name made lowercase.
    major_naml = models.CharField(max_length=200L, db_column='MAJOR_NAML', blank=True) # Field name made lowercase.
    major_nams = models.CharField(max_length=10L, db_column='MAJOR_NAMS', blank=True) # Field name made lowercase.
    major_namt = models.CharField(max_length=10L, db_column='MAJOR_NAMT', blank=True) # Field name made lowercase.
    nopart1_cb = models.CharField(max_length=1L, db_column='NOPART1_CB', blank=True) # Field name made lowercase.
    nopart2_cb = models.CharField(max_length=1L, db_column='NOPART2_CB', blank=True) # Field name made lowercase.
    part1_1_cb = models.CharField(max_length=1L, db_column='PART1_1_CB', blank=True) # Field name made lowercase.
    part1_2_cb = models.CharField(max_length=1L, db_column='PART1_2_CB', blank=True) # Field name made lowercase.
    prn_namf = models.CharField(max_length=45L, db_column='PRN_NAMF', blank=True) # Field name made lowercase.
    prn_naml = models.CharField(max_length=200L, db_column='PRN_NAML', blank=True) # Field name made lowercase.
    prn_nams = models.CharField(max_length=10L, db_column='PRN_NAMS', blank=True) # Field name made lowercase.
    prn_namt = models.CharField(max_length=10L, db_column='PRN_NAMT', blank=True) # Field name made lowercase.
    rcpcmte_id = models.CharField(max_length=9L, db_column='RCPCMTE_ID', blank=True) # Field name made lowercase.
    rcpcmte_nm = models.CharField(max_length=200L, db_column='RCPCMTE_NM', blank=True) # Field name made lowercase.
    rec_type = models.CharField(max_length=3L, db_column='REC_TYPE') # Field name made lowercase.
    report_num = models.CharField(max_length=3L, db_column='REPORT_NUM') # Field name made lowercase.
    rpt_date = models.DateField(db_column='RPT_DATE') # Field name made lowercase.
    sender_id = models.CharField(max_length=9L, db_column='SENDER_ID') # Field name made lowercase.
    sig_date = models.DateField(db_column='SIG_DATE') # Field name made lowercase.
    sig_loc = models.CharField(max_length=45L, db_column='SIG_LOC', blank=True) # Field name made lowercase.
    sig_namf = models.CharField(max_length=45L, db_column='SIG_NAMF', blank=True) # Field name made lowercase.
    sig_naml = models.CharField(max_length=200L, db_column='SIG_NAML', blank=True) # Field name made lowercase.
    sig_nams = models.CharField(max_length=10L, db_column='SIG_NAMS', blank=True) # Field name made lowercase.
    sig_namt = models.CharField(max_length=10L, db_column='SIG_NAMT', blank=True) # Field name made lowercase.
    sig_title = models.CharField(max_length=45L, db_column='SIG_TITLE', blank=True) # Field name made lowercase.
    thru_date = models.DateField(db_column='THRU_DATE') # Field name made lowercase.
    class Meta:
        db_table = 'CVR_LOBBY_DISCLOSURE_CD'

class CvrRegistrationCd(models.Model):
    a_b_adr1 = models.CharField(max_length=55L, db_column='A_B_ADR1', blank=True) # Field name made lowercase.
    a_b_adr2 = models.CharField(max_length=55L, db_column='A_B_ADR2', blank=True) # Field name made lowercase.
    a_b_city = models.CharField(max_length=30L, db_column='A_B_CITY', blank=True) # Field name made lowercase.
    a_b_name = models.CharField(max_length=200L, db_column='A_B_NAME', blank=True) # Field name made lowercase.
    a_b_st = models.CharField(max_length=2L, db_column='A_B_ST', blank=True) # Field name made lowercase.
    a_b_zip4 = models.CharField(max_length=10L, db_column='A_B_ZIP4', blank=True) # Field name made lowercase.
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    auth_adr1 = models.CharField(max_length=55L, db_column='AUTH_ADR1', blank=True) # Field name made lowercase.
    auth_adr2 = models.CharField(max_length=55L, db_column='AUTH_ADR2', blank=True) # Field name made lowercase.
    auth_city = models.CharField(max_length=30L, db_column='AUTH_CITY', blank=True) # Field name made lowercase.
    auth_name = models.CharField(max_length=200L, db_column='AUTH_NAME', blank=True) # Field name made lowercase.
    auth_st = models.CharField(max_length=2L, db_column='AUTH_ST', blank=True) # Field name made lowercase.
    auth_zip4 = models.CharField(max_length=10L, db_column='AUTH_ZIP4', blank=True) # Field name made lowercase.
    bus_adr1 = models.CharField(max_length=55L, db_column='BUS_ADR1', blank=True) # Field name made lowercase.
    bus_adr2 = models.CharField(max_length=55L, db_column='BUS_ADR2', blank=True) # Field name made lowercase.
    bus_cb = models.CharField(max_length=1L, db_column='BUS_CB', blank=True) # Field name made lowercase.
    bus_city = models.CharField(max_length=30L, db_column='BUS_CITY') # Field name made lowercase.
    bus_class = models.CharField(max_length=3L, db_column='BUS_CLASS', blank=True) # Field name made lowercase.
    bus_descr = models.CharField(max_length=100L, db_column='BUS_DESCR', blank=True) # Field name made lowercase.
    bus_email = models.CharField(max_length=60L, db_column='BUS_EMAIL', blank=True) # Field name made lowercase.
    bus_fax = models.CharField(max_length=20L, db_column='BUS_FAX', blank=True) # Field name made lowercase.
    bus_phon = models.CharField(max_length=20L, db_column='BUS_PHON', blank=True) # Field name made lowercase.
    bus_st = models.CharField(max_length=2L, db_column='BUS_ST', blank=True) # Field name made lowercase.
    bus_zip4 = models.CharField(max_length=10L, db_column='BUS_ZIP4', blank=True) # Field name made lowercase.
    c_less50 = models.CharField(max_length=1L, db_column='C_LESS50', blank=True) # Field name made lowercase.
    c_more50 = models.CharField(max_length=1L, db_column='C_MORE50', blank=True) # Field name made lowercase.
    complet_dt = models.DateField(null=True, db_column='COMPLET_DT', blank=True) # Field name made lowercase.
    descrip_1 = models.CharField(max_length=300L, db_column='DESCRIP_1', blank=True) # Field name made lowercase.
    descrip_2 = models.CharField(max_length=300L, db_column='DESCRIP_2', blank=True) # Field name made lowercase.
    eff_date = models.DateField(null=True, db_column='EFF_DATE', blank=True) # Field name made lowercase.
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD', blank=True) # Field name made lowercase.
    filer_id = models.CharField(max_length=9L, db_column='FILER_ID') # Field name made lowercase.
    filer_namf = models.CharField(max_length=45L, db_column='FILER_NAMF', blank=True) # Field name made lowercase.
    filer_naml = models.CharField(max_length=200L, db_column='FILER_NAML', blank=True) # Field name made lowercase.
    filer_nams = models.CharField(max_length=10L, db_column='FILER_NAMS', blank=True) # Field name made lowercase.
    filer_namt = models.CharField(max_length=10L, db_column='FILER_NAMT', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(null=True, db_column='FILING_ID', blank=True) # Field name made lowercase.
    firm_name = models.CharField(max_length=200L, db_column='FIRM_NAME', blank=True) # Field name made lowercase.
    form_type = models.CharField(max_length=4L, db_column='FORM_TYPE', blank=True) # Field name made lowercase.
    ind_cb = models.CharField(max_length=1L, db_column='IND_CB', blank=True) # Field name made lowercase.
    ind_class = models.CharField(max_length=3L, db_column='IND_CLASS', blank=True) # Field name made lowercase.
    ind_descr = models.CharField(max_length=100L, db_column='IND_DESCR', blank=True) # Field name made lowercase.
    influen_yn = models.IntegerField(null=True, db_column='INFLUEN_YN', blank=True) # Field name made lowercase.
    l_firm_cb = models.CharField(max_length=1L, db_column='L_FIRM_CB', blank=True) # Field name made lowercase.
    lby_604_cb = models.CharField(max_length=1L, db_column='LBY_604_CB', blank=True) # Field name made lowercase.
    lby_reg_cb = models.CharField(max_length=1L, db_column='LBY_REG_CB', blank=True) # Field name made lowercase.
    lobby_cb = models.CharField(max_length=1L, db_column='LOBBY_CB', blank=True) # Field name made lowercase.
    lobby_int = models.CharField(max_length=300L, db_column='LOBBY_INT', blank=True) # Field name made lowercase.
    ls_beg_yr = models.IntegerField(null=True, db_column='LS_BEG_YR', blank=True) # Field name made lowercase.
    ls_end_yr = models.IntegerField(db_column='LS_END_YR') # Field name made lowercase.
    mail_adr1 = models.CharField(max_length=55L, db_column='MAIL_ADR1', blank=True) # Field name made lowercase.
    mail_adr2 = models.CharField(max_length=55L, db_column='MAIL_ADR2', blank=True) # Field name made lowercase.
    mail_city = models.CharField(max_length=30L, db_column='MAIL_CITY', blank=True) # Field name made lowercase.
    mail_phon = models.CharField(max_length=20L, db_column='MAIL_PHON', blank=True) # Field name made lowercase.
    mail_st = models.CharField(max_length=2L, db_column='MAIL_ST', blank=True) # Field name made lowercase.
    mail_zip4 = models.CharField(max_length=10L, db_column='MAIL_ZIP4', blank=True) # Field name made lowercase.
    newcert_cb = models.CharField(max_length=1L, db_column='NEWCERT_CB', blank=True) # Field name made lowercase.
    oth_cb = models.CharField(max_length=1L, db_column='OTH_CB', blank=True) # Field name made lowercase.
    prn_namf = models.CharField(max_length=45L, db_column='PRN_NAMF', blank=True) # Field name made lowercase.
    prn_naml = models.CharField(max_length=200L, db_column='PRN_NAML', blank=True) # Field name made lowercase.
    prn_nams = models.CharField(max_length=10L, db_column='PRN_NAMS', blank=True) # Field name made lowercase.
    prn_namt = models.CharField(max_length=10L, db_column='PRN_NAMT', blank=True) # Field name made lowercase.
    qual_date = models.DateField(null=True, db_column='QUAL_DATE', blank=True) # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE', blank=True) # Field name made lowercase.
    rencert_cb = models.CharField(max_length=1L, db_column='RENCERT_CB', blank=True) # Field name made lowercase.
    report_num = models.CharField(max_length=3L, db_column='REPORT_NUM', blank=True) # Field name made lowercase.
    rpt_date = models.DateField(db_column='RPT_DATE') # Field name made lowercase.
    sender_id = models.CharField(max_length=9L, db_column='SENDER_ID') # Field name made lowercase.
    sig_date = models.DateField(null=True, db_column='SIG_DATE', blank=True) # Field name made lowercase.
    sig_loc = models.CharField(max_length=45L, db_column='SIG_LOC', blank=True) # Field name made lowercase.
    sig_namf = models.CharField(max_length=45L, db_column='SIG_NAMF', blank=True) # Field name made lowercase.
    sig_naml = models.CharField(max_length=200L, db_column='SIG_NAML', blank=True) # Field name made lowercase.
    sig_nams = models.CharField(max_length=10L, db_column='SIG_NAMS', blank=True) # Field name made lowercase.
    sig_namt = models.CharField(max_length=10L, db_column='SIG_NAMT', blank=True) # Field name made lowercase.
    sig_title = models.CharField(max_length=45L, db_column='SIG_TITLE', blank=True) # Field name made lowercase.
    st_agency = models.CharField(max_length=100L, db_column='ST_AGENCY', blank=True) # Field name made lowercase.
    st_leg_yn = models.IntegerField(null=True, db_column='ST_LEG_YN', blank=True) # Field name made lowercase.
    stmt_firm = models.CharField(max_length=90L, db_column='STMT_FIRM', blank=True) # Field name made lowercase.
    trade_cb = models.CharField(max_length=1L, db_column='TRADE_CB', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'CVR_REGISTRATION_CD'

class DebtCd(models.Model):
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    amt_incur = models.DecimalField(decimal_places=2, max_digits=14, db_column='AMT_INCUR') # Field name made lowercase.
    amt_paid = models.DecimalField(decimal_places=2, max_digits=14, db_column='AMT_PAID') # Field name made lowercase.
    bakref_tid = models.CharField(max_length=20L, db_column='BAKREF_TID', blank=True) # Field name made lowercase.
    beg_bal = models.DecimalField(decimal_places=2, max_digits=14, db_column='BEG_BAL') # Field name made lowercase.
    cmte_id = models.CharField(max_length=9L, db_column='CMTE_ID', blank=True) # Field name made lowercase.
    end_bal = models.DecimalField(decimal_places=2, max_digits=14, db_column='END_BAL') # Field name made lowercase.
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD', blank=True) # Field name made lowercase.
    expn_code = models.CharField(max_length=3L, db_column='EXPN_CODE', blank=True) # Field name made lowercase.
    expn_dscr = models.CharField(max_length=400L, db_column='EXPN_DSCR', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    form_type = models.CharField(max_length=1L, db_column='FORM_TYPE') # Field name made lowercase.
    line_item = models.IntegerField(db_column='LINE_ITEM') # Field name made lowercase.
    memo_code = models.CharField(max_length=1L, db_column='MEMO_CODE', blank=True) # Field name made lowercase.
    memo_refno = models.CharField(max_length=20L, db_column='MEMO_REFNO', blank=True) # Field name made lowercase.
    payee_adr1 = models.CharField(max_length=55L, db_column='PAYEE_ADR1', blank=True) # Field name made lowercase.
    payee_adr2 = models.CharField(max_length=55L, db_column='PAYEE_ADR2', blank=True) # Field name made lowercase.
    payee_city = models.CharField(max_length=30L, db_column='PAYEE_CITY', blank=True) # Field name made lowercase.
    payee_namf = models.CharField(max_length=45L, db_column='PAYEE_NAMF', blank=True) # Field name made lowercase.
    payee_naml = models.CharField(max_length=200L, db_column='PAYEE_NAML') # Field name made lowercase.
    payee_nams = models.CharField(max_length=10L, db_column='PAYEE_NAMS', blank=True) # Field name made lowercase.
    payee_namt = models.CharField(max_length=100L, db_column='PAYEE_NAMT', blank=True) # Field name made lowercase.
    payee_st = models.CharField(max_length=2L, db_column='PAYEE_ST', blank=True) # Field name made lowercase.
    payee_zip4 = models.CharField(max_length=10L, db_column='PAYEE_ZIP4', blank=True) # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE') # Field name made lowercase.
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID') # Field name made lowercase.
    tres_adr1 = models.CharField(max_length=55L, db_column='TRES_ADR1', blank=True) # Field name made lowercase.
    tres_adr2 = models.CharField(max_length=55L, db_column='TRES_ADR2', blank=True) # Field name made lowercase.
    tres_city = models.CharField(max_length=30L, db_column='TRES_CITY', blank=True) # Field name made lowercase.
    tres_namf = models.CharField(max_length=45L, db_column='TRES_NAMF', blank=True) # Field name made lowercase.
    tres_naml = models.CharField(max_length=200L, db_column='TRES_NAML', blank=True) # Field name made lowercase.
    tres_nams = models.CharField(max_length=10L, db_column='TRES_NAMS', blank=True) # Field name made lowercase.
    tres_namt = models.CharField(max_length=100L, db_column='TRES_NAMT', blank=True) # Field name made lowercase.
    tres_st = models.CharField(max_length=2L, db_column='TRES_ST', blank=True) # Field name made lowercase.
    tres_zip4 = models.CharField(max_length=10L, db_column='TRES_ZIP4', blank=True) # Field name made lowercase.
    xref_match = models.CharField(max_length=1L, db_column='XREF_MATCH', blank=True) # Field name made lowercase.
    xref_schnm = models.CharField(max_length=2L, db_column='XREF_SCHNM', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'DEBT_CD'

class ExpnCd(models.Model):
    agent_namf = models.CharField(max_length=45L, db_column='AGENT_NAMF', blank=True) # Field name made lowercase.
    agent_naml = models.CharField(max_length=200L, db_column='AGENT_NAML', blank=True) # Field name made lowercase.
    agent_nams = models.CharField(max_length=10L, db_column='AGENT_NAMS', blank=True) # Field name made lowercase.
    agent_namt = models.CharField(max_length=10L, db_column='AGENT_NAMT', blank=True) # Field name made lowercase.
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    amount = models.DecimalField(decimal_places=2, max_digits=14, db_column='AMOUNT') # Field name made lowercase.
    bakref_tid = models.CharField(max_length=20L, db_column='BAKREF_TID', blank=True) # Field name made lowercase.
    bal_juris = models.CharField(max_length=40L, db_column='BAL_JURIS', blank=True) # Field name made lowercase.
    bal_name = models.CharField(max_length=200L, db_column='BAL_NAME', blank=True) # Field name made lowercase.
    bal_num = models.CharField(max_length=7L, db_column='BAL_NUM', blank=True) # Field name made lowercase.
    cand_namf = models.CharField(max_length=45L, db_column='CAND_NAMF', blank=True) # Field name made lowercase.
    cand_naml = models.CharField(max_length=200L, db_column='CAND_NAML', blank=True) # Field name made lowercase.
    cand_nams = models.CharField(max_length=10L, db_column='CAND_NAMS', blank=True) # Field name made lowercase.
    cand_namt = models.CharField(max_length=10L, db_column='CAND_NAMT', blank=True) # Field name made lowercase.
    cmte_id = models.CharField(max_length=9L, db_column='CMTE_ID', blank=True) # Field name made lowercase.
    cum_oth = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='CUM_OTH', blank=True) # Field name made lowercase.
    cum_ytd = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='CUM_YTD', blank=True) # Field name made lowercase.
    dist_no = models.CharField(max_length=3L, db_column='DIST_NO', blank=True) # Field name made lowercase.
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD', blank=True) # Field name made lowercase.
    expn_chkno = models.CharField(max_length=20L, db_column='EXPN_CHKNO', blank=True) # Field name made lowercase.
    expn_code = models.CharField(max_length=3L, db_column='EXPN_CODE', blank=True) # Field name made lowercase.
    expn_date = models.DateField(null=True, db_column='EXPN_DATE', blank=True) # Field name made lowercase.
    expn_dscr = models.CharField(max_length=400L, db_column='EXPN_DSCR', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    form_type = models.CharField(max_length=6L, db_column='FORM_TYPE') # Field name made lowercase.
    g_from_e_f = models.CharField(max_length=1L, db_column='G_FROM_E_F', blank=True) # Field name made lowercase.
    juris_cd = models.CharField(max_length=3L, db_column='JURIS_CD', blank=True) # Field name made lowercase.
    juris_dscr = models.CharField(max_length=40L, db_column='JURIS_DSCR', blank=True) # Field name made lowercase.
    line_item = models.IntegerField(db_column='LINE_ITEM') # Field name made lowercase.
    memo_code = models.CharField(max_length=1L, db_column='MEMO_CODE', blank=True) # Field name made lowercase.
    memo_refno = models.CharField(max_length=20L, db_column='MEMO_REFNO', blank=True) # Field name made lowercase.
    off_s_h_cd = models.CharField(max_length=1L, db_column='OFF_S_H_CD', blank=True) # Field name made lowercase.
    offic_dscr = models.CharField(max_length=40L, db_column='OFFIC_DSCR', blank=True) # Field name made lowercase.
    office_cd = models.CharField(max_length=3L, db_column='OFFICE_CD', blank=True) # Field name made lowercase.
    payee_adr1 = models.CharField(max_length=55L, db_column='PAYEE_ADR1', blank=True) # Field name made lowercase.
    payee_adr2 = models.CharField(max_length=55L, db_column='PAYEE_ADR2', blank=True) # Field name made lowercase.
    payee_city = models.CharField(max_length=30L, db_column='PAYEE_CITY', blank=True) # Field name made lowercase.
    payee_namf = models.CharField(max_length=45L, db_column='PAYEE_NAMF', blank=True) # Field name made lowercase.
    payee_naml = models.CharField(max_length=200L, db_column='PAYEE_NAML', blank=True) # Field name made lowercase.
    payee_nams = models.CharField(max_length=10L, db_column='PAYEE_NAMS', blank=True) # Field name made lowercase.
    payee_namt = models.CharField(max_length=10L, db_column='PAYEE_NAMT', blank=True) # Field name made lowercase.
    payee_st = models.CharField(max_length=2L, db_column='PAYEE_ST', blank=True) # Field name made lowercase.
    payee_zip4 = models.CharField(max_length=10L, db_column='PAYEE_ZIP4', blank=True) # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE') # Field name made lowercase.
    sup_opp_cd = models.CharField(max_length=1L, db_column='SUP_OPP_CD', blank=True) # Field name made lowercase.
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID') # Field name made lowercase.
    tres_adr1 = models.CharField(max_length=55L, db_column='TRES_ADR1', blank=True) # Field name made lowercase.
    tres_adr2 = models.CharField(max_length=55L, db_column='TRES_ADR2', blank=True) # Field name made lowercase.
    tres_city = models.CharField(max_length=30L, db_column='TRES_CITY', blank=True) # Field name made lowercase.
    tres_namf = models.CharField(max_length=45L, db_column='TRES_NAMF', blank=True) # Field name made lowercase.
    tres_naml = models.CharField(max_length=200L, db_column='TRES_NAML', blank=True) # Field name made lowercase.
    tres_nams = models.CharField(max_length=10L, db_column='TRES_NAMS', blank=True) # Field name made lowercase.
    tres_namt = models.CharField(max_length=10L, db_column='TRES_NAMT', blank=True) # Field name made lowercase.
    tres_st = models.CharField(max_length=2L, db_column='TRES_ST', blank=True) # Field name made lowercase.
    tres_zip4 = models.CharField(max_length=10L, db_column='TRES_ZIP4', blank=True) # Field name made lowercase.
    xref_match = models.CharField(max_length=1L, db_column='XREF_MATCH', blank=True) # Field name made lowercase.
    xref_schnm = models.CharField(max_length=2L, db_column='XREF_SCHNM', blank=True) # Field name made lowercase.
    current_filing = models.CharField(max_length=1L, blank=True)
    class Meta:
        db_table = 'EXPN_CD'

class FilernameCd(models.Model):
    xref_filer_id = models.CharField(max_length=7L, db_column='XREF_FILER_ID') # Field name made lowercase.
    filer_id = models.IntegerField(db_column='FILER_ID') # Field name made lowercase.
    filer_type = models.CharField(max_length=45L, db_column='FILER_TYPE') # Field name made lowercase.
    status = models.CharField(max_length=10L, db_column='STATUS') # Field name made lowercase.
    effect_dt = models.DateField(db_column='EFFECT_DT') # Field name made lowercase.
    naml = models.CharField(max_length=200L, db_column='NAML') # Field name made lowercase.
    namf = models.CharField(max_length=55L, db_column='NAMF', blank=True) # Field name made lowercase.
    namt = models.CharField(max_length=28L, db_column='NAMT', blank=True) # Field name made lowercase.
    nams = models.CharField(max_length=32L, db_column='NAMS', blank=True) # Field name made lowercase.
    adr1 = models.CharField(max_length=200L, db_column='ADR1', blank=True) # Field name made lowercase.
    adr2 = models.CharField(max_length=200L, db_column='ADR2', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=55L, db_column='CITY', blank=True) # Field name made lowercase.
    st = models.CharField(max_length=4L, db_column='ST', blank=True) # Field name made lowercase.
    zip4 = models.CharField(max_length=10L, db_column='ZIP4', blank=True) # Field name made lowercase.
    phon = models.CharField(max_length=60L, db_column='PHON', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=60L, db_column='FAX', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=60L, db_column='EMAIL', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'FILERNAME_CD'

class FilersCd(models.Model):
    filer_id = models.IntegerField(db_column='FILER_ID') # Field name made lowercase.
    class Meta:
        db_table = 'FILERS_CD'

class FilerAcronymsCd(models.Model):
    acronym = models.CharField(max_length=32L)
    filer_id = models.IntegerField()
    class Meta:
        db_table = 'FILER_ACRONYMS_CD'

class FilerFilingsCd(models.Model):
    filer_id = models.IntegerField(db_column='FILER_ID') # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    period_id = models.IntegerField(null=True, db_column='PERIOD_ID', blank=True) # Field name made lowercase.
    form_id = models.CharField(max_length=7L, db_column='FORM_ID') # Field name made lowercase.
    filing_sequence = models.IntegerField(db_column='FILING_SEQUENCE') # Field name made lowercase.
    filing_date = models.DateField(db_column='FILING_DATE') # Field name made lowercase.
    stmnt_type = models.IntegerField(db_column='STMNT_TYPE') # Field name made lowercase.
    stmnt_status = models.IntegerField(db_column='STMNT_STATUS') # Field name made lowercase.
    session_id = models.IntegerField(db_column='SESSION_ID') # Field name made lowercase.
    user_id = models.CharField(max_length=12L, db_column='USER_ID') # Field name made lowercase.
    special_audit = models.IntegerField(null=True, db_column='SPECIAL_AUDIT', blank=True) # Field name made lowercase.
    fine_audit = models.IntegerField(null=True, db_column='FINE_AUDIT', blank=True) # Field name made lowercase.
    rpt_start = models.DateField(null=True, db_column='RPT_START', blank=True) # Field name made lowercase.
    rpt_end = models.DateField(null=True, db_column='RPT_END', blank=True) # Field name made lowercase.
    rpt_date = models.DateField(null=True, db_column='RPT_DATE', blank=True) # Field name made lowercase.
    filing_type = models.IntegerField(null=True, db_column='FILING_TYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'FILER_FILINGS_CD'

class FilerInterestsCd(models.Model):
    filer_id = models.IntegerField(db_column='FILER_ID') # Field name made lowercase.
    session_id = models.IntegerField(db_column='SESSION_ID') # Field name made lowercase.
    interest_cd = models.IntegerField(db_column='INTEREST_CD') # Field name made lowercase.
    effect_date = models.DateTimeField(db_column='EFFECT_DATE') # Field name made lowercase.
    class Meta:
        db_table = 'FILER_INTERESTS_CD'

class FilerLinksCd(models.Model):
    filer_id_a = models.IntegerField(db_column='FILER_ID_A') # Field name made lowercase.
    filer_id_b = models.IntegerField(db_column='FILER_ID_B') # Field name made lowercase.
    active_flg = models.CharField(max_length=1L, db_column='ACTIVE_FLG') # Field name made lowercase.
    session_id = models.IntegerField(db_column='SESSION_ID') # Field name made lowercase.
    link_type = models.IntegerField(db_column='LINK_TYPE') # Field name made lowercase.
    link_desc = models.CharField(max_length=255L, db_column='LINK_DESC', blank=True) # Field name made lowercase.
    effect_dt = models.DateField(db_column='EFFECT_DT') # Field name made lowercase.
    dominate_filer = models.CharField(max_length=1L, db_column='DOMINATE_FILER', blank=True) # Field name made lowercase.
    termination_dt = models.DateField(null=True, db_column='TERMINATION_DT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'FILER_LINKS_CD'

class FilerStatusTypesCd(models.Model):
    status_type = models.CharField(max_length=11L, db_column='STATUS_TYPE') # Field name made lowercase.
    status_desc = models.CharField(max_length=11L, db_column='STATUS_DESC') # Field name made lowercase.
    class Meta:
        db_table = 'FILER_STATUS_TYPES_CD'

class FilerToFilerTypeCd(models.Model):
    filer_id = models.IntegerField(db_column='FILER_ID') # Field name made lowercase.
    filer_type = models.IntegerField(db_column='FILER_TYPE') # Field name made lowercase.
    active = models.CharField(max_length=1L, db_column='ACTIVE') # Field name made lowercase.
    race = models.IntegerField(null=True, db_column='RACE', blank=True) # Field name made lowercase.
    session_id = models.IntegerField(db_column='SESSION_ID') # Field name made lowercase.
    category = models.IntegerField(null=True, db_column='CATEGORY', blank=True) # Field name made lowercase.
    category_type = models.IntegerField(null=True, db_column='CATEGORY_TYPE', blank=True) # Field name made lowercase.
    sub_category = models.IntegerField(null=True, db_column='SUB_CATEGORY', blank=True) # Field name made lowercase.
    effect_dt = models.DateField(db_column='EFFECT_DT') # Field name made lowercase.
    sub_category_type = models.IntegerField(null=True, db_column='SUB_CATEGORY_TYPE', blank=True) # Field name made lowercase.
    election_type = models.IntegerField(null=True, db_column='ELECTION_TYPE', blank=True) # Field name made lowercase.
    sub_category_a = models.CharField(max_length=1L, db_column='SUB_CATEGORY_A', blank=True) # Field name made lowercase.
    nyq_dt = models.DateField(null=True, db_column='NYQ_DT', blank=True) # Field name made lowercase.
    party_cd = models.IntegerField(null=True, db_column='PARTY_CD', blank=True) # Field name made lowercase.
    county_cd = models.IntegerField(null=True, db_column='COUNTY_CD', blank=True) # Field name made lowercase.
    district_cd = models.IntegerField(null=True, db_column='DISTRICT_CD', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'FILER_TO_FILER_TYPE_CD'

class FilerTypesCd(models.Model):
    filer_type = models.IntegerField(db_column='FILER_TYPE') # Field name made lowercase.
    description = models.CharField(max_length=255L, db_column='DESCRIPTION') # Field name made lowercase.
    grp_type = models.IntegerField(null=True, db_column='GRP_TYPE', blank=True) # Field name made lowercase.
    calc_use = models.CharField(max_length=1L, db_column='CALC_USE', blank=True) # Field name made lowercase.
    grace_period = models.CharField(max_length=12L, db_column='GRACE_PERIOD', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'FILER_TYPES_CD'

class FilerXrefCd(models.Model):
    filer_id = models.IntegerField(db_column='FILER_ID') # Field name made lowercase.
    xref_id = models.CharField(max_length=32L, db_column='XREF_ID') # Field name made lowercase.
    effect_dt = models.DateField(db_column='EFFECT_DT') # Field name made lowercase.
    migration_source = models.CharField(max_length=50L, db_column='MIGRATION_SOURCE') # Field name made lowercase.
    class Meta:
        db_table = 'FILER_XREF_CD'

class Filings(models.Model):
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    filing_type = models.IntegerField(db_column='FILING_TYPE') # Field name made lowercase.
    class Meta:
        db_table = 'FILINGS'

class FilingPeriodCd(models.Model):
    period_id = models.IntegerField(db_column='PERIOD_ID') # Field name made lowercase.
    start_date = models.DateField(db_column='START_DATE') # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE') # Field name made lowercase.
    period_type = models.IntegerField(db_column='PERIOD_TYPE') # Field name made lowercase.
    per_grp_type = models.IntegerField(db_column='PER_GRP_TYPE') # Field name made lowercase.
    period_desc = models.CharField(max_length=255L, db_column='PERIOD_DESC') # Field name made lowercase.
    deadline = models.DateField(db_column='DEADLINE') # Field name made lowercase.
    class Meta:
        db_table = 'FILING_PERIOD_CD'

class HdrCd(models.Model):
    amend_id = models.IntegerField(db_column='AMEND_ID')
    cal_ver = models.CharField(max_length=4L, db_column='CAL_VER', blank=True)
    ef_type = models.CharField(max_length=3L, db_column='EF_TYPE', blank=True)
    filing_id = models.IntegerField(db_column='FILING_ID')
    hdr_comment = models.CharField(max_length=200L, db_column='HDRCOMMENT', blank=True)
    rec_type = models.CharField(max_length=3L, db_column='REC_TYPE', blank=True)
    soft_name = models.CharField(max_length=90L, db_column='SOFT_NAME', blank=True)
    soft_ver = models.CharField(max_length=16L, db_column='SOFT_VER', blank=True)
    state_cd = models.CharField(max_length=2L, db_column='STATE_CD', blank=True)
    class Meta:
        db_table = 'HDR_CD'

class LattCd(models.Model):
    amend_id = models.IntegerField(db_column='AMEND_ID')
    amount = models.DecimalField(max_digits=16, decimal_places=2, db_column='AMOUNT')
    cum_amt = models.DecimalField(max_digits=16, decimal_places=2, db_column='CUM_AMT')
    cumbeg_dt = models.DateField(db_column='CUMBEG_DT')
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD', blank=True)
    filing_id = models.IntegerField(db_column='FILING_ID')
    form_type = models.CharField(max_length=6L, db_column='FORM_TYPE')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    memo_code = models.CharField(max_length=1L, db_column='MEMO_CODE', blank=True)
    memo_refno = models.CharField(max_length=20L, db_column='MEMO_REFNO', blank=True)
    pmt_date = models.DateField(db_column='PMT_DATE')
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE', blank=True)
    recip_adr1 = models.CharField(max_length=55L, db_column='RECIP_ADR1', blank=True)
    recip_adr2 = models.CharField(max_length=55L, db_column='RECIP_ADR2', blank=True)
    recip_city = models.CharField(max_length=30L, db_column='RECIP_CITY', blank=True)
    recip_namf = models.CharField(max_length=45L, db_column='RECIP_NAMF', blank=True)
    recip_naml = models.CharField(max_length=200L, db_column='RECIP_NAML', blank=True)
    recip_nams = models.CharField(max_length=10L, db_column='RECIP_NAMS', blank=True)
    recip_namt = models.CharField(max_length=10L, db_column='RECIP_NAMT', blank=True)
    recip_st = models.CharField(max_length=2L, db_column='RECIP_ST', blank=True)
    recip_zip4 = models.CharField(max_length=10L, db_column='RECIP_ZIP4', blank=True)
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID', blank=True)
    class Meta:
        db_table = 'LATT_CD'

class LccmCd(models.Model):
    acct_name = models.CharField(max_length=90L, db_column='ACCT_NAME', blank=True)
    amend_id = models.IntegerField(db_column='AMEND_ID')
    amount = models.DecimalField(max_digits=16, decimal_places=2, db_column='AMOUNT')
    bakref_tid = models.CharField(max_length=20L, db_column='BAKREF_TID', blank=True)
    ctrib_date = models.DateField(db_column='CTRIB_DATE')
    ctrib_namf = models.CharField(max_length=45L, db_column='CTRIB_NAMF', blank=True)
    ctrib_naml = models.CharField(max_length=45L, db_column='CTRIB_NAML', blank=True)
    ctrib_nams = models.CharField(max_length=10L, db_column='CTRIB_NAMS', blank=True)
    ctrib_namt = models.CharField(max_length=10L, db_column='CTRIB_NAMT', blank=True)
    entity_cd = models.CharField(max_length=3, db_column='ENTITY_CD', blank=True)
    filing_id = models.IntegerField(db_column='FILING_ID')
    form_type = models.CharField(max_length=7L, db_column='FORM_TYPE', blank=True)
    line_item = models.IntegerField(db_column='LINE_ITEM')
    memo_code = models.CharField(max_length=1L, db_column='MEMO_CODE', blank=True)
    memo_refno = models.CharField(max_length=20L, db_column='MEMO_REFNO', blank=True)
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE', blank=True)
    recip_adr1 = models.CharField(max_length=55L, db_column='RECIP_ADR1', blank=True)
    recip_adr2 = models.CharField(max_length=55L, db_column='RECIP_ADR2', blank=True)
    recip_city = models.CharField(max_length=30L, db_column='RECIP_CITY', blank=True)
    recip_id = models.CharField(max_length=9L, db_column='RECIP_ID', blank=True)
    recip_namf = models.CharField(max_length=45L, db_column='RECIP_NAMF', blank=True)
    recip_naml = models.CharField(max_length=200L, db_column='RECIP_NAML', blank=True)
    recip_nams = models.CharField(max_length=10L, db_column='RECIP_NAMS', blank=True)
    recip_namt = models.CharField(max_length=10L, db_column='RECIP_NAMT', blank=True)
    recip_st = models.CharField(max_length=2L, db_column='RECIP_ST', blank=True)
    recip_zip4 = models.CharField(max_length=10L, db_column='RECIP_ZIP4', blank=True)
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID', blank=True)
    class Meta:
        db_table = 'LCCM_CD'

class LempCd(models.Model):
    agencylist = models.CharField(max_length=200L, db_column='AGENCYLIST', blank=True) # Field name made lowercase.
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    cli_adr1 = models.CharField(max_length=55L, db_column='CLI_ADR1', blank=True) # Field name made lowercase.
    cli_adr2 = models.CharField(max_length=55L, db_column='CLI_ADR2', blank=True) # Field name made lowercase.
    cli_city = models.CharField(max_length=30L, db_column='CLI_CITY') # Field name made lowercase.
    cli_namf = models.CharField(max_length=45L, db_column='CLI_NAMF', blank=True) # Field name made lowercase.
    cli_naml = models.CharField(max_length=200L, db_column='CLI_NAML') # Field name made lowercase.
    cli_nams = models.CharField(max_length=10L, db_column='CLI_NAMS', blank=True) # Field name made lowercase.
    cli_namt = models.CharField(max_length=10L, db_column='CLI_NAMT', blank=True) # Field name made lowercase.
    cli_phon = models.CharField(max_length=20L, db_column='CLI_PHON', blank=True) # Field name made lowercase.
    cli_st = models.CharField(max_length=2L, db_column='CLI_ST', blank=True) # Field name made lowercase.
    cli_zip4 = models.CharField(max_length=10L, db_column='CLI_ZIP4') # Field name made lowercase.
    client_id = models.CharField(max_length=9L, db_column='CLIENT_ID', blank=True) # Field name made lowercase.
    con_period = models.CharField(max_length=30L, db_column='CON_PERIOD', blank=True) # Field name made lowercase.
    descrip = models.CharField(max_length=100L, db_column='DESCRIP', blank=True) # Field name made lowercase.
    eff_date = models.DateField(null=True, db_column='EFF_DATE', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    form_type = models.CharField(max_length=7L, db_column='FORM_TYPE') # Field name made lowercase.
    line_item = models.IntegerField(db_column='LINE_ITEM') # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE') # Field name made lowercase.
    sub_adr1 = models.CharField(max_length=55L, db_column='SUB_ADR1', blank=True) # Field name made lowercase.
    sub_adr2 = models.CharField(max_length=55L, db_column='SUB_ADR2', blank=True) # Field name made lowercase.
    sub_city = models.CharField(max_length=30L, db_column='SUB_CITY', blank=True) # Field name made lowercase.
    sub_name = models.CharField(max_length=200L, db_column='SUB_NAME', blank=True) # Field name made lowercase.
    sub_phon = models.CharField(max_length=20L, db_column='SUB_PHON', blank=True) # Field name made lowercase.
    sub_st = models.CharField(max_length=2L, db_column='SUB_ST', blank=True) # Field name made lowercase.
    sub_zip4 = models.CharField(max_length=10L, db_column='SUB_ZIP4', blank=True) # Field name made lowercase.
    subfirm_id = models.CharField(max_length=9L, db_column='SUBFIRM_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'LEMP_CD'

class LexpCd(models.Model):
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    amount = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='AMOUNT', blank=True) # Field name made lowercase.
    bakref_tid = models.CharField(max_length=20L, db_column='BAKREF_TID', blank=True) # Field name made lowercase.
    bene_amt = models.CharField(max_length=12L, db_column='BENE_AMT', blank=True) # Field name made lowercase.
    bene_name = models.CharField(max_length=90L, db_column='BENE_NAME', blank=True) # Field name made lowercase.
    bene_posit = models.CharField(max_length=90L, db_column='BENE_POSIT', blank=True) # Field name made lowercase.
    credcardco = models.CharField(max_length=200L, db_column='CREDCARDCO', blank=True) # Field name made lowercase.
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD') # Field name made lowercase.
    expn_date = models.DateField(null=True, db_column='EXPN_DATE', blank=True) # Field name made lowercase.
    expn_dscr = models.CharField(max_length=90L, db_column='EXPN_DSCR', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    form_type = models.CharField(max_length=7L, db_column='FORM_TYPE') # Field name made lowercase.
    line_item = models.IntegerField(db_column='LINE_ITEM') # Field name made lowercase.
    memo_code = models.CharField(max_length=1L, db_column='MEMO_CODE', blank=True) # Field name made lowercase.
    memo_refno = models.CharField(max_length=20L, db_column='MEMO_REFNO', blank=True) # Field name made lowercase.
    payee_adr1 = models.CharField(max_length=55L, db_column='PAYEE_ADR1', blank=True) # Field name made lowercase.
    payee_adr2 = models.CharField(max_length=55L, db_column='PAYEE_ADR2', blank=True) # Field name made lowercase.
    payee_city = models.CharField(max_length=30L, db_column='PAYEE_CITY', blank=True) # Field name made lowercase.
    payee_namf = models.CharField(max_length=45L, db_column='PAYEE_NAMF', blank=True) # Field name made lowercase.
    payee_naml = models.CharField(max_length=200L, db_column='PAYEE_NAML', blank=True) # Field name made lowercase.
    payee_nams = models.CharField(max_length=10L, db_column='PAYEE_NAMS', blank=True) # Field name made lowercase.
    payee_namt = models.CharField(max_length=10L, db_column='PAYEE_NAMT', blank=True) # Field name made lowercase.
    payee_st = models.CharField(max_length=2L, db_column='PAYEE_ST', blank=True) # Field name made lowercase.
    payee_zip4 = models.CharField(max_length=10L, db_column='PAYEE_ZIP4', blank=True) # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE') # Field name made lowercase.
    recsubtype = models.CharField(max_length=1L, db_column='RECSUBTYPE') # Field name made lowercase.
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID') # Field name made lowercase.
    class Meta:
        db_table = 'LEXP_CD'

class LoanCd(models.Model):
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    bakref_tid = models.CharField(max_length=20L, db_column='BAKREF_TID', blank=True) # Field name made lowercase.
    cmte_id = models.CharField(max_length=9L, db_column='CMTE_ID', blank=True) # Field name made lowercase.
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    form_type = models.CharField(max_length=2L, db_column='FORM_TYPE') # Field name made lowercase.
    intr_adr1 = models.CharField(max_length=55L, db_column='INTR_ADR1', blank=True) # Field name made lowercase.
    intr_adr2 = models.CharField(max_length=55L, db_column='INTR_ADR2', blank=True) # Field name made lowercase.
    intr_city = models.CharField(max_length=30L, db_column='INTR_CITY', blank=True) # Field name made lowercase.
    intr_namf = models.CharField(max_length=45L, db_column='INTR_NAMF', blank=True) # Field name made lowercase.
    intr_naml = models.CharField(max_length=200L, db_column='INTR_NAML', blank=True) # Field name made lowercase.
    intr_nams = models.CharField(max_length=10L, db_column='INTR_NAMS', blank=True) # Field name made lowercase.
    intr_namt = models.CharField(max_length=10L, db_column='INTR_NAMT', blank=True) # Field name made lowercase.
    intr_st = models.CharField(max_length=2L, db_column='INTR_ST', blank=True) # Field name made lowercase.
    intr_zip4 = models.CharField(max_length=10L, db_column='INTR_ZIP4', blank=True) # Field name made lowercase.
    line_item = models.IntegerField(db_column='LINE_ITEM') # Field name made lowercase.
    lndr_namf = models.CharField(max_length=45L, db_column='LNDR_NAMF', blank=True) # Field name made lowercase.
    lndr_naml = models.CharField(max_length=200L, db_column='LNDR_NAML') # Field name made lowercase.
    lndr_nams = models.CharField(max_length=10L, db_column='LNDR_NAMS', blank=True) # Field name made lowercase.
    lndr_namt = models.CharField(max_length=10L, db_column='LNDR_NAMT', blank=True) # Field name made lowercase.
    loan_adr1 = models.CharField(max_length=55L, db_column='LOAN_ADR1', blank=True) # Field name made lowercase.
    loan_adr2 = models.CharField(max_length=55L, db_column='LOAN_ADR2', blank=True) # Field name made lowercase.
    loan_amt1 = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='LOAN_AMT1', blank=True) # Field name made lowercase.
    loan_amt2 = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='LOAN_AMT2', blank=True) # Field name made lowercase.
    loan_amt3 = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='LOAN_AMT3', blank=True) # Field name made lowercase.
    loan_amt4 = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='LOAN_AMT4', blank=True) # Field name made lowercase.
    loan_amt5 = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='LOAN_AMT5', blank=True) # Field name made lowercase.
    loan_amt6 = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='LOAN_AMT6', blank=True) # Field name made lowercase.
    loan_amt7 = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='LOAN_AMT7', blank=True) # Field name made lowercase.
    loan_amt8 = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='LOAN_AMT8', blank=True) # Field name made lowercase.
    loan_city = models.CharField(max_length=30L, db_column='LOAN_CITY', blank=True) # Field name made lowercase.
    loan_date1 = models.DateField(db_column='LOAN_DATE1') # Field name made lowercase.
    loan_date2 = models.DateField(null=True, db_column='LOAN_DATE2', blank=True) # Field name made lowercase.
    loan_emp = models.CharField(max_length=200L, db_column='LOAN_EMP', blank=True) # Field name made lowercase.
    loan_occ = models.CharField(max_length=60L, db_column='LOAN_OCC', blank=True) # Field name made lowercase.
    loan_rate = models.CharField(max_length=30L, db_column='LOAN_RATE', blank=True) # Field name made lowercase.
    loan_self = models.CharField(max_length=1L, db_column='LOAN_SELF', blank=True) # Field name made lowercase.
    loan_st = models.CharField(max_length=2L, db_column='LOAN_ST', blank=True) # Field name made lowercase.
    loan_type = models.CharField(max_length=3L, db_column='LOAN_TYPE', blank=True) # Field name made lowercase.
    loan_zip4 = models.CharField(max_length=10L, db_column='LOAN_ZIP4', blank=True) # Field name made lowercase.
    memo_code = models.CharField(max_length=1L, db_column='MEMO_CODE', blank=True) # Field name made lowercase.
    memo_refno = models.CharField(max_length=20L, db_column='MEMO_REFNO', blank=True) # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE') # Field name made lowercase.
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID') # Field name made lowercase.
    tres_adr1 = models.CharField(max_length=55L, db_column='TRES_ADR1', blank=True) # Field name made lowercase.
    tres_adr2 = models.CharField(max_length=55L, db_column='TRES_ADR2', blank=True) # Field name made lowercase.
    tres_city = models.CharField(max_length=30L, db_column='TRES_CITY', blank=True) # Field name made lowercase.
    tres_namf = models.CharField(max_length=45L, db_column='TRES_NAMF', blank=True) # Field name made lowercase.
    tres_naml = models.CharField(max_length=200L, db_column='TRES_NAML', blank=True) # Field name made lowercase.
    tres_nams = models.CharField(max_length=10L, db_column='TRES_NAMS', blank=True) # Field name made lowercase.
    tres_namt = models.CharField(max_length=10L, db_column='TRES_NAMT', blank=True) # Field name made lowercase.
    tres_st = models.CharField(max_length=2L, db_column='TRES_ST', blank=True) # Field name made lowercase.
    tres_zip4 = models.CharField(max_length=10L, db_column='TRES_ZIP4', blank=True) # Field name made lowercase.
    xref_match = models.CharField(max_length=1L, db_column='XREF_MATCH', blank=True) # Field name made lowercase.
    xref_schnm = models.CharField(max_length=2L, db_column='XREF_SCHNM', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'LOAN_CD'

class LobbyAmendmentsCd(models.Model):
    filing_id = models.CharField(max_length=9L, db_column='FILING_ID') # Field name made lowercase.
    amend_id = models.CharField(max_length=8L, db_column='AMEND_ID') # Field name made lowercase.
    rec_type = models.CharField(max_length=8L, db_column='REC_TYPE') # Field name made lowercase.
    form_type = models.CharField(max_length=9L, db_column='FORM_TYPE') # Field name made lowercase.
    exec_date = models.CharField(max_length=22L, db_column='EXEC_DATE') # Field name made lowercase.
    from_date = models.CharField(max_length=22L, db_column='FROM_DATE') # Field name made lowercase.
    thru_date = models.CharField(max_length=22L, db_column='THRU_DATE') # Field name made lowercase.
    add_l_cb = models.CharField(max_length=1L, db_column='ADD_L_CB', blank=True) # Field name made lowercase.
    add_l_eff = models.DateField(null=True, db_column='ADD_L_EFF', blank=True) # Field name made lowercase.
    a_l_naml = models.CharField(max_length=200L, db_column='A_L_NAML', blank=True) # Field name made lowercase.
    a_l_namf = models.CharField(max_length=45L, db_column='A_L_NAMF', blank=True) # Field name made lowercase.
    a_l_namt = models.CharField(max_length=10L, db_column='A_L_NAMT', blank=True) # Field name made lowercase.
    a_l_nams = models.CharField(max_length=10L, db_column='A_L_NAMS', blank=True) # Field name made lowercase.
    del_l_cb = models.CharField(max_length=8L, db_column='DEL_L_CB', blank=True) # Field name made lowercase.
    del_l_eff = models.CharField(max_length=22L, db_column='DEL_L_EFF', blank=True) # Field name made lowercase.
    d_l_naml = models.CharField(max_length=56L, db_column='D_L_NAML', blank=True) # Field name made lowercase.
    d_l_namf = models.CharField(max_length=35L, db_column='D_L_NAMF', blank=True) # Field name made lowercase.
    d_l_namt = models.CharField(max_length=10L, db_column='D_L_NAMT', blank=True) # Field name made lowercase.
    d_l_nams = models.CharField(max_length=8L, db_column='D_L_NAMS', blank=True) # Field name made lowercase.
    add_le_cb = models.CharField(max_length=1L, db_column='ADD_LE_CB', blank=True) # Field name made lowercase.
    add_le_eff = models.DateField(null=True, db_column='ADD_LE_EFF', blank=True) # Field name made lowercase.
    a_le_naml = models.CharField(max_length=200L, db_column='A_LE_NAML', blank=True) # Field name made lowercase.
    a_le_namf = models.CharField(max_length=45L, db_column='A_LE_NAMF', blank=True) # Field name made lowercase.
    a_le_namt = models.CharField(max_length=10L, db_column='A_LE_NAMT', blank=True) # Field name made lowercase.
    a_le_nams = models.CharField(max_length=10L, db_column='A_LE_NAMS', blank=True) # Field name made lowercase.
    del_le_cb = models.CharField(max_length=9L, db_column='DEL_LE_CB', blank=True) # Field name made lowercase.
    del_le_eff = models.CharField(max_length=22L, db_column='DEL_LE_EFF', blank=True) # Field name made lowercase.
    d_le_naml = models.CharField(max_length=160L, db_column='D_LE_NAML', blank=True) # Field name made lowercase.
    d_le_namf = models.CharField(max_length=45L, db_column='D_LE_NAMF', blank=True) # Field name made lowercase.
    d_le_namt = models.CharField(max_length=9L, db_column='D_LE_NAMT', blank=True) # Field name made lowercase.
    d_le_nams = models.CharField(max_length=9L, db_column='D_LE_NAMS', blank=True) # Field name made lowercase.
    add_lf_cb = models.CharField(max_length=1L, db_column='ADD_LF_CB', blank=True) # Field name made lowercase.
    add_lf_eff = models.DateField(null=True, db_column='ADD_LF_EFF', blank=True) # Field name made lowercase.
    a_lf_name = models.CharField(max_length=200L, db_column='A_LF_NAME', blank=True) # Field name made lowercase.
    del_lf_cb = models.CharField(max_length=1L, db_column='DEL_LF_CB', blank=True) # Field name made lowercase.
    del_lf_eff = models.DateField(null=True, db_column='DEL_LF_EFF', blank=True) # Field name made lowercase.
    d_lf_name = models.CharField(max_length=200L, db_column='D_LF_NAME', blank=True) # Field name made lowercase.
    other_cb = models.CharField(max_length=1L, db_column='OTHER_CB', blank=True) # Field name made lowercase.
    other_eff = models.DateField(null=True, db_column='OTHER_EFF', blank=True) # Field name made lowercase.
    other_desc = models.CharField(max_length=100L, db_column='OTHER_DESC', blank=True) # Field name made lowercase.
    f606_yes = models.CharField(max_length=1L, db_column='F606_YES', blank=True) # Field name made lowercase.
    f606_no = models.CharField(max_length=1L, db_column='F606_NO', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'LOBBY_AMENDMENTS_CD'

class LothCd(models.Model):
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    amount = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='AMOUNT', blank=True) # Field name made lowercase.
    cum_amt = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='CUM_AMT', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    firm_adr1 = models.CharField(max_length=55L, db_column='FIRM_ADR1', blank=True) # Field name made lowercase.
    firm_adr2 = models.CharField(max_length=55L, db_column='FIRM_ADR2', blank=True) # Field name made lowercase.
    firm_city = models.CharField(max_length=30L, db_column='FIRM_CITY', blank=True) # Field name made lowercase.
    firm_name = models.CharField(max_length=200L, db_column='FIRM_NAME', blank=True) # Field name made lowercase.
    firm_phon = models.CharField(max_length=20L, db_column='FIRM_PHON', blank=True) # Field name made lowercase.
    firm_st = models.CharField(max_length=2L, db_column='FIRM_ST', blank=True) # Field name made lowercase.
    firm_zip4 = models.CharField(max_length=10L, db_column='FIRM_ZIP4', blank=True) # Field name made lowercase.
    form_type = models.CharField(max_length=7L, db_column='FORM_TYPE') # Field name made lowercase.
    line_item = models.IntegerField(db_column='LINE_ITEM') # Field name made lowercase.
    memo_code = models.CharField(max_length=1L, db_column='MEMO_CODE', blank=True) # Field name made lowercase.
    memo_refno = models.CharField(max_length=20L, db_column='MEMO_REFNO', blank=True) # Field name made lowercase.
    pmt_date = models.DateField(null=True, db_column='PMT_DATE', blank=True) # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE') # Field name made lowercase.
    subj_namf = models.CharField(max_length=45L, db_column='SUBJ_NAMF', blank=True) # Field name made lowercase.
    subj_naml = models.CharField(max_length=200L, db_column='SUBJ_NAML', blank=True) # Field name made lowercase.
    subj_nams = models.CharField(max_length=45L, db_column='SUBJ_NAMS', blank=True) # Field name made lowercase.
    subj_namt = models.CharField(max_length=45L, db_column='SUBJ_NAMT', blank=True) # Field name made lowercase.
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID') # Field name made lowercase.
    class Meta:
        db_table = 'LOTH_CD'

class LpayCd(models.Model):
    advan_amt = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='ADVAN_AMT', blank=True) # Field name made lowercase.
    advan_dscr = models.CharField(max_length=100L, db_column='ADVAN_DSCR', blank=True) # Field name made lowercase.
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    bakref_tid = models.CharField(max_length=20L, db_column='BAKREF_TID', blank=True) # Field name made lowercase.
    cum_total = models.DecimalField(decimal_places=2, max_digits=14, db_column='CUM_TOTAL') # Field name made lowercase.
    emplr_adr1 = models.CharField(max_length=55L, db_column='EMPLR_ADR1', blank=True) # Field name made lowercase.
    emplr_adr2 = models.CharField(max_length=55L, db_column='EMPLR_ADR2', blank=True) # Field name made lowercase.
    emplr_city = models.CharField(max_length=30L, db_column='EMPLR_CITY', blank=True) # Field name made lowercase.
    emplr_id = models.CharField(max_length=9L, db_column='EMPLR_ID', blank=True) # Field name made lowercase.
    emplr_namf = models.CharField(max_length=45L, db_column='EMPLR_NAMF', blank=True) # Field name made lowercase.
    emplr_naml = models.CharField(max_length=200L, db_column='EMPLR_NAML') # Field name made lowercase.
    emplr_nams = models.CharField(max_length=10L, db_column='EMPLR_NAMS', blank=True) # Field name made lowercase.
    emplr_namt = models.CharField(max_length=10L, db_column='EMPLR_NAMT', blank=True) # Field name made lowercase.
    emplr_phon = models.CharField(max_length=20L, db_column='EMPLR_PHON', blank=True) # Field name made lowercase.
    emplr_st = models.CharField(max_length=2L, db_column='EMPLR_ST', blank=True) # Field name made lowercase.
    emplr_zip4 = models.CharField(max_length=10L, db_column='EMPLR_ZIP4', blank=True) # Field name made lowercase.
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD', blank=True) # Field name made lowercase.
    fees_amt = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='FEES_AMT', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    form_type = models.CharField(max_length=7L, db_column='FORM_TYPE') # Field name made lowercase.
    lby_actvty = models.CharField(max_length=200L, db_column='LBY_ACTVTY', blank=True) # Field name made lowercase.
    line_item = models.IntegerField(db_column='LINE_ITEM') # Field name made lowercase.
    memo_code = models.CharField(max_length=1L, db_column='MEMO_CODE', blank=True) # Field name made lowercase.
    memo_refno = models.CharField(max_length=20L, db_column='MEMO_REFNO', blank=True) # Field name made lowercase.
    per_total = models.DecimalField(decimal_places=2, max_digits=14, db_column='PER_TOTAL') # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE') # Field name made lowercase.
    reimb_amt = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='REIMB_AMT', blank=True) # Field name made lowercase.
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID') # Field name made lowercase.
    class Meta:
        db_table = 'LPAY_CD'

class Names(models.Model):
    namid = models.IntegerField(db_column='NAMID') # Field name made lowercase.
    naml = models.CharField(max_length=200L, db_column='NAML') # Field name made lowercase.
    namf = models.CharField(max_length=50L, db_column='NAMF') # Field name made lowercase.
    namt = models.CharField(max_length=100L, db_column='NAMT', blank=True) # Field name made lowercase.
    nams = models.CharField(max_length=30L, db_column='NAMS', blank=True) # Field name made lowercase.
    moniker = models.CharField(max_length=30L, db_column='MONIKER', blank=True) # Field name made lowercase.
    moniker_pos = models.CharField(max_length=9L, db_column='MONIKER_POS', blank=True) # Field name made lowercase.
    namm = models.CharField(max_length=20L, db_column='NAMM', blank=True) # Field name made lowercase.
    fullname = models.CharField(max_length=200L, db_column='FULLNAME') # Field name made lowercase.
    naml_search = models.CharField(max_length=200L, db_column='NAML_SEARCH') # Field name made lowercase.
    class Meta:
        db_table = 'NAMES'

class RcptCd(models.Model):
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    amount = models.DecimalField(decimal_places=2, max_digits=14, db_column='AMOUNT') # Field name made lowercase.
    bakref_tid = models.CharField(max_length=20L, db_column='BAKREF_TID', blank=True) # Field name made lowercase.
    bal_juris = models.CharField(max_length=40L, db_column='BAL_JURIS', blank=True) # Field name made lowercase.
    bal_name = models.CharField(max_length=200L, db_column='BAL_NAME', blank=True) # Field name made lowercase.
    bal_num = models.CharField(max_length=7L, db_column='BAL_NUM', blank=True) # Field name made lowercase.
    cand_namf = models.CharField(max_length=45L, db_column='CAND_NAMF', blank=True) # Field name made lowercase.
    cand_naml = models.CharField(max_length=200L, db_column='CAND_NAML', blank=True) # Field name made lowercase.
    cand_nams = models.CharField(max_length=10L, db_column='CAND_NAMS', blank=True) # Field name made lowercase.
    cand_namt = models.CharField(max_length=10L, db_column='CAND_NAMT', blank=True) # Field name made lowercase.
    cmte_id = models.CharField(max_length=9L, db_column='CMTE_ID', blank=True) # Field name made lowercase.
    ctrib_adr1 = models.CharField(max_length=55L, db_column='CTRIB_ADR1', blank=True) # Field name made lowercase.
    ctrib_adr2 = models.CharField(max_length=55L, db_column='CTRIB_ADR2', blank=True) # Field name made lowercase.
    ctrib_city = models.CharField(max_length=30L, db_column='CTRIB_CITY', blank=True) # Field name made lowercase.
    ctrib_dscr = models.CharField(max_length=90L, db_column='CTRIB_DSCR', blank=True) # Field name made lowercase.
    ctrib_emp = models.CharField(max_length=200L, db_column='CTRIB_EMP', blank=True) # Field name made lowercase.
    ctrib_namf = models.CharField(max_length=45L, db_column='CTRIB_NAMF', blank=True) # Field name made lowercase.
    ctrib_naml = models.CharField(max_length=200L, db_column='CTRIB_NAML') # Field name made lowercase.
    ctrib_nams = models.CharField(max_length=10L, db_column='CTRIB_NAMS', blank=True) # Field name made lowercase.
    ctrib_namt = models.CharField(max_length=10L, db_column='CTRIB_NAMT', blank=True) # Field name made lowercase.
    ctrib_occ = models.CharField(max_length=60L, db_column='CTRIB_OCC', blank=True) # Field name made lowercase.
    ctrib_self = models.CharField(max_length=1L, db_column='CTRIB_SELF', blank=True) # Field name made lowercase.
    ctrib_st = models.CharField(max_length=2L, db_column='CTRIB_ST', blank=True) # Field name made lowercase.
    ctrib_zip4 = models.CharField(max_length=10L, db_column='CTRIB_ZIP4', blank=True) # Field name made lowercase.
    cum_oth = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='CUM_OTH', blank=True) # Field name made lowercase.
    cum_ytd = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='CUM_YTD', blank=True) # Field name made lowercase.
    date_thru = models.DateField(null=True, db_column='DATE_THRU', blank=True) # Field name made lowercase.
    dist_no = models.CharField(max_length=3L, db_column='DIST_NO', blank=True) # Field name made lowercase.
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    form_type = models.CharField(max_length=9L, db_column='FORM_TYPE') # Field name made lowercase.
    int_rate = models.CharField(max_length=9L, db_column='INT_RATE', blank=True) # Field name made lowercase.
    intr_adr1 = models.CharField(max_length=55L, db_column='INTR_ADR1', blank=True) # Field name made lowercase.
    intr_adr2 = models.CharField(max_length=55L, db_column='INTR_ADR2', blank=True) # Field name made lowercase.
    intr_city = models.CharField(max_length=30L, db_column='INTR_CITY', blank=True) # Field name made lowercase.
    intr_cmteid = models.CharField(max_length=9L, db_column='INTR_CMTEID', blank=True) # Field name made lowercase.
    intr_emp = models.CharField(max_length=200L, db_column='INTR_EMP', blank=True) # Field name made lowercase.
    intr_namf = models.CharField(max_length=45L, db_column='INTR_NAMF', blank=True) # Field name made lowercase.
    intr_naml = models.CharField(max_length=200L, db_column='INTR_NAML', blank=True) # Field name made lowercase.
    intr_nams = models.CharField(max_length=10L, db_column='INTR_NAMS', blank=True) # Field name made lowercase.
    intr_namt = models.CharField(max_length=10L, db_column='INTR_NAMT', blank=True) # Field name made lowercase.
    intr_occ = models.CharField(max_length=60L, db_column='INTR_OCC', blank=True) # Field name made lowercase.
    intr_self = models.CharField(max_length=1L, db_column='INTR_SELF', blank=True) # Field name made lowercase.
    intr_st = models.CharField(max_length=2L, db_column='INTR_ST', blank=True) # Field name made lowercase.
    intr_zip4 = models.CharField(max_length=10L, db_column='INTR_ZIP4', blank=True) # Field name made lowercase.
    juris_cd = models.CharField(max_length=3L, db_column='JURIS_CD', blank=True) # Field name made lowercase.
    juris_dscr = models.CharField(max_length=40L, db_column='JURIS_DSCR', blank=True) # Field name made lowercase.
    line_item = models.IntegerField(db_column='LINE_ITEM') # Field name made lowercase.
    memo_code = models.CharField(max_length=1L, db_column='MEMO_CODE', blank=True) # Field name made lowercase.
    memo_refno = models.CharField(max_length=20L, db_column='MEMO_REFNO', blank=True) # Field name made lowercase.
    off_s_h_cd = models.CharField(max_length=1L, db_column='OFF_S_H_CD', blank=True) # Field name made lowercase.
    offic_dscr = models.CharField(max_length=40L, db_column='OFFIC_DSCR', blank=True) # Field name made lowercase.
    office_cd = models.CharField(max_length=3L, db_column='OFFICE_CD', blank=True) # Field name made lowercase.
    rcpt_date = models.DateField(db_column='RCPT_DATE') # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE') # Field name made lowercase.
    sup_opp_cd = models.CharField(max_length=1L, db_column='SUP_OPP_CD', blank=True) # Field name made lowercase.
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID') # Field name made lowercase.
    tran_type = models.CharField(max_length=1L, db_column='TRAN_TYPE', blank=True) # Field name made lowercase.
    tres_adr1 = models.CharField(max_length=55L, db_column='TRES_ADR1', blank=True) # Field name made lowercase.
    tres_adr2 = models.CharField(max_length=55L, db_column='TRES_ADR2', blank=True) # Field name made lowercase.
    tres_city = models.CharField(max_length=30L, db_column='TRES_CITY', blank=True) # Field name made lowercase.
    tres_namf = models.CharField(max_length=45L, db_column='TRES_NAMF', blank=True) # Field name made lowercase.
    tres_naml = models.CharField(max_length=200L, db_column='TRES_NAML', blank=True) # Field name made lowercase.
    tres_nams = models.CharField(max_length=10L, db_column='TRES_NAMS', blank=True) # Field name made lowercase.
    tres_namt = models.CharField(max_length=10L, db_column='TRES_NAMT', blank=True) # Field name made lowercase.
    tres_st = models.CharField(max_length=2L, db_column='TRES_ST', blank=True) # Field name made lowercase.
    tres_zip4 = models.IntegerField(null=True, db_column='TRES_ZIP4', blank=True) # Field name made lowercase.
    xref_match = models.CharField(max_length=1L, db_column='XREF_MATCH', blank=True) # Field name made lowercase.
    xref_schnm = models.CharField(max_length=2L, db_column='XREF_SCHNM', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'RCPT_CD'

class SmryCd(models.Model):
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    line_item = models.CharField(max_length=8L, db_column='LINE_ITEM') # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE') # Field name made lowercase.
    form_type = models.CharField(max_length=8L, db_column='FORM_TYPE') # Field name made lowercase.
    amount_a = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='AMOUNT_A', blank=True) # Field name made lowercase.
    amount_b = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='AMOUNT_B', blank=True) # Field name made lowercase.
    amount_c = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='AMOUNT_C', blank=True) # Field name made lowercase.
    elec_dt = models.DateField(null=True, db_column='ELEC_DT', blank=True) # Field name made lowercase.
    current_filing = models.CharField(max_length=1L, blank=True)
    class Meta:
        db_table = 'SMRY_CD'

class SpltCd(models.Model):
    amend_id = models.IntegerField(db_column='AMEND_ID')
    elec_amount = models.DecimalField(max_digits=16, decimal_places=2, db_column='ELEC_AMOUNT')
    elec_code = models.CharField(max_length=2L, db_column='ELEC_CODE', blank=True)
    elec_date = models.DateField(db_column='ELEC_DATE')
    filing_id = models.IntegerField(db_column='FILING_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    pform_type = models.CharField(max_length=7L, db_column='PFORM_TYPE', blank=True)
    ptran_id = models.CharField(max_length=32L, db_column='PTRAN_ID', blank=True)
    class Meta:
        db_table = 'SPLT_CD'

class CurrentExpn(models.Model):
    agent_namf = models.CharField(max_length=45L, db_column='AGENT_NAMF', blank=True) # Field name made lowercase.
    agent_naml = models.CharField(max_length=200L, db_column='AGENT_NAML', blank=True) # Field name made lowercase.
    agent_nams = models.CharField(max_length=10L, db_column='AGENT_NAMS', blank=True) # Field name made lowercase.
    agent_namt = models.CharField(max_length=10L, db_column='AGENT_NAMT', blank=True) # Field name made lowercase.
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    amount = models.DecimalField(decimal_places=2, max_digits=14, db_column='AMOUNT') # Field name made lowercase.
    bakref_tid = models.CharField(max_length=20L, db_column='BAKREF_TID', blank=True) # Field name made lowercase.
    bal_juris = models.CharField(max_length=40L, db_column='BAL_JURIS', blank=True) # Field name made lowercase.
    bal_name = models.CharField(max_length=200L, db_column='BAL_NAME', blank=True) # Field name made lowercase.
    bal_num = models.CharField(max_length=7L, db_column='BAL_NUM', blank=True) # Field name made lowercase.
    cand_namf = models.CharField(max_length=45L, db_column='CAND_NAMF', blank=True) # Field name made lowercase.
    cand_naml = models.CharField(max_length=200L, db_column='CAND_NAML', blank=True) # Field name made lowercase.
    cand_nams = models.CharField(max_length=10L, db_column='CAND_NAMS', blank=True) # Field name made lowercase.
    cand_namt = models.CharField(max_length=10L, db_column='CAND_NAMT', blank=True) # Field name made lowercase.
    cmte_id = models.CharField(max_length=9L, db_column='CMTE_ID', blank=True) # Field name made lowercase.
    cum_oth = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='CUM_OTH', blank=True) # Field name made lowercase.
    cum_ytd = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='CUM_YTD', blank=True) # Field name made lowercase.
    dist_no = models.CharField(max_length=3L, db_column='DIST_NO', blank=True) # Field name made lowercase.
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD', blank=True) # Field name made lowercase.
    expn_chkno = models.CharField(max_length=20L, db_column='EXPN_CHKNO', blank=True) # Field name made lowercase.
    expn_code = models.CharField(max_length=3L, db_column='EXPN_CODE', blank=True) # Field name made lowercase.
    expn_date = models.DateField(null=True, db_column='EXPN_DATE', blank=True) # Field name made lowercase.
    expn_dscr = models.CharField(max_length=400L, db_column='EXPN_DSCR', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    form_type = models.CharField(max_length=6L, db_column='FORM_TYPE') # Field name made lowercase.
    g_from_e_f = models.CharField(max_length=1L, db_column='G_FROM_E_F', blank=True) # Field name made lowercase.
    juris_cd = models.CharField(max_length=3L, db_column='JURIS_CD', blank=True) # Field name made lowercase.
    juris_dscr = models.CharField(max_length=40L, db_column='JURIS_DSCR', blank=True) # Field name made lowercase.
    line_item = models.IntegerField(db_column='LINE_ITEM') # Field name made lowercase.
    memo_code = models.CharField(max_length=1L, db_column='MEMO_CODE', blank=True) # Field name made lowercase.
    memo_refno = models.CharField(max_length=20L, db_column='MEMO_REFNO', blank=True) # Field name made lowercase.
    off_s_h_cd = models.CharField(max_length=1L, db_column='OFF_S_H_CD', blank=True) # Field name made lowercase.
    offic_dscr = models.CharField(max_length=40L, db_column='OFFIC_DSCR', blank=True) # Field name made lowercase.
    office_cd = models.CharField(max_length=3L, db_column='OFFICE_CD', blank=True) # Field name made lowercase.
    payee_adr1 = models.CharField(max_length=55L, db_column='PAYEE_ADR1', blank=True) # Field name made lowercase.
    payee_adr2 = models.CharField(max_length=55L, db_column='PAYEE_ADR2', blank=True) # Field name made lowercase.
    payee_city = models.CharField(max_length=30L, db_column='PAYEE_CITY', blank=True) # Field name made lowercase.
    payee_namf = models.CharField(max_length=45L, db_column='PAYEE_NAMF', blank=True) # Field name made lowercase.
    payee_naml = models.CharField(max_length=200L, db_column='PAYEE_NAML', blank=True) # Field name made lowercase.
    payee_nams = models.CharField(max_length=10L, db_column='PAYEE_NAMS', blank=True) # Field name made lowercase.
    payee_namt = models.CharField(max_length=10L, db_column='PAYEE_NAMT', blank=True) # Field name made lowercase.
    payee_st = models.CharField(max_length=2L, db_column='PAYEE_ST', blank=True) # Field name made lowercase.
    payee_zip4 = models.CharField(max_length=10L, db_column='PAYEE_ZIP4', blank=True) # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE') # Field name made lowercase.
    sup_opp_cd = models.CharField(max_length=1L, db_column='SUP_OPP_CD', blank=True) # Field name made lowercase.
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID') # Field name made lowercase.
    tres_adr1 = models.CharField(max_length=55L, db_column='TRES_ADR1', blank=True) # Field name made lowercase.
    tres_adr2 = models.CharField(max_length=55L, db_column='TRES_ADR2', blank=True) # Field name made lowercase.
    tres_city = models.CharField(max_length=30L, db_column='TRES_CITY', blank=True) # Field name made lowercase.
    tres_namf = models.CharField(max_length=45L, db_column='TRES_NAMF', blank=True) # Field name made lowercase.
    tres_naml = models.CharField(max_length=200L, db_column='TRES_NAML', blank=True) # Field name made lowercase.
    tres_nams = models.CharField(max_length=10L, db_column='TRES_NAMS', blank=True) # Field name made lowercase.
    tres_namt = models.CharField(max_length=10L, db_column='TRES_NAMT', blank=True) # Field name made lowercase.
    tres_st = models.CharField(max_length=2L, db_column='TRES_ST', blank=True) # Field name made lowercase.
    tres_zip4 = models.CharField(max_length=10L, db_column='TRES_ZIP4', blank=True) # Field name made lowercase.
    xref_match = models.CharField(max_length=1L, db_column='XREF_MATCH', blank=True) # Field name made lowercase.
    xref_schnm = models.CharField(max_length=2L, db_column='XREF_SCHNM', blank=True) # Field name made lowercase.
    current_filing = models.CharField(max_length=1L, blank=True)
    class Meta:
        db_table = 'current_expn'

class CurrentRcpt(models.Model):
    amend_id = models.IntegerField(db_column='AMEND_ID') # Field name made lowercase.
    amount = models.DecimalField(decimal_places=2, max_digits=14, db_column='AMOUNT') # Field name made lowercase.
    bakref_tid = models.CharField(max_length=20L, db_column='BAKREF_TID', blank=True) # Field name made lowercase.
    bal_juris = models.CharField(max_length=40L, db_column='BAL_JURIS', blank=True) # Field name made lowercase.
    bal_name = models.CharField(max_length=200L, db_column='BAL_NAME', blank=True) # Field name made lowercase.
    bal_num = models.CharField(max_length=7L, db_column='BAL_NUM', blank=True) # Field name made lowercase.
    cand_namf = models.CharField(max_length=45L, db_column='CAND_NAMF', blank=True) # Field name made lowercase.
    cand_naml = models.CharField(max_length=200L, db_column='CAND_NAML', blank=True) # Field name made lowercase.
    cand_nams = models.CharField(max_length=10L, db_column='CAND_NAMS', blank=True) # Field name made lowercase.
    cand_namt = models.CharField(max_length=10L, db_column='CAND_NAMT', blank=True) # Field name made lowercase.
    cmte_id = models.CharField(max_length=9L, db_column='CMTE_ID', blank=True) # Field name made lowercase.
    ctrib_adr1 = models.CharField(max_length=55L, db_column='CTRIB_ADR1', blank=True) # Field name made lowercase.
    ctrib_adr2 = models.CharField(max_length=55L, db_column='CTRIB_ADR2', blank=True) # Field name made lowercase.
    ctrib_city = models.CharField(max_length=30L, db_column='CTRIB_CITY', blank=True) # Field name made lowercase.
    ctrib_dscr = models.CharField(max_length=90L, db_column='CTRIB_DSCR', blank=True) # Field name made lowercase.
    ctrib_emp = models.CharField(max_length=200L, db_column='CTRIB_EMP', blank=True) # Field name made lowercase.
    ctrib_namf = models.CharField(max_length=45L, db_column='CTRIB_NAMF', blank=True) # Field name made lowercase.
    ctrib_naml = models.CharField(max_length=200L, db_column='CTRIB_NAML') # Field name made lowercase.
    ctrib_nams = models.CharField(max_length=10L, db_column='CTRIB_NAMS', blank=True) # Field name made lowercase.
    ctrib_namt = models.CharField(max_length=10L, db_column='CTRIB_NAMT', blank=True) # Field name made lowercase.
    ctrib_occ = models.CharField(max_length=60L, db_column='CTRIB_OCC', blank=True) # Field name made lowercase.
    ctrib_self = models.CharField(max_length=1L, db_column='CTRIB_SELF', blank=True) # Field name made lowercase.
    ctrib_st = models.CharField(max_length=2L, db_column='CTRIB_ST', blank=True) # Field name made lowercase.
    ctrib_zip4 = models.CharField(max_length=10L, db_column='CTRIB_ZIP4', blank=True) # Field name made lowercase.
    cum_oth = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='CUM_OTH', blank=True) # Field name made lowercase.
    cum_ytd = models.DecimalField(decimal_places=2, null=True, max_digits=14, db_column='CUM_YTD', blank=True) # Field name made lowercase.
    date_thru = models.DateField(null=True, db_column='DATE_THRU', blank=True) # Field name made lowercase.
    dist_no = models.CharField(max_length=3L, db_column='DIST_NO', blank=True) # Field name made lowercase.
    entity_cd = models.CharField(max_length=3L, db_column='ENTITY_CD', blank=True) # Field name made lowercase.
    filing_id = models.IntegerField(db_column='FILING_ID') # Field name made lowercase.
    form_type = models.CharField(max_length=9L, db_column='FORM_TYPE') # Field name made lowercase.
    int_rate = models.CharField(max_length=9L, db_column='INT_RATE', blank=True) # Field name made lowercase.
    intr_adr1 = models.CharField(max_length=55L, db_column='INTR_ADR1', blank=True) # Field name made lowercase.
    intr_adr2 = models.CharField(max_length=55L, db_column='INTR_ADR2', blank=True) # Field name made lowercase.
    intr_city = models.CharField(max_length=30L, db_column='INTR_CITY', blank=True) # Field name made lowercase.
    intr_cmteid = models.CharField(max_length=9L, db_column='INTR_CMTEID', blank=True) # Field name made lowercase.
    intr_emp = models.CharField(max_length=200L, db_column='INTR_EMP', blank=True) # Field name made lowercase.
    intr_namf = models.CharField(max_length=45L, db_column='INTR_NAMF', blank=True) # Field name made lowercase.
    intr_naml = models.CharField(max_length=200L, db_column='INTR_NAML', blank=True) # Field name made lowercase.
    intr_nams = models.CharField(max_length=10L, db_column='INTR_NAMS', blank=True) # Field name made lowercase.
    intr_namt = models.CharField(max_length=10L, db_column='INTR_NAMT', blank=True) # Field name made lowercase.
    intr_occ = models.CharField(max_length=60L, db_column='INTR_OCC', blank=True) # Field name made lowercase.
    intr_self = models.CharField(max_length=1L, db_column='INTR_SELF', blank=True) # Field name made lowercase.
    intr_st = models.CharField(max_length=2L, db_column='INTR_ST', blank=True) # Field name made lowercase.
    intr_zip4 = models.CharField(max_length=10L, db_column='INTR_ZIP4', blank=True) # Field name made lowercase.
    juris_cd = models.CharField(max_length=3L, db_column='JURIS_CD', blank=True) # Field name made lowercase.
    juris_dscr = models.CharField(max_length=40L, db_column='JURIS_DSCR', blank=True) # Field name made lowercase.
    line_item = models.IntegerField(db_column='LINE_ITEM') # Field name made lowercase.
    memo_code = models.CharField(max_length=1L, db_column='MEMO_CODE', blank=True) # Field name made lowercase.
    memo_refno = models.CharField(max_length=20L, db_column='MEMO_REFNO', blank=True) # Field name made lowercase.
    off_s_h_cd = models.CharField(max_length=1L, db_column='OFF_S_H_CD', blank=True) # Field name made lowercase.
    offic_dscr = models.CharField(max_length=40L, db_column='OFFIC_DSCR', blank=True) # Field name made lowercase.
    office_cd = models.CharField(max_length=3L, db_column='OFFICE_CD', blank=True) # Field name made lowercase.
    rcpt_date = models.DateField(db_column='RCPT_DATE') # Field name made lowercase.
    rec_type = models.CharField(max_length=4L, db_column='REC_TYPE') # Field name made lowercase.
    sup_opp_cd = models.CharField(max_length=1L, db_column='SUP_OPP_CD', blank=True) # Field name made lowercase.
    tran_id = models.CharField(max_length=20L, db_column='TRAN_ID') # Field name made lowercase.
    tran_type = models.CharField(max_length=1L, db_column='TRAN_TYPE', blank=True) # Field name made lowercase.
    tres_adr1 = models.CharField(max_length=55L, db_column='TRES_ADR1', blank=True) # Field name made lowercase.
    tres_adr2 = models.CharField(max_length=55L, db_column='TRES_ADR2', blank=True) # Field name made lowercase.
    tres_city = models.CharField(max_length=30L, db_column='TRES_CITY', blank=True) # Field name made lowercase.
    tres_namf = models.CharField(max_length=45L, db_column='TRES_NAMF', blank=True) # Field name made lowercase.
    tres_naml = models.CharField(max_length=200L, db_column='TRES_NAML', blank=True) # Field name made lowercase.
    tres_nams = models.CharField(max_length=10L, db_column='TRES_NAMS', blank=True) # Field name made lowercase.
    tres_namt = models.CharField(max_length=10L, db_column='TRES_NAMT', blank=True) # Field name made lowercase.
    tres_st = models.CharField(max_length=2L, db_column='TRES_ST', blank=True) # Field name made lowercase.
    tres_zip4 = models.IntegerField(null=True, db_column='TRES_ZIP4', blank=True) # Field name made lowercase.
    xref_match = models.CharField(max_length=1L, db_column='XREF_MATCH', blank=True) # Field name made lowercase.
    xref_schnm = models.CharField(max_length=2L, db_column='XREF_SCHNM', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'current_rcpt'
