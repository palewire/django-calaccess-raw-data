#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Models for storing lobbying activity tables from the CAL-ACCESS database.
"""
# Models
from django.db import models
from calaccess_raw import fields
from .base import CalAccessBaseModel

# Annotations
from calaccess_raw import annotations
from calaccess_raw.annotations import DocumentCloud


class CvrRegistrationCd(CalAccessBaseModel):
    """
    The cover page of lobbying-registration forms.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=8),
        DocumentCloud(id='2711614', start_page=35, end_page=39),
        DocumentCloud(id='2711616', start_page=22, end_page=27),
        DocumentCloud(id='2712033', start_page=68, end_page=71),
        DocumentCloud(id='2712034', start_page=82, end_page=86),
    ]
    FILING_FORMS = [
        annotations.get_form('F601'),
        annotations.get_form('F602'),
        annotations.get_form('F603'),
        annotations.get_form('F604'),
        annotations.get_form('F606'),
        annotations.get_form('F607'),
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
            DocumentCloud(id='2712033', start_page=70),
            DocumentCloud(id='2712034', start_page=82),
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
        ('FRM', annotations.choices.LOBBYING_ENTITY_CODES['FRM']),
        ('LBY', annotations.choices.LOBBYING_ENTITY_CODES['LBY']),
        ('LCO', annotations.choices.LOBBYING_ENTITY_CODES['LCO']),
        ('LEM', annotations.choices.LOBBYING_ENTITY_CODES['LEM']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        help_text='Entity Code describing the filer',
        choices=ENTITY_CODE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712034', start_page=82),
            DocumentCloud(id='2712033', start_page=68),
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
        help_text="Unique filing identification number",
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
            DocumentCloud(id='2712033', start_page=68),
            DocumentCloud(id='2712034', start_page=82),
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
            DocumentCloud(id='2712034', start_page=85),
            DocumentCloud(id='2712033', start_page=70),
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
        ('y', 'Yes'),
        ('N', 'No'),
        ('n', 'No'),
        ('X', 'Yes'),
    )
    influen_yn = fields.CharField(
        null=True,
        max_length=1,
        choices=INFLUEN_YN_CHOICES,
        db_column='INFLUEN_YN',
        blank=True,
        help_text='Attempt to influence state legislation',
        documentcloud_pages=[
            DocumentCloud(id='2712034', start_page=86),
            DocumentCloud(id='2712033', start_page=71),
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
        help_text='Record Type Value: CVR',
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=68),
            DocumentCloud(id='2712034', start_page=82),
        ]
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
            DocumentCloud(id='2712034', start_page=86),
            DocumentCloud(id='2712033', start_page=71),
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'CVR_REGISTRATION_CD'
        ordering = ("-rpt_date",)

    def __str__(self):
        return str(self.filing_id)


class Cvr2RegistrationCd(CalAccessBaseModel):
    """
    Additional names provided on lobbying-registration forms.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=8),
        DocumentCloud(id='2711614', start_page=44, end_page=45),
        DocumentCloud(id='2711616', start_page=37, end_page=37),
        DocumentCloud(id='2712033', start_page=72, end_page=73),
        DocumentCloud(id='2712034', start_page=87, end_page=88),
    ]
    FILING_FORMS = [
        annotations.get_form('F601'),
        annotations.get_form('F602'),
        annotations.get_form('F603'),
    ]
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
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
        help_text="Record Type Value: CVR2",
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=72),
            DocumentCloud(id='2712034', start_page=87),
        ]
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=10,
        db_column='FORM_TYPE',
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=72),
            DocumentCloud(id='2712034', start_page=87),
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
        ('AGY', annotations.choices.LOBBYING_ENTITY_CODES['AGY']),
        ('EMP', annotations.choices.LOBBYING_ENTITY_CODES['EMP']),
        ('FRM', annotations.choices.LOBBYING_ENTITY_CODES['FRM']),
        ('LBY', annotations.choices.LOBBYING_ENTITY_CODES['LBY']),
        ('MBR', annotations.choices.LOBBYING_ENTITY_CODES['MBR']),
        ('SCL', annotations.choices.LOBBYING_ENTITY_CODES['SCL']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
        help_text="Entity code of the entity described by the record",
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=72),
            DocumentCloud(id='2712034', start_page=87),
        ]
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'CVR2_REGISTRATION_CD'

    def __str__(self):
        return str(self.filing_id)


class LobbyAmendmentsCd(CalAccessBaseModel):
    """
    Amendments to lobbyist-registration forms.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=10),
        DocumentCloud(id='2711614', start_page=90, end_page=91),
        DocumentCloud(id='2711616', start_page=64, end_page=66),
        DocumentCloud(id='2712033', start_page=74),
        DocumentCloud(id='2712034', start_page=88, end_page=89),
    ]
    FILING_FORMS = [
        annotations.get_form('F601'),
        annotations.get_form('F603'),
    ]
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
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
        help_text='Record Type Value: F605',
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=74),
            DocumentCloud(id='2712034', start_page=88),
        ]
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=9,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=74),
            DocumentCloud(id='2712034', start_page=88),
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBY_AMENDMENTS_CD'
        ordering = ("-exec_date",)

    def __str__(self):
        return str(self.filing_id)


class LobbyingChgLogCd(CalAccessBaseModel):
    """
    Log of lobbyist filings compiled for display on the state website.
    """
    UNIQUE_KEY = (
        "FILER_ID",
        "CHANGE_NO"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=10),
        DocumentCloud(id='2711614', start_page=91, end_page=92)
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
    filer_type = fields.ForeignKeyField(
        'FilerTypesCd',
        related_name='lobby_change_logs',
        db_constraint=False,
        help_text="Foreign key referencing FilerTypesCd.filer_type",
        db_column='FILER_TYPE',
        on_delete=models.CASCADE
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
        db_column="FILER_FULL_NAME",
        help_text='Full name of filer',
    )
    filer_city = fields.CharField(
        max_length=200,
        db_column="FILER_CITY",
        help_text='City address of filer',
    )
    filer_st = fields.CharField(
        max_length=200,
        db_column="FILER_ST",
        verbose_name="Filer state",
        help_text='State address of filer',
    )
    filer_zip = fields.IntegerField(
        db_column="FILER_ZIP",
        null=True,
        verbose_name="Filer ZIP Code",
        help_text='ZIP Code of filer',
    )
    filer_phone = fields.CharField(
        db_column="FILER_PHONE",
        null=True,
        max_length=12,
        verbose_name="Filer phone number",
        help_text="Phone number of filer",
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
FILER_TYPES_CD.FILER_TYPE or GROUP_TYPES_CD.GRP_ID, but that's just a guess."
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYING_CHG_LOG_CD'
        ordering = ("-log_dt",)

    def __str__(self):
        return str(self.filer_id)


class LempCd(CalAccessBaseModel):
    """
    Lobbyist employers and subcontracted clients.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=10),
        DocumentCloud(id='2711614', start_page=85, end_page=86),
        DocumentCloud(id='2711616', start_page=56, end_page=57),
        DocumentCloud(id='2712033', start_page=75),
        DocumentCloud(id='2712034', start_page=90, end_page=91),
    ]
    FILING_FORMS = [
        annotations.get_form('F601').get_section('P2A'),
        annotations.get_form('F601').get_section('P2B'),
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
        help_text="Unique filing identification number"
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        verbose_name='form type',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=75),
            DocumentCloud(id='2712034', start_page=90),
        ]
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
        help_text='Record Type Value: LEMP',
        choices=REC_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=75),
            DocumentCloud(id='2712034', start_page=90),
        ]
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LEMP_CD'
        ordering = ("-eff_date",)

    def __str__(self):
        return str(self.filing_id)


class CvrLobbyDisclosureCd(CalAccessBaseModel):
    """
    The cover page of lobbying-disclosure forms.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=8),
        DocumentCloud(id='2711614', start_page=32, end_page=35),
        DocumentCloud(id='2711616', start_page=17, end_page=21),
        DocumentCloud(id='2712033', start_page=53, end_page=56),
        DocumentCloud(id='2712034', start_page=66, end_page=70),
    ]
    FILING_FORMS = [
        annotations.get_form('F615'),
        annotations.get_form('F625'),
        annotations.get_form('F635'),
        annotations.get_form('F645'),
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
        ('CLI', 'Unknown'),
        ('FRM', annotations.choices.LOBBYING_ENTITY_CODES['FRM']),
        ('IND', annotations.choices.LOBBYING_ENTITY_CODES['IND']),
        ('LBY', annotations.choices.LOBBYING_ENTITY_CODES['LBY']),
        ('LCO', annotations.choices.LOBBYING_ENTITY_CODES['LCO']),
        ('LEM', annotations.choices.LOBBYING_ENTITY_CODES['LEM']),
        ('OTH', annotations.choices.LOBBYING_ENTITY_CODES['OTH']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
        help_text="Entity Code describing the filer",
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=53),
            DocumentCloud(id='2712034', start_page=67),
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
        help_text="Unique filing identification number"
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
            DocumentCloud(id='2712033', start_page=53),
            DocumentCloud(id='2712034', start_page=66),
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
        help_text="Record Type Value: CVR",
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=53),
            DocumentCloud(id='2712034', start_page=66),
        ]
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'CVR_LOBBY_DISCLOSURE_CD'
        ordering = ("-rpt_date",)

    def __str__(self):
        return str(self.filing_id)


class Cvr2LobbyDisclosureCd(CalAccessBaseModel):
    """
    Extra information from the cover sheets of lobbyist-disclosure form.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=8),
        DocumentCloud(id='2711614', start_page=43, end_page=44),
        DocumentCloud(id='2711616', start_page=36),
        DocumentCloud(id='2712033', start_page=57),
        DocumentCloud(id='2712034', start_page=71),
    ]
    FILING_FORMS = [
        annotations.get_form('F625'),
        annotations.get_form('F635'),
    ]
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    ENTITY_CODE_CHOICES = (
        ('EMP', annotations.choices.LOBBYING_ENTITY_CODES['EMP']),
        ('OFF', annotations.choices.LOBBYING_ENTITY_CODES['OFF']),
        ('OWN', annotations.choices.LOBBYING_ENTITY_CODES['OWN']),
        ('PTN', annotations.choices.LOBBYING_ENTITY_CODES['PTN']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
        help_text='Entity code of the entity described by the record',
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=57),
            DocumentCloud(id='2712034', start_page=71),
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
        help_text="Unique filing identification number"
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=4,
        db_column='FORM_TYPE',
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=57),
            DocumentCloud(id='2712034', start_page=71),
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
        help_text='Record Type Value: CVR2',
        choices=REC_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=57),
            DocumentCloud(id='2712034', start_page=71),
        ]
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'CVR2_LOBBY_DISCLOSURE_CD'

    def __str__(self):
        return str(self.filing_id)


class F690P2Cd(CalAccessBaseModel):
    """
    Amendments to lobbying-disclosure filings.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=8),
        DocumentCloud(id='2711614', start_page=59, end_page=60),
        DocumentCloud(id='2711616', start_page=50, end_page=51),
        DocumentCloud(id='2712033', start_page=58),
        DocumentCloud(id='2712034', start_page=72),
    ]
    FILING_FORMS = [
        annotations.get_form('F615'),
        annotations.get_form('F625'),
        annotations.get_form('F635'),
        annotations.get_form('F645'),
    ]
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
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
        help_text="Record Type Value: F690",
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=58),
            DocumentCloud(id='2712034', start_page=72),
        ]
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=4,
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=58),
            DocumentCloud(id='2712034', start_page=72),
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'F690P2_CD'
        ordering = ("-exec_date",)

    def __str__(self):
        return str(self.filing_id)


class LattCd(CalAccessBaseModel):
    """
    Attachments for lobbying payments.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=81, end_page=82),
        DocumentCloud(id='2711616', start_page=52, end_page=53),
        DocumentCloud(id='2712033', start_page=65),
        DocumentCloud(id='2712034', start_page=79, end_page=80),
    ]
    FILING_FORMS = [
        annotations.get_form('S630'),
        annotations.get_form('S635C'),
        annotations.get_form('S640'),
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
        ('FRM', annotations.choices.LOBBYING_ENTITY_CODES['FRM']),
        ('IND', annotations.choices.LOBBYING_ENTITY_CODES['IND']),
        ('LBY', annotations.choices.LOBBYING_ENTITY_CODES['LBY']),
        ('LCO', annotations.choices.LOBBYING_ENTITY_CODES['LCO']),
        ('LEM', annotations.choices.LOBBYING_ENTITY_CODES['LEM']),
        ('OTH', annotations.choices.LOBBYING_ENTITY_CODES['OTH']),
        ('RCP', annotations.choices.LOBBYING_ENTITY_CODES['RCP']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
        help_text='Entity Code of the Payment Recipient/Payee',
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=65),
            DocumentCloud(id='2712034', start_page=80),
        ]
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=6,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711616', start_page=52),
            DocumentCloud(id='2712033', start_page=65),
            DocumentCloud(id='2712034', start_page=79),
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
        help_text="Record Type Value: LATT",
        choices=REC_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=65),
            DocumentCloud(id='2712034', start_page=79),
        ]
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LATT_CD'
        ordering = ("-pmt_date",)

    def __str__(self):
        return str(self.filing_id)


class LexpCd(CalAccessBaseModel):
    """
    Lobbying activity expenditures.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=10),
        DocumentCloud(id='2711614', start_page=86, end_page=87),
        DocumentCloud(id='2711616', start_page=58, end_page=59),
        DocumentCloud(id='2712033', start_page=61),
        DocumentCloud(id='2712034', start_page=74, end_page=75),
    ]
    FILING_FORMS = [
        annotations.get_form('F615').get_section('P1'),
        annotations.get_form('F625').get_section('P3A'),
        annotations.get_form('F635').get_section('P3C'),
        annotations.get_form('F645').get_section('P2A'),
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
        ('IND', annotations.choices.LOBBYING_ENTITY_CODES['IND']),
        ('OTH', annotations.choices.LOBBYING_ENTITY_CODES['OTH']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
        help_text="Entity Code of the Payee",
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=61),
            DocumentCloud(id='2712034', start_page=75),
        ]
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
        help_text="Unique filing identification number"
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=61),
            DocumentCloud(id='2712034', start_page=74),
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
        help_text="Record Type Value: LEXP",
        choices=REC_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=61),
            DocumentCloud(id='2712034', start_page=74),
        ]
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
        help_text='Record Subtype',
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=61),
            DocumentCloud(id='2712034', start_page=74),
        ]
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LEXP_CD'
        ordering = ("-expn_date",)

    def __str__(self):
        return str(self.filing_id)


class LccmCd(CalAccessBaseModel):
    """
    Lobbyist campaign contributions.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=10),
        DocumentCloud(id='2711614', start_page=83, end_page=84),
        DocumentCloud(id='2711616', start_page=54, end_page=55),
        DocumentCloud(id='2712033', start_page=64),
        DocumentCloud(id='2712034', start_page=78, end_page=79),
    ]
    FILING_FORMS = [
        annotations.get_form('F615').get_section('P2'),
        annotations.get_form('F625').get_section('P4B'),
        annotations.get_form('F635').get_section('P4B'),
        annotations.get_form('F645').get_section('P3B'),
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
        ('COM', annotations.choices.LOBBYING_ENTITY_CODES['COM']),
        ('RCP', annotations.choices.LOBBYING_ENTITY_CODES['RCP']),
        # Not sure this is a valid value of lobbying records, but has over 1,000 occurrences
        ('CTL', annotations.choices.CAMPAIGN_ENTITY_CODES['CTL']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        help_text='Entity Code for Recipient of the Campaign Contribution Value',
        choices=ENTITY_CODE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=64),
            DocumentCloud(id='2712034', start_page=78),
        ],
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=64),
            DocumentCloud(id='2712034', start_page=78, end_page=79),
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
        help_text="Record Type Value: LCCM",
        choices=REC_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=64),
            DocumentCloud(id='2712034', start_page=78),
        ],
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LCCM_CD'
        ordering = ("-ctrib_date",)

    def __str__(self):
        return str(self.filing_id)


class LpayCd(CalAccessBaseModel):
    """
    Payments made or received by lobbying firms.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=107, end_page=109),
        DocumentCloud(id='2711616', start_page=69, end_page=70),
        DocumentCloud(id='2712033', start_page=62),
        DocumentCloud(id='2712034', start_page=76, end_page=77),
    ]
    FILING_FORMS = [
        annotations.get_form('F625').get_section('P2'),
        annotations.get_form('F635').get_section('P3B'),
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
        ('FRM', annotations.choices.LOBBYING_ENTITY_CODES['FRM']),
        ('LCO', annotations.choices.LOBBYING_ENTITY_CODES['LCO']),
        ('LEM', annotations.choices.LOBBYING_ENTITY_CODES['LEM']),
        ('OTH', annotations.choices.LOBBYING_ENTITY_CODES['OTH']),
        ('128', 'Unknown'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
        help_text='Entity Code of the Employer Values',
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=62),
            DocumentCloud(id='2712034', start_page=76),
        ]
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
        help_text="Unique filing identification number"
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        verbose_name='form type',
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=62),
            DocumentCloud(id='2712034', start_page=76),
        ]
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
        help_text="Record Type Value: LPAY",
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=62),
            DocumentCloud(id='2712034', start_page=76),
        ]
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LPAY_CD'

    def __str__(self):
        return str(self.filing_id)


class LothCd(CalAccessBaseModel):
    """
    Payments to other lobbying firms.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=106, end_page=107),
        DocumentCloud(id='2711616', start_page=67, end_page=68),
        DocumentCloud(id='2712033', start_page=63),
        DocumentCloud(id='2712034', start_page=77, end_page=78),
    ]
    FILING_FORMS = [
        annotations.get_form('F625').get_section('P3B'),
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
        help_text="Unique filing identification number"
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
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=63),
            DocumentCloud(id='2712034', start_page=77),
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
        help_text='Record Type Value: LOTH',
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=63),
            DocumentCloud(id='2712034', start_page=77),
        ]
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOTH_CD'
        ordering = ("-pmt_date",)

    def __str__(self):
        return str(self.filing_id)
