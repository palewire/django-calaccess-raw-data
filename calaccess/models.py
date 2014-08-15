from __future__ import unicode_literals
from django.db import models
from calaccess import managers


class CalAccessBaseModel(models.Model):
    """
    An abstract model with some tricks we'll reuse below.
    """
    DATE_FIELDS = ()
    objects = managers.CalAccessManager()

    def get_csv_name(self):
        return self.__class__.objects.get_csv_name()

    def get_csv_path(self):
        return self.__class__.objects.get_csv_path()

    class Meta:
        abstract = True


class AcronymsCd(CalAccessBaseModel):
    DATE_FIELDS = (
        "EFFECT_DT",
    )
    acronym = models.CharField(max_length=25, db_column="ACRONYM")
    stands_for = models.CharField(max_length=4, db_column="STANDS_FOR")
    effect_dt = models.DateField(db_column="EFFECT_DT")
    a_desc = models.CharField(max_length=25, db_column="A_DESC")

    class Meta:
        db_table = "ACRONYMS_CD"


class AddressCd(CalAccessBaseModel):
    adrid = models.IntegerField(db_column="ADRID")
    city = models.CharField(max_length=500, db_column="CITY")
    st = models.CharField(max_length=500, db_column="ST")
    zip4 = models.IntegerField(db_column="ZIP4")
    phon = models.IntegerField(db_column="PHON")
    fax = models.IntegerField(db_column="FAX")
    email = models.CharField(max_length=500, db_column="EMAIL")

    class Meta:
        db_table = "ADDRESS_CD"


class BallotMeasuresCd(CalAccessBaseModel):
    election_date = models.DateField(db_column='ELECTION_DATE')
    filer_id = models.IntegerField(db_column='FILER_ID')
    measure_no = models.CharField(db_column='MEASURE_NO', max_length=2)
    measure_name = models.CharField(db_column='MEASURE_NAME', max_length=163)
    measure_short_name = models.CharField(
        db_column='MEASURE_SHORT_NAME',
        max_length=50, blank=True
    )
    jurisdiction = models.CharField(db_column='JURISDICTION', max_length=9)

    class Meta:
        db_table = 'BALLOT_MEASURES_CD'






class CvrE530Cd(CalAccessBaseModel):
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    rec_type = models.CharField(db_column='REC_TYPE', max_length=3)
    form_type = models.CharField(db_column='FORM_TYPE', max_length=4)
    entity_cd = models.CharField(
        db_column='ENTITY_CD', max_length=32, blank=True
    )
    filer_naml = models.CharField(db_column='FILER_NAML', max_length=200)
    filer_namf = models.CharField(
        db_column='FILER_NAMF', max_length=4, blank=True
    )
    filer_namt = models.CharField(
        db_column='FILER_NAMT', max_length=32, blank=True
    )
    filer_nams = models.CharField(
        db_column='FILER_NAMS', max_length=32, blank=True
    )
    report_num = models.CharField(
        db_column='REPORT_NUM', max_length=32, blank=True
    )
    rpt_date = models.DateField(db_column='RPT_DATE')
    filer_city = models.CharField(
        db_column='FILER_CITY', max_length=16, blank=True
    )
    filer_st = models.CharField(db_column='FILER_ST', max_length=4, blank=True)
    filer_zip4 = models.CharField(
        db_column='FILER_ZIP4', max_length=10, blank=True
    )
    occupation = models.CharField(
        db_column='OCCUPATION', max_length=15, blank=True
    )
    employer = models.CharField(
        db_column='EMPLOYER', max_length=13, blank=True
    )
    cand_naml = models.CharField(db_column='CAND_NAML', max_length=46)
    cand_namf = models.CharField(
        db_column='CAND_NAMF', max_length=21, blank=True
    )
    cand_namt = models.CharField(
        db_column='CAND_NAMT', max_length=32, blank=True
    )
    cand_nams = models.CharField(
        db_column='CAND_NAMS', max_length=32, blank=True
    )
    district_cd = models.IntegerField(db_column='DISTRICT_CD')
    office_cd = models.IntegerField(db_column='OFFICE_CD')
    pmnt_dt = models.DateField(db_column='PMNT_DT')
    pmnt_amount = models.FloatField(db_column='PMNT_AMOUNT')
    type_literature = models.IntegerField(db_column='TYPE_LITERATURE')
    type_printads = models.IntegerField(db_column='TYPE_PRINTADS')
    type_radio = models.IntegerField(db_column='TYPE_RADIO')
    type_tv = models.IntegerField(db_column='TYPE_TV')
    type_it = models.IntegerField(db_column='TYPE_IT')
    type_billboards = models.IntegerField(db_column='TYPE_BILLBOARDS')
    type_other = models.IntegerField(db_column='TYPE_OTHER')
    other_desc = models.CharField(db_column='OTHER_DESC', max_length=49)

    class Meta:
        db_table = 'CVR_E530_CD'


class CvrLobbyDisclosureCd(CalAccessBaseModel):
    DATE_FIELDS = [
        'CUM_BEG_DT',
        'FROM_DATE',
        'RPT_DATE',
        'SIG_DATE',
        'THRU_DATE'
    ]
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




class EfsFilingLogCd(CalAccessBaseModel):
    filing_date = models.DateTimeField(db_column='FILING_DATE')
    filingstatus = models.IntegerField(db_column='FILINGSTATUS')
    vendor = models.CharField(db_column='VENDOR', max_length=250)
    filer_id = models.CharField(db_column='FILER_ID', max_length=250)
    form_type = models.CharField(db_column='FORM_TYPE', max_length=250)
    error_no = models.CharField(db_column='ERROR_NO', max_length=250)

    class Meta:
        db_table = 'EFS_FILING_LOG_CD'







class F690P2Cd(CalAccessBaseModel):
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    rec_type = models.CharField(db_column='REC_TYPE', max_length=4)
    form_type = models.CharField(db_column='FORM_TYPE', max_length=4)
    exec_date = models.DateField(db_column='EXEC_DATE')
    from_date = models.DateField(db_column='FROM_DATE')
    thru_date = models.DateField(db_column='THRU_DATE')
    chg_parts = models.CharField(
        db_column='CHG_PARTS', max_length=100, blank=True
    )
    chg_sects = models.CharField(
        db_column='CHG_SECTS', max_length=100, blank=True
    )
    amend_txt1 = models.CharField(
        db_column='AMEND_TXT1', max_length=330, blank=True
    )

    class Meta:
        db_table = 'F690P2_CD'


class FilernameCd(CalAccessBaseModel):
    DATE_FIELDS = ['EFFECT_DT', ]
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
        ordering = ("id",)

    def __unicode__(self):
        return self.acronym


class FilerAddressCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    adrid = models.IntegerField(db_column='ADRID')
    effect_dt = models.DateTimeField(
        db_column='EFFECT_DT', blank=True, null=True
    )
    add_type = models.IntegerField(db_column='ADD_TYPE', blank=True, null=True)
    session_id = models.IntegerField(
        db_column='SESSION_ID', blank=True, null=True
    )

    class Meta:
        db_table = 'FILER_ADDRESS_CD'


class FilerEthicsClassCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    ethics_date = models.DateTimeField(db_column='ETHICS_DATE')

    class Meta:
        db_table = 'FILER_ETHICS_CLASS_CD'


class FilerFilingsCd(CalAccessBaseModel):
    DATE_FIELDS = [
        'FILING_DATE',
        'RPT_START',
        'RPT_END',
        'RPT_DATE'
    ]
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
    DATE_FIELDS = [
        'EFFECT_DATE',
    ]
    filer_id = models.IntegerField(db_column='FILER_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    interest_cd = models.IntegerField(db_column='INTEREST_CD')
    effect_date = models.DateTimeField(db_column='EFFECT_DATE')

    class Meta:
        db_table = 'FILER_INTERESTS_CD'


class FilerLinksCd(CalAccessBaseModel):
    DATE_FIELDS = [
        'EFFECT_DT',
        'TERMINATION_DT'
    ]
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
    DATE_FIELDS = [
        'EFFECT_DT',
        'NYQ_DT'
    ]
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
    DATE_FIELDS = [
        'EFFECT_DT',
    ]
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
    DATE_FIELDS = [
        'START_DATE',
        'END_DATE',
        'DEADLINE'
    ]
    period_id = models.IntegerField(db_column='PERIOD_ID')
    start_date = models.DateField(db_column='START_DATE')
    end_date = models.DateField(db_column='END_DATE')
    period_type = models.IntegerField(db_column='PERIOD_TYPE')
    per_grp_type = models.IntegerField(db_column='PER_GRP_TYPE')
    period_desc = models.CharField(max_length=255L, db_column='PERIOD_DESC')
    deadline = models.DateField(db_column='DEADLINE')

    class Meta:
        db_table = 'FILING_PERIOD_CD'


class GroupTypesCd(CalAccessBaseModel):
    grp_id = models.IntegerField(db_column='GRP_ID')
    grp_name = models.CharField(
        db_column='GRP_NAME', max_length=28, blank=True
    )
    grp_desc = models.CharField(
        db_column='GRP_DESC', max_length=32, blank=True
    )

    class Meta:
        db_table = 'GROUP_TYPES_CD'


class HeaderCd(CalAccessBaseModel):
    line_number = models.IntegerField(db_column='LINE_NUMBER')
    form_id = models.CharField(db_column='FORM_ID', max_length=5)
    rec_type = models.CharField(db_column='REC_TYPE', max_length=11)
    section_label = models.CharField(
        db_column='SECTION_LABEL', max_length=58, blank=True
    )
    comments1 = models.CharField(
        db_column='COMMENTS1', max_length=48, blank=True
    )
    comments2 = models.CharField(
        db_column='COMMENTS2', max_length=48, blank=True
    )
    label = models.CharField(db_column='LABEL', max_length=98)
    column_a = models.IntegerField(db_column='COLUMN_A', blank=True, null=True)
    column_b = models.IntegerField(db_column='COLUMN_B', blank=True, null=True)
    column_c = models.IntegerField(db_column='COLUMN_C', blank=True, null=True)
    show_c = models.IntegerField(db_column='SHOW_C', blank=True, null=True)
    show_b = models.IntegerField(db_column='SHOW_B', blank=True, null=True)

    class Meta:
        db_table = 'HEADER_CD'


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


class ImageLinksCd(CalAccessBaseModel):
    img_link_id = models.IntegerField(db_column='IMG_LINK_ID')
    img_link_type = models.IntegerField(db_column='IMG_LINK_TYPE')
    img_id = models.IntegerField(db_column='IMG_ID')
    img_type = models.IntegerField(db_column='IMG_TYPE')
    img_dt = models.DateField(db_column='IMG_DT')

    class Meta:
        db_table = 'IMAGE_LINKS_CD'


class LattCd(CalAccessBaseModel):
    DATE_FIELDS = [
        'CUMBEG_DT',
        'PMT_DATE',
    ]
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


class LegislativeSessionsCd(CalAccessBaseModel):
    session_id = models.IntegerField(db_column='SESSION_ID')
    begin_date = models.DateField(db_column='BEGIN_DATE')
    end_date = models.DateField(db_column='END_DATE')

    class Meta:
        db_table = 'LEGISLATIVE_SESSIONS_CD'


class LccmCd(CalAccessBaseModel):
    DATE_FIELDS = [
        'CTRIB_DATE',
    ]
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
    DATE_FIELDS = [
        'EFF_DATE',
    ]
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
    DATE_FIELDS = [
        'EXPN_DATE',
    ]
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




class LobbyAmendmentsCd(CalAccessBaseModel):
    DATE_FIELDS = [
        'ADD_L_EFF',
        'ADD_LE_EFF',
        'ADD_LF_EFF',
        'DEL_LF_EFF',
        'OTHER_EFF'
    ]
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


class LobbyingChgLogCd(CalAccessBaseModel):
    DATE_FIELDS = (
        "LOG_DT",
        "ETHICS_DT",
        "EFFECT_DT",
    )
    filer_id = models.IntegerField(db_column='FILER_ID')
    change_no = models.IntegerField(db_column='CHANGE_NO')
    session_id = models.IntegerField(db_column='SESSION_ID')
    log_dt = models.DateField(db_column="LOG_DT")
    filer_type = models.IntegerField(db_column='FILER_TYPE')
    correction_flag = models.CharField(
        max_length=200,
        db_column="CORRECTION_FLG"
    )
    action = models.CharField(max_length=200, db_column="ACTION")
    attribute_changed = models.CharField(
        max_length=200,
        db_column="ATTRIBUTE_CHANGED"
    )
    ethics_dt = models.DateField(db_column="ETHICS_DT")
    interests = models.CharField(max_length=200, db_column="INTERESTS")
    filer_full_name = models.CharField(
        max_length=200,
        db_column="FILER_FULL_NAME"
    )
    filer_city = models.CharField(max_length=200, db_column="FILER_CITY")
    filer_st = models.CharField(max_length=200, db_column="FILER_ST")
    filer_zip = models.IntegerField(db_column="FILER_ZIP")
    filer_phone = models.IntegerField(db_column="FILER_PHONE")
    entity_type = models.IntegerField(db_column="ENTITY_TYPE")
    entity_name = models.CharField(max_length=500, db_column="ENTITY_NAME")
    entity_city = models.CharField(max_length=500, db_column="ENTITY_CITY")
    entity_st = models.CharField(max_length=500, db_column="ENTITY_ST")
    entity_zip = models.IntegerField(db_column="ENTITY_ZIP")
    entity_phone = models.IntegerField(db_column="ENTITY_PHONE")
    entity_id = models.IntegerField(db_column="ENTITY_ID")
    responsible_officer = models.CharField(
        max_length=500, db_column="RESPONSIBLE_OFFICER"
    )
    effect_dt = models.DateField(db_column="EFFECT_DT")

    class Meta:
        db_table = 'LOBBYING_CHG_LOG_CD'


class LobbyistContributions1Cd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    filing_period_start_dt = models.DateField(
        db_column='FILING_PERIOD_START_DT'
    )
    filing_period_end_dt = models.DateField(db_column='FILING_PERIOD_END_DT')
    contribution_dt = models.CharField(
        db_column='CONTRIBUTION_DT', max_length=32, blank=True
    )
    recipient_name = models.CharField(
        db_column='RECIPIENT_NAME', max_length=106, blank=True
    )
    recipient_id = models.IntegerField(
        db_column='RECIPIENT_ID', blank=True, null=True
    )
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)

    class Meta:
        db_table = 'LOBBYIST_CONTRIBUTIONS1_CD'


class LobbyistContributions2Cd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    filing_period_start_dt = models.DateField(
        db_column='FILING_PERIOD_START_DT'
    )
    filing_period_end_dt = models.DateField(
        db_column='FILING_PERIOD_END_DT'
    )
    contribution_dt = models.CharField(
        db_column='CONTRIBUTION_DT', max_length=32, blank=True
    )
    recipient_name = models.CharField(
        db_column='RECIPIENT_NAME', max_length=106, blank=True
    )
    recipient_id = models.IntegerField(
        db_column='RECIPIENT_ID', blank=True, null=True
    )
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)

    class Meta:
        db_table = 'LOBBYIST_CONTRIBUTIONS2_CD'


class LobbyistContributions3Cd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    filing_period_start_dt = models.DateField(
        db_column='FILING_PERIOD_START_DT'
    )
    filing_period_end_dt = models.DateField(
        db_column='FILING_PERIOD_END_DT'
    )
    contribution_dt = models.CharField(
        db_column='CONTRIBUTION_DT', max_length=32, blank=True
    )
    recipient_name = models.CharField(
        db_column='RECIPIENT_NAME', max_length=106, blank=True
    )
    recipient_id = models.IntegerField(
        db_column='RECIPIENT_ID', blank=True, null=True
    )
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)

    class Meta:
        db_table = 'LOBBYIST_CONTRIBUTIONS3_CD'


class LobbyistEmployer1Cd(CalAccessBaseModel):
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=162)
    current_qtr_amt = models.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = models.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = models.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    interest_cd = models.IntegerField(
        db_column='INTEREST_CD', blank=True, null=True
    )
    interest_name = models.CharField(
        db_column='INTEREST_NAME', max_length=24, blank=True
    )
    session_yr_1 = models.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = models.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = models.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = models.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = models.FloatField(db_column='QTR_1')
    qtr_2 = models.FloatField(db_column='QTR_2')
    qtr_3 = models.FloatField(db_column='QTR_3')
    qtr_4 = models.FloatField(db_column='QTR_4')
    qtr_5 = models.FloatField(db_column='QTR_5')
    qtr_6 = models.FloatField(db_column='QTR_6')
    qtr_7 = models.FloatField(db_column='QTR_7')
    qtr_8 = models.FloatField(db_column='QTR_8')

    class Meta:
        db_table = 'LOBBYIST_EMPLOYER1_CD'


class LobbyistEmployer2Cd(CalAccessBaseModel):
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=162)
    current_qtr_amt = models.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = models.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = models.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    interest_cd = models.IntegerField(
        db_column='INTEREST_CD', blank=True, null=True
    )
    interest_name = models.CharField(
        db_column='INTEREST_NAME', max_length=24, blank=True
    )
    session_yr_1 = models.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = models.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = models.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = models.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = models.FloatField(db_column='QTR_1')
    qtr_2 = models.FloatField(db_column='QTR_2')
    qtr_3 = models.FloatField(db_column='QTR_3')
    qtr_4 = models.FloatField(db_column='QTR_4')
    qtr_5 = models.FloatField(db_column='QTR_5')
    qtr_6 = models.FloatField(db_column='QTR_6')
    qtr_7 = models.FloatField(db_column='QTR_7')
    qtr_8 = models.FloatField(db_column='QTR_8')

    class Meta:
        db_table = 'LOBBYIST_EMPLOYER2_CD'


class LobbyistEmployer3Cd(CalAccessBaseModel):
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=162)
    current_qtr_amt = models.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = models.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = models.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    interest_cd = models.IntegerField(
        db_column='INTEREST_CD', blank=True, null=True
    )
    interest_name = models.CharField(
        db_column='INTEREST_NAME', max_length=24, blank=True
    )
    session_yr_1 = models.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = models.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = models.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = models.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = models.FloatField(db_column='QTR_1')
    qtr_2 = models.FloatField(db_column='QTR_2')
    qtr_3 = models.FloatField(db_column='QTR_3')
    qtr_4 = models.FloatField(db_column='QTR_4')
    qtr_5 = models.FloatField(db_column='QTR_5')
    qtr_6 = models.FloatField(db_column='QTR_6')
    qtr_7 = models.FloatField(db_column='QTR_7')
    qtr_8 = models.FloatField(db_column='QTR_8')

    class Meta:
        db_table = 'LOBBYIST_EMPLOYER3_CD'


class LobbyistEmployerFirms1Cd(CalAccessBaseModel):
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    firm_id = models.IntegerField(db_column='FIRM_ID')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=117)
    session_id = models.IntegerField(db_column='SESSION_ID')
    termination_dt = models.CharField(
        db_column='TERMINATION_DT', max_length=32, blank=True
    )

    class Meta:
        db_table = 'LOBBYIST_EMPLOYER_FIRMS1_CD'


class LobbyistEmployerFirms2Cd(CalAccessBaseModel):
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    firm_id = models.IntegerField(db_column='FIRM_ID')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=117)
    session_id = models.IntegerField(db_column='SESSION_ID')
    termination_dt = models.CharField(
        db_column='TERMINATION_DT', max_length=32, blank=True
    )

    class Meta:
        db_table = 'LOBBYIST_EMPLOYER_FIRMS2_CD'


class LobbyistEmpLobbyist1Cd(CalAccessBaseModel):
    lobbyist_id = models.IntegerField(db_column='LOBBYIST_ID')
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    lobbyist_last_name = models.CharField(
        db_column='LOBBYIST_LAST_NAME', max_length=17
    )
    lobbyist_first_name = models.CharField(
        db_column='LOBBYIST_FIRST_NAME', max_length=17
    )
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=117)
    session_id = models.IntegerField(db_column='SESSION_ID')

    class Meta:
        db_table = 'LOBBYIST_EMP_LOBBYIST1_CD'


class LobbyistEmpLobbyist2Cd(CalAccessBaseModel):
    lobbyist_id = models.IntegerField(db_column='LOBBYIST_ID')
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    lobbyist_last_name = models.CharField(
        db_column='LOBBYIST_LAST_NAME', max_length=17
    )
    lobbyist_first_name = models.CharField(
        db_column='LOBBYIST_FIRST_NAME', max_length=17
    )
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=117)
    session_id = models.IntegerField(db_column='SESSION_ID')

    class Meta:
        db_table = 'LOBBYIST_EMP_LOBBYIST2_CD'


class LobbyistFirm1Cd(CalAccessBaseModel):
    firm_id = models.IntegerField(db_column='FIRM_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=60)
    current_qtr_amt = models.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = models.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = models.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    session_yr_1 = models.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = models.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = models.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = models.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = models.FloatField(db_column='QTR_1')
    qtr_2 = models.FloatField(db_column='QTR_2')
    qtr_3 = models.FloatField(db_column='QTR_3')
    qtr_4 = models.FloatField(db_column='QTR_4')
    qtr_5 = models.FloatField(db_column='QTR_5')
    qtr_6 = models.FloatField(db_column='QTR_6')
    qtr_7 = models.FloatField(db_column='QTR_7')
    qtr_8 = models.FloatField(db_column='QTR_8')

    class Meta:
        db_table = 'LOBBYIST_FIRM1_CD'


class LobbyistFirm2Cd(CalAccessBaseModel):
    firm_id = models.IntegerField(db_column='FIRM_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=60)
    current_qtr_amt = models.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = models.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = models.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    session_yr_1 = models.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = models.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = models.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = models.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = models.FloatField(db_column='QTR_1')
    qtr_2 = models.FloatField(db_column='QTR_2')
    qtr_3 = models.FloatField(db_column='QTR_3')
    qtr_4 = models.FloatField(db_column='QTR_4')
    qtr_5 = models.FloatField(db_column='QTR_5')
    qtr_6 = models.FloatField(db_column='QTR_6')
    qtr_7 = models.FloatField(db_column='QTR_7')
    qtr_8 = models.FloatField(db_column='QTR_8')

    class Meta:
        db_table = 'LOBBYIST_FIRM2_CD'


class LobbyistFirm3Cd(CalAccessBaseModel):
    firm_id = models.IntegerField(db_column='FIRM_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=60)
    current_qtr_amt = models.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = models.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = models.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    session_yr_1 = models.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = models.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = models.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = models.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = models.FloatField(db_column='QTR_1')
    qtr_2 = models.FloatField(db_column='QTR_2')
    qtr_3 = models.FloatField(db_column='QTR_3')
    qtr_4 = models.FloatField(db_column='QTR_4')
    qtr_5 = models.FloatField(db_column='QTR_5')
    qtr_6 = models.FloatField(db_column='QTR_6')
    qtr_7 = models.FloatField(db_column='QTR_7')
    qtr_8 = models.FloatField(db_column='QTR_8')

    class Meta:
        db_table = 'LOBBYIST_FIRM3_CD'


class LobbyistFirmEmployer1Cd(CalAccessBaseModel):
    firm_id = models.IntegerField(db_column='FIRM_ID')
    filing_id = models.IntegerField(db_column='FILING_ID')
    filing_sequence = models.IntegerField(db_column='FILING_SEQUENCE')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=58)
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=75)
    rpt_start = models.DateField(db_column='RPT_START')
    rpt_end = models.DateField(db_column='RPT_END')
    per_total = models.FloatField(db_column='PER_TOTAL')
    cum_total = models.FloatField(db_column='CUM_TOTAL')
    lby_actvty = models.CharField(
        db_column='LBY_ACTVTY', max_length=182, blank=True
    )
    ext_lby_actvty = models.CharField(
        db_column='EXT_LBY_ACTVTY', max_length=32, blank=True
    )

    class Meta:
        db_table = 'LOBBYIST_FIRM_EMPLOYER1_CD'


class LobbyistFirmEmployer2Cd(CalAccessBaseModel):
    firm_id = models.IntegerField(db_column='FIRM_ID')
    filing_id = models.IntegerField(db_column='FILING_ID')
    filing_sequence = models.IntegerField(db_column='FILING_SEQUENCE')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=58)
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=75)
    rpt_start = models.DateField(db_column='RPT_START')
    rpt_end = models.DateField(db_column='RPT_END')
    per_total = models.FloatField(db_column='PER_TOTAL')
    cum_total = models.FloatField(db_column='CUM_TOTAL')
    lby_actvty = models.CharField(
        db_column='LBY_ACTVTY', max_length=182, blank=True
    )
    ext_lby_actvty = models.CharField(
        db_column='EXT_LBY_ACTVTY', max_length=32, blank=True
    )

    class Meta:
        db_table = 'LOBBYIST_FIRM_EMPLOYER2_CD'


class LobbyistFirmLobbyist1Cd(CalAccessBaseModel):
    lobbyist_id = models.IntegerField(db_column='LOBBYIST_ID')
    firm_id = models.IntegerField(db_column='FIRM_ID')
    lobbyist_last_name = models.CharField(
        db_column='LOBBYIST_LAST_NAME', max_length=15
    )
    lobbyist_first_name = models.CharField(
        db_column='LOBBYIST_FIRST_NAME', max_length=17
    )
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=60)
    session_id = models.IntegerField(db_column='SESSION_ID')

    class Meta:
        db_table = 'LOBBYIST_FIRM_LOBBYIST1_CD'


class LobbyistFirmLobbyist2Cd(CalAccessBaseModel):
    lobbyist_id = models.IntegerField(db_column='LOBBYIST_ID')
    firm_id = models.IntegerField(db_column='FIRM_ID')
    lobbyist_last_name = models.CharField(
        db_column='LOBBYIST_LAST_NAME', max_length=15
    )
    lobbyist_first_name = models.CharField(
        db_column='LOBBYIST_FIRST_NAME', max_length=17
    )
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=60)
    session_id = models.IntegerField(db_column='SESSION_ID')

    class Meta:
        db_table = 'LOBBYIST_FIRM_LOBBYIST2_CD'


class LookupCode(CalAccessBaseModel):
    code_type = models.IntegerField()
    code_id = models.IntegerField()
    code_desc = models.CharField(max_length=100)

    class Meta:
        db_table = 'LOOKUP_CODES_CD'


class LothCd(CalAccessBaseModel):
    DATE_FIELDS = [
        'PMT_DATE',
    ]
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

class ReceivedFilingsCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    filing_file_name = models.CharField(
        db_column='FILING_FILE_NAME', max_length=14
    )
    received_date = models.DateTimeField(db_column='RECEIVED_DATE')
    filing_directory = models.CharField(
        db_column='FILING_DIRECTORY', max_length=45
    )
    filing_id = models.IntegerField(
        db_column='FILING_ID', blank=True, null=True
    )
    form_id = models.CharField(db_column='FORM_ID', max_length=4, blank=True)
    receive_comment = models.CharField(
        db_column='RECEIVE_COMMENT', max_length=51
    )

    class Meta:
        db_table = 'RECEIVED_FILINGS_CD'


class ReportsCd(CalAccessBaseModel):
    rpt_id = models.IntegerField(db_column='RPT_ID')
    rpt_name = models.CharField(db_column='RPT_NAME', max_length=74)
    rpt_desc_field = models.CharField(
        db_column='RPT_DESC_', max_length=32, blank=True)
    path = models.CharField(db_column='PATH', max_length=32, blank=True)
    data_object = models.CharField(db_column='DATA_OBJECT', max_length=38)
    parms_flg_y_n = models.IntegerField(
        db_column='PARMS_FLG_Y_N', blank=True, null=True
    )
    rpt_type = models.IntegerField(db_column='RPT_TYPE')
    parm_definition = models.IntegerField(db_column='PARM_DEFINITION')

    class Meta:
        db_table = 'REPORTS_CD'


class SmryCd(CalAccessBaseModel):
    DATE_FIELDS = [
        'ELEC_DT'
    ]
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












class TextMemoCd(CalAccessBaseModel):
    filing_id = models.IntegerField(db_column='FILING_ID')
    amend_id = models.IntegerField(db_column='AMEND_ID')
    line_item = models.IntegerField(db_column='LINE_ITEM')
    rec_type = models.CharField(db_column='REC_TYPE', max_length=4)
    form_type = models.CharField(db_column='FORM_TYPE', max_length=8)
    ref_no = models.CharField(db_column='REF_NO', max_length=20, blank=True)
    text4000 = models.CharField(
        db_column='TEXT4000',
        max_length=4000, blank=True
    )

    class Meta:
        db_table = 'TEXT_MEMO_CD'
