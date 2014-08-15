from __future__ import unicode_literals
from django.db import models
from .base import CalAccessBaseModel


class CvrRegistrationCd(CalAccessBaseModel):
    DATE_FIELDS = [
        'COMPLET_DT',
        'EFF_DATE',
        'QUAL_DATE',
        'RPT_DATE',
        'SIG_DATE'
    ]
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
        app_label = 'calaccess'
        db_table = 'CVR_REGISTRATION_CD'
