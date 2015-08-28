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
    #   max_length=55,
    #   db_column='A_B_ADR1',
    #   blank=True,
    #   help_text="First line of individual or business entity address"
    # )
    # a_b_adr2 = fields.CharField(
    #   max_length=55,
    #   db_column='A_B_ADR2',
    #   blank=True,
    #   help_text="Second line of individual or business entity address"
    # )
    a_b_city = fields.CharField(
        max_length=30,
        db_column='A_B_CITY',
        blank=True,
        help_text='Individual or business entity city',
    )
    a_b_name = fields.CharField(
        max_length=200,
        db_column='A_B_NAME',
        blank=True,
        help_text='Name of individual or business entity',
    )
    a_b_st = fields.CharField(
        max_length=2,
        db_column='A_B_ST',
        blank=True,
        help_text='Individual or business entity state',
    )
    a_b_zip4 = fields.CharField(
        max_length=10,
        db_column='A_B_ZIP4',
        blank=True,
        help_text='Individual or business entity ZIP Code.',
    )
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    # auth_adr1 = fields.CharField(
    #   max_length=55,
    #   db_column='AUTH_ADR1',
    #   blank=True,
    #   help_text='First line of authorized lobbying firm business address',
    # )
    # auth_adr2 = fields.CharField(
    #   max_length=55,
    #   db_column='AUTH_ADR2',
    #   blank=True,
    #   help_text='Second line of authorized lobbying firm business address',
    # )
    auth_city = fields.CharField(
        max_length=30,
        db_column='AUTH_CITY',
        blank=True,
        help_text='Authorized lobbying firm business address city',
    )
    auth_name = fields.CharField(
        max_length=200,
        db_column='AUTH_NAME',
        blank=True,
        help_text='Authorized lobbying firm business name. \
Applies to Form 602.',
    )
    auth_st = fields.CharField(
        max_length=2,
        db_column='AUTH_ST',
        blank=True,
        help_text='Authorized lobbying firm business address state',
    )
    auth_zip4 = fields.CharField(
        max_length=10,
        db_column='AUTH_ZIP4',
        blank=True,
        help_text='Authorized lobbying firm business address ZIP Code',
    )
    # bus_adr1 = fields.CharField(
    #   max_length=55,
    #   db_column='BUS_ADR1',
    #   blank=True,
    #   help_text='First line of filer business street address',
    # )
    # bus_adr2 = fields.CharField(
    #   max_length=55,
    #   db_column='BUS_ADR2',
    #   blank=True,
    #   help_text='Second line of filer business street address',
    # )
    bus_cb = fields.CharField(
        max_length=1,
        db_column='BUS_CB',
        blank=True,
        help_text='Business included activity checkbox',
    )
    bus_city = fields.CharField(
        max_length=30,
        db_column='BUS_CITY',
        help_text='Filer business address city',
    )
    bus_class = fields.CharField(
        max_length=3,
        db_column='BUS_CLASS',
        blank=True,
        help_text='Classifiction values of business related entities. \
This field is exclusive of the business class field. One these \
must be populated but not both.',
    )
    bus_descr = fields.CharField(
        max_length=100,
        db_column='BUS_DESCR',
        blank=True,
        help_text='Description of business classification if coded as other',
    )
    bus_email = fields.CharField(
        max_length=60,
        db_column='BUS_EMAIL',
        blank=True,
        help_text='Filer business address email',
    )
    bus_fax = fields.CharField(
        max_length=20,
        db_column='BUS_FAX',
        blank=True,
        help_text='Filer business address fax number',
    )
    bus_phon = fields.CharField(
        max_length=20,
        db_column='BUS_PHON',
        blank=True,
        help_text='Filer business address phone number',
    )
    bus_st = fields.CharField(
        max_length=2,
        db_column='BUS_ST',
        blank=True,
        help_text='Filer business address state',
    )
    bus_zip4 = fields.CharField(
        max_length=10,
        db_column='BUS_ZIP4',
        blank=True,
        help_text='Filer business address ZIP Code',
    )
    c_less50 = fields.CharField(
        max_length=1,
        db_column='C_LESS50',
        blank=True,
        help_text='Industry associations with fewer than 50 members \
check this box',
    )
    c_more50 = fields.CharField(
        max_length=1,
        db_column='C_MORE50',
        blank=True,
        help_text='Industry associations with more than 50 \
check this box.',
    )
    complet_dt = fields.DateField(
        null=True,
        db_column='COMPLET_DT',
        blank=True,
        help_text='Ethics orientation class completion date. Applies to \
Form 604. As filed by the lobbyist.',
    )
    descrip_1 = fields.CharField(
        max_length=300,
        db_column='DESCRIP_1',
        blank=True,
        help_text='Description of business activity, industry or other',
    )
    descrip_2 = fields.CharField(
        max_length=300,
        db_column='DESCRIP_2',
        blank=True,
        help_text='Description of specific or other lobbying interest',
    )
    eff_date = fields.DateField(
        null=True,
        db_column='EFF_DATE',
        blank=True,
        help_text='Effective date of authoarization or termination',
    )
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
        max_length=45,
        db_column='FILER_NAMF',
        blank=True,
        help_text='Filer first name',
    )
    filer_naml = fields.CharField(
        max_length=200,
        db_column='FILER_NAML',
        blank=True,
        help_text='Filer last name',
    )
    filer_nams = fields.CharField(
        max_length=10,
        db_column='FILER_NAMS',
        blank=True,
        help_text='Filer suffix',
    )
    filer_namt = fields.CharField(
        max_length=10,
        db_column='FILER_NAMT',
        blank=True,
        help_text='Filer title or prefix',
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
        max_length=200,
        db_column='FIRM_NAME',
        blank=True,
        help_text='Name of the lobbyist employer or firm. Applies to \
Forms 604, 606, 607.',
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
    ind_cb = fields.CharField(
        max_length=1,
        db_column='IND_CB',
        blank=True,
        help_text='Individual checkbox',
    )
    ind_class = fields.CharField(
        max_length=3,
        db_column='IND_CLASS',
        blank=True,
        help_text='Classification values to category industry related \
entities. This field is exclusive of the business class field. One these \
must be populated but not both.',
    )
    ind_descr = fields.CharField(
        max_length=100,
        db_column='IND_DESCR',
        blank=True,
        help_text='Description of industry classification \
if coded as other',
    )
    INFLUEN_YN_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    influen_yn = fields.CharField(
        null=True,
        max_length=1,
        choices=INFLUEN_YN_CHOICES,
        db_column='INFLUEN_YN',
        blank=True,
        help_text='Attempt to influence state legislation',
    )
    l_firm_cb = fields.CharField(
        max_length=1,
        db_column='L_FIRM_CB',
        blank=True,
        help_text="'Lobbying firm within the ... ' checkbox. \
Applies to Form 607.",
    )
    lby_604_cb = fields.CharField(
        max_length=1,
        db_column='LBY_604_CB',
        blank=True,
        help_text="'Lobbying Agency in this 604 statement' checkbox. \
Applies to Form 604.",
    )
    lby_reg_cb = fields.CharField(
        max_length=1,
        db_column='LBY_REG_CB',
        blank=True,
        help_text="'Lobbying Agency in form 601/603 registration \
statement' checkbox. Applies to Form 604.",
    )
    lobby_cb = fields.CharField(
        max_length=1,
        db_column='LOBBY_CB',
        blank=True,
        help_text='\'Lobbying within the meaning...\' checkbox. \
Applies to Form 607.',
    )
    lobby_int = fields.CharField(
        max_length=300,
        db_column='LOBBY_INT',
        blank=True,
        help_text='Description of Part III lobbying interests. \
Applies to Form 603',
    )
    ls_beg_yr = fields.CharField(
        null=True,
        db_column='LS_BEG_YR',
        blank=True,
        max_length=5,
        help_text='Year legislative session begins',
    )
    ls_end_yr = fields.CharField(
        db_column='LS_END_YR',
        max_length=5,
        help_text='Year legislative sessions ends',
    )
    # mail_adr1 = fields.CharField(
    #   max_length=55,
    #   db_column='MAIL_ADR1',
    #   blank=True,
    #   help_text='First line of filer mailing street address',
    # )
    # mail_adr2 = fields.CharField(
    #   max_length=55,
    #   db_column='MAIL_ADR2',
    #   blank=True,
    #   help_text='Second line of filer mailing street address',
    # )
    mail_city = fields.CharField(
        max_length=30,
        db_column='MAIL_CITY',
        blank=True,
        help_text='Filer mailing address city',
    )
    mail_phon = fields.CharField(
        max_length=20,
        db_column='MAIL_PHON',
        blank=True,
        help_text='Filer mailing address phone number',
    )
    mail_st = fields.CharField(
        max_length=2,
        db_column='MAIL_ST',
        blank=True,
        help_text='Filer mailing address state',
    )
    mail_zip4 = fields.CharField(
        max_length=10,
        db_column='MAIL_ZIP4',
        blank=True,
        help_text='Filer mailing address ZIP Code',
    )
    newcert_cb = fields.CharField(
        max_length=1,
        db_column='NEWCERT_CB',
        blank=True,
        help_text='Will require a new certification checkbox. \
Applies to Form 604.',
    )
    oth_cb = fields.CharField(
        max_length=1,
        db_column='OTH_CB',
        blank=True,
        help_text='Other checkbox',
    )
    prn_namf = fields.CharField(
        max_length=45,
        db_column='PRN_NAMF',
        blank=True,
        help_text='Signer first name',
    )
    prn_naml = fields.CharField(
        max_length=200,
        db_column='PRN_NAML',
        blank=True,
        help_text='Signer last name',
    )
    prn_nams = fields.CharField(
        max_length=10,
        db_column='PRN_NAMS',
        blank=True,
        help_text='Signer suffix',
    )
    prn_namt = fields.CharField(
        max_length=10,
        db_column='PRN_NAMT',
        blank=True,
        help_text='Signer title or prefix',
    )
    qual_date = fields.DateField(
        null=True,
        db_column='QUAL_DATE',
        blank=True,
        help_text='Date qualified. Applies to forms 601 and 603. Only \
occurs once in lobbying filings.',
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
        max_length=1,
        db_column='RENCERT_CB',
        blank=True,
        help_text='Will take a renewel certification checkbox. Applies to \
Form 604.',
    )
    report_num = fields.CharField(
        max_length=3,
        db_column='REPORT_NUM',
        blank=True,
        help_text='Amendment number as reported by the filer. 000 is the \
original. 001-999 are amendments.',
    )
    rpt_date = fields.DateField(
        db_column='RPT_DATE',
        null=True,
        help_text='Date this report or amendment is filed, as reported \
by the filer',
    )
    sender_id = fields.CharField(
        max_length=9,
        db_column='SENDER_ID',
        help_text='Identification number of the lobbyist entity submitting \
this report. This is equal to the filer ID if the filer is the submitting \
the report and the firm or employer if they are submitting the report.',
    )
    sig_date = fields.DateField(
        null=True,
        db_column='SIG_DATE',
        blank=True,
        help_text="Date signed"
    )
    sig_loc = fields.CharField(
        max_length=45,
        db_column='SIG_LOC',
        blank=True,
        help_text='Signer city and state',
    )
    sig_namf = fields.CharField(
        max_length=45,
        db_column='SIG_NAMF',
        blank=True,
        help_text='Signer first name',
    )
    sig_naml = fields.CharField(
        max_length=200,
        db_column='SIG_NAML',
        blank=True,
        help_text='Signer last name',
    )
    sig_nams = fields.CharField(
        max_length=10,
        db_column='SIG_NAMS',
        blank=True,
        help_text='Signer suffix',
    )
    sig_namt = fields.CharField(
        max_length=10,
        db_column='SIG_NAMT',
        blank=True,
        help_text='Signer title or prefix',
    )
    sig_title = fields.CharField(
        max_length=45,
        db_column='SIG_TITLE',
        blank=True,
        help_text='Title of signer',
    )
    st_agency = fields.CharField(
        max_length=100,
        db_column='ST_AGENCY',
        blank=True,
        help_text='List of identified state agencies. Applies to Form 604.',
    )
    ST_LEG_YN_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    st_leg_yn = fields.CharField(
        max_length=1,
        db_column='ST_LEG_YN',
        choices=ST_LEG_YN_CHOICES,
        blank=True,
        help_text='Will lobby state legislature checkbox. \
Applies to Form 604.',
    )
    stmt_firm = fields.CharField(
        max_length=90,
        db_column='STMT_FIRM',
        blank=True,
        help_text='Lobby firm named in \'Statement of Responsible Officer\'\
This field only applies to Form 601.',
    )
    trade_cb = fields.CharField(
        max_length=1,
        db_column='TRADE_CB',
        null=True,
        blank=True,
        help_text="Industry, trade or professional checkbox",
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
    exec_date = fields.CharField(
        max_length=22,
        db_column='EXEC_DATE',
        help_text='Date this amendment executed on',
    )
    from_date = fields.CharField(
        max_length=22,
        db_column='FROM_DATE',
        help_text='',
    )
    thru_date = fields.CharField(
        max_length=22,
        db_column='THRU_DATE',
        help_text='Reporting date to/through date of original',
    )
    add_l_cb = fields.CharField(
        max_length=1,
        db_column='ADD_L_CB',
        blank=True,
        help_text='Add lobbyist checkbox',
    )
    add_l_eff = fields.DateField(
        null=True,
        db_column='ADD_L_EFF',
        blank=True,
        help_text='Add lobbyist effective date',
    )
    a_l_naml = fields.CharField(
        max_length=200,
        db_column='A_L_NAML',
        blank=True,
        help_text='Add lobbyist last name',
    )
    a_l_namf = fields.CharField(
        max_length=45,
        db_column='A_L_NAMF',
        blank=True,
        help_text='Add lobbyist first name',
    )
    a_l_namt = fields.CharField(
        max_length=10,
        db_column='A_L_NAMT',
        blank=True,
        help_text='Add lobbyist title or prefix',
    )
    a_l_nams = fields.CharField(
        max_length=10,
        db_column='A_L_NAMS',
        blank=True,
        help_text='Add lobbyist suffix',
    )
    del_l_cb = fields.CharField(
        max_length=8,
        db_column='DEL_L_CB',
        blank=True,
        help_text='Delete lobbyist checkbox',
    )
    del_l_eff = fields.CharField(
        max_length=22,
        db_column='DEL_L_EFF',
        blank=True,
        help_text='Delete lobbyist effective date',
    )
    d_l_naml = fields.CharField(
        max_length=56,
        db_column='D_L_NAML',
        blank=True,
        help_text='Delete lobbyist last name',
    )
    d_l_namf = fields.CharField(
        max_length=35,
        db_column='D_L_NAMF',
        blank=True,
        help_text='Delete lobbyist first name',
    )
    d_l_namt = fields.CharField(
        max_length=10,
        db_column='D_L_NAMT',
        blank=True,
        help_text='Delete lobbyist title or prefix',
    )
    d_l_nams = fields.CharField(
        max_length=8,
        db_column='D_L_NAMS',
        blank=True,
        help_text='Delete lobbyiest suffix',
    )
    add_le_cb = fields.CharField(
        max_length=1,
        db_column='ADD_LE_CB',
        blank=True,
        help_text='Add lobbyiest employer checkbox',
    )
    add_le_eff = fields.DateField(
        null=True,
        db_column='ADD_LE_EFF',
        blank=True,
        help_text='Add lobbyist employer effective date',
    )
    a_le_naml = fields.CharField(
        max_length=200,
        db_column='A_LE_NAML',
        blank=True,
        help_text='Add lobbyist employer last name',
    )
    a_le_namf = fields.CharField(
        max_length=45,
        db_column='A_LE_NAMF',
        blank=True,
        help_text='Add lobbyist or employer first name',
    )
    a_le_namt = fields.CharField(
        max_length=10,
        db_column='A_LE_NAMT',
        blank=True,
        help_text='Add lobbyist employer title or prefix',
    )
    a_le_nams = fields.CharField(
        max_length=10,
        db_column='A_LE_NAMS',
        blank=True,
        help_text='Add lobbyist employer suffix',
    )
    del_le_cb = fields.CharField(
        max_length=9,
        db_column='DEL_LE_CB',
        blank=True,
        help_text='Delete lobbyist employer check box',
    )
    del_le_eff = fields.CharField(
        max_length=22,
        db_column='DEL_LE_EFF',
        blank=True,
        help_text='Delete lobbyist employer effective date',
    )
    d_le_naml = fields.CharField(
        max_length=160,
        db_column='D_LE_NAML',
        blank=True,
        help_text='Delete lobbyist employer last name',
    )
    d_le_namf = fields.CharField(
        max_length=45,
        db_column='D_LE_NAMF',
        blank=True,
        help_text='Delete lobbyiest employer first name',
    )
    d_le_namt = fields.CharField(
        max_length=12,
        db_column='D_LE_NAMT',
        blank=True,
        help_text='Delete lobbyist employer name title or prefix',
    )
    d_le_nams = fields.CharField(
        max_length=9,
        db_column='D_LE_NAMS',
        blank=True,
        help_text='Delete lobbyist employer name',
    )
    add_lf_cb = fields.CharField(
        max_length=1,
        db_column='ADD_LF_CB',
        blank=True,
        help_text='Add lobbying firm checkbox',
    )
    add_lf_eff = fields.DateField(
        null=True,
        db_column='ADD_LF_EFF',
        blank=True,
        help_text='Add lobbying firm effective date',
    )
    a_lf_name = fields.CharField(
        max_length=200,
        db_column='A_LF_NAME',
        blank=True,
        help_text='Add lobbying firm name',
    )
    del_lf_cb = fields.CharField(
        max_length=1,
        db_column='DEL_LF_CB',
        blank=True,
        help_text='Delete lobbying firm checkbox',
    )
    del_lf_eff = fields.DateField(
        null=True,
        db_column='DEL_LF_EFF',
        blank=True,
        help_text='Delete lobbying firm effective date',
    )
    d_lf_name = fields.CharField(
        max_length=200,
        db_column='D_LF_NAME',
        blank=True,
        help_text='Delete lobbying firm name',
    )
    other_cb = fields.CharField(
        max_length=1,
        db_column='OTHER_CB',
        blank=True,
        help_text='Other amendments checkbox',
    )
    other_eff = fields.DateField(
        null=True,
        db_column='OTHER_EFF',
        blank=True,
        help_text='Other amendments effective date',
    )
    other_desc = fields.CharField(
        max_length=100,
        db_column='OTHER_DESC',
        blank=True,
        help_text='Description of changes',
    )
    f606_yes = fields.CharField(
        max_length=1,
        db_column='F606_YES',
        blank=True,
        help_text='Lobbyist ceasing all activity',
    )
    f606_no = fields.CharField(
        max_length=1,
        db_column='F606_NO',
        blank=True,
        help_text='Lobbyist ceasing employment but staying active',
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
        db_column='AMOUNT',
        help_text='Amount of payment',
    )
    cum_amt = fields.DecimalField(
        max_digits=16,
        decimal_places=2,
        db_column='CUM_AMT',
        help_text='Cumulative total to date',
    )
    cumbeg_dt = fields.DateField(
        db_column='CUMBEG_DT',
        null=True,
        help_text='Cumulative period beginning to date',
    )
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
        blank=True,
        help_text='Memo amount flag',
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text='Reference to the text in a TEXT record',
    )
    pmt_date = fields.DateField(
        db_column='PMT_DATE',
        null=True,
        help_text='Date of payment',
    )
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
    #   max_length=55,
    #   db_column='RECIP_ADR1',
    #   blank=True,
    #   help_text='First line of the recipient street address',
    # )
    # recip_adr2 = fields.CharField(
    #   max_length=55,
    #   db_column='RECIP_ADR2',
    #   blank=True,
    #   help_text='Second line of the recipient street address',
    # )
    recip_city = fields.CharField(
        max_length=30,
        db_column='RECIP_CITY',
        blank=True,
        help_text='Recipient city',
    )
    recip_namf = fields.CharField(
        max_length=45,
        db_column='RECIP_NAMF',
        blank=True,
        help_text='Recipient first name',
    )
    recip_naml = fields.CharField(
        max_length=200,
        db_column='RECIP_NAML',
        blank=True,
        help_text='Recipient last name or business name',
    )
    recip_nams = fields.CharField(
        max_length=10,
        db_column='RECIP_NAMS',
        blank=True,
        help_text='Recipient suffix',
    )
    recip_namt = fields.CharField(
        max_length=10,
        db_column='RECIP_NAMT',
        blank=True,
        help_text='Recipient title or prefix',
    )
    recip_st = fields.CharField(
        max_length=2,
        db_column='RECIP_ST',
        blank=True,
        help_text='Recipient state',
    )
    recip_zip4 = fields.CharField(
        max_length=10,
        db_column='RECIP_ZIP4',
        blank=True,
        help_text='Recipient ZIP Code',
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
    Lobbying activity expenditures
    """
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    amount = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='AMOUNT',
        blank=True,
        help_text='Amount of payment',
    )
    bakref_tid = fields.CharField(
        max_length=20,
        db_column='BAKREF_TID',
        blank=True,
        help_text='Backreference to the tranaction identifer of parent record',
    )
    bene_amt = fields.CharField(
        max_length=12,
        db_column='BENE_AMT',
        blank=True,
        help_text='Amount benefiting benficiary',
    )
    bene_name = fields.CharField(
        max_length=90,
        db_column='BENE_NAME',
        blank=True,
        help_text='Name of the person beneifiting',
    )
    bene_posit = fields.CharField(
        max_length=90,
        db_column='BENE_POSIT',
        blank=True,
        help_text='Official position of the person beneifiting',
    )
    credcardco = fields.CharField(
        max_length=200,
        db_column='CREDCARDCO',
        blank=True,
        help_text='Name of the credit card company, if paid using a card',
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
    expn_date = fields.DateField(
        null=True,
        db_column='EXPN_DATE',
        blank=True,
        help_text='Date of expenditure',
    )
    expn_dscr = fields.CharField(
        max_length=90,
        db_column='EXPN_DSCR',
        blank=True,
        help_text='Purpose of the expense and a description or explanation',
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
        max_length=1,
        db_column='MEMO_CODE',
        blank=True,
        help_text='Memo amount flag',
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text='Reference to the text in a TEXT record',
    )
    # payee_adr1 = fields.CharField(
    #   max_length=55,
    #   db_column='PAYEE_ADR1',
    #   blank=True,
    #   help_text='First line of payee street address',
    # )
    # payee_adr2 = fields.CharField(
    #   max_length=55,
    #   db_column='PAYEE_ADR2',
    #   blank=True,
    #   help_text='Second line of payee street address',
    # )
    payee_city = fields.CharField(
        max_length=30,
        db_column='PAYEE_CITY',
        blank=True,
        help_text='Payee city',
    )
    payee_namf = fields.CharField(
        max_length=45,
        db_column='PAYEE_NAMF',
        blank=True,
        help_text='Payee first name',
    )
    payee_naml = fields.CharField(
        max_length=200,
        db_column='PAYEE_NAML',
        blank=True,
        help_text='Payee last name or business name',
    )
    payee_nams = fields.CharField(
        max_length=10,
        db_column='PAYEE_NAMS',
        blank=True,
        help_text='Payee suffix',
    )
    payee_namt = fields.CharField(
        max_length=10,
        db_column='PAYEE_NAMT',
        blank=True,
        help_text='Payee title or prefix',
    )
    payee_st = fields.CharField(
        max_length=2,
        db_column='PAYEE_ST',
        blank=True,
        help_text='Payee state',
    )
    payee_zip4 = fields.CharField(
        max_length=10,
        db_column='PAYEE_ZIP4',
        blank=True,
        help_text='Payee ZIP Code',
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
    REC_SUBTYPE_CHOICES = (
        ('1', 'Main'),
        ('2', 'Detail'),
    )
    recsubtype = fields.CharField(
        max_length=1,
        db_column='RECSUBTYPE',
        choices=REC_SUBTYPE_CHOICES,
        verbose_name='record subtype',
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
        db_table = 'LEXP_CD'
        verbose_name = 'LEXP_CD'
        verbose_name_plural = 'LEXP_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class LccmCd(CalAccessBaseModel):
    """
    Lobbying campaign contributions
    """
    # acct_name = fields.CharField(
    #   max_length=90,
    #   db_column='ACCT_NAME',
    #   blank=True,
    #   help_text='name of separate account'
    # )
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
        db_column='AMOUNT',
        help_text='amount of contribution',
    )
    bakref_tid = fields.CharField(
        max_length=20,
        db_column='BAKREF_TID',
        blank=True,
        help_text='Back reference to transaction identifier of parent record',
    )
    ctrib_date = fields.DateField(
        db_column='CTRIB_DATE',
        null=True,
        help_text='Date of contribution',
    )
    ctrib_namf = fields.CharField(
        max_length=45,
        db_column='CTRIB_NAMF',
        blank=True,
        help_text='Contributor first name',
    )
    ctrib_naml = fields.CharField(
        max_length=120,
        db_column='CTRIB_NAML',
        blank=True,
        help_text='Contributor last name or business name',
    )
    ctrib_nams = fields.CharField(
        max_length=10,
        db_column='CTRIB_NAMS',
        blank=True,
        help_text='Contributor suffix',
    )
    ctrib_namt = fields.CharField(
        max_length=10,
        db_column='CTRIB_NAMT',
        blank=True,
        help_text='Contributor prefix or title.',
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
        max_length=1,
        db_column='MEMO_CODE',
        blank=True,
        help_text='Memo amount flag',
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text='Reference to the text contained in the TEXT record',
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
    #   max_length=55,
    #   db_column='RECIP_ADR1',
    #   blank=True,
    #   help_text='First line of recipient street address'
    # )
    # recip_adr2 = fields.CharField(
    #   max_length=55,
    #   db_column='RECIP_ADR2',
    #   blank=True,
    #   help_text='Second line of recipient street address'
    # )
    recip_city = fields.CharField(
        max_length=30,
        db_column='RECIP_CITY',
        blank=True,
        help_text='Recipient city',
    )
    recip_id = fields.CharField(
        max_length=9,
        db_column='RECIP_ID',
        blank=True,
        help_text='Recipient identification number',
    )
    recip_namf = fields.CharField(
        max_length=45,
        db_column='RECIP_NAMF',
        blank=True,
        help_text='Recipient first name',
    )
    recip_naml = fields.CharField(
        max_length=200,
        db_column='RECIP_NAML',
        blank=True,
        help_text='Recipient last name',
    )
    recip_nams = fields.CharField(
        max_length=10,
        db_column='RECIP_NAMS',
        blank=True,
        help_text='Recipient name suffix',
    )
    recip_namt = fields.CharField(
        max_length=10,
        db_column='RECIP_NAMT',
        blank=True,
        help_text='Recipient name prefix or title',
    )
    recip_st = fields.CharField(
        max_length=2,
        db_column='RECIP_ST',
        blank=True,
        help_text='Recipient state',
    )
    recip_zip4 = fields.CharField(
        max_length=10,
        db_column='RECIP_ZIP4',
        blank=True,
        help_text='Recipient ZIP Code',
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
    Payment to other lobbying firms
    """
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    amount = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='AMOUNT',
        blank=True,
        help_text='Amount of payment',
    )
    cum_amt = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='CUM_AMT',
        blank=True,
        help_text='Cumulative total to date',
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    # firm_adr1 = fields.CharField(
    #   max_length=55,
    #   db_column='FIRM_ADR1',
    #   blank=True,
    #   help_text='First line of firm, employer or coalition\'s address',
    # )
    # firm_adr2 = fields.CharField(
    #   max_length=55,
    #   db_column='FIRM_ADR2',
    #   blank=True,
    #   help_text='Second line of firm, employer or coalition\'s address',
    # )
    firm_city = fields.CharField(
        max_length=30,
        db_column='FIRM_CITY',
        blank=True,
        help_text='Firm, employer or coalition\'s city',
    )
    firm_name = fields.CharField(
        max_length=200,
        db_column='FIRM_NAME',
        blank=True,
        help_text='Firm, employer or coalition\'s name',
    )
    firm_phon = fields.CharField(
        max_length=20,
        db_column='FIRM_PHON',
        blank=True,
        help_text='Firm, employer or coalition\'s phone number',
    )
    firm_st = fields.CharField(
        max_length=2,
        db_column='FIRM_ST',
        blank=True,
        help_text='Firm, employer or coalition\'s ZIP Code',
    )
    firm_zip4 = fields.CharField(
        max_length=10,
        db_column='FIRM_ZIP4',
        blank=True,
        help_text='',
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
        max_length=1,
        db_column='MEMO_CODE',
        blank=True,
        help_text='Memo amount flag',
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text='Reference to text contained in a TEXT record',
    )
    pmt_date = fields.DateField(
        null=True,
        db_column='PMT_DATE',
        blank=True,
        help_text='Date of payment',
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
        max_length=45,
        db_column='SUBJ_NAMF',
        blank=True,
        help_text='First name of employer/client subject of lobbying',
    )
    subj_naml = fields.CharField(
        max_length=200,
        db_column='SUBJ_NAML',
        blank=True,
        help_text='Last name of employer/client subject of lobbying',
    )
    subj_nams = fields.CharField(
        max_length=45,
        db_column='SUBJ_NAMS',
        blank=True,
        help_text='Suffix of employer/client subject of lobbying',
    )
    subj_namt = fields.CharField(
        max_length=45,
        db_column='SUBJ_NAMT',
        blank=True,
        help_text="Prefix or title of employer/client subject of lobbying"
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
    Lobbyist employers and subcontracted clients
    """
    agencylist = fields.CharField(
        max_length=200,
        db_column='AGENCYLIST',
        blank=True,
        help_text='Agencies to be lobbied'
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
    cli_city = fields.CharField(
        max_length=30,
        db_column='CLI_CITY',
        help_text='Employing client city'
    )
    cli_namf = fields.CharField(
        max_length=45,
        db_column='CLI_NAMF',
        blank=True,
        help_text='Employing client first name'
    )
    cli_naml = fields.CharField(
        max_length=200,
        db_column='CLI_NAML',
        help_text='Employing client last name'
    )
    cli_nams = fields.CharField(
        max_length=10,
        db_column='CLI_NAMS',
        blank=True,
        help_text="Employing client suffix"
    )
    cli_namt = fields.CharField(
        max_length=10,
        db_column='CLI_NAMT',
        blank=True,
        help_text='Employing client prefix or title'
    )
    cli_phon = fields.CharField(
        max_length=20,
        db_column='CLI_PHON',
        blank=True,
        help_text="Employing client phone number"
    )
    cli_st = fields.CharField(
        max_length=2,
        db_column='CLI_ST',
        blank=True,
        help_text='Employing client state'
    )
    cli_zip4 = fields.CharField(
        max_length=10,
        db_column='CLI_ZIP4',
        help_text='Employing client ZIP Code'
    )
    client_id = fields.CharField(
        max_length=9,
        db_column='CLIENT_ID',
        blank=True,
        help_text="Identification number of the Part 2A employer or \
Part 2B Client/Employer"
    )
    con_period = fields.CharField(
        max_length=30,
        db_column='CON_PERIOD',
        blank=True,
        help_text="Period of the contract"
    )
    descrip = fields.CharField(
        max_length=100,
        db_column='DESCRIP',
        blank=True,
        help_text='Description of employer/client lobbying interest'
    )
    eff_date = fields.DateField(
        null=True,
        db_column='EFF_DATE',
        blank=True,
        help_text='Effective Date of Lobbying Contract'
    )
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
        max_length=30,
        db_column='SUB_CITY',
        blank=True,
        help_text='Subcontracting lobbying firm city'
    )
    sub_name = fields.CharField(
        max_length=200,
        db_column='SUB_NAME',
        blank=True,
        help_text='Subcontracting lobbying firms name'
    )
    sub_phon = fields.CharField(
        max_length=20,
        db_column='SUB_PHON',
        blank=True,
        help_text='Subcontracting lobbying firm phone number'
    )
    sub_st = fields.CharField(
        max_length=2,
        db_column='SUB_ST',
        blank=True,
        help_text='Subcontracting lobbying firm state'
    )
    sub_zip4 = fields.CharField(
        max_length=10,
        db_column='SUB_ZIP4',
        blank=True,
        help_text='Subcontracting lobbying firm ZIP Code'
    )
    subfirm_id = fields.CharField(
        max_length=9,
        db_column='SUBFIRM_ID',
        blank=True,
        help_text='Identification number of subcontracting lobbying firm'
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
    Payments made or received by lobbying firms
    """
    advan_amt = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='ADVAN_AMT',
        blank=True,
        help_text='Advance and other payments amount',
    )
    advan_dscr = fields.CharField(
        max_length=100,
        db_column='ADVAN_DSCR',
        blank=True,
        help_text='Description of advance and other payments',
    )
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    bakref_tid = fields.CharField(
        max_length=20,
        db_column='BAKREF_TID',
        blank=True,
        help_text='Backreference to transaction identifer of parent record',
    )
    cum_total = fields.DecimalField(
        decimal_places=2,
        max_digits=14,
        db_column='CUM_TOTAL',
        help_text='Cumulative total to date',
    )
    # emplr_adr1 = fields.CharField(
    #   max_length=55,
    #   db_column='EMPLR_ADR1',
    #   blank=True,
    #   help_text='First line of employer street address',
    # )
    # emplr_adr2 = fields.CharField(
    #   max_length=55,
    #   db_column='EMPLR_ADR2',
    #   blank=True,
    #   help_text='Second line of employer street address',
    # )
    emplr_city = fields.CharField(
        max_length=30,
        db_column='EMPLR_CITY',
        blank=True,
        help_text='Employer city',
    )
    emplr_id = fields.CharField(
        max_length=9,
        db_column='EMPLR_ID',
        blank=True,
        help_text='This field is undocumented',
    )
    emplr_namf = fields.CharField(
        max_length=45,
        db_column='EMPLR_NAMF',
        blank=True,
        help_text='Employer first name',
    )
    emplr_naml = fields.CharField(
        max_length=200,
        db_column='EMPLR_NAML',
        help_text='Name of firm, employer or coalition',
    )
    emplr_nams = fields.CharField(
        max_length=10,
        db_column='EMPLR_NAMS',
        blank=True,
        help_text='Employer suffix',
    )
    emplr_namt = fields.CharField(
        max_length=10,
        db_column='EMPLR_NAMT',
        blank=True,
        help_text='Employer title or prefix',
    )
    emplr_phon = fields.CharField(
        max_length=20,
        db_column='EMPLR_PHON',
        blank=True,
        help_text='Employer phone number',
    )
    emplr_st = fields.CharField(
        max_length=2,
        db_column='EMPLR_ST',
        blank=True,
        help_text='Employer state',
    )
    emplr_zip4 = fields.CharField(
        max_length=10,
        db_column='EMPLR_ZIP4',
        blank=True,
        help_text='Employer ZIP Code',
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
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='FEES_AMT',
        blank=True,
        help_text='Fees and retainers amount',
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
        max_length=200,
        db_column='LBY_ACTVTY',
        blank=True,
        help_text='Description of lobbying activity',
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    memo_code = fields.CharField(
        max_length=1,
        db_column='MEMO_CODE',
        blank=True,
        help_text='Memo amount flag',
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text='Reference to the text contained in a TEXT record',
    )
    per_total = fields.DecimalField(
        decimal_places=2,
        max_digits=14,
        db_column='PER_TOTAL',
        help_text='Total this reporting period',
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
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='REIMB_AMT',
        blank=True,
        help_text='Reimbursements of expense amount',
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
