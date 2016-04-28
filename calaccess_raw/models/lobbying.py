#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .base import CalAccessBaseModel
from calaccess_raw import fields
from calaccess_raw.annotations import DocumentCloud, choices
from calaccess_raw.annotations.filing_forms import get_filing_form
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class CvrRegistrationCd(CalAccessBaseModel):
    """
    Cover page of lobbying disclosure forms (601, 602, 603, 604, 606, and 607)
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=8),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=35, end_page=39),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=22, end_page=27),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=68, end_page=71),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=82, end_page=86),
    ]
    FILING_FORMS = [
        get_filing_form('F601'),
        get_filing_form('F602'),
        get_filing_form('F603'),
        get_filing_form('F604'),
        get_filing_form('F606'),
        get_filing_form('F607'),
    ]
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
    BUS_CLASS_CHOICES = (
        ("ENT", "Entertainment/Recreation"),
        ("FIN", "Finance/Insurance"),
        ("LOG", "Lodging/Restaurants"),
        ("MAN", "Manufacturing/Industrial"),
        ("MER", "Merchandise/Retail"),
        ("OIL", "Oil and Gas"),
        ("OTH", "Other"),
        ("PRO", "Professional/Trade"),
        ("REA", "Real Estate"),
        ("TRN", "Transportation")
    )
    bus_class = fields.CharField(
        max_length=3,
        db_column='BUS_CLASS',
        blank=True,
        choices=BUS_CLASS_CHOICES,
        help_text='Classifiction values of business related entities. \
This field is exclusive of the business class field. One these \
must be populated but not both.',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=70),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=82),
        ]
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
        ('BUS', 'Unknown'),
        ('FRM', choices.LOBBYING_ENTITY_CODES['FRM']),
        ('LBY', choices.LOBBYING_ENTITY_CODES['LBY']),
        ('LCO', choices.LOBBYING_ENTITY_CODES['LCO']),
        ('LEM', choices.LOBBYING_ENTITY_CODES['LEM']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712034-Cal-Format-201', start_page=82),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=68),
        ]
    )
    filer_id = fields.CharField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        max_length=9,
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
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=4,
        db_column='FORM_TYPE',
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=68),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=82),
        ]
    )
    ind_cb = fields.CharField(
        max_length=1,
        db_column='IND_CB',
        blank=True,
        help_text='Individual checkbox',
    )
    IND_CLASS_CHOICES = (
        ("AGR", "Agriculture"),
        ("EDU", "Education"),
        ("GOV", "Government"),
        ("HEA", "Health"),
        ("LAB", "Labor Unions"),
        ("LEG", "Legal"),
        ("OTH", "Other"),
        ("POL", "Political Organizations"),
        ("PUB", "Public Employees"),
        ("UTL", "Utilities")
    )
    ind_class = fields.CharField(
        max_length=3,
        db_column='IND_CLASS',
        blank=True,
        choices=IND_CLASS_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712034-Cal-Format-201', start_page=85),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=70),
        ],
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
        ('X', 'Yes'),
        ('n', 'No'),
    )
    influen_yn = fields.CharField(
        null=True,
        max_length=1,
        choices=INFLUEN_YN_CHOICES,
        db_column='INFLUEN_YN',
        blank=True,
        help_text='Attempt to influence state legislation',
        documentcloud_pages=[
            DocumentCloud(id='2712034-Cal-Format-201', start_page=86),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=71),
        ]
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
        ('y', 'Yes'),
        ('N', 'No'),
        ('n', 'No'),
        ('X', 'Yes'),
        ('x', 'Yes'),
    )
    st_leg_yn = fields.CharField(
        max_length=1,
        db_column='ST_LEG_YN',
        choices=ST_LEG_YN_CHOICES,
        blank=True,
        help_text='Will lobby state legislature checkbox. \
Applies to Form 604.',
        documentcloud_pages=[
            DocumentCloud(id='2712034-Cal-Format-201', start_page=86),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=71),
        ]
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
    Cover page of lobbying disclosure forms
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=44, end_page=45),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=37, end_page=37),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=72, end_page=73),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=87, end_page=88),
    ]
    FILING_FORMS = [
        get_filing_form('F601'),
        get_filing_form('F602'),
        get_filing_form('F603'),
    ]
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
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=10,
        db_column='FORM_TYPE',
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=72),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=87),
        ]
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
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-format.html#document/p9
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
        max_length=200,
        db_column='ENTY_NAML',
        blank=True,
        help_text='Entity last name',
    )
    enty_namf = fields.CharField(
        max_length=45,
        db_column='ENTY_NAMF',
        blank=True,
        help_text='Entity first name',
    )
    enty_namt = fields.CharField(
        max_length=10,
        db_column='ENTY_NAMT',
        blank=True,
        help_text='Entity title or suffix'
    )
    enty_nams = fields.CharField(
        max_length=10,
        db_column='ENTY_NAMS',
        blank=True,
        help_text='Entity suffix',
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
    Cover page information for lobbying disclosure forms
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=32, end_page=35),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=17, end_page=21),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=53, end_page=56),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=65, end_page=70),
    ]
    FILING_FORMS = [
        get_filing_form('F615'),
        get_filing_form('F625'),
        get_filing_form('F635'),
        get_filing_form('F645'),
    ]
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    ctrib_n_cb = fields.CharField(
        max_length=1,
        db_column='CTRIB_N_CB',
        blank=True,
        help_text="'Campaign contribtions? P4 attached' checkbox. Applies \
to forms 625, 635, 645.",
    )
    ctrib_y_cb = fields.CharField(
        max_length=1,
        db_column='CTRIB_Y_CB',
        blank=True,
        help_text="'Campaign contribtions? P4 attached' checkbox. Applies \
to forms 625, 635, 645.",
    )
    cum_beg_dt = fields.DateField(
        null=True,
        db_column='CUM_BEG_DT',
        blank=True,
        help_text='Cumulative period beginning date',
    )
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-format.html#document/p9
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
        max_length=9,
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
        help_text='Filer last name or business name',
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
        help_text="Unique filing identificiation number"
    )
    # firm_adr1 = fields.CharField(
    #   max_length=55,
    #   db_column='FIRM_ADR1',
    #   blank=True,
    #   help_text='First line of Firm, employer or coalition address',',
    # )
    # firm_adr2 = fields.CharField(
    #   max_length=55,
    #   db_column='FIRM_ADR2',
    #   blank=True,
    #   help_text='Second line of firm, employer or coalition address',
    # )
    firm_city = fields.CharField(
        max_length=30,
        db_column='FIRM_CITY',
        blank=True,
        help_text='Firm, employer or coalition business city',
    )
    firm_id = fields.CharField(
        max_length=9,
        db_column='FIRM_ID',
        blank=True,
        help_text='Identification number of firm, employer or coalition',
    )
    firm_name = fields.CharField(
        max_length=200,
        db_column='FIRM_NAME',
        blank=True,
        help_text='Name of firm, employer or coalition',
    )
    firm_phon = fields.CharField(
        max_length=20,
        db_column='FIRM_PHON',
        blank=True,
        help_text='Firm, employer or coalition business phone number',
    )
    firm_st = fields.CharField(
        max_length=2,
        db_column='FIRM_ST',
        blank=True,
        help_text='Firm, employer or coalition business state',
    )
    firm_zip4 = fields.CharField(
        max_length=10,
        db_column='FIRM_ZIP4',
        blank=True,
        help_text='Form, employer or coalition business ZIP Code',
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=4,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=53),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=66),
        ]
    )
    from_date = fields.DateField(
        db_column='FROM_DATE',
        null=True,
        help_text='Reporting period from date',
    )
    lby_actvty = fields.CharField(
        max_length=400,
        db_column='LBY_ACTVTY',
        blank=True,
        help_text='Description of lobbying activity. Applies to forms \
635 and 645. Additional description may be provided in text records.',
    )
    lobby_n_cb = fields.CharField(
        max_length=1,
        db_column='LOBBY_N_CB',
        blank=True,
        help_text="'Lobbying activity none' checkbox. Applies \
only to Form 625.",
    )
    lobby_y_cb = fields.CharField(
        max_length=1,
        db_column='LOBBY_Y_CB',
        blank=True,
        help_text="'Lobbying activity Form 630 attached' checkbox. Applies \
only to Form 625.",
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
    major_namf = fields.CharField(
        max_length=45,
        db_column='MAJOR_NAMF',
        blank=True,
        help_text='Major donor first name. Applies only to \
individuals and forms 625, 635, 645.',
    )
    major_naml = fields.CharField(
        max_length=200,
        db_column='MAJOR_NAML',
        blank=True,
        help_text='Major donor last name. Applies only to \
individuals and forms 625, 635, 645.',
    )
    major_nams = fields.CharField(
        max_length=10,
        db_column='MAJOR_NAMS',
        blank=True,
        help_text='Major donor suffix. Applies only to \
individuals and forms 625, 635, 645.',
    )
    major_namt = fields.CharField(
        max_length=10,
        db_column='MAJOR_NAMT',
        blank=True,
        help_text='Major donor title or prefix. Applies only to \
individuals and forms 625, 635, 645.',
    )
    nopart1_cb = fields.CharField(
        max_length=1,
        db_column='NOPART1_CB',
        blank=True,
        help_text="'No Part I information' checkbox. Applies only \
to Form 615.",
    )
    nopart2_cb = fields.CharField(
        max_length=1,
        db_column='NOPART2_CB',
        blank=True,
        help_text="'No Part II information' checkbox. Applies only \
to Form 615.",
    )
    part1_1_cb = fields.CharField(
        max_length=1,
        db_column='PART1_1_CB',
        blank=True,
        help_text="'Partners, owners Form 615 attached ...' checkbox. \
Applies only to form 625.",
    )
    part1_2_cb = fields.CharField(
        max_length=1,
        db_column='PART1_2_CB',
        blank=True,
        help_text="'Partners, owners listed below ...' checkbox. Applies only \
to Form 625.",
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
    rcpcmte_id = fields.CharField(
        max_length=9,
        db_column='RCPCMTE_ID',
        blank=True,
        help_text='Recipient committee or major donor identification number',
    )
    rcpcmte_nm = fields.CharField(
        max_length=200,
        db_column='RCPCMTE_NM',
        blank=True,
        help_text='Recipient committee name',
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
    report_num = fields.CharField(
        max_length=3,
        db_column='REPORT_NUM',
        help_text='Amendment number. 000 is the original. \
001-999 are amendments.',
    )
    rpt_date = fields.DateField(
        db_column='RPT_DATE',
        null=True,
        help_text='Date this report was filed, as reported by the filer',
    )
    sender_id = fields.CharField(
        max_length=9,
        db_column='SENDER_ID',
        help_text='Identification number of lobbyist entity that is \
submitting this report. The field is used to authenticate the filer and \
allows the firm to submit forms for its lobbyists.',
    )
    sig_date = fields.DateField(
        db_column='SIG_DATE',
        null=True,
        help_text='Date when signed',
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
    thru_date = fields.DateField(
        db_column='THRU_DATE',
        null=True,
        help_text='Reporting period through date',
    )

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
    Additional data from lobbyist disclosure forms (615, 625, 635, and 645)
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=8),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=43, end_page=44),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=36),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=57),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=71),
    ]
    FILING_FORMS = [
        get_filing_form('F625'),
        get_filing_form('F635'),
    ]
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    ENTITY_CODE_CHOICES = (
        ('EMP', choices.LOBBYING_ENTITY_CODES['EMP']),
        ('OFF', choices.LOBBYING_ENTITY_CODES['OFF']),
        ('OWN', choices.LOBBYING_ENTITY_CODES['OWN']),
        ('PTN', choices.LOBBYING_ENTITY_CODES['PTN']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=57),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=71),
        ]
    )
    entity_id = fields.CharField(
        max_length=9,
        db_column='ENTITY_ID',
        blank=True,
        help_text='Entity identification number',
    )
    enty_namf = fields.CharField(
        max_length=45,
        db_column='ENTY_NAMF',
        blank=True,
        help_text='Entity first name',
    )
    enty_naml = fields.CharField(
        max_length=200,
        db_column='ENTY_NAML',
        blank=True,
        help_text='Entity last name or business name',
    )
    enty_nams = fields.CharField(
        max_length=10,
        db_column='ENTY_NAMS',
        blank=True,
        help_text='Entity suffix',
    )
    enty_namt = fields.CharField(
        max_length=10,
        db_column='ENTY_NAMT',
        blank=True,
        help_text='Entity title or prefix',
    )
    enty_title = fields.CharField(
        max_length=45,
        db_column='ENTY_TITLE',
        blank=True,
        help_text='Title of partner, owner, officer, employer if the \
entity is an individual. Only required by Form 635.',
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=4,
        db_column='FORM_TYPE',
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=57),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=71),
        ]
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
    Lobbyist registration amendment information (Form 605 Part I).
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=90, end_page=91),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=64, end_page=66),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=74),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=88, end_page=89),
    ]
    FILING_FORMS = [
        get_filing_form('F601'),
        get_filing_form('F603'),
    ]
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
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=9,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=74),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=88),
        ]
    )
    exec_date = fields.DateField(
        max_length=22,
        db_column='EXEC_DATE',
        verbose_name='executed date',
        help_text='Date this amendment executed on',
    )
    from_date = fields.DateField(
        max_length=22,
        db_column='FROM_DATE',
        verbose_name='reported from date',
        help_text='Reporting period from date of original report',
    )
    thru_date = fields.DateField(
        max_length=22,
        db_column='THRU_DATE',
        verbose_name='reported through date',
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
        max_length=200,
        db_column='D_L_NAML',
        blank=True,
        help_text='Delete lobbyist last name',
    )
    d_l_namf = fields.CharField(
        max_length=45,
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
        max_length=10,
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
        max_length=200,
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
        max_length=10,
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
    Amends lobbying disclosure filings (Form 690)
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=8),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=59, end_page=60),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=50, end_page=51),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=58),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=72),
    ]
    FILING_FORMS = [
        get_filing_form('F615'),
        get_filing_form('F625'),
        get_filing_form('F635'),
        get_filing_form('F645'),
    ]
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
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=4,
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=58),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=72),
        ]
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
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=81, end_page=82),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=52, end_page=53),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=65),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=79, end_page=80),
    ]
    FILING_FORMS = [
        get_filing_form('S630'),
        get_filing_form('S635C'),
        get_filing_form('S640'),
    ]
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
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-format.html#document/p9
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
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=6,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=52),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=65),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=79),
        ]
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
    Lobbying activity expenditures schedule information, reported in
    Forms 615 Part 1, 625 Part 3A, 635 Part 3C, and 645 Part 2A.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=86, end_page=87),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=58, end_page=59),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=61),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=74, end_page=75),
    ]
    FILING_FORMS = [
        get_filing_form('F615').get_section('P1'),
        get_filing_form('F625').get_section('P3A'),
        get_filing_form('F635').get_section('P3C'),
        get_filing_form('F645').get_section('P2A'),
    ]
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
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-format.html#document/p9
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
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=61),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=74),
        ]
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
    Lobbying campaign contributions reported on Forms 615 Part 2,
    625 Part 4B, 635 Part 4B and the 645 Part 3B.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=83, end_page=84),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=54, end_page=55),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=64),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=78, end_page=79),
    ]
    FILING_FORMS = [
        get_filing_form('F615').get_section('P2'),
        get_filing_form('F625').get_section('P4B'),
        get_filing_form('F635').get_section('P4B'),
        get_filing_form('F645').get_section('P3B'),
    ]
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
        help_text='Amount of contribution',
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
        max_length=200,
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
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-format.html#document/p9
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
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=64),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=78, end_page=79),
        ]
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
class LempCd(CalAccessBaseModel):
    """
    Lobbyist employers and subcontracted clients (Form 601)
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=85, end_page=86),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=56, end_page=57)
    ]
    FILING_FORMS = [
        get_filing_form('F601').get_section('P2A'),
        get_filing_form('F601').get_section('P2B'),
    ]
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
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        verbose_name='form type',
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
class LobbyingChgLogCd(CalAccessBaseModel):
    """
    Holds lobbyist log data for web display
    """
    UNIQUE_KEY = (
        "FILER_ID",
        "CHANGE_NO"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=91, end_page=92)
    ]
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    change_no = fields.IntegerField(
        db_column='CHANGE_NO',
        help_text="Number of changes this session"
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    log_dt = fields.DateField(
        db_column="LOG_DT",
        null=True,
        help_text="This field is undocumented"
    )
    filer_type = fields.IntegerField(
        db_column='FILER_TYPE',
        help_text="This field is undocumented"
    )
    correction_flag = fields.CharField(
        max_length=200,
        db_column="CORRECTION_FLG",
        help_text="This field is undocumented"
    )
    action = fields.CharField(
        max_length=200,
        db_column="ACTION",
        help_text="This field is undocumented"
    )
    attribute_changed = fields.CharField(
        max_length=200,
        db_column="ATTRIBUTE_CHANGED",
        help_text="This field is undocumented"
    )
    ethics_dt = fields.DateField(
        db_column="ETHICS_DT",
        null=True,
        help_text="This field is undocumented"
    )
    interests = fields.CharField(
        max_length=200,
        db_column="INTERESTS",
        help_text="This field is undocumented"
    )
    filer_full_name = fields.CharField(
        max_length=200,
        db_column="FILER_FULL_NAME"
    )
    filer_city = fields.CharField(
        max_length=200,
        db_column="FILER_CITY"
    )
    filer_st = fields.CharField(
        max_length=200,
        db_column="FILER_ST",
        verbose_name="Filer state"
    )
    filer_zip = fields.IntegerField(
        db_column="FILER_ZIP",
        null=True,
        verbose_name="Filer ZIP Code"
    )
    filer_phone = fields.CharField(
        db_column="FILER_PHONE",
        null=True,
        max_length=12,
        verbose_name="Filer phone number"
    )
    ENTITY_TYPE_CHOICES = (
        (0, 'n/a'),
        (1, 'Client'),
        (2, 'Employer'),
        (3, 'Firm'),
        (4, 'Lobbyist'),
        (10, 'Major Donor'),
        (16, 'Recipient Committee'),
        (20, 'Treasurer/Responsible Officer'),
    )
    entity_type = fields.IntegerField(
        db_column="ENTITY_TYPE",
        null=True,
        choices=ENTITY_TYPE_CHOICES,
        help_text="This field is undocumented. The values might refer to either \
FILER_TYPE_CD.FILER_TYPE or GROUP_TYPE_CD.GRP_ID, but that's just a guess."
    )
    entity_name = fields.CharField(
        max_length=500,
        db_column="ENTITY_NAME",
        help_text="This field is undocumented"
    )
    entity_city = fields.CharField(
        max_length=500,
        db_column="ENTITY_CITY",
        help_text="This field is undocumented"
    )
    entity_st = fields.CharField(
        max_length=500,
        db_column="ENTITY_ST",
        help_text="This field is undocumented"
    )
    entity_zip = fields.CharField(
        db_column="ENTITY_ZIP",
        blank=True,
        max_length=10,
        help_text="This field is undocumented"
    )
    entity_phone = fields.CharField(
        db_column="ENTITY_PHONE",
        null=True,
        max_length=12,
        help_text="Entity phone number"
    )
    entity_id = fields.IntegerField(
        db_column="ENTITY_ID",
        null=True,
        help_text="Entity identification number"
    )
    responsible_officer = fields.CharField(
        max_length=500,
        db_column="RESPONSIBLE_OFFICER",
        help_text="This field is undocumented"
    )
    effect_dt = fields.DateField(
        db_column="EFFECT_DT",
        null=True,
        verbose_name="Effective date",
        help_text="This field is undocumented"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYING_CHG_LOG_CD'
        verbose_name = 'LOBBYING_CHG_LOG_CD'
        verbose_name_plural = 'LOBBYING_CHG_LOG_CD'
        # not in the right place
        # documentcloud_pages = [
        #     DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=91, end_page=92),
        # ]

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class LobbyistContributions1Cd(CalAccessBaseModel):
    """
    Lobbyist contribution disclosure table.
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id="2711614-CalAccessTablesWeb", start_page=10),
        DocumentCloud(id="2711614-CalAccessTablesWeb", start_page=92, end_page=93),
    ]
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    filing_period_start_dt = fields.DateField(
        null=True,
        db_column='FILING_PERIOD_START_DT',
        verbose_name='Filing period start date'
    )
    filing_period_end_dt = fields.DateField(
        db_column='FILING_PERIOD_END_DT',
        null=True,
        verbose_name='Filing period end date'
    )
    contribution_dt = fields.CharField(
        db_column='CONTRIBUTION_DT',
        max_length=32,
        blank=True,
        verbose_name='Contribution date'
    )
    recipient_name = fields.CharField(
        db_column='RECIPIENT_NAME',
        max_length=106,
        blank=True,
        help_text="Recipient's name"
    )
    recipient_id = fields.IntegerField(
        db_column='RECIPIENT_ID',
        blank=True,
        null=True,
        help_text="Recipient's identification number"
    )
    amount = fields.FloatField(
        db_column='AMOUNT',
        blank=True,
        null=True,
        help_text="Amount received"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_CONTRIBUTIONS1_CD'
        verbose_name = 'LOBBYIST_CONTRIBUTIONS1_CD'
        verbose_name_plural = 'LOBBYIST_CONTRIBUTIONS1_CD'

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class LobbyistContributions2Cd(CalAccessBaseModel):
    """
    Lobbyist contribution disclosure table. Temporary table used to generate
    disclosure table (Lobbyist Contributions 3)
    """
    UNIQUE_KEY = False
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10, end_page=11),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=93, end_page=94),
    ]
    filing_period_start_dt = fields.DateField(
        null=True,
        db_column='FILING_PERIOD_START_DT',
        verbose_name='Filing period start date'
    )
    filing_period_end_dt = fields.DateField(
        db_column='FILING_PERIOD_END_DT',
        null=True,
        verbose_name='Filing period end date'
    )
    contribution_dt = fields.CharField(
        db_column='CONTRIBUTION_DT',
        max_length=32,
        blank=True,
        verbose_name='Contribution date'
    )
    recipient_name = fields.CharField(
        db_column='RECIPIENT_NAME',
        max_length=106,
        blank=True,
        help_text="Recipient's name"
    )
    recipient_id = fields.IntegerField(
        db_column='RECIPIENT_ID',
        blank=True,
        null=True,
        help_text="Recipient's identification number"
    )
    amount = fields.FloatField(
        db_column='AMOUNT',
        blank=True,
        null=True,
        help_text="Amount received"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_CONTRIBUTIONS2_CD'
        verbose_name = 'LOBBYIST_CONTRIBUTIONS2_CD'
        verbose_name_plural = 'LOBBYIST_CONTRIBUTIONS2_CD'

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class LobbyistContributions3Cd(CalAccessBaseModel):
    """
    Lobbyist contribution disclosure table.
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=11),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=94),
    ]
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    filing_period_start_dt = fields.DateField(
        null=True,
        db_column='FILING_PERIOD_START_DT',
        verbose_name='Filing period start date'
    )
    filing_period_end_dt = fields.DateField(
        db_column='FILING_PERIOD_END_DT',
        null=True,
        verbose_name='Filing period end date'
    )
    contribution_dt = fields.CharField(
        db_column='CONTRIBUTION_DT',
        max_length=32,
        blank=True,
        verbose_name='Contribution date'
    )
    recipient_name = fields.CharField(
        db_column='RECIPIENT_NAME',
        max_length=106,
        blank=True,
        help_text="Recipient's name"
    )
    recipient_id = fields.IntegerField(
        db_column='RECIPIENT_ID',
        blank=True,
        null=True,
        help_text="Recipient's identification number"
    )
    amount = fields.FloatField(
        db_column='AMOUNT',
        blank=True,
        null=True,
        help_text="Amount received"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_CONTRIBUTIONS3_CD'
        verbose_name = 'LOBBYIST_CONTRIBUTIONS3_CD'
        verbose_name_plural = 'LOBBYIST_CONTRIBUTIONS3_CD'

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class LobbyistEmployer1Cd(CalAccessBaseModel):
    """
    Information for lobbyist's primary employer
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=11),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=97, end_page=98),
    ]
    employer_id = fields.IntegerField(
        db_column='EMPLOYER_ID',
        help_text="Employer identification number",
        verbose_name="Employer ID"
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    employer_name = fields.CharField(
        db_column='EMPLOYER_NAME',
        max_length=300,
        help_text="Employer name"
    )
    current_qtr_amt = fields.FloatField(
        db_column='CURRENT_QTR_AMT',
        help_text="Current quarter amount"
    )
    session_total_amt = fields.FloatField(
        db_column='SESSION_TOTAL_AMT',
        help_text="Total amount for the session"
    )
    contributor_id = fields.IntegerField(
        db_column='CONTRIBUTOR_ID',
        blank=True,
        null=True,
        verbose_name="contributor ID",
        help_text="Contributor identification number"
    )
    interest_cd = fields.IntegerField(
        db_column='INTEREST_CD',
        blank=True,
        null=True,
        verbose_name="interest code"
    )
    interest_name = fields.CharField(
        db_column='INTEREST_NAME',
        max_length=24,
        blank=True,
        help_text="Interest name"
    )
    session_yr_1 = fields.IntegerField(
        db_column='SESSION_YR_1',
        help_text="Total amount of year 1 of the session",
    )
    session_yr_2 = fields.IntegerField(
        db_column='SESSION_YR_2',
        help_text="Total amount of year 2 of the session",
    )
    yr_1_ytd_amt = fields.FloatField(
        db_column='YR_1_YTD_AMT',
        verbose_name="Year 1 year-to-date-amount",
    )
    yr_2_ytd_amt = fields.FloatField(
        db_column='YR_2_YTD_AMT',
        verbose_name="Year 2 year-to-date-amount",
    )
    qtr_1 = fields.FloatField(
        db_column='QTR_1',
        verbose_name="Quarter 1",
        help_text="Quarter total amount",
    )
    qtr_2 = fields.FloatField(
        db_column='QTR_2',
        verbose_name="Quarter 2",
        help_text="Quarter total amount",
    )
    qtr_3 = fields.FloatField(
        db_column='QTR_3',
        verbose_name="Quarter 3",
        help_text="Quarter total amount",
    )
    qtr_4 = fields.FloatField(
        db_column='QTR_4',
        verbose_name="Quarter 4",
        help_text="Quarter total amount",
    )
    qtr_5 = fields.FloatField(
        db_column='QTR_5',
        verbose_name="Quarter 5",
        help_text="Quarter total amount",
    )
    qtr_6 = fields.FloatField(
        db_column='QTR_6',
        verbose_name="Quarter 6",
        help_text="Quarter total amount",
    )
    qtr_7 = fields.FloatField(
        db_column='QTR_7',
        verbose_name="Quarter 7",
        help_text="Quarter total amount",
    )
    qtr_8 = fields.FloatField(
        db_column='QTR_8',
        verbose_name="Quarter 8",
        help_text="Quarter total amount",
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMPLOYER1_CD'
        verbose_name = 'LOBBYIST_EMPLOYER1_CD'
        verbose_name_plural = 'LOBBYIST_EMPLOYER1_CD'

    def __str__(self):
        return str(self.employer_id)


@python_2_unicode_compatible
class LobbyistEmployer2Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=11),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=98, end_page=99),
    ]
    employer_id = fields.IntegerField(
        db_column='EMPLOYER_ID',
        help_text="Employer identification number",
        verbose_name="Employer ID"
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    employer_name = fields.CharField(
        db_column='EMPLOYER_NAME',
        max_length=300,
        help_text="Employer name"
    )
    current_qtr_amt = fields.FloatField(
        db_column='CURRENT_QTR_AMT',
        help_text="Current quarter amount"
    )
    session_total_amt = fields.FloatField(
        db_column='SESSION_TOTAL_AMT',
        help_text="Total amount for the session"
    )
    contributor_id = fields.IntegerField(
        db_column='CONTRIBUTOR_ID',
        blank=True,
        null=True,
        verbose_name="contributor ID",
        help_text="Contributor identification number"
    )
    interest_cd = fields.IntegerField(
        db_column='INTEREST_CD',
        blank=True,
        null=True,
        verbose_name="interest code"
    )
    interest_name = fields.CharField(
        db_column='INTEREST_NAME',
        max_length=24,
        blank=True,
        help_text="Interest name"
    )
    session_yr_1 = fields.IntegerField(
        db_column='SESSION_YR_1',
        help_text="Total amount of year 1 of the session",
    )
    session_yr_2 = fields.IntegerField(
        db_column='SESSION_YR_2',
        help_text="Total amount of year 2 of the session",
    )
    yr_1_ytd_amt = fields.FloatField(
        db_column='YR_1_YTD_AMT',
        verbose_name="Year 1 year-to-date-amount",
    )
    yr_2_ytd_amt = fields.FloatField(
        db_column='YR_2_YTD_AMT',
        verbose_name="Year 2 year-to-date-amount",
    )
    qtr_1 = fields.FloatField(
        db_column='QTR_1',
        verbose_name="Quarter 1",
        help_text="Quarter total amount",
    )
    qtr_2 = fields.FloatField(
        db_column='QTR_2',
        verbose_name="Quarter 2",
        help_text="Quarter total amount",
    )
    qtr_3 = fields.FloatField(
        db_column='QTR_3',
        verbose_name="Quarter 3",
        help_text="Quarter total amount",
    )
    qtr_4 = fields.FloatField(
        db_column='QTR_4',
        verbose_name="Quarter 4",
        help_text="Quarter total amount",
    )
    qtr_5 = fields.FloatField(
        db_column='QTR_5',
        verbose_name="Quarter 5",
        help_text="Quarter total amount",
    )
    qtr_6 = fields.FloatField(
        db_column='QTR_6',
        verbose_name="Quarter 6",
        help_text="Quarter total amount",
    )
    qtr_7 = fields.FloatField(
        db_column='QTR_7',
        verbose_name="Quarter 7",
        help_text="Quarter total amount",
    )
    qtr_8 = fields.FloatField(
        db_column='QTR_8',
        verbose_name="Quarter 8",
        help_text="Quarter total amount",
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMPLOYER2_CD'
        verbose_name = 'LOBBYIST_EMPLOYER2_CD'
        verbose_name_plural = 'LOBBYIST_EMPLOYER2_CD'

    def __str__(self):
        return str(self.employer_id)


@python_2_unicode_compatible
class LobbyistEmployer3Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=11),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=99),
    ]
    employer_id = fields.IntegerField(
        db_column='EMPLOYER_ID',
        help_text="Employer identification number",
        verbose_name="Employer ID"
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    employer_name = fields.CharField(
        db_column='EMPLOYER_NAME',
        max_length=300,
        help_text="Employer name"
    )
    current_qtr_amt = fields.FloatField(
        db_column='CURRENT_QTR_AMT',
        help_text="Current quarter amount"
    )
    session_total_amt = fields.FloatField(
        db_column='SESSION_TOTAL_AMT',
        help_text="Total amount for the session"
    )
    contributor_id = fields.IntegerField(
        db_column='CONTRIBUTOR_ID',
        blank=True,
        null=True,
        verbose_name="contributor ID",
        help_text="Contributor identification number"
    )
    interest_cd = fields.IntegerField(
        db_column='INTEREST_CD',
        blank=True,
        null=True,
        verbose_name="interest code"
    )
    interest_name = fields.CharField(
        db_column='INTEREST_NAME',
        max_length=24,
        blank=True,
        help_text="Interest name"
    )
    session_yr_1 = fields.IntegerField(
        db_column='SESSION_YR_1',
        help_text="Total amount of year 1 of the session",
    )
    session_yr_2 = fields.IntegerField(
        db_column='SESSION_YR_2',
        help_text="Total amount of year 2 of the session",
    )
    yr_1_ytd_amt = fields.FloatField(
        db_column='YR_1_YTD_AMT',
        verbose_name="Year 1 year-to-date-amount",
    )
    yr_2_ytd_amt = fields.FloatField(
        db_column='YR_2_YTD_AMT',
        verbose_name="Year 2 year-to-date-amount",
    )
    qtr_1 = fields.FloatField(
        db_column='QTR_1',
        verbose_name="Quarter 1",
        help_text="Quarter total amount",
    )
    qtr_2 = fields.FloatField(
        db_column='QTR_2',
        verbose_name="Quarter 2",
        help_text="Quarter total amount",
    )
    qtr_3 = fields.FloatField(
        db_column='QTR_3',
        verbose_name="Quarter 3",
        help_text="Quarter total amount",
    )
    qtr_4 = fields.FloatField(
        db_column='QTR_4',
        verbose_name="Quarter 4",
        help_text="Quarter total amount",
    )
    qtr_5 = fields.FloatField(
        db_column='QTR_5',
        verbose_name="Quarter 5",
        help_text="Quarter total amount",
    )
    qtr_6 = fields.FloatField(
        db_column='QTR_6',
        verbose_name="Quarter 6",
        help_text="Quarter total amount",
    )
    qtr_7 = fields.FloatField(
        db_column='QTR_7',
        verbose_name="Quarter 7",
        help_text="Quarter total amount",
    )
    qtr_8 = fields.FloatField(
        db_column='QTR_8',
        verbose_name="Quarter 8",
        help_text="Quarter total amount",
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMPLOYER3_CD'
        verbose_name = 'LOBBYIST_EMPLOYER3_CD'
        verbose_name_plural = 'LOBBYIST_EMPLOYER3_CD'

    def __str__(self):
        return str(self.employer_id)


@python_2_unicode_compatible
class LobbyistEmployerFirms1Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=11),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=95, end_page=96),
    ]
    employer_id = fields.IntegerField(
        db_column='EMPLOYER_ID',
        help_text="Employer identification number",
        verbose_name="Employer ID"
    )
    firm_id = fields.IntegerField(
        db_column='FIRM_ID',
        verbose_name="Firm ID",
        help_text="Identification number of the firm, employer or coalition"
    )
    firm_name = fields.CharField(
        db_column='FIRM_NAME',
        max_length=400,
        help_text="Name of firm, employer or coalition",
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    termination_dt = fields.CharField(
        verbose_name='termination date',
        db_column='TERMINATION_DT',
        max_length=32,
        blank=True,
        help_text="Termination effective date"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMPLOYER_FIRMS1_CD'
        verbose_name = 'LOBBYIST_EMPLOYER_FIRMS1_CD'
        verbose_name_plural = 'LOBBYIST_EMPLOYER_FIRMS1_CD'

    def __str__(self):
        return str(self.employer_id)


@python_2_unicode_compatible
class LobbyistEmployerFirms2Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=11),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=96),
    ]
    employer_id = fields.IntegerField(
        db_column='EMPLOYER_ID',
        help_text="Employer identification number",
        verbose_name="Employer ID"
    )
    firm_id = fields.IntegerField(
        db_column='FIRM_ID',
        verbose_name="Firm ID",
        help_text="Identification number of the firm, employer or coalition"
    )
    firm_name = fields.CharField(
        db_column='FIRM_NAME',
        max_length=400,
        help_text="Name of firm, employer or coalition",
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    termination_dt = fields.CharField(
        verbose_name='termination date',
        db_column='TERMINATION_DT',
        max_length=32,
        blank=True,
        help_text="Termination effective date"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMPLOYER_FIRMS2_CD'
        verbose_name = 'LOBBYIST_EMPLOYER_FIRMS2_CD'
        verbose_name_plural = 'LOBBYIST_EMPLOYER_FIRMS2_CD'

    def __str__(self):
        return str(self.employer_id)


@python_2_unicode_compatible
class LobbyistEmpLobbyist1Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=11),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=94, end_page=95),
    ]
    lobbyist_id = fields.IntegerField(
        db_column='LOBBYIST_ID',
        verbose_name="Lobbyist ID",
        help_text="Lobbyist identification number"
    )
    employer_id = fields.IntegerField(
        db_column='EMPLOYER_ID',
        help_text="Employer identification number",
        verbose_name="Employer ID"
    )
    lobbyist_last_name = fields.CharField(
        db_column='LOBBYIST_LAST_NAME',
        max_length=17,
        help_text="Lobbyist last name"
    )
    lobbyist_first_name = fields.CharField(
        db_column='LOBBYIST_FIRST_NAME',
        max_length=17,
        help_text="Lobbyist first name"
    )
    employer_name = fields.CharField(
        db_column='EMPLOYER_NAME',
        max_length=300,
        help_text="Employer name"
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMP_LOBBYIST1_CD'
        verbose_name = 'LOBBYIST_EMP_LOBBYIST1_CD'
        verbose_name_plural = 'LOBBYIST_EMP_LOBBYIST1_CD'

    def __str__(self):
        return str(self.lobbyist_id)


@python_2_unicode_compatible
class LobbyistEmpLobbyist2Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=11),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=95),
    ]
    lobbyist_id = fields.IntegerField(
        db_column='LOBBYIST_ID',
        verbose_name="Lobbyist ID",
        help_text="Lobbyist identification number"
    )
    employer_id = fields.IntegerField(
        db_column='EMPLOYER_ID',
        help_text="Employer identification number",
        verbose_name="Employer ID"
    )
    lobbyist_last_name = fields.CharField(
        db_column='LOBBYIST_LAST_NAME',
        max_length=17,
        help_text="Lobbyist last name"
    )
    lobbyist_first_name = fields.CharField(
        db_column='LOBBYIST_FIRST_NAME',
        max_length=17,
        help_text="Lobbyist first name"
    )
    employer_name = fields.CharField(
        db_column='EMPLOYER_NAME',
        max_length=300,
        help_text="Employer name"
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMP_LOBBYIST2_CD'
        verbose_name = 'LOBBYIST_EMP_LOBBYIST2_CD'
        verbose_name_plural = 'LOBBYIST_EMP_LOBBYIST2_CD'

    def __str__(self):
        return str(self.lobbyist_id)


@python_2_unicode_compatible
class LobbyistFirm1Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    firm_id = fields.IntegerField(
        db_column='FIRM_ID',
        verbose_name="Firm ID",
        help_text="Identification number of the firm, employer or coalition"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=12),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=103, end_page=104),
    ]
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    firm_name = fields.CharField(
        db_column='FIRM_NAME',
        max_length=400,
        help_text="Name of firm, employer or coalition",
    )
    current_qtr_amt = fields.FloatField(
        db_column='CURRENT_QTR_AMT',
        help_text="Current quarter amount"
    )
    session_total_amt = fields.FloatField(
        db_column='SESSION_TOTAL_AMT',
        help_text="Total amount for the session"
    )
    contributor_id = fields.IntegerField(
        db_column='CONTRIBUTOR_ID',
        blank=True,
        null=True,
        verbose_name="contributor ID",
        help_text="Contributor identification number"
    )
    session_yr_1 = fields.IntegerField(
        db_column='SESSION_YR_1',
        help_text="Total amount of year 1 of the session",
    )
    session_yr_2 = fields.IntegerField(
        db_column='SESSION_YR_2',
        help_text="Total amount of year 2 of the session",
    )
    yr_1_ytd_amt = fields.FloatField(
        db_column='YR_1_YTD_AMT',
        verbose_name="Year 1 year-to-date-amount",
    )
    yr_2_ytd_amt = fields.FloatField(
        db_column='YR_2_YTD_AMT',
        verbose_name="Year 2 year-to-date-amount",
    )
    qtr_1 = fields.FloatField(
        db_column='QTR_1',
        verbose_name="Quarter 1",
        help_text="Quarter total amount",
    )
    qtr_2 = fields.FloatField(
        db_column='QTR_2',
        verbose_name="Quarter 2",
        help_text="Quarter total amount",
    )
    qtr_3 = fields.FloatField(
        db_column='QTR_3',
        verbose_name="Quarter 3",
        help_text="Quarter total amount",
    )
    qtr_4 = fields.FloatField(
        db_column='QTR_4',
        verbose_name="Quarter 4",
        help_text="Quarter total amount",
    )
    qtr_5 = fields.FloatField(
        db_column='QTR_5',
        verbose_name="Quarter 5",
        help_text="Quarter total amount",
    )
    qtr_6 = fields.FloatField(
        db_column='QTR_6',
        verbose_name="Quarter 6",
        help_text="Quarter total amount",
    )
    qtr_7 = fields.FloatField(
        db_column='QTR_7',
        verbose_name="Quarter 7",
        help_text="Quarter total amount",
    )
    qtr_8 = fields.FloatField(
        db_column='QTR_8',
        verbose_name="Quarter 8",
        help_text="Quarter total amount",
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM1_CD'
        verbose_name = 'LOBBYIST_FIRM1_CD'
        verbose_name_plural = 'LOBBYIST_FIRM1_CD'

    def __str__(self):
        return str(self.firm_id)


@python_2_unicode_compatible
class LobbyistFirm2Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=12),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=104),
    ]
    firm_id = fields.IntegerField(
        db_column='FIRM_ID',
        verbose_name="Firm ID",
        help_text="Identification number of the firm, employer or coalition"
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    firm_name = fields.CharField(
        db_column='FIRM_NAME',
        max_length=400,
        help_text="Name of firm, employer or coalition",
    )
    current_qtr_amt = fields.FloatField(
        db_column='CURRENT_QTR_AMT',
        help_text="Current quarter amount"
    )
    session_total_amt = fields.FloatField(
        db_column='SESSION_TOTAL_AMT',
        help_text="Total amount for the session"
    )
    contributor_id = fields.IntegerField(
        db_column='CONTRIBUTOR_ID',
        blank=True,
        null=True,
        verbose_name="contributor ID",
        help_text="Contributor identification number"
    )
    session_yr_1 = fields.IntegerField(
        db_column='SESSION_YR_1',
        help_text="Total amount of year 1 of the session",
    )
    session_yr_2 = fields.IntegerField(
        db_column='SESSION_YR_2',
        help_text="Total amount of year 2 of the session",
    )
    yr_1_ytd_amt = fields.FloatField(
        db_column='YR_1_YTD_AMT',
        verbose_name="Year 1 year-to-date-amount",
    )
    yr_2_ytd_amt = fields.FloatField(
        db_column='YR_2_YTD_AMT',
        verbose_name="Year 2 year-to-date-amount",
    )
    qtr_1 = fields.FloatField(
        db_column='QTR_1',
        verbose_name="Quarter 1",
        help_text="Quarter total amount",
    )
    qtr_2 = fields.FloatField(
        db_column='QTR_2',
        verbose_name="Quarter 2",
        help_text="Quarter total amount",
    )
    qtr_3 = fields.FloatField(
        db_column='QTR_3',
        verbose_name="Quarter 3",
        help_text="Quarter total amount",
    )
    qtr_4 = fields.FloatField(
        db_column='QTR_4',
        verbose_name="Quarter 4",
        help_text="Quarter total amount",
    )
    qtr_5 = fields.FloatField(
        db_column='QTR_5',
        verbose_name="Quarter 5",
        help_text="Quarter total amount",
    )
    qtr_6 = fields.FloatField(
        db_column='QTR_6',
        verbose_name="Quarter 6",
        help_text="Quarter total amount",
    )
    qtr_7 = fields.FloatField(
        db_column='QTR_7',
        verbose_name="Quarter 7",
        help_text="Quarter total amount",
    )
    qtr_8 = fields.FloatField(
        db_column='QTR_8',
        verbose_name="Quarter 8",
        help_text="Quarter total amount",
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM2_CD'
        verbose_name = 'LOBBYIST_FIRM2_CD'
        verbose_name_plural = 'LOBBYIST_FIRM2_CD'

    def __str__(self):
        return str(self.firm_id)


@python_2_unicode_compatible
class LobbyistFirm3Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=12),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=105),
    ]
    firm_id = fields.IntegerField(
        db_column='FIRM_ID',
        verbose_name="Firm ID",
        help_text="Identification number of the firm, employer or coalition"
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    firm_name = fields.CharField(
        db_column='FIRM_NAME',
        max_length=400,
        help_text="Name of firm, employer or coalition",
    )
    current_qtr_amt = fields.FloatField(
        db_column='CURRENT_QTR_AMT',
        help_text="Current quarter amount"
    )
    session_total_amt = fields.FloatField(
        db_column='SESSION_TOTAL_AMT',
        help_text="Total amount for the session"
    )
    contributor_id = fields.IntegerField(
        db_column='CONTRIBUTOR_ID',
        blank=True,
        null=True,
        verbose_name="contributor ID",
        help_text="Contributor identification number"
    )
    session_yr_1 = fields.IntegerField(
        db_column='SESSION_YR_1',
        help_text="Total amount of year 1 of the session",
    )
    session_yr_2 = fields.IntegerField(
        db_column='SESSION_YR_2',
        help_text="Total amount of year 2 of the session",
    )
    yr_1_ytd_amt = fields.FloatField(
        db_column='YR_1_YTD_AMT',
        verbose_name="Year 1 year-to-date-amount",
    )
    yr_2_ytd_amt = fields.FloatField(
        db_column='YR_2_YTD_AMT',
        verbose_name="Year 2 year-to-date-amount",
    )
    qtr_1 = fields.FloatField(
        db_column='QTR_1',
        verbose_name="Quarter 1",
        help_text="Quarter total amount",
    )
    qtr_2 = fields.FloatField(
        db_column='QTR_2',
        verbose_name="Quarter 2",
        help_text="Quarter total amount",
    )
    qtr_3 = fields.FloatField(
        db_column='QTR_3',
        verbose_name="Quarter 3",
        help_text="Quarter total amount",
    )
    qtr_4 = fields.FloatField(
        db_column='QTR_4',
        verbose_name="Quarter 4",
        help_text="Quarter total amount",
    )
    qtr_5 = fields.FloatField(
        db_column='QTR_5',
        verbose_name="Quarter 5",
        help_text="Quarter total amount",
    )
    qtr_6 = fields.FloatField(
        db_column='QTR_6',
        verbose_name="Quarter 6",
        help_text="Quarter total amount",
    )
    qtr_7 = fields.FloatField(
        db_column='QTR_7',
        verbose_name="Quarter 7",
        help_text="Quarter total amount",
    )
    qtr_8 = fields.FloatField(
        db_column='QTR_8',
        verbose_name="Quarter 8",
        help_text="Quarter total amount",
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM3_CD'
        verbose_name = 'LOBBYIST_FIRM3_CD'
        verbose_name_plural = 'LOBBYIST_FIRM3_CD'

    def __str__(self):
        return str(self.firm_id)


@python_2_unicode_compatible
class LobbyistFirmEmployer1Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=11),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=100),
    ]
    firm_id = fields.IntegerField(
        db_column='FIRM_ID',
        verbose_name="Firm ID",
        help_text="Identification number of the firm, employer or coalition"
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    filing_sequence = fields.IntegerField(
        db_column='FILING_SEQUENCE',
        help_text="Amendment number. 0 is the original filing. \
1 to 999 are amendments"
    )
    firm_name = fields.CharField(
        db_column='FIRM_NAME',
        max_length=400,
        help_text="Name of firm, employer or coalition",
    )
    employer_name = fields.CharField(
        db_column='EMPLOYER_NAME',
        max_length=300,
        help_text="Employer name"
    )
    rpt_start = fields.DateField(
        db_column='RPT_START',
        null=True,
        help_text="Starting date for the period the report covers"
    )
    rpt_end = fields.DateField(
        db_column='RPT_END',
        null=True,
        help_text="Ending date for the period the report covers"
    )
    per_total = fields.FloatField(
        db_column='PER_TOTAL',
        help_text="Total this reporting period"
    )
    cum_total = fields.FloatField(
        db_column='CUM_TOTAL',
        help_text='Cumulative total to date'
    )
    lby_actvty = fields.CharField(
        db_column='LBY_ACTVTY',
        max_length=182,
        blank=True,
        help_text="Description of lobbying activity"
    )
    ext_lby_actvty = fields.CharField(
        db_column='EXT_LBY_ACTVTY',
        max_length=32,
        blank=True,
        help_text="This field is undocumented"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM_EMPLOYER1_CD'
        verbose_name = 'LOBBYIST_FIRM_EMPLOYER1_CD'
        verbose_name_plural = 'LOBBYIST_FIRM_EMPLOYER1_CD'

    def __str__(self):
        return str(self.firm_id)


@python_2_unicode_compatible
class LobbyistFirmEmployer2Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=11, end_page=12),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=100, end_page=101),
    ]
    firm_id = fields.IntegerField(
        db_column='FIRM_ID',
        verbose_name="Firm ID",
        help_text="Identification number of the firm, employer or coalition"
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    filing_sequence = fields.IntegerField(
        db_column='FILING_SEQUENCE',
        help_text="Amendment number. 0 is the original filing. \
1 to 999 are amendments"
    )
    firm_name = fields.CharField(
        db_column='FIRM_NAME',
        max_length=400,
        help_text="Name of firm, employer or coalition",
    )
    employer_name = fields.CharField(
        db_column='EMPLOYER_NAME',
        max_length=300,
        help_text="Employer name"
    )
    rpt_start = fields.DateField(
        db_column='RPT_START',
        null=True,
        help_text="Starting date for the period the report covers"
    )
    rpt_end = fields.DateField(
        db_column='RPT_END',
        null=True,
        help_text="Ending date for the period the report covers"
    )
    per_total = fields.FloatField(
        db_column='PER_TOTAL',
        help_text="Total this reporting period"
    )
    cum_total = fields.FloatField(
        db_column='CUM_TOTAL',
        help_text='Cumulative total to date'
    )
    lby_actvty = fields.CharField(
        db_column='LBY_ACTVTY',
        max_length=182,
        blank=True,
        help_text="Description of lobbying activity"
    )
    ext_lby_actvty = fields.CharField(
        db_column='EXT_LBY_ACTVTY',
        max_length=32,
        blank=True,
        help_text="This field is undocumented"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM_EMPLOYER2_CD'
        verbose_name = 'LOBBYIST_FIRM_EMPLOYER2_CD'
        verbose_name_plural = 'LOBBYIST_FIRM_EMPLOYER2_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class LobbyistFirmLobbyist1Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=12),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=102),
    ]
    lobbyist_id = fields.IntegerField(
        db_column='LOBBYIST_ID',
        verbose_name="Lobbyist ID",
        help_text="Lobbyist identification number"
    )
    firm_id = fields.IntegerField(
        db_column='FIRM_ID',
        verbose_name="Firm ID",
        help_text="Identification number of the firm, employer or coalition"
    )
    lobbyist_last_name = fields.CharField(
        db_column='LOBBYIST_LAST_NAME',
        max_length=15,
        help_text="Lobbyist last name"
    )
    lobbyist_first_name = fields.CharField(
        db_column='LOBBYIST_FIRST_NAME',
        max_length=17,
        help_text="Lobbyist first name"
    )
    firm_name = fields.CharField(
        db_column='FIRM_NAME',
        max_length=400,
        help_text="Name of firm, employer or coalition",
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM_LOBBYIST1_CD'
        verbose_name = 'LOBBYIST_FIRM_LOBBYIST1_CD'
        verbose_name_plural = 'LOBBYIST_FIRM_LOBBYIST1_CD'

    def __str__(self):
        return str(self.lobbyist_id)


@python_2_unicode_compatible
class LobbyistFirmLobbyist2Cd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=12),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=102, end_page=103),
    ]
    lobbyist_id = fields.IntegerField(
        db_column='LOBBYIST_ID',
        verbose_name="Lobbyist ID",
        help_text="Lobbyist identification number"
    )
    firm_id = fields.IntegerField(
        db_column='FIRM_ID',
        verbose_name="Firm ID",
        help_text="Identification number of the firm, employer or coalition"
    )
    lobbyist_last_name = fields.CharField(
        db_column='LOBBYIST_LAST_NAME',
        max_length=15,
        help_text="Lobbyist last name"
    )
    lobbyist_first_name = fields.CharField(
        db_column='LOBBYIST_FIRST_NAME',
        max_length=17,
        help_text="Lobbyist first name"
    )
    firm_name = fields.CharField(
        db_column='FIRM_NAME',
        max_length=400,
        help_text="Name of firm, employer or coalition",
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM_LOBBYIST2_CD'
        verbose_name = 'LOBBYIST_FIRM_LOBBYIST2_CD'
        verbose_name_plural = 'LOBBYIST_FIRM_LOBBYIST2_CD'

    def __str__(self):
        return str(self.lobbyist_id)


@python_2_unicode_compatible
class LothCd(CalAccessBaseModel):
    """
    Payment to other lobbying firms listed of Form 625 Part 3B
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=106, end_page=107),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=67, end_page=68),
    ]
    FILING_FORMS = [
        get_filing_form('F625').get_section('P3B'),
    ]
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
        help_text='Firm ZIP Code',
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        verbose_name='form type',
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
class LpayCd(CalAccessBaseModel):
    """
    Payments made or received by lobbying firms, reported on
    Form 625 Part 2 and 635 Part 3B
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    FILING_FORMS = [
        get_filing_form('F625').get_section('P2'),
        get_filing_form('F635').get_section('P3B'),
    ]
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=107, end_page=109),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=69, end_page=70)
    ]
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
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-format.html#document/p9
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
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        verbose_name='form type',
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


@python_2_unicode_compatible
class LobbyistEmployerHistoryCd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=11),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=96, end_page=97),
    ]
    contributor_id = fields.IntegerField(
        db_column="CONTRIBUTOR_ID",
        help_text="Contributor identification number."
    )
    current_qtr_amt = fields.IntegerField(
        db_column="CURRENT_QTR_AMT",
        help_text="Current Quarter Amount"
    )
    employer_id = fields.IntegerField(
        db_column="EMPLOYER_ID",
        help_text="Employer identification number."
    )
    employer_name = fields.CharField(
        db_column="EMPLOYER_NAME",
        max_length=300,
        blank=True,
        help_text="Employer Name"
    )
    interest_cd = fields.IntegerField(
        db_column="INTEREST_CD",
        help_text="Interest code."
    )
    interest_name = fields.CharField(
        db_column="INTEREST_NAME",
        max_length=300,
        blank=True,
        help_text="Interest name."
    )
    qtr_1 = fields.IntegerField(
        db_column="QTR_1",
        help_text="Quarter total amount."
    )
    qtr_2 = fields.IntegerField(
        db_column="QTR_2",
        help_text="Quarter total amount."
    )
    qtr_3 = fields.IntegerField(
        db_column="QTR_3",
        help_text="Quarter total amount."
    )
    qtr_4 = fields.IntegerField(
        db_column="QTR_4",
        help_text="Quarter total amount."
    )
    qtr_5 = fields.IntegerField(
        db_column="QTR_5",
        help_text="Quarter total amount."
    )
    qtr_6 = fields.IntegerField(
        db_column="QTR_6",
        help_text="Quarter total amount."
    )
    qtr_7 = fields.IntegerField(
        db_column="QTR_7",
        help_text="Quarter total amount."
    )
    qtr_8 = fields.IntegerField(
        db_column="QTR_8",
        help_text="Quarter total amount."
    )
    session_id = fields.IntegerField(
        db_column="SESSION_ID",
        help_text="Session identification number."
    )
    session_total_amt = fields.IntegerField(
        db_column="SESSION_TOTAL_AMT",
        help_text="Total amount for the session."
    )
    session_yr_1 = fields.IntegerField(
        db_column="SESSION_YR_1",
        help_text="Total amount for year 1 of the session."
    )
    session_yr_2 = fields.IntegerField(
        db_column="SESSION_YR_2",
        help_text="Total amount for year 2 of the session."
    )
    yr_1_ytd_amt = fields.IntegerField(
        db_column="YR_1_YTD_AMT",
        help_text="Year 1 year to date amount."
    )
    yr_2_ytd_amt = fields.IntegerField(
        db_column="YR_2_YTD_AMT",
        help_text="Year 2 year to date amount."
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMPLOYER_HISTORY_CD'
        verbose_name = 'LOBBYIST_EMPLOYER_HISTORY_CD'
        verbose_name_plural = 'LOBBYIST_EMPLOYER_HISTORY_CD'

    def __str__(self):
        return str(self.contributor_id)


@python_2_unicode_compatible
class LobbyistFirmHistoryCd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "Matt
    needs to describe the relationship between the multiple tables. Documentation
    should be cloned from D H's documentation on these tables. Cox 5/11/2000"
    """
    UNIQUE_KEY = (
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=12),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=101, end_page=102),
    ]
    contributor_id = fields.IntegerField(
        db_column="CONTRIBUTOR_ID",
        help_text="Contributor identification number."
    )
    current_qtr_amt = fields.IntegerField(
        db_column="CURRENT_QTR_AMT",
        help_text="Current Quarter Amount"
    )
    firm_id = fields.IntegerField(
        db_column="FIRM_ID",
        help_text="Identification number of the Firm/Employer/Coalition."
    )
    firm_name = fields.CharField(
        db_column="FIRM_NAME",
        max_length=300,
        help_text="Name of Firm/Employer/Coalition"
    )
    qtr_1 = fields.IntegerField(
        db_column="QTR_1",
        help_text="Quarter total amount."
    )
    qtr_2 = fields.IntegerField(
        db_column="QTR_2",
        help_text="Quarter total amount."
    )
    qtr_3 = fields.IntegerField(
        db_column="QTR_3",
        help_text="Quarter total amount."
    )
    qtr_4 = fields.IntegerField(
        db_column="QTR_4",
        help_text="Quarter total amount."
    )
    qtr_5 = fields.IntegerField(
        db_column="QTR_5",
        help_text="Quarter total amount."
    )
    qtr_6 = fields.IntegerField(
        db_column="QTR_6",
        help_text="Quarter total amount."
    )
    qtr_7 = fields.IntegerField(
        db_column="QTR_7",
        help_text="Quarter total amount."
    )
    qtr_8 = fields.IntegerField(
        db_column="QTR_8",
        help_text="Quarter total amount."
    )
    session_id = fields.IntegerField(
        db_column="SESSION_ID",
        help_text="Session identification number."
    )
    session_total_amt = fields.IntegerField(
        db_column="SESSION_TOTAL_AMT",
        help_text="Total amount for the session."
    )
    session_yr_1 = fields.IntegerField(
        db_column="SESSION_YR_1",
        help_text="Total amount for year 1 of the session."
    )
    session_yr_2 = fields.IntegerField(
        db_column="SESSION_YR_2",
        help_text="Total amount for year 2 of the session."
    )
    yr_1_ytd_amt = fields.IntegerField(
        db_column="YR_1_YTD_AMT",
        help_text="YR_1_YTD_AMT"
    )
    yr_2_ytd_amt = fields.IntegerField(
        db_column="YR_2_YTD_AMT",
        help_text="Year 2 year to date amount."
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM_HISTORY_CD'
        verbose_name = 'LOBBYIST_FIRM_HISTORY_CD'
        verbose_name_plural = 'LOBBYIST_FIRM_HISTORY_CD'

    def __str__(self):
        return str(self.contributor_id)
