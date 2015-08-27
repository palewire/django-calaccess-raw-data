from __future__ import unicode_literals
from calaccess_raw import fields
from django.utils.encoding import python_2_unicode_compatible
from .base import CalAccessBaseModel


@python_2_unicode_compatible
class CvrRegistrationCd(CalAccessBaseModel):
    """
    Cover page of lobbying disclosure forms
    """
    # a_b_adr1 = fields.CharField(
    #     max_length=55, db_column='A_B_ADR1', blank=True
    # )
    # a_b_adr2 = fields.CharField(
    #     max_length=55, db_column='A_B_ADR2', blank=True
    # )
    a_b_city = fields.CharField(
        max_length=30, db_column='A_B_CITY', blank=True
    )
    a_b_name = fields.CharField(
        max_length=200, db_column='A_B_NAME', blank=True
    )
    a_b_st = fields.CharField(max_length=2, db_column='A_B_ST', blank=True)
    a_b_zip4 = fields.CharField(
        max_length=10, db_column='A_B_ZIP4', blank=True
    )
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    # auth_adr1 = fields.CharField(
    #     max_length=55, db_column='AUTH_ADR1', blank=True
    # )
    # auth_adr2 = fields.CharField(
    #     max_length=55, db_column='AUTH_ADR2', blank=True
    # )
    auth_city = fields.CharField(
        max_length=30, db_column='AUTH_CITY', blank=True
    )
    auth_name = fields.CharField(
        max_length=200, db_column='AUTH_NAME', blank=True
    )
    auth_st = fields.CharField(max_length=2, db_column='AUTH_ST', blank=True)
    auth_zip4 = fields.CharField(
        max_length=10, db_column='AUTH_ZIP4', blank=True
    )
    # bus_adr1 = fields.CharField(
    #     max_length=55, db_column='BUS_ADR1', blank=True
    # )
    # bus_adr2 = fields.CharField(
    #     max_length=55, db_column='BUS_ADR2', blank=True
    # )
    bus_cb = fields.CharField(max_length=1, db_column='BUS_CB', blank=True)
    bus_city = fields.CharField(max_length=30, db_column='BUS_CITY')
    bus_class = fields.CharField(
        max_length=3, db_column='BUS_CLASS', blank=True
    )
    bus_descr = fields.CharField(
        max_length=100, db_column='BUS_DESCR', blank=True
    )
    bus_email = fields.CharField(
        max_length=60, db_column='BUS_EMAIL', blank=True
    )
    bus_fax = fields.CharField(max_length=20, db_column='BUS_FAX', blank=True)
    bus_phon = fields.CharField(
        max_length=20, db_column='BUS_PHON', blank=True
    )
    bus_st = fields.CharField(max_length=2, db_column='BUS_ST', blank=True)
    bus_zip4 = fields.CharField(
        max_length=10, db_column='BUS_ZIP4', blank=True
    )
    c_less50 = fields.CharField(
        max_length=1, db_column='C_LESS50', blank=True
    )
    c_more50 = fields.CharField(
        max_length=1, db_column='C_MORE50', blank=True
    )
    complet_dt = fields.DateField(
        null=True, db_column='COMPLET_DT', blank=True
    )
    descrip_1 = fields.CharField(
        max_length=300, db_column='DESCRIP_1', blank=True
    )
    descrip_2 = fields.CharField(
        max_length=300, db_column='DESCRIP_2', blank=True
    )
    eff_date = fields.DateField(null=True, db_column='EFF_DATE', blank=True)
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('BUS', 'BUS (Unknown)'),
        ('FRM', 'Lobbying firm'),
        ('LBY', 'Lobbyist (an individual)'),
        ('LCO', 'Lobbying coalition'),
        ('LEM', 'Lobbying employer'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
    )
    filer_id = fields.CharField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        max_length=8,
        blank=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    filer_namf = fields.CharField(
        max_length=45, db_column='FILER_NAMF', blank=True
    )
    filer_naml = fields.CharField(
        max_length=200, db_column='FILER_NAML', blank=True
    )
    filer_nams = fields.CharField(
        max_length=10, db_column='FILER_NAMS', blank=True
    )
    filer_namt = fields.CharField(
        max_length=10, db_column='FILER_NAMT', blank=True
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number",
        null=True,
        blank=True,
    )
    firm_name = fields.CharField(
        max_length=200, db_column='FIRM_NAME', blank=True
    )
    FORM_TYPE_CHOICES = (
        ('F601', 'Form 601 (Lobbying firm registration statement)'),
        ('F602', 'Form 602 (Lobbying firm activity authorization)'),
        ('F603', 'Form 603 (Lobbyist employer or lobbying coalition \
registration statement)'),
        ('F604', 'Form 604 (Lobbyist certification statement)'),
        ('F606', 'Form 606 (Notice of termination)'),
        ('F607', 'Form 607 (Notice of withdrawal)'),
    )
    form_type = fields.CharField(
        max_length=4,
        db_column='FORM_TYPE',
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES
    )
    ind_cb = fields.CharField(max_length=1, db_column='IND_CB', blank=True)
    ind_class = fields.CharField(
        max_length=3, db_column='IND_CLASS', blank=True
    )
    ind_descr = fields.CharField(
        max_length=100, db_column='IND_DESCR', blank=True
    )
    influen_yn = fields.IntegerField(
        null=True, db_column='INFLUEN_YN', blank=True
    )
    l_firm_cb = fields.CharField(
        max_length=1, db_column='L_FIRM_CB', blank=True
    )
    lby_604_cb = fields.CharField(
        max_length=1, db_column='LBY_604_CB', blank=True
    )
    lby_reg_cb = fields.CharField(
        max_length=1, db_column='LBY_REG_CB', blank=True
    )
    lobby_cb = fields.CharField(
        max_length=1, db_column='LOBBY_CB', blank=True
    )
    lobby_int = fields.CharField(
        max_length=300, db_column='LOBBY_INT', blank=True
    )
    ls_beg_yr = fields.CharField(
        null=True, db_column='LS_BEG_YR', blank=True, max_length=5
    )
    ls_end_yr = fields.CharField(
        db_column='LS_END_YR', max_length=5
    )
    # mail_adr1 = fields.CharField(
    #     max_length=55, db_column='MAIL_ADR1', blank=True
    # )
    # mail_adr2 = fields.CharField(
    #     max_length=55, db_column='MAIL_ADR2', blank=True
    # )
    mail_city = fields.CharField(
        max_length=30, db_column='MAIL_CITY', blank=True
    )
    mail_phon = fields.CharField(
        max_length=20, db_column='MAIL_PHON', blank=True
    )
    mail_st = fields.CharField(max_length=2, db_column='MAIL_ST', blank=True)
    mail_zip4 = fields.CharField(
        max_length=10, db_column='MAIL_ZIP4', blank=True
    )
    newcert_cb = fields.CharField(
        max_length=1, db_column='NEWCERT_CB', blank=True
    )
    oth_cb = fields.CharField(max_length=1, db_column='OTH_CB', blank=True)
    prn_namf = fields.CharField(
        max_length=45, db_column='PRN_NAMF', blank=True
    )
    prn_naml = fields.CharField(
        max_length=200, db_column='PRN_NAML', blank=True
    )
    prn_nams = fields.CharField(
        max_length=10, db_column='PRN_NAMS', blank=True
    )
    prn_namt = fields.CharField(
        max_length=10, db_column='PRN_NAMT', blank=True
    )
    qual_date = fields.DateField(
        null=True, db_column='QUAL_DATE', blank=True
    )
    REC_TYPE_CHOICES = (
        ("CVR", "CVR"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    rencert_cb = fields.CharField(
        max_length=1, db_column='RENCERT_CB', blank=True
    )
    report_num = fields.CharField(
        max_length=3, db_column='REPORT_NUM', blank=True
    )
    rpt_date = fields.DateField(db_column='RPT_DATE', null=True)
    sender_id = fields.CharField(max_length=9, db_column='SENDER_ID')
    sig_date = fields.DateField(
        null=True, db_column='SIG_DATE', blank=True
    )
    sig_loc = fields.CharField(
        max_length=45, db_column='SIG_LOC', blank=True
    )
    sig_namf = fields.CharField(
        max_length=45, db_column='SIG_NAMF', blank=True
    )
    sig_naml = fields.CharField(
        max_length=200, db_column='SIG_NAML', blank=True
    )
    sig_nams = fields.CharField(
        max_length=10, db_column='SIG_NAMS', blank=True
    )
    sig_namt = fields.CharField(
        max_length=10, db_column='SIG_NAMT', blank=True
    )
    sig_title = fields.CharField(
        max_length=45, db_column='SIG_TITLE', blank=True
    )
    st_agency = fields.CharField(
        max_length=100, db_column='ST_AGENCY', blank=True
    )
    st_leg_yn = fields.IntegerField(
        null=True, db_column='ST_LEG_YN', blank=True
    )
    stmt_firm = fields.CharField(
        max_length=90, db_column='STMT_FIRM', blank=True
    )
    trade_cb = fields.CharField(
        max_length=1, db_column='TRADE_CB', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR_REGISTRATION_CD'
        verbose_name = 'CVR_REGISTRATION_CD'
        verbose_name_plural = 'CVR_REGISTRATION_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class Cvr2RegistrationCd(CalAccessBaseModel):
    """
    Cover page of lobbying dislcosure forms
    """
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    REC_TYPE_CHOICES = (
        ("CVR2", "CVR2"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        max_length=4,
        db_column='REC_TYPE',
        choices=REC_TYPE_CHOICES,
    )
    FORM_TYPE_CHOICES = (
        ('F601', 'Form 601 (Lobbying firm registration statement)'),
        ('F602', 'Form 602 (Lobbying firm activity authorization)'),
        ('F603', 'Form 603 (Lobbyist employer or lobbying coalition \
registration statement)'),
    )
    form_type = fields.CharField(
        max_length=10,
        db_column='FORM_TYPE',
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES,
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('AGY', 'State agency'),
        ('EMP', 'Employer'),
        ('FRM', 'Lobbying firm'),
        ('LBY', 'Lobbyist (an individual)'),
        ('MBR', 'Member of association'),
        ('SCL', 'Subcontracted client'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
    )
    entity_id = fields.CharField(
        verbose_name='Entity ID',
        max_length=9,
        db_column='ENTITY_ID',
        blank=True,
        help_text='Identification number of the entity described by \
the record',
    )
    enty_naml = fields.CharField(
        verbose_name='last name',
        max_length=200,
        db_column='ENTY_NAML',
        blank=True
    )
    enty_namf = fields.CharField(
        verbose_name='first name',
        max_length=45,
        db_column='ENTY_NAMF',
        blank=True
    )
    enty_namt = fields.CharField(
        verbose_name='title',
        max_length=10,
        db_column='ENTY_NAMT',
        blank=True
    )
    enty_nams = fields.CharField(
        verbose_name='title',
        max_length=10,
        db_column='ENTY_NAMS',
        blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR2_REGISTRATION_CD'
        verbose_name = 'CVR2_REGISTRATION_CD'
        verbose_name_plural = 'CVR2_REGISTRATION_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class CvrLobbyDisclosureCd(CalAccessBaseModel):
    """
    Cover page information for the lobbying disclosure forms

        F615 -- Lobbyist Report
        F625 -- Report of Lobbying Firm
        F635 -- Report of Lobbyist Employer and Report of Lobbying Coalition
        F645 -- Report of Person Spending $5,000 or more to influence
                Legislative or administrative action
    """
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    ctrib_n_cb = fields.CharField(
        max_length=1, db_column='CTRIB_N_CB', blank=True
    )
    ctrib_y_cb = fields.CharField(
        max_length=1, db_column='CTRIB_Y_CB', blank=True
    )
    cum_beg_dt = fields.DateField(
        null=True, db_column='CUM_BEG_DT', blank=True
    )
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('CLI', 'CLI (Unknown)'),
        ('FRM', 'Lobbying firm'),
        ('IND', 'Person (Spending > $5,000'),
        ('LBY', 'Lobbyist (an individual)'),
        ('LCO', 'Lobbying coalition'),
        ('LEM', 'Lobbying employer'),
        ('OTH', 'Other'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
    )
    filer_id = fields.CharField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        max_length=8,
        blank=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    filer_namf = fields.CharField(
        max_length=45, db_column='FILER_NAMF', blank=True
    )
    filer_naml = fields.CharField(max_length=200, db_column='FILER_NAML')
    filer_nams = fields.CharField(
        max_length=10, db_column='FILER_NAMS', blank=True
    )
    filer_namt = fields.CharField(
        max_length=10, db_column='FILER_NAMT', blank=True
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    # firm_adr1 = fields.CharField(
    #     max_length=55,
    #     db_column='FIRM_ADR1',
    #     blank=True
    # )
    # firm_adr2 = fields.CharField(
    #     max_length=55,
    #     db_column='FIRM_ADR2',
    #     blank=True
    # )
    firm_city = fields.CharField(
        max_length=30,
        db_column='FIRM_CITY',
        blank=True
    )
    firm_id = fields.CharField(max_length=9, db_column='FIRM_ID', blank=True)
    firm_name = fields.CharField(
        max_length=200,
        db_column='FIRM_NAME',
        blank=True
    )
    firm_phon = fields.CharField(
        max_length=20, db_column='FIRM_PHON', blank=True
    )
    firm_st = fields.CharField(max_length=2, db_column='FIRM_ST', blank=True)
    firm_zip4 = fields.CharField(
        max_length=10, db_column='FIRM_ZIP4', blank=True
    )
    FORM_TYPE_CHOICES = (
        ('F615', ''),
        ('F625', ''),
        ('F635', ''),
        ('F645', ''),
    )
    form_type = fields.CharField(
        max_length=4,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
    )
    from_date = fields.DateField(db_column='FROM_DATE', null=True)
    lby_actvty = fields.CharField(
        max_length=400, db_column='LBY_ACTVTY', blank=True
    )
    lobby_n_cb = fields.CharField(
        max_length=1, db_column='LOBBY_N_CB', blank=True
    )
    lobby_y_cb = fields.CharField(
        max_length=1, db_column='LOBBY_Y_CB', blank=True
    )
    # mail_adr1 = fields.CharField(
    #     max_length=55, db_column='MAIL_ADR1', blank=True
    # )
    # mail_adr2 = fields.CharField(
    #     max_length=55, db_column='MAIL_ADR2', blank=True
    # )
    mail_city = fields.CharField(
        max_length=30, db_column='MAIL_CITY', blank=True
    )
    mail_phon = fields.CharField(
        max_length=20, db_column='MAIL_PHON', blank=True
    )
    mail_st = fields.CharField(
        max_length=2, db_column='MAIL_ST', blank=True
    )
    mail_zip4 = fields.CharField(
        max_length=10, db_column='MAIL_ZIP4', blank=True
    )
    major_namf = fields.CharField(
        max_length=45, db_column='MAJOR_NAMF', blank=True
    )
    major_naml = fields.CharField(
        max_length=200, db_column='MAJOR_NAML', blank=True
    )
    major_nams = fields.CharField(
        max_length=10, db_column='MAJOR_NAMS', blank=True
    )
    major_namt = fields.CharField(
        max_length=10, db_column='MAJOR_NAMT', blank=True
    )
    nopart1_cb = fields.CharField(
        max_length=1, db_column='NOPART1_CB', blank=True
    )
    nopart2_cb = fields.CharField(
        max_length=1, db_column='NOPART2_CB', blank=True
    )
    part1_1_cb = fields.CharField(
        max_length=1, db_column='PART1_1_CB', blank=True
    )
    part1_2_cb = fields.CharField(
        max_length=1, db_column='PART1_2_CB', blank=True
    )
    prn_namf = fields.CharField(
        max_length=45, db_column='PRN_NAMF', blank=True
    )
    prn_naml = fields.CharField(
        max_length=200, db_column='PRN_NAML', blank=True
    )
    prn_nams = fields.CharField(
        max_length=10, db_column='PRN_NAMS', blank=True
    )
    prn_namt = fields.CharField(
        max_length=10, db_column='PRN_NAMT', blank=True
    )
    rcpcmte_id = fields.CharField(
        max_length=9, db_column='RCPCMTE_ID', blank=True
    )
    rcpcmte_nm = fields.CharField(
        max_length=200, db_column='RCPCMTE_NM', blank=True
    )
    REC_TYPE_CHOICES = (
        ("CVR", "CVR"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    report_num = fields.CharField(max_length=3, db_column='REPORT_NUM')
    rpt_date = fields.DateField(db_column='RPT_DATE', null=True)
    sender_id = fields.CharField(max_length=9, db_column='SENDER_ID')
    sig_date = fields.DateField(db_column='SIG_DATE', null=True)
    sig_loc = fields.CharField(max_length=45, db_column='SIG_LOC', blank=True)
    sig_namf = fields.CharField(
        max_length=45, db_column='SIG_NAMF', blank=True
    )
    sig_naml = fields.CharField(
        max_length=200, db_column='SIG_NAML', blank=True
    )
    sig_nams = fields.CharField(
        max_length=10, db_column='SIG_NAMS', blank=True
    )
    sig_namt = fields.CharField(
        max_length=10, db_column='SIG_NAMT', blank=True
    )
    sig_title = fields.CharField(
        max_length=45, db_column='SIG_TITLE', blank=True
    )
    thru_date = fields.DateField(db_column='THRU_DATE', null=True)

    class Meta:
        app_label = "calaccess_raw"
        db_table = 'CVR_LOBBY_DISCLOSURE_CD'
        verbose_name = 'CVR_LOBBY_DISCLOSURE_CD'
        verbose_name_plural = 'CVR_LOBBY_DISCLOSURE_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class Cvr2LobbyDisclosureCd(CalAccessBaseModel):
    """
    Additional names data for the lobbyist disclosure forms

        F615 -- Lobbyist Report
        F625 -- Report of Lobbying Firm
        F635 -- Report of Lobbyist Employer and Report of Lobbying Coalition
        F645 -- Report of Person Spending $5,000 or more to influence
                Legislative or administrative action
    """
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('EMP', 'Employer'),
        ('OFF', 'Officer (responsible)'),
        ('OWN', 'Owner'),
        ('PTM', 'PTM (Unknown)'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
    )
    entity_id = fields.CharField(
        max_length=9, db_column='ENTITY_ID', blank=True
    )
    enty_namf = fields.CharField(
        max_length=45, db_column='ENTY_NAMF', blank=True
    )
    enty_naml = fields.CharField(
        max_length=200, db_column='ENTY_NAML', blank=True
    )
    enty_nams = fields.CharField(
        max_length=10, db_column='ENTY_NAMS', blank=True
    )
    enty_namt = fields.CharField(
        max_length=10, db_column='ENTY_NAMT', blank=True
    )
    enty_title = fields.CharField(
        max_length=45, db_column='ENTY_TITLE', blank=True
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = (
        ('F625', ''),
        ('F635', ''),
    )
    form_type = fields.CharField(
        max_length=4,
        db_column='FORM_TYPE',
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES,
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    REC_TYPE_CHOICES = (
        ("CVR2", "CVR2"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR2_LOBBY_DISCLOSURE_CD'
        verbose_name = 'CVR2_LOBBY_DISCLOSURE_CD'
        verbose_name_plural = 'CVR2_LOBBY_DISCLOSURE_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class LobbyAmendmentsCd(CalAccessBaseModel):
    """
    Lobbyist registration amendment information

        Form 605 Part I
    """
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    REC_TYPE_CHOICES = (
        ("F605", "F605"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    FORM_TYPE_CHOICES = (
        ('F601', ''),
        ('F603', ''),
    )
    form_type = fields.CharField(
        max_length=9,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
    )
    exec_date = fields.CharField(max_length=22, db_column='EXEC_DATE')
    from_date = fields.CharField(max_length=22, db_column='FROM_DATE')
    thru_date = fields.CharField(max_length=22, db_column='THRU_DATE')
    add_l_cb = fields.CharField(
        max_length=1, db_column='ADD_L_CB', blank=True
    )
    add_l_eff = fields.DateField(null=True, db_column='ADD_L_EFF', blank=True)
    a_l_naml = fields.CharField(
        max_length=200, db_column='A_L_NAML', blank=True
    )
    a_l_namf = fields.CharField(
        max_length=45, db_column='A_L_NAMF', blank=True
    )
    a_l_namt = fields.CharField(
        max_length=10, db_column='A_L_NAMT', blank=True
    )
    a_l_nams = fields.CharField(
        max_length=10, db_column='A_L_NAMS', blank=True
    )
    del_l_cb = fields.CharField(
        max_length=8, db_column='DEL_L_CB', blank=True
    )
    del_l_eff = fields.CharField(
        max_length=22, db_column='DEL_L_EFF', blank=True
    )
    d_l_naml = fields.CharField(
        max_length=56, db_column='D_L_NAML', blank=True
    )
    d_l_namf = fields.CharField(
        max_length=35, db_column='D_L_NAMF', blank=True
    )
    d_l_namt = fields.CharField(
        max_length=10, db_column='D_L_NAMT', blank=True
    )
    d_l_nams = fields.CharField(
        max_length=8, db_column='D_L_NAMS', blank=True
    )
    add_le_cb = fields.CharField(
        max_length=1, db_column='ADD_LE_CB', blank=True
    )
    add_le_eff = fields.DateField(
        null=True, db_column='ADD_LE_EFF', blank=True
    )
    a_le_naml = fields.CharField(
        max_length=200, db_column='A_LE_NAML', blank=True
    )
    a_le_namf = fields.CharField(
        max_length=45, db_column='A_LE_NAMF', blank=True
    )
    a_le_namt = fields.CharField(
        max_length=10, db_column='A_LE_NAMT', blank=True
    )
    a_le_nams = fields.CharField(
        max_length=10, db_column='A_LE_NAMS', blank=True
    )
    del_le_cb = fields.CharField(
        max_length=9, db_column='DEL_LE_CB', blank=True
    )
    del_le_eff = fields.CharField(
        max_length=22, db_column='DEL_LE_EFF', blank=True
    )
    d_le_naml = fields.CharField(
        max_length=160, db_column='D_LE_NAML', blank=True
    )
    d_le_namf = fields.CharField(
        max_length=45, db_column='D_LE_NAMF', blank=True
    )
    d_le_namt = fields.CharField(
        max_length=12, db_column='D_LE_NAMT', blank=True
    )
    d_le_nams = fields.CharField(
        max_length=9, db_column='D_LE_NAMS', blank=True
    )
    add_lf_cb = fields.CharField(
        max_length=1, db_column='ADD_LF_CB', blank=True
    )
    add_lf_eff = fields.DateField(
        null=True, db_column='ADD_LF_EFF', blank=True
    )
    a_lf_name = fields.CharField(
        max_length=200, db_column='A_LF_NAME', blank=True
    )
    del_lf_cb = fields.CharField(
        max_length=1, db_column='DEL_LF_CB', blank=True
    )
    del_lf_eff = fields.DateField(
        null=True, db_column='DEL_LF_EFF', blank=True
    )
    d_lf_name = fields.CharField(
        max_length=200, db_column='D_LF_NAME', blank=True
    )
    other_cb = fields.CharField(
        max_length=1, db_column='OTHER_CB', blank=True
    )
    other_eff = fields.DateField(
        null=True, db_column='OTHER_EFF', blank=True
    )
    other_desc = fields.CharField(
        max_length=100, db_column='OTHER_DESC', blank=True
    )
    f606_yes = fields.CharField(
        max_length=1, db_column='F606_YES', blank=True
    )
    f606_no = fields.CharField(
        max_length=1, db_column='F606_NO', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBY_AMENDMENTS_CD'
        verbose_name = 'LOBBY_AMENDMENTS_CD'
        verbose_name_plural = 'LOBBY_AMENDMENTS_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class F690P2Cd(CalAccessBaseModel):
    """
    Amends lobbying disclosure filings

        F690 Amendment to Lobbying Disclosure Report
    """
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    REC_TYPE_CHOICES = (
        ("F690", "F690"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    FORM_TYPE_CHOICES = (
        ('F615', ''),
        ('F625', ''),
        ('F635', ''),
        ('F645', ''),
    )
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=4,
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
    )
    exec_date = fields.DateField(
        db_column='EXEC_DATE',
        null=True,
        help_text="date the original report (or prior amendment to \
the original report) was executed on."
    )
    from_date = fields.DateField(
        db_column='FROM_DATE',
        null=True,
        help_text="reporting period from date of original report"
    )
    thru_date = fields.DateField(
        db_column='THRU_DATE',
        null=True,
        help_text="report period to/through date of original."
    )
    chg_parts = fields.CharField(
        db_column='CHG_PARTS',
        max_length=100,
        blank=True,
        help_text="amended into affects items on part(s) text description."
    )
    chg_sects = fields.CharField(
        db_column='CHG_SECTS',
        max_length=100,
        blank=True,
        help_text="amended into affects items on sections(s) \
text description."
    )
    amend_txt1 = fields.CharField(
        db_column='AMEND_TXT1',
        max_length=330,
        blank=True,
        help_text="description of changes to the filing"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'F690P2_CD'
        verbose_name = 'F690P2_CD'
        verbose_name_plural = 'F690P2_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class LattCd(CalAccessBaseModel):
    """
    Lobbyist disclosure attachment schedules for payments
        F630 -- Payments made to Lobbying Coalitions (Attatchment)
        F635C -- Payments received by Lobbying Coalitions (Attatchment)
        F640 -- Government Agencies Reporting of "Other Payments to Influence
                Legislative or Administrative Action" (Attatchment)
    """
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    amount = fields.DecimalField(
        max_digits=16,
        decimal_places=2,
        db_column='AMOUNT'
    )
    cum_amt = fields.DecimalField(
        max_digits=16,
        decimal_places=2,
        db_column='CUM_AMT'
    )
    cumbeg_dt = fields.DateField(db_column='CUMBEG_DT', null=True)
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('FRM', 'Lobbying firm'),
        ('IND', 'Person (Spending > $5,000'),
        ('LBY', 'Lobbyist (an individual)'),
        ('LCO', 'Lobbying coalition'),
        ('LEM', 'Lobbying employer'),
        ('OTH', 'Other'),
        ('RCP', 'Recipient committee'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = (
        ('S630', ''),
        ('S635-C', ''),
        ('S640', ''),
    )
    form_type = fields.CharField(
        max_length=6,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    memo_code = fields.CharField(
        max_length=1,
        db_column='MEMO_CODE',
        blank=True
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True
    )
    pmt_date = fields.DateField(db_column='PMT_DATE', null=True)
    REC_TYPE_CHOICES = (
        ("LATT", "LATT"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    # recip_adr1 = fields.CharField(
    #     max_length=55,
    #     db_column='RECIP_ADR1',
    #     blank=True
    # )
    # recip_adr2 = fields.CharField(
    #     max_length=55,
    #     db_column='RECIP_ADR2',
    #     blank=True
    # )
    recip_city = fields.CharField(
        max_length=30,
        db_column='RECIP_CITY',
        blank=True
    )
    recip_namf = fields.CharField(
        max_length=45,
        db_column='RECIP_NAMF',
        blank=True
    )
    recip_naml = fields.CharField(
        max_length=200,
        db_column='RECIP_NAML',
        blank=True
    )
    recip_nams = fields.CharField(
        max_length=10,
        db_column='RECIP_NAMS',
        blank=True
    )
    recip_namt = fields.CharField(
        max_length=10,
        db_column='RECIP_NAMT',
        blank=True
    )
    recip_st = fields.CharField(
        max_length=2,
        db_column='RECIP_ST',
        blank=True
    )
    recip_zip4 = fields.CharField(
        max_length=10,
        db_column='RECIP_ZIP4',
        blank=True
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LATT_CD'
        verbose_name = 'LATT_CD'
        verbose_name_plural = 'LATT_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class LexpCd(CalAccessBaseModel):
    """
    Lobbying Activity Expenditure Schedule information (Gifts)
    Reported in filings of the forms

        F615 Part 1
        F625 Part 3A
        F635 Part 3C
        F645 Part 2A
    """
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    amount = fields.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='AMOUNT', blank=True
    )
    bakref_tid = fields.CharField(
        max_length=20, db_column='BAKREF_TID', blank=True
    )
    bene_amt = fields.CharField(
        max_length=12, db_column='BENE_AMT', blank=True
    )
    bene_name = fields.CharField(
        max_length=90, db_column='BENE_NAME', blank=True
    )
    bene_posit = fields.CharField(
        max_length=90, db_column='BENE_POSIT', blank=True
    )
    credcardco = fields.CharField(
        max_length=200, db_column='CREDCARDCO', blank=True
    )
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('IND', 'Person (Spending > $5,000'),
        ('OTH', 'Other'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
    )
    expn_date = fields.DateField(null=True, db_column='EXPN_DATE', blank=True)
    expn_dscr = fields.CharField(
        max_length=90, db_column='EXPN_DSCR', blank=True
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = (
        ('F615P1', ''),
        ('F625P3A', ''),
        ('F635P3C', ''),
        ('F645P2A', ''),
    )
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    memo_code = fields.CharField(
        max_length=1, db_column='MEMO_CODE', blank=True
    )
    memo_refno = fields.CharField(
        max_length=20, db_column='MEMO_REFNO', blank=True
    )
    # payee_adr1 = fields.CharField(
    #     max_length=55, db_column='PAYEE_ADR1', blank=True
    # )
    # payee_adr2 = fields.CharField(
    #     max_length=55, db_column='PAYEE_ADR2', blank=True
    # )
    payee_city = fields.CharField(
        max_length=30, db_column='PAYEE_CITY', blank=True
    )
    payee_namf = fields.CharField(
        max_length=45, db_column='PAYEE_NAMF', blank=True
    )
    payee_naml = fields.CharField(
        max_length=200, db_column='PAYEE_NAML', blank=True
    )
    payee_nams = fields.CharField(
        max_length=10, db_column='PAYEE_NAMS', blank=True
    )
    payee_namt = fields.CharField(
        max_length=10, db_column='PAYEE_NAMT', blank=True
    )
    payee_st = fields.CharField(
        max_length=2, db_column='PAYEE_ST', blank=True
    )
    payee_zip4 = fields.CharField(
        max_length=10, db_column='PAYEE_ZIP4', blank=True
    )
    REC_TYPE_CHOICES = (
        ("LEXP", "LEXP"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    recsubtype = fields.CharField(max_length=1, db_column='RECSUBTYPE')
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LEXP_CD'
        verbose_name = 'LEXP_CD'
        verbose_name_plural = 'LEXP_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class LccmCd(CalAccessBaseModel):
    """
    Lobbying Campaign Contributions reported on forms

        F615 Part 2
        F625 Part 4B
        F635 Part 4B
        F645 Part 3B
    """
    # acct_name = fields.CharField(
    #     max_length=90, db_column='ACCT_NAME', blank=True
    # )
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    amount = fields.DecimalField(
        max_digits=16, decimal_places=2, db_column='AMOUNT'
    )
    bakref_tid = fields.CharField(
        max_length=20, db_column='BAKREF_TID', blank=True
    )
    ctrib_date = fields.DateField(db_column='CTRIB_DATE', null=True)
    ctrib_namf = fields.CharField(
        max_length=45, db_column='CTRIB_NAMF', blank=True
    )
    ctrib_naml = fields.CharField(
        max_length=120, db_column='CTRIB_NAML', blank=True
    )
    ctrib_nams = fields.CharField(
        max_length=10, db_column='CTRIB_NAMS', blank=True
    )
    ctrib_namt = fields.CharField(
        max_length=10, db_column='CTRIB_NAMT', blank=True
    )
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('COM', 'Committee'),
        ('CTL', 'Controlling committee'),
        ('RCP', 'Recipient committee')
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = (
        ('F615P2', ''),
        ('F625P4B', ''),
        ('F635P4B', ''),
        ('F645P3B', ''),
    )
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES,
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    memo_code = fields.CharField(
        max_length=1, db_column='MEMO_CODE', blank=True
    )
    memo_refno = fields.CharField(
        max_length=20, db_column='MEMO_REFNO', blank=True
    )
    REC_TYPE_CHOICES = (
        ("LCCM", "LCCM"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    # recip_adr1 = fields.CharField(
    #     max_length=55, db_column='RECIP_ADR1', blank=True
    # )
    # recip_adr2 = fields.CharField(
    #     max_length=55, db_column='RECIP_ADR2', blank=True
    # )
    recip_city = fields.CharField(
        max_length=30, db_column='RECIP_CITY', blank=True
    )
    recip_id = fields.CharField(
        max_length=9, db_column='RECIP_ID', blank=True
    )
    recip_namf = fields.CharField(
        max_length=45, db_column='RECIP_NAMF', blank=True
    )
    recip_naml = fields.CharField(
        max_length=200, db_column='RECIP_NAML', blank=True
    )
    recip_nams = fields.CharField(
        max_length=10, db_column='RECIP_NAMS', blank=True
    )
    recip_namt = fields.CharField(
        max_length=10, db_column='RECIP_NAMT', blank=True
    )
    recip_st = fields.CharField(
        max_length=2, db_column='RECIP_ST', blank=True
    )
    recip_zip4 = fields.CharField(
        max_length=10, db_column='RECIP_ZIP4', blank=True
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LCCM_CD'
        verbose_name = 'LCCM_CD'
        verbose_name_plural = 'LCCM_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class LothCd(CalAccessBaseModel):
    """
    Payment to other lobbying firms reported on form

        F625 Part 3B
    """
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    amount = fields.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='AMOUNT', blank=True
    )
    cum_amt = fields.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='CUM_AMT', blank=True
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    # firm_adr1 = fields.CharField(
    #     max_length=55, db_column='FIRM_ADR1', blank=True
    # )
    # firm_adr2 = fields.CharField(
    #     max_length=55, db_column='FIRM_ADR2', blank=True
    # )
    firm_city = fields.CharField(
        max_length=30, db_column='FIRM_CITY', blank=True
    )
    firm_name = fields.CharField(
        max_length=200, db_column='FIRM_NAME', blank=True
    )
    firm_phon = fields.CharField(
        max_length=20, db_column='FIRM_PHON', blank=True
    )
    firm_st = fields.CharField(
        max_length=2, db_column='FIRM_ST', blank=True
    )
    firm_zip4 = fields.CharField(
        max_length=10, db_column='FIRM_ZIP4', blank=True
    )
    FORM_TYPE_CHOICES = (
        ('F625P3B', ''),
    )
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    memo_code = fields.CharField(
        max_length=1, db_column='MEMO_CODE', blank=True
    )
    memo_refno = fields.CharField(
        max_length=20, db_column='MEMO_REFNO', blank=True
    )
    pmt_date = fields.DateField(
        null=True, db_column='PMT_DATE', blank=True
    )
    REC_TYPE_CHOICES = (
        ("LOTH", "LOTH"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    subj_namf = fields.CharField(
        max_length=45, db_column='SUBJ_NAMF', blank=True
    )
    subj_naml = fields.CharField(
        max_length=200, db_column='SUBJ_NAML', blank=True
    )
    subj_nams = fields.CharField(
        max_length=45, db_column='SUBJ_NAMS', blank=True
    )
    subj_namt = fields.CharField(
        max_length=45, db_column='SUBJ_NAMT', blank=True
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOTH_CD'
        verbose_name = 'LOTH_CD'
        verbose_name_plural = 'LOTH_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class LempCd(CalAccessBaseModel):
    """
    Lobbyist Employers/Subcontracted Clients data from

        F601 -- Lobbying Firm Registration Statement
        F601 Part 2 A
        F601 Part 2 B
    """
    agencylist = fields.CharField(
        max_length=200, db_column='AGENCYLIST', blank=True
    )
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    # cli_adr1 = fields.CharField(
    #     max_length=55, db_column='CLI_ADR1', blank=True
    # )
    # cli_adr2 = fields.CharField(
    #     max_length=55, db_column='CLI_ADR2', blank=True
    # )
    cli_city = fields.CharField(max_length=30, db_column='CLI_CITY')
    cli_namf = fields.CharField(
        max_length=45, db_column='CLI_NAMF', blank=True
    )
    cli_naml = fields.CharField(max_length=200, db_column='CLI_NAML')
    cli_nams = fields.CharField(
        max_length=10, db_column='CLI_NAMS', blank=True
    )
    cli_namt = fields.CharField(
        max_length=10, db_column='CLI_NAMT', blank=True
    )
    cli_phon = fields.CharField(
        max_length=20, db_column='CLI_PHON', blank=True
    )
    cli_st = fields.CharField(max_length=2, db_column='CLI_ST', blank=True)
    cli_zip4 = fields.CharField(max_length=10, db_column='CLI_ZIP4', help_text='Employing client zipcode')
    client_id = fields.CharField(
        max_length=9, db_column='CLIENT_ID', blank=True
    )
    con_period = fields.CharField(
        max_length=30, db_column='CON_PERIOD', blank=True
    )
    descrip = fields.CharField(
        max_length=100, db_column='DESCRIP', blank=True, help_text='Description of employer/client lobbying interest'
    )
    eff_date = fields.DateField(null=True, db_column='EFF_DATE', blank=True, help_text='Effective Date of Lobbying Contract')
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = (
        ('F601P2A', ''),
        ('F601P2B', ''),
    )
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    REC_TYPE_CHOICES = (
        ("LEMP", "LEMP"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    # sub_adr1 = fields.CharField(
    #     max_length=55, db_column='SUB_ADR1', blank=True
    # )
    # sub_adr2 = fields.CharField(
    #     max_length=55, db_column='SUB_ADR2', blank=True
    # )
    sub_city = fields.CharField(
        max_length=30, db_column='SUB_CITY', blank=True, help_text='Sub-contracting lobbying firm city'
    )
    sub_name = fields.CharField(
        max_length=200, db_column='SUB_NAME', blank=True, help_text='sub-contracting lobbying firms name'
    )
    sub_phon = fields.CharField(
        max_length=20, db_column='SUB_PHON', blank=True
    )
    sub_st = fields.CharField(max_length=2, db_column='SUB_ST', blank=True)
    sub_zip4 = fields.CharField(
        max_length=10, db_column='SUB_ZIP4', blank=True
    )
    subfirm_id = fields.CharField(
        max_length=9, db_column='SUBFIRM_ID', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LEMP_CD'
        verbose_name = 'LEMP_CD'
        verbose_name_plural = 'LEMP_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class LpayCd(CalAccessBaseModel):
    """
    Payments made/received to/from Lobbying Firms reported on forms

        F625 Part 2
        F635 Part 3B
    """
    advan_amt = fields.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='ADVAN_AMT', blank=True
    )
    advan_dscr = fields.CharField(
        max_length=100, db_column='ADVAN_DSCR', blank=True
    )
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    bakref_tid = fields.CharField(
        max_length=20, db_column='BAKREF_TID', blank=True
    )
    cum_total = fields.DecimalField(
        decimal_places=2, max_digits=14, db_column='CUM_TOTAL'
    )
    # emplr_adr1 = fields.CharField(
    #     max_length=55, db_column='EMPLR_ADR1', blank=True
    # )
    # emplr_adr2 = fields.CharField(
    #     max_length=55, db_column='EMPLR_ADR2', blank=True
    # )
    emplr_city = fields.CharField(
        max_length=30, db_column='EMPLR_CITY', blank=True
    )
    emplr_id = fields.CharField(
        max_length=9, db_column='EMPLR_ID', blank=True
    )
    emplr_namf = fields.CharField(
        max_length=45, db_column='EMPLR_NAMF', blank=True
    )
    emplr_naml = fields.CharField(max_length=200, db_column='EMPLR_NAML')
    emplr_nams = fields.CharField(
        max_length=10, db_column='EMPLR_NAMS', blank=True
    )
    emplr_namt = fields.CharField(
        max_length=10, db_column='EMPLR_NAMT', blank=True
    )
    emplr_phon = fields.CharField(
        max_length=20, db_column='EMPLR_PHON', blank=True
    )
    emplr_st = fields.CharField(
        max_length=2, db_column='EMPLR_ST', blank=True
    )
    emplr_zip4 = fields.CharField(
        max_length=10, db_column='EMPLR_ZIP4', blank=True
    )
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('128', '128 (Unknown)'),
        ('FRM', 'Lobbying firm'),
        ('LCO', 'Lobbying coalition'),
        ('LEM', 'Lobbying employer'),
        ('OTH', 'Other'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
    )
    fees_amt = fields.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='FEES_AMT', blank=True
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = (
        ('F625P2', ''),
        ('F635P3B', ''),
    )
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
    )
    lby_actvty = fields.CharField(
        max_length=200, db_column='LBY_ACTVTY', blank=True
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    memo_code = fields.CharField(
        max_length=1, db_column='MEMO_CODE', blank=True
    )
    memo_refno = fields.CharField(
        max_length=20, db_column='MEMO_REFNO', blank=True
    )
    per_total = fields.DecimalField(
        decimal_places=2, max_digits=14, db_column='PER_TOTAL'
    )
    REC_TYPE_CHOICES = (
        ("LPAY", "LPAY"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    reimb_amt = fields.DecimalField(
        decimal_places=2, null=True, max_digits=14,
        db_column='REIMB_AMT', blank=True
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LPAY_CD'
        verbose_name = 'LPAY_CD'
        verbose_name_plural = 'LPAY_CD'

    def __str__(self):
        return str(self.filing_id)
