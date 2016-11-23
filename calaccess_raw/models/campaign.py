#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Models for storing campaign finance tables from the CAL-ACCESS database.
"""
from __future__ import unicode_literals
from calaccess_raw import fields
from .base import CalAccessBaseModel
from calaccess_raw.annotations.filing_forms import get_filing_form
from django.utils.encoding import python_2_unicode_compatible
from calaccess_raw.annotations import (
    DocumentCloud,
    choices,
    get_sorted_choices
)


@python_2_unicode_compatible
class CvrSoCd(CalAccessBaseModel):
    """
    The cover page for statement-of-organization forms that create or terminate an entity.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "REC_TYPE",
        "FORM_TYPE",
    )
    DOCUMENTCLOUD_PAGES = [
        # CAL-ACCESS record layout
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=39, end_page=41),
        # Mapping of .CAL format to CAL-ACCESS database table / fields
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=28, end_page=31),
        # .CAL Format v1.05.02
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=46, end_page=47),
        # .CAL Formate v2.01
        DocumentCloud(id='2712034-Cal-Format-201', start_page=59, end_page=61),
    ]
    FILING_FORMS = [
        get_filing_form('F400').get_section('P1'),
        get_filing_form('F400').get_section('P2'),
        get_filing_form('F400').get_section('P4'),
        get_filing_form('F402').get_section('CVR'),
        get_filing_form('F410').get_section('P1'),
        get_filing_form('F410').get_section('P2'),
        get_filing_form('F410').get_section('P4'),
    ]
    acct_opendt = fields.DateField(
        db_column="ACCT_OPENDT",
        verbose_name='account opened datetime',
        null=True,
        help_text='Date Account Opened'
    )
    ACTIVITY_LVL_CHOICES = (
        ("CI", "City"),
        ("CO", "County"),
        ("ST", "State"),
        ("St", "State"),
        ("st", "State"),
    )
    actvty_lvl = fields.CharField(
        max_length=2,
        db_column="ACTVTY_LVL",
        blank=True,
        choices=ACTIVITY_LVL_CHOICES,
        verbose_name="activity level",
        help_text="Organization's level of activity",
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=30),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=47),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=60),
        ]
    )
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        verbose_name="amendment ID",
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
    )
    bank_adr1 = fields.CharField(
        max_length=55,
        db_column="BANK_ADR1",
        blank=True,
        verbose_name='bank address 1',
        help_text='Street 1 of Financial Institution',
    )
    bank_adr2 = fields.CharField(
        max_length=55,
        db_column="BANK_ADR2",
        blank=True,
        verbose_name='bank address 2',
        help_text='Street 2 of Financial Institution',
    )
    bank_city = fields.CharField(
        max_length=30,
        db_column="BANK_CITY",
        blank=True,
        verbose_name='bank city',
        help_text='City of Financial Institution',
    )
    bank_nam = fields.CharField(
        max_length=200,
        db_column="BANK_NAM",
        blank=True,
        verbose_name='bank name',
        help_text='Name of Financial Institution',
    )
    bank_phon = fields.CharField(
        max_length=20,
        db_column="BANK_PHON",
        blank=True,
        verbose_name='bank phone',
        help_text='Phone of Financial Institution',
    )
    bank_st = fields.CharField(
        max_length=2,
        db_column="BANK_ST",
        blank=True,
        verbose_name='bank street',
        help_text='State of Financial Institution',
    )
    bank_zip4 = fields.CharField(
        max_length=10,
        db_column="BANK_ZIP4",
        blank=True,
        verbose_name='bank zip4',
        help_text='ZIP+4 of Financial Institution',
    )
    brdbase_cb = fields.CharField(
        max_length=1,
        db_column="BRDBASE_CB",
        blank=True,
        verbose_name='broad based committee check-box',
        help_text='Broad Based Committee Check-box',
    )
    city = fields.CharField(
        max_length=30,
        db_column="CITY",
        blank=True,
        verbose_name='city',
        help_text='City of Org / Committee / Candidate or Office holder',
    )
    cmte_email = fields.CharField(
        max_length=60,
        db_column="CMTE_EMAIL",
        blank=True,
        verbose_name='committee email',
        help_text='Optional Committee EMAIL address',
    )
    cmte_fax = fields.CharField(
        max_length=20,
        db_column="CMTE_FAX",
        blank=True,
        verbose_name='committee fax',
        help_text='Optional Committee FAX number',
    )
    com82013id = fields.CharField(
        max_length=9,
        db_column="COM82013ID",
        blank=True,
        verbose_name='committee 82013 id',
        help_text='ID of 82013 Committee (if Com82013Nm is a RCP cmtte)',
    )
    com82013nm = fields.CharField(
        max_length=200,
        db_column="COM82013NM",
        blank=True,
        verbose_name='committee 82013 name',
        help_text='Name of 82013 Committee (F400; when Com82013YN=Y)',
    )
    com82013yn = fields.CharField(
        max_length=1,
        db_column="COM82013YN",
        blank=True,
        verbose_name='committee 82013 yes/no',
        help_text='Is this SMO a 82013 "Committee"? (Yes/No) (F400)',
    )
    control_cb = fields.CharField(
        max_length=1,
        db_column="CONTROL_CB",
        blank=True,
        verbose_name='controlled checkbox',
        help_text='Controlled Committee Check-box',
    )
    county_act = fields.CharField(
        max_length=20,
        db_column="COUNTY_ACT",
        blank=True,
        verbose_name="county active",
        help_text='County where Active (F410)',
    )
    county_res = fields.CharField(
        max_length=20,
        db_column="COUNTY_RES",
        blank=True,
        verbose_name='county residence',
        help_text='County of Domicile, Residence, or Location',
    )
    ENTITY_CD_CHOICES = (
        ('BMC', choices.CAMPAIGN_ENTITY_CODES['BMC']),
        ('CAO', choices.CAMPAIGN_ENTITY_CODES['CAO']),
        ('COM', choices.CAMPAIGN_ENTITY_CODES['COM']),
        ('CTL', choices.CAMPAIGN_ENTITY_CODES['CTL']),
        ('RCP', choices.CAMPAIGN_ENTITY_CODES['RCP']),
        ('SMO', choices.CAMPAIGN_ENTITY_CODES['SMO']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column="ENTITY_CD",
        blank=True,
        choices=ENTITY_CD_CHOICES,
        verbose_name="Entity code",
        help_text="Entity Code of the Filer. Values: \
SMO - Slate Mailer Organization (F400,402) [COM|RCP] - Recipient Committee (F410)",
        documentcloud_pages=choices.DOCS['entity_codes'] + [
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=46),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=59),
        ],
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
        db_column="FILER_NAMF",
        blank=True,
        verbose_name="filer first name",
        help_text="Filer first name",
    )
    filer_naml = fields.CharField(
        max_length=200,
        db_column="FILER_NAML",
        blank=True,
        verbose_name="filer last name",
        help_text="Filer last name",
    )
    filer_nams = fields.CharField(
        max_length=10,
        db_column="FILER_NAMS",
        blank=True,
        verbose_name="filer name suffix",
        help_text="Filer name suffix",
    )
    filer_namt = fields.CharField(
        max_length=10,
        db_column="FILER_NAMT",
        blank=True,
        verbose_name="filer name title",
        help_text="Filer name title",
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing id',
        help_text="Unique filing identification number"
    )
    FORM_TYPE_CHOICES = (
        ('F400', get_filing_form('F400').full_title),
        ('F402', get_filing_form('F402').full_title),
        ('F410', get_filing_form('F410').full_title),
    )
    form_type = fields.CharField(
        max_length=4,
        db_column="FORM_TYPE",
        verbose_name='form type',
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=46),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=59),
        ]
    )
    genpurp_cb = fields.CharField(
        max_length=1,
        db_column="GENPURP_CB",
        blank=True,
        verbose_name='general purpose checkbox',
        help_text='General Purpose Committee Check-box',
    )
    gpc_descr = fields.CharField(
        max_length=300,
        db_column="GPC_DESCR",
        blank=True,
        verbose_name='general purpose committee description',
        help_text='Brief description of Activity of GPC',
    )
    mail_city = fields.CharField(
        max_length=30,
        db_column="MAIL_CITY",
        blank=True,
        verbose_name='mail city',
        help_text='Mailing Address of Filing Committee - City',
    )
    mail_st = fields.CharField(
        max_length=2,
        db_column="MAIL_ST",
        blank=True,
        verbose_name='mail street',
        help_text='Mailing Address of Filing Committee - State',
    )
    mail_zip4 = fields.CharField(
        max_length=10,
        db_column="MAIL_ZIP4",
        blank=True,
        verbose_name='mail zip4',
        help_text='Mailing Address of Filing Committee - ZIP+4',
    )
    phone = fields.CharField(
        max_length=20,
        db_column="PHONE",
        blank=True,
        verbose_name='phone',
        help_text='Phone Number of Org / Committee / Candidate or Office holder',
    )
    primfc_cb = fields.CharField(
        max_length=1,
        db_column="PRIMFC_CB",
        blank=True,
        verbose_name='primarily formed committee check-box',
        help_text='Primarily Formed Committee Check-box',
    )
    qualfy_dt = fields.DateField(
        db_column="QUALFY_DT",
        null=True,
        verbose_name="qualified datetime",
        help_text="Date qualified as an organization"
    )
    qual_cb = fields.CharField(
        max_length=1,
        db_column="QUAL_CB",
        blank=True,
        verbose_name='qualified checkbox',
        help_text='Qualified Committee check-box (Req. if SMO)',
    )
    REC_TYPE_CHOICES = (
        ("CVR", "Cover Page for Stmt of Organization / Slate Mailer Org, Stmt of \
Termination / Slate Mailer Org or Stmt of Organization / Recipient Committee"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        help_text="Record Type Value: CVR",
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=28),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=46),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=59),
        ],
    )
    report_num = fields.CharField(
        max_length=3,
        db_column="REPORT_NUM",
        blank=True,
        verbose_name='report number',
        help_text='Report Number - Values: \
000 - Original Report 001 thru 999 - Amended Rpt #1-#999',
    )
    rpt_date = fields.DateField(
        db_column="RPT_DATE",
        null=True,
        verbose_name='report date',
        help_text='Date this report is filed',
    )
    smcont_qualdt = fields.DateField(
        db_column="SMCONT_QUALDT",
        null=True,
        verbose_name='small contributor qualified datetime',
        help_text='Date Small Contributor Committee Qualified',
    )
    sponsor_cb = fields.CharField(
        max_length=1,
        db_column="SPONSOR_CB",
        blank=True,
        verbose_name='sponsored checkbox',
        help_text='Sponsored Committee Check-box',
    )
    st = fields.CharField(
        max_length=2,
        db_column="ST",
        blank=True,
        verbose_name='street',
        help_text='State of Org / Committee / Candidate or Office holder',
    )
    surplusdsp = fields.CharField(
        max_length=90,
        db_column="SURPLUSDSP",
        blank=True,
        verbose_name='surplus disposition',
        help_text='Disposition of Surplus Funds',
    )
    term_date = fields.DateField(
        db_column="TERM_DATE",
        null=True,
        verbose_name='termination date',
        help_text='Termination Effective Date (Req. if F402)',
    )
    tres_city = fields.CharField(
        max_length=30,
        db_column="TRES_CITY",
        blank=True,
        verbose_name="treasurer city",
        help_text="Treasurer's city",
    )
    tres_namf = fields.CharField(
        max_length=45,
        db_column="TRES_NAMF",
        blank=True,
        verbose_name="treasurer first name",
        help_text="Treasurer's first name",
    )
    tres_naml = fields.CharField(
        max_length=200,
        db_column="TRES_NAML",
        blank=True,
        verbose_name="treasurer last name",
        help_text="Treasurer's last name",
    )
    tres_nams = fields.CharField(
        max_length=10,
        db_column="TRES_NAMS",
        blank=True,
        verbose_name="treasurer name suffix",
        help_text="Treasurer's name suffix",
    )
    tres_namt = fields.CharField(
        max_length=10,
        db_column="TRES_NAMT",
        blank=True,
        verbose_name="treasurer name title",
        help_text="Treasurer's name title",
    )
    tres_phon = fields.CharField(
        max_length=20,
        db_column="TRES_PHON",
        blank=True,
        verbose_name="treasurer phone number",
        help_text="Treasurer's phone number",
    )
    tres_st = fields.CharField(
        max_length=2,
        db_column="TRES_ST",
        blank=True,
        verbose_name="treasurer street",
        help_text="Treasurer's street",
    )
    tres_zip4 = fields.CharField(
        max_length=10,
        db_column="TRES_ZIP4",
        blank=True,
        verbose_name="treasurer zip code",
        help_text="Treasurer's ZIP Code",
    )
    zip4 = fields.CharField(
        max_length=10,
        db_column="ZIP4",
        blank=True,
        verbose_name='zip4',
        help_text='ZIP+4 for Org / Committee / Candidate or Office holder',
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = "CVR_SO_CD"
        ordering = ("-rpt_date",)

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class Cvr2SoCd(CalAccessBaseModel):
    """
    Extra information from a statement-of-organization form.
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
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=45, end_page=46),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=38, end_page=40),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=48, end_page=49),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=62, end_page=64),
    ]
    FILING_FORMS = [
        get_filing_form('F400').get_section('P3'),
        get_filing_form('F410').get_section('P4'),
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
        verbose_name="amendment ID",
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        db_index=True,
        verbose_name='line item',
        help_text="Line item number of this record",
    )
    REC_TYPE_CHOICES = (
        ("CVR2", "Cover Page; Additional Names & Addresses"),
    )
    rec_type = fields.CharField(
        choices=REC_TYPE_CHOICES,
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        verbose_name='record type',
        help_text='Type of record. This column will always contain "CVR2".',
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=38),
            DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=46),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=45),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=58),
        ]
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        choices=FORM_TYPE_CHOICES,
        db_column='FORM_TYPE',
        max_length=4,
        verbose_name='form type',
        help_text="Form type of the filing the record is included in. This must \
equal the form_type of the parent filing's cover (CVR) record.",
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=38),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=45, end_page=46),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=58, end_page=59),
        ]
    )
    tran_id = fields.CharField(
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        verbose_name='transaction ID',
        help_text='Permanent value unique to this item',
    )
    ENTITY_CD_CHOICES = (
        ('ATH', choices.CAMPAIGN_ENTITY_CODES['ATH']),
        ('ATR', choices.CAMPAIGN_ENTITY_CODES['ATR']),
        ('BNM', choices.CAMPAIGN_ENTITY_CODES['BNM']),
        ('CAO', choices.CAMPAIGN_ENTITY_CODES['CAO']),
        ('COM', choices.CAMPAIGN_ENTITY_CODES['COM']),
        ('CTL', choices.CAMPAIGN_ENTITY_CODES['CTL']),
        ('OFF', choices.CAMPAIGN_ENTITY_CODES['OFF']),
        ('POF', choices.CAMPAIGN_ENTITY_CODES['POF']),
        ('PRO', choices.CAMPAIGN_ENTITY_CODES['PRO']),
        ('SPO', choices.CAMPAIGN_ENTITY_CODES['SPO']),
        ('BMN', 'Unknown'),  # Misspelling of 'BNM'?
    )
    entity_cd = fields.CharField(
        choices=ENTITY_CD_CHOICES,
        blank=True,
        db_column='ENTITY_CD',
        max_length=3,
        verbose_name='entity code',
        help_text='Entity code of the entity described by the record.',
        documentcloud_pages=choices.DOCS['entity_codes'] + [
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=38),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=48),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=62),
        ]
    )
    enty_naml = fields.CharField(
        db_column='ENTY_NAML',
        max_length=200,
        blank=True,
        verbose_name='entity last name',
        help_text="Entity's business name or last name if the entity is an \
individual"
    )
    enty_namf = fields.CharField(
        db_column='ENTY_NAMF',
        max_length=45,
        blank=True,
        verbose_name='entity first name',
        help_text="Entity's first name if the entity is an individual"
    )
    enty_namt = fields.CharField(
        db_column='ENTY_NAMT',
        max_length=10,
        blank=True,
        verbose_name='entity name title',
        help_text="Entity's name prefix or title if the entity is an \
individual"
    )
    enty_nams = fields.CharField(
        db_column='ENTY_NAMS',
        max_length=10,
        blank=True,
        verbose_name='entity name suffix',
        help_text="Entity's name suffix if the entity is an individual"
    )
    ITEM_CD_CHOICES = (
        ('ATR', 'Assistant Treasurer (F410)'),
        ('CAO', choices.CAMPAIGN_ENTITY_CODES['CAO']),
        ('CTL', 'Controlled Committee (F410)'),
        ('P5B', 'Unknown'),
        ('PFC', 'Primarily Formed Committee Item (F410)'),
        ('Pfc', 'Primarily Formed Committee Item (F410)'),
        ('POF', 'Principal Officer (F400, F410'),
        ('PRO', choices.CAMPAIGN_ENTITY_CODES['PRO']),
        ('SMA', 'Slate Mailer Authorizer (F400)'),
        ('SPO', 'Sponsored Committee Itemization (F410)'),
        ('n/a', 'Not Applicable'),
        ('CON', 'Unknown'),
        ('CST', 'Unknown'),
    )
    item_cd = fields.CharField(
        db_column='ITEM_CD',
        max_length=4,
        blank=True,
        choices=ITEM_CD_CHOICES,
        verbose_name='item code',
        help_text="Section of the Statement of Organization this itemization \
relates to. See CAL document for the definition of legal values for this column.",
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=8),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=10),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=48),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=62),
        ],
    )
    mail_city = fields.CharField(
        db_column='MAIL_CITY',
        max_length=30,
        blank=True,
        verbose_name='mail city',
        help_text="City portion of the entity's mailing address"
    )
    mail_st = fields.CharField(
        db_column='MAIL_ST',
        max_length=4,
        blank=True,
        verbose_name='mail street',
        help_text="State portion of the entity's mailing address"
    )
    mail_zip4 = fields.CharField(
        db_column='MAIL_ZIP4',
        max_length=10,
        blank=True,
        verbose_name='mail zip4',
        help_text="Zipcode portion of the entity's mailing address",
    )
    day_phone = fields.CharField(
        db_column='DAY_PHONE',
        max_length=20,
        blank=True,
        verbose_name='day phone',
        help_text="Entity's daytime phone number"
    )
    fax_phone = fields.CharField(
        db_column='FAX_PHONE',
        max_length=20,
        blank=True,
        verbose_name='fax phone number',
        help_text="Entity's fax number"
    )
    email_adr = fields.CharField(
        db_column='EMAIL_ADR',
        max_length=60,
        blank=True,
        verbose_name='email address',
        help_text="Email address. Not contained in current forms."
    )
    cmte_id = fields.IntegerField(
        db_column='CMTE_ID',
        blank=True,
        null=True,
        verbose_name="Committee ID",
        help_text="Entity's identification number"
    )
    ind_group = fields.CharField(
        db_column='IND_GROUP',
        max_length=90,
        blank=True,
        verbose_name='industry group',
        help_text="Industry group/affiliation description"
    )
    OFFICE_CD_CHOICES = get_sorted_choices(choices.OFFICE_CODES) + (
        ('Asm', choices.OFFICE_CODES['ASM']),
        ('LEG', choices.OFFICE_CODES['ASM']),
        ('OF', choices.OFFICE_CODES['ASM']),
        ('REP', choices.OFFICE_CODES['ASM']),
        ('05', choices.OFFICE_CODES['ASM']),
        # Only one record: http://cal-access.ss.ca.gov/PDFGen/pdfgen.prg?filingid=1388367&amendid=0
        # Looks like this was corrected on a later amendment.
        # Don't think they actually mean to specify a jurisdiction
        ('H', 'N/A'),
        # Only one record: http://cal-access.ss.ca.gov/PDFGen/pdfgen.prg?filingid=1613541&amendid=1
        # Seems like this committee is supporting a state measure, rather than any candidate
        # Don't think they actually mean to specify an office. Was removed on later amendment
        ('PRO', 'N/A'),
        # All over the board
        ('PAC', 'Unknown'),
    )
    office_cd = fields.CharField(
        db_column='OFFICE_CD',
        max_length=3,
        blank=True,
        verbose_name="office code",
        help_text="Identifies the office being sought",
        choices=OFFICE_CD_CHOICES,
        documentcloud_pages=choices.DOCS['office_codes']
    )
    offic_dscr = fields.CharField(
        db_column='OFFIC_DSCR',
        max_length=40,
        blank=True,
        verbose_name='office description',
        help_text="Office sought description used if the office sought code \
(OFFICE_CD) equals other (OTH)."
    )
    JURIS_CD_CHOICES = get_sorted_choices(choices.JURIS_CODES) + (
        # Only one record: http://cal-access.ss.ca.gov/PDFGen/pdfgen.prg?filingid=1388367&amendid=0
        # Looks like this was corrected on a later amendment.
        # Don't think they actually mean to specify a jurisdiction
        ('FED', 'N/A'),
        # Only one record: http://cal-access.ss.ca.gov/PDFGen/pdfgen.prg?filingid=1125823&amendid=0
        ('JR', 'N/A'),
    )
    juris_cd = fields.CharField(
        choices=JURIS_CD_CHOICES,
        db_column='JURIS_CD',
        max_length=4,
        blank=True,
        verbose_name='jurisdiction code',
        help_text="Office jurisdiction code. See CAL document for a \
list of legal values.",
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=39),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=49),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=63),
        ],
    )
    juris_dscr = fields.CharField(
        db_column='JURIS_DSCR',
        max_length=40,
        blank=True,
        verbose_name='jurisdiction description',
        help_text="Office jurisdiction description provided if the \
        jurisdiction code (JURIS_CD) equals other (OTH)."
    )
    dist_no = fields.CharField(
        db_column='DIST_NO',
        max_length=4,
        blank=True,
        verbose_name='district name',
        help_text="Office district number for Senate, Assembly, and Board \
of Equalization districts."
    )
    OFF_S_H_CD_CHOICES = get_sorted_choices(choices.OFF_S_H_CODES)
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        verbose_name='office is sought or held code',
        help_text='Office sought/held code. Legal values are "S" for \
sought and "H" for held',
        choices=OFF_S_H_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=46),
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=39),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=49),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=63),
        ]
    )
    non_pty_cb = fields.CharField(
        db_column='NON_PTY_CB',
        max_length=4,
        blank=True,
        verbose_name='non-party checkbox',
        help_text="Non-partisan check-box. Legal values are 'X' and null."
    )
    party_name = fields.CharField(
        db_column='PARTY_NAME',
        max_length=200,
        blank=True,
        verbose_name='party name',
        help_text="Name of party (if partisan)"
    )
    bal_num = fields.CharField(
        db_column='BAL_NUM',
        max_length=7,
        blank=True,
        verbose_name='balance number',
        help_text="Ballot measure number or letter"
    )
    bal_juris = fields.CharField(
        db_column='BAL_JURIS',
        max_length=40,
        blank=True,
        verbose_name='balance jurisdiction',
        help_text="Jurisdiction of ballot measure"
    )
    SUP_OPP_CD_CHOICES = get_sorted_choices(choices.SUP_OPP_CODES)
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text="Support or opposition code",
        verbose_name='support or opposition code',
        choices=SUP_OPP_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=46),
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=40),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=49),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=64),
        ]
    )
    year_elect = fields.CharField(
        db_column='YEAR_ELECT',
        max_length=4,
        blank=True,
        verbose_name="year of election",
        help_text="Year of election",
    )
    pof_title = fields.CharField(
        db_column='POF_TITLE',
        max_length=45,
        blank=True,
        verbose_name='principal officer title',
        help_text="Position/title of the principal officer",
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'CVR2_SO_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class CvrCampaignDisclosureCd(CalAccessBaseModel):
    """
    The cover page of campaign-disclosure forms.
    """
    UNIQUE_KEY = ('FILING_ID', 'AMEND_ID',)
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id="2711614-CalAccessTablesWeb", start_page=7),
        DocumentCloud(id="2711614-CalAccessTablesWeb", start_page=25, end_page=29),
        DocumentCloud(id="2711616-MapCalFormat2Fields", start_page=6, end_page=14),
        DocumentCloud(id="2712033-Cal-Format-1-05-02", start_page=18, end_page=22),
        DocumentCloud(id="2712034-Cal-Format-201", start_page=22, end_page=30),
    ]
    FILING_FORMS = [
        get_filing_form('F401').get_section('CVR'),
        get_filing_form('F425').get_section('P1'),
        get_filing_form('F450').get_section('CVR'),
        get_filing_form('F460').get_section('CVR'),
        get_filing_form('F461').get_section('P1'),
        get_filing_form('F461').get_section('P2'),
        get_filing_form('F465').get_section('P1'),
        get_filing_form('F465').get_section('P2'),
        get_filing_form('F496').get_section('P1'),
        get_filing_form('F497'),
        get_filing_form('F498'),
        get_filing_form('F511'),
        get_filing_form('F900'),
    ]
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    amendexp_1 = fields.CharField(
        max_length=100,
        db_column='AMENDEXP_1',
        blank=True,
        help_text='Amendment explanation line 1'
    )
    amendexp_2 = fields.CharField(
        max_length=100,
        db_column='AMENDEXP_2',
        blank=True,
        help_text="Amendment explanation line 2"
    )
    amendexp_3 = fields.CharField(
        max_length=100,
        db_column='AMENDEXP_3',
        blank=True,
        help_text="Amendment explanation line 3"
    )
    assoc_cb = fields.CharField(
        max_length=4,
        db_column='ASSOC_CB',
        blank=True,
        help_text="Association Interests info included check-box. Legal \
values are 'X' and null."
    )
    assoc_int = fields.CharField(
        max_length=90,
        db_column='ASSOC_INT',
        blank=True,
        help_text="Description of association interests"
    )
    bal_id = fields.CharField(
        max_length=9,
        db_column='BAL_ID',
        blank=True,
        help_text='.CAL format to db tables doc says: "Not Used-AMS KDE"'
    )
    bal_juris = fields.CharField(
        max_length=40,
        db_column='BAL_JURIS',
        blank=True,
        help_text="Ballot measure jurisdiction"
    )
    bal_name = fields.CharField(
        max_length=200,
        db_column='BAL_NAME',
        blank=True,
        help_text="Ballot measure name"
    )
    bal_num = fields.CharField(
        max_length=4,
        db_column='BAL_NUM',
        blank=True,
        help_text="Ballot measure number or letter"
    )
    brdbase_yn = fields.CharField(
        max_length=1,
        db_column='BRDBASE_YN',
        blank=True,
        help_text="Broad Base Committee (yes/no) check box. Legal \
values are 'Y' or 'N'."
    )
    # these fields are described in the following docs:
    # https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/25.html
    # but are not included on the .tsv file
    # bus_adr1 = fields.CharField(
    #     max_length=55,
    #     db_column='BUS_ADR1',
    #     blank=True,
    #     help_text="First line of the employer/business street address. Applies to the form 461.",
    # )
    # bus_adr2 = fields.CharField(
    #     max_length=55,
    #     db_column='BUS_ADR2',
    #     blank=True,
    #     help_text="Second line of the employer/business street address. Applies to the form 461.",
    # )
    bus_city = fields.CharField(
        max_length=30,
        db_column='BUS_CITY',
        blank=True,
        help_text="Employer/business address city"
    )
    bus_inter = fields.CharField(
        max_length=40,
        db_column='BUS_INTER',
        blank=True,
        help_text="Employer/business interest description"
    )
    bus_name = fields.CharField(
        max_length=200,
        db_column='BUS_NAME',
        blank=True,
        help_text="Name of employer/business. Applies to the form 461."
    )
    bus_st = fields.CharField(
        max_length=2,
        db_column='BUS_ST',
        blank=True,
        help_text="Employer/business address state"
    )
    bus_zip4 = fields.CharField(
        max_length=10,
        db_column='BUS_ZIP4',
        blank=True,
        help_text="Employer/business address ZIP Code"
    )
    busact_cb = fields.CharField(
        max_length=10,
        db_column='BUSACT_CB',
        blank=True,
        help_text="Business activity info included check-box. Valid values \
are 'X' and null"
    )
    busactvity = fields.CharField(
        max_length=90,
        db_column='BUSACTVITY',
        blank=True,
        help_text="Business activity description"
    )
    # these fields are described in the following docs:
    # https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/25.html
    # but are not included on the .tsv file
    # cand_adr1 = fields.CharField(
    #     max_length=55,
    #     db_column='CAND_ADR1',
    #     blank=True,
    #     help_text="First line of the candidate/officeholder's street address. \
# Applies to form 460, 465, and 496.",
    # )
    # cand_adr2 = fields.CharField(
    #     max_length=55,
    #     db_column='CAND_ADR2',
    #     blank=True,
    #     help_text="Second line of the candidate/officeholder's street address.",
    # )
    cand_city = fields.CharField(
        max_length=30,
        db_column='CAND_CITY',
        blank=True,
        help_text='Candidate/officeholder city'
    )
    cand_email = fields.CharField(
        max_length=60,
        db_column='CAND_EMAIL',
        blank=True,
        help_text='Candidate/officeholder email. This field \
is not contained on the forms.'
    )
    cand_fax = fields.CharField(
        max_length=20,
        db_column='CAND_FAX',
        blank=True,
        help_text='Candidate/officeholder fax. This field \
is not contained on the forms.'
    )
    cand_id = fields.CharField(
        max_length=9,
        db_column='CAND_ID',
        blank=True,
        help_text='.CAL format to db tables doc says: "Not Used-AMS KDE"',
    )
    cand_namf = fields.CharField(
        max_length=45,
        db_column='CAND_NAMF',
        blank=True,
        help_text='Candidate/officeholder first name'
    )
    cand_naml = fields.CharField(
        max_length=200,
        db_column='CAND_NAML',
        blank=True,
        help_text="Candidate/officeholder's last name. Applies to forms \
460, 465, and 496."
    )
    cand_nams = fields.CharField(
        max_length=10,
        db_column='CAND_NAMS',
        blank=True,
        help_text="Candidate/officeholder's name suffix"
    )
    cand_namt = fields.CharField(
        max_length=10,
        db_column='CAND_NAMT',
        blank=True,
        help_text="Candidate/officeholder's prefix or title"
    )
    cand_phon = fields.CharField(
        max_length=20,
        db_column='CAND_PHON',
        blank=True,
        help_text='Candidate/officeholder phone'
    )
    cand_st = fields.CharField(
        max_length=4,
        db_column='CAND_ST',
        blank=True,
        help_text="Candidate/officeholder's state"
    )
    cand_zip4 = fields.CharField(
        max_length=10,
        db_column='CAND_ZIP4',
        blank=True,
        help_text="Candidate/officeholder's ZIP Code"
    )
    cmtte_id = fields.CharField(
        max_length=9,
        db_column='CMTTE_ID',
        blank=True,
        verbose_name="Committee ID",
        help_text="Committee ID (Filer_id) of recipient Committee who's \
campaign statement is attached. This field applies to the form 401."
    )
    CMTTE_TYPE_CHOICES = (
        ('C', 'Candidate or officeholder controlled committee'),
        ('P', 'Candidate or officeholder primarily formed committee'),
        ('B', 'Ballot-measure committee'),
        ('G', 'General-purpose committee'),
    )
    cmtte_type = fields.CharField(
        max_length=1,
        db_column='CMTTE_TYPE',
        blank=True,
        choices=CMTTE_TYPE_CHOICES,
        verbose_name="Committee type",
        help_text="Type of Recipient Committee. Applies to the 450/460.",
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=10),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=19),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=24),
        ]
    )
    control_yn = fields.IntegerField(
        null=True,
        db_column='CONTROL_YN',
        blank=True,
        help_text="Controlled Committee (yes/no) check box. Legal values \
are 'Y' or 'N'."
    )
    dist_no = fields.CharField(
        max_length=4,
        db_column='DIST_NO',
        blank=True,
        help_text="District number for the office being sought. Populated \
for Senate, Assembly, or Board of Equalization races."
    )
    elect_date = fields.DateField(
        null=True,
        db_column='ELECT_DATE',
        blank=True,
        help_text="Date of the General Election"
    )
    emplbus_cb = fields.CharField(
        max_length=4,
        db_column='EMPLBUS_CB',
        blank=True,
        help_text="Employer/Business Info included check-box. Legal \
values are 'X' or null. Applies to the Form 461."
    )
    employer = fields.CharField(
        max_length=200,
        db_column='EMPLOYER',
        blank=True,
        help_text="Employer. This field is most likely unused."
    )
    ENTITY_CD_CHOICES = (
        ('BMC', choices.CAMPAIGN_ENTITY_CODES['BMC']),
        ('CAO', choices.CAMPAIGN_ENTITY_CODES['CAO']),
        ('COM', choices.CAMPAIGN_ENTITY_CODES['COM']),
        ('CTL', choices.CAMPAIGN_ENTITY_CODES['CTL']),
        ('IND', choices.CAMPAIGN_ENTITY_CODES['IND']),
        ('MDI', choices.CAMPAIGN_ENTITY_CODES['MDI']),
        ('OTH', choices.CAMPAIGN_ENTITY_CODES['OTH']),
        ('PTY', choices.CAMPAIGN_ENTITY_CODES['PTY']),
        ('RCP', choices.CAMPAIGN_ENTITY_CODES['RCP']),
        ('SCC', choices.CAMPAIGN_ENTITY_CODES['SCC']),
        ('SMO', choices.CAMPAIGN_ENTITY_CODES['SMO']),
    )
    entity_cd = fields.CharField(
        max_length=4,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        help_text="The entity type of the filer. These codes vary by form type.",
        choices=ENTITY_CD_CHOICES,
        documentcloud_pages=choices.DOCS['entity_codes'] + [
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=6),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=18),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=22),
        ]
    )
    file_email = fields.CharField(
        max_length=60,
        db_column='FILE_EMAIL',
        blank=True,
        help_text="Filer's email address"
    )
    # these fields are described in the following docs:
    # https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/26.html
    # but are not included on the .tsv file
    # filer_adr1 = fields.CharField(
    #     max_length=55,
    #     db_column='FILER_ADR1',
    #     blank=True,
    #     help_text="First line of the filer's address",
    # )
    # filer_adr2 = fields.CharField(
    #     max_length=55,
    #     db_column='FILER_ADR2',
    #     blank=True,
    #     help_text="Second line of the filer's address",
    # )
    filer_city = fields.CharField(
        max_length=30,
        db_column='FILER_CITY',
        blank=True,
        help_text="Filer's city"
    )
    filer_fax = fields.CharField(
        max_length=20,
        db_column='FILER_FAX',
        blank=True,
        help_text="Filer's fax"
    )
    filer_id = fields.CharField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        max_length=15,
        blank=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    filer_namf = fields.CharField(
        max_length=45,
        db_column='FILER_NAMF',
        blank=True,
        help_text="Filer's first name, if an individual"
    )
    filer_naml = fields.CharField(
        max_length=200,
        db_column='FILER_NAML',
        help_text="The committee's or organization's name or if an \
individual the filer's last name."
    )
    filer_nams = fields.CharField(
        max_length=10,
        db_column='FILER_NAMS',
        blank=True,
        help_text="Filer's suffix, if an individual"
    )
    filer_namt = fields.CharField(
        max_length=10,
        db_column='FILER_NAMT',
        blank=True,
        help_text="Filer's title or prefix, if an individual"
    )
    filer_phon = fields.CharField(
        max_length=20,
        db_column='FILER_PHON',
        blank=True,
        help_text="Filer phone number"
    )
    filer_st = fields.CharField(
        max_length=4,
        db_column='FILER_ST',
        blank=True,
        help_text="Filer state"
    )
    filer_zip4 = fields.CharField(
        max_length=10,
        db_column='FILER_ZIP4',
        blank=True,
        help_text="Filer ZIP Code"
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
    )
    FORM_TYPE_CHOICES = (
        ('F401', get_filing_form('F401').full_title),
        ('F425', get_filing_form('F425').full_title),
        ('F450', get_filing_form('F450').full_title),
        ('F460', get_filing_form('F460').full_title),
        ('F461', get_filing_form('F461').full_title),
        ('F465', get_filing_form('F465').full_title),
        ('F496', get_filing_form('F496').full_title),
        ('F497', get_filing_form('F497').full_title),
        ('F498', get_filing_form('F498').full_title),
        ('F511', get_filing_form('F511').full_title),
        ('F900', get_filing_form('F900').full_title),
    )
    form_type = fields.CharField(
        choices=FORM_TYPE_CHOICES,
        max_length=4,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=18),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=22),
        ]
    )
    from_date = fields.DateField(
        null=True,
        db_column='FROM_DATE',
        blank=True,
        help_text="Reporting period from date"
    )
    JURIS_CD_CHOICES = get_sorted_choices(choices.JURIS_CODES) + (
        # alt cases
        ('sen', choices.JURIS_CODES['SEN']),
        ('Gov', choices.JURIS_CODES['STW']),
        # statewide office codes
        ('ATT', choices.JURIS_CODES['STW']),
        ('CON', choices.JURIS_CODES['STW']),
        ('GOV', choices.JURIS_CODES['STW']),
        ('SOS', choices.JURIS_CODES['STW']),
        ('SPM', choices.JURIS_CODES['STW']),
        # assembly member districts
        ('46', choices.JURIS_CODES['ASM']),
        ('55', choices.JURIS_CODES['ASM']),
        # county office codes
        ('BSU', choices.JURIS_CODES['CTY']),
        ('CSU', choices.JURIS_CODES['CTY']),
        ('DAT', choices.JURIS_CODES['CTY']),
        ('SHC', choices.JURIS_CODES['CTY']),
        # city office codes
        ('MAY', choices.JURIS_CODES['CIT']),
        ('CCM', choices.JURIS_CODES['CIT']),
        # other office codes
        ('APP', choices.JURIS_CODES['OTH']),
        ('BED', choices.JURIS_CODES['OTH']),
        ('SCJ', choices.JURIS_CODES['OTH']),
        # probably means 'San Diego', rows with this value are all for Arlie Ricasa's
        # Board of Education campaign
        ('SD', choices.JURIS_CODES['OTH']),
        # probably means Orange County, rows with this value are all for Lou Correa's
        # Board of Supervisor's campaign
        ('OC', choices.JURIS_CODES['CTY']),
        # One record for Joaquin Arambula's state assembly run
        ('AD', choices.JURIS_CODES['ASM']),
        # Often "State of California" but sometimes State Assembly, State Senate or other juris
        ('CA', 'Unknown'),
        ('F', 'Unknown'),
    )
    juris_cd = fields.CharField(
        max_length=3,
        choices=JURIS_CD_CHOICES,
        db_column='JURIS_CD',
        blank=True,
        help_text="Office jurisdiction code",
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=13),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=21, end_page=22),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=28, end_page=29),
        ]
    )
    juris_dscr = fields.CharField(
        max_length=40,
        db_column='JURIS_DSCR',
        blank=True,
        help_text="Office Jurisdiction description if the field JURIS_CD is \
set to city (CIT), county (CTY), local (LOC), or other \
(OTH)."
    )
    late_rptno = fields.CharField(
        max_length=30,
        db_column='LATE_RPTNO',
        blank=True,
        help_text="Identifying Report Number used to distinguish multiple \
reports filed during the same filing period. For example, \
this field allows for multiple form 497s to be filed on the \
same day."
    )
    # these fields are described in the following docs:
    # https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/27.html
    # but are not included on the .tsv file
    # mail_adr1 = fields.CharField(
    #     max_length=55,
    #     db_column='MAIL_ADR1',
    #     blank=True,
    #     help_text="First line of the filer's mailing address. Required if \
    #                different than the filer's street address.",
    # )
    # mail_adr2 = fields.CharField(
    #     max_length=55,
    #     db_column='MAIL_ADR2',
    #     blank=True,
    #     help_text="Second line of the filer's mailing address.",
    # )
    mail_city = fields.CharField(
        max_length=30,
        db_column='MAIL_CITY',
        blank=True,
        help_text="Filer mailing address city"
    )
    mail_st = fields.CharField(
        max_length=4,
        db_column='MAIL_ST',
        blank=True,
        help_text="Filer mailing address state"
    )
    mail_zip4 = fields.CharField(
        max_length=10,
        db_column='MAIL_ZIP4',
        blank=True,
        help_text="Filer mailing address ZIP Code"
    )
    occupation = fields.CharField(
        max_length=60,
        db_column='OCCUPATION',
        blank=True,
        help_text="Occupation. This field is most likely unused."
    )
    OFF_S_H_CD_CHOICES = (
        ('S', choices.OFF_S_H_CODES['S']),
        ('H', choices.OFF_S_H_CODES['H']),
        ('s', choices.OFF_S_H_CODES['S']),
        ('h', choices.OFF_S_H_CODES['H']),
        # The codes below appear in the database but are undocumented
        ('F', 'UNKNOWN'),
        ('O', 'UNKNOWN'),
    )
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text='Office is sought or held code',
        choices=OFF_S_H_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=21),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=28),
        ]
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office sought description if the field OFFICE_CD is set \
to other (OTH)"
    )
    OFFICE_CD_CHOICES = get_sorted_choices(choices.OFFICE_CODES) + (
        ('Gov', choices.OFFICE_CODES['GOV']),
        ('Sen', choices.OFFICE_CODES['SEN']),
        ('LOC', choices.OFFICE_CODES['CCB']),
        ('LEG', choices.OFFICE_CODES['SEN']),
        ('REP', choices.OFFICE_CODES['ASM']),
        # Rows with this value are all for Local Fire Board campaigns, with usually
        # categorize as "Other"
        ('Mem', choices.OFFICE_CODES['OTH']),
        # Looks like a mis-write by Richard Alarcon for Assembly campaign
        ('CIT', choices.OFFICE_CODES['ASM']),
        # Rows with these value could be any number of offices
        ('PAC', 'Unknown'),
        ('F', 'Unknown'),
        # No idea on this one
        ('COM', 'Unknown'),
    )
    office_cd = fields.CharField(
        db_column='OFFICE_CD',
        max_length=3,
        blank=True,
        verbose_name="office code",
        help_text="Identifies the office being sought",
        choices=OFFICE_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=10),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=12),
        ]
    )
    other_cb = fields.CharField(
        max_length=1,
        db_column='OTHER_CB',
        blank=True,
        help_text="Other entity interests info included check-box. Legal \
values are 'X' and null."
    )
    other_int = fields.CharField(
        max_length=90,
        db_column='OTHER_INT',
        blank=True,
        help_text="Other entity interests description"
    )
    primfrm_yn = fields.CharField(
        max_length=1,
        db_column='PRIMFRM_YN',
        blank=True,
        help_text="Primarily Formed Committee (yes/no) checkbox. Legal \
values are 'Y' or 'N'."
    )
    REC_TYPE_CHOICES = (
        ("CVR", "Cover Page"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        help_text='Record Type Value: CVR',
        documentcloud_pages=[
            DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=25),
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=6),
            DocumentCloud(id="2712033-Cal-Format-1-05-02", start_page=18),
            DocumentCloud(id="2712034-Cal-Format-201", start_page=22),
        ]
    )
    report_num = fields.CharField(
        max_length=3,
        db_column='REPORT_NUM',
        help_text="Amendment number, as reported by the filer \
Report Number 000 represents an original filing. 001-999 are amendments."
    )
    REPORTNAME_CHOICES = (
        ('450', get_filing_form('F450').full_title),
        ('460', get_filing_form('F460').full_title),
        ('461', get_filing_form('F461').full_title),
    )
    reportname = fields.CharField(
        max_length=3,
        db_column='REPORTNAME',
        blank=True,
        choices=REPORTNAME_CHOICES,
        help_text="Attached campaign disclosure statement type. Legal \
values are 450, 460, and 461.",
        documentcloud_pages=(
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=15),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=20),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=19),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=26),
        )
    )
    rpt_att_cb = fields.CharField(
        max_length=4,
        db_column='RPT_ATT_CB',
        blank=True,
        help_text="Committee Report Attached check-box. Legal values \
are 'X' or null. This field applies to the form 401."
    )
    rpt_date = fields.DateField(
        db_column='RPT_DATE',
        null=True,
        help_text="Date this report was filed, according to the filer"
    )
    rptfromdt = fields.DateField(
        null=True,
        db_column='RPTFROMDT',
        blank=True,
        help_text="Attached campaign disclosure statement - Period from \
date."
    )
    rptthrudt = fields.DateField(
        null=True,
        db_column='RPTTHRUDT',
        blank=True,
        help_text="Attached campaign disclosure statement - Period \
through date."
    )
    selfemp_cb = fields.CharField(
        max_length=1,
        db_column='SELFEMP_CB',
        blank=True,
        help_text='Self employed check-box. CAL format to db tables doc says: \
"Not Used-AMS KDE"',
    )
    sponsor_yn = fields.IntegerField(
        null=True,
        db_column='SPONSOR_YN',
        blank=True,
        help_text="Sponsored Committee (yes/no) checkbox. Legal values \
are 'Y' or 'N'."
    )
    STMT_TYPE_CHOICES = (
        ('PE', choices.STMT_TYPES['PE']),
        ('QT', choices.STMT_TYPES['QT']),
        ('SA', choices.STMT_TYPES['SA']),
        ('SE', choices.STMT_TYPES['SE']),
        ('SY', choices.STMT_TYPES['SY']),
        ('S1', choices.STMT_TYPES['S1']),
        ('S2', choices.STMT_TYPES['S2']),
        ('TS', choices.STMT_TYPES['TS']),
        ('pe', choices.STMT_TYPES['PE']),
        ('qt', choices.STMT_TYPES['QT']),
        ('sa', choices.STMT_TYPES['SA']),
        ('se', choices.STMT_TYPES['SE']),
        ('sy', choices.STMT_TYPES['SY']),
        ('ts', choices.STMT_TYPES['TS']),
        ("**", "Amendment"),
        ("1", "Unknown"),
        ("2", "Unknown"),
        ("CA", "Unknown"),
        ("MD", "Unknown"),
        ("NA", "Unknown"),
        ("PR", "Unknown"),
        ("QS", "Unknown"),
        ("S", "Unknown"),
        ("x", "Unknown"),
        ("YE", "Unknown"),
    )
    stmt_type = fields.CharField(
        max_length=2,
        db_column='STMT_TYPE',
        blank=True,
        help_text='Type of statement',
        choices=STMT_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=7),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=18),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=23),
        ]
    )
    SUP_OPP_CD_CHOICES = (
        ('S', choices.SUP_OPP_CODES['S']),
        ('O', choices.SUP_OPP_CODES['O']),
        ('s', choices.SUP_OPP_CODES['S']),
        ('o', choices.SUP_OPP_CODES['O']),
    )
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text="Support or opposition code",
        choices=SUP_OPP_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=28),
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=14),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=21),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=28),
        ]
    )
    thru_date = fields.DateField(
        null=True,
        db_column='THRU_DATE',
        blank=True,
        help_text='Reporting period through date'
    )
    # these fields are described in the following docs:
    # https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/28.html
    # but are not included on the .tsv file
    # tres_adr1 = fields.CharField(
    #     max_length=55,
    #     db_column='TRES_ADR1',
    #     blank=True,
    #     help_text="First line of the treasurer or responsible officer's street address."
    # )
    # tres_adr2 = fields.CharField(
    #     max_length=55,
    #     db_column='TRES_ADR2',
    #     blank=True,
    #     help_text="Second line of the treasurer or responsible officer's street address."
    # )
    tres_city = fields.CharField(
        max_length=30,
        db_column='TRES_CITY',
        blank=True,
        help_text="City portion of the treasurer or responsible \
officer's street address."
    )
    tres_email = fields.CharField(
        max_length=60,
        db_column='TRES_EMAIL',
        blank=True,
        help_text="Treasurer or responsible officer's email"
    )
    tres_fax = fields.CharField(
        max_length=20,
        db_column='TRES_FAX',
        blank=True,
        help_text="Treasurer or responsible officer's fax number"
    )
    tres_namf = fields.CharField(
        max_length=45,
        db_column='TRES_NAMF',
        blank=True,
        help_text="Treasurer or responsible officer's first name"
    )
    tres_naml = fields.CharField(
        max_length=200,
        db_column='TRES_NAML',
        blank=True,
        help_text="Treasurer or responsible officer's last name"
    )
    tres_nams = fields.CharField(
        max_length=10,
        db_column='TRES_NAMS',
        blank=True,
        help_text="Treasurer or responsible officer's suffix"
    )
    tres_namt = fields.CharField(
        max_length=10,
        db_column='TRES_NAMT',
        blank=True,
        help_text="Treasurer or responsible officer's prefix or title"
    )
    tres_phon = fields.CharField(
        max_length=20,
        db_column='TRES_PHON',
        blank=True,
        help_text="Treasurer or responsible officer's phone number"
    )
    tres_st = fields.CharField(
        max_length=2,
        db_column='TRES_ST',
        blank=True,
        help_text="Treasurer or responsible officer's state"
    )
    tres_zip4 = fields.CharField(
        max_length=10,
        db_column='TRES_ZIP4',
        blank=True,
        help_text="Treasurer or responsible officer's ZIP Code"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'CVR_CAMPAIGN_DISCLOSURE_CD'
        ordering = ("-rpt_date",)

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class Cvr2CampaignDisclosureCd(CalAccessBaseModel):
    """
    Extra information from campaign-disclosure forms.
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
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=41, end_page=43),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=32, end_page=35),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=23, end_page=24),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=31, end_page=34),
    ]
    FILING_FORMS = [
        get_filing_form('F425').get_section('P1'),
        get_filing_form('F450').get_section('P3'),
        get_filing_form('F460').get_section('CVR2'),
        get_filing_form('F465').get_section('P5'),
    ]
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    bal_juris = fields.CharField(
        max_length=40,
        db_column='BAL_JURIS',
        blank=True,
        help_text="Ballot measure jurisdiction"
    )
    bal_name = fields.CharField(
        max_length=200,
        db_column='BAL_NAME',
        blank=True,
        help_text="Ballot measure name"
    )
    bal_num = fields.CharField(
        max_length=7,
        db_column='BAL_NUM',
        blank=True,
        help_text="Ballot measure number or letter"
    )
    cmte_id = fields.CharField(
        max_length=9,
        db_column='CMTE_ID',
        blank=True,
        help_text="Committee identification number, when the entity \
is a committee"
    )
    control_yn = fields.IntegerField(
        null=True,
        db_column='CONTROL_YN',
        blank=True,
        help_text='Controlled Committee (yes/no) checkbox. Legal values \
are "Y" or "N".'
    )
    dist_no = fields.CharField(
        max_length=3,
        db_column='DIST_NO',
        blank=True,
        help_text="District number for the office being sought. Populated \
for Senate, Assembly, or Board of Equalization races."
    )
    ENTITY_CD_CHOICES = (
        ('ATR', choices.CAMPAIGN_ENTITY_CODES['ATR']),
        ('BNM', choices.CAMPAIGN_ENTITY_CODES['BNM']),
        ('CAO', choices.CAMPAIGN_ENTITY_CODES['CAO']),
        ('COM', choices.CAMPAIGN_ENTITY_CODES['COM']),
        ('CTL', choices.CAMPAIGN_ENTITY_CODES['CTL']),
        ('OFF', choices.CAMPAIGN_ENTITY_CODES['OFF']),
        ('POF', choices.CAMPAIGN_ENTITY_CODES['POF']),
        ('PRO', choices.CAMPAIGN_ENTITY_CODES['PRO']),
        ('RCP', choices.CAMPAIGN_ENTITY_CODES['RCP']),
        # Values observed in this field but not found in docs
        ('FIL', 'Unknown'),
        ('PEX', 'Unknown'),
        ('RDP', 'Unknown'),  # Misspelling of RCP?
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CD_CHOICES,
        help_text="Entity code used to identify the type of entity being described \
with in the record.",
        documentcloud_pages=choices.DOCS['entity_codes'] + [
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=32),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=23, end_page=24),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=32),
        ]
    )
    # enty_adr1 = fields.CharField(
    #     max_length=55, db_column='ENTY_ADR1', blank=True
    # )
    # enty_adr2 = fields.CharField(
    #     max_length=55, db_column='ENTY_ADR2', blank=True
    # )
    enty_city = fields.CharField(
        max_length=30,
        db_column='ENTY_CITY',
        blank=True,
        help_text="Entity city"
    )
    enty_email = fields.CharField(
        max_length=60,
        db_column='ENTY_EMAIL',
        blank=True,
        help_text="Entity email address"
    )
    enty_fax = fields.CharField(
        max_length=20,
        db_column='ENTY_FAX',
        blank=True,
        help_text="Entity fax number"
    )
    enty_namf = fields.CharField(
        max_length=45,
        db_column='ENTY_NAMF',
        blank=True,
        help_text="Entity first name, if an individual"
    )
    enty_naml = fields.CharField(
        max_length=200,
        db_column='ENTY_NAML',
        blank=True,
        help_text="Entity name, or last name if an individual"
    )
    enty_nams = fields.CharField(
        max_length=10,
        db_column='ENTY_NAMS',
        blank=True,
        help_text="Entity suffix, if an individual"
    )
    enty_namt = fields.CharField(
        max_length=10,
        db_column='ENTY_NAMT',
        blank=True,
        help_text="Entity prefix or title, if an individual"
    )
    enty_phon = fields.CharField(
        max_length=20,
        db_column='ENTY_PHON',
        blank=True,
        help_text="Entity phone number"
    )
    enty_st = fields.CharField(
        max_length=2,
        db_column='ENTY_ST',
        blank=True,
        help_text="Entity state"
    )
    enty_zip4 = fields.CharField(
        max_length=10,
        db_column='ENTY_ZIP4',
        blank=True,
        help_text="Entity ZIP code"
    )
    F460_PART_CHOICES = (
        ('3', 'Part 3: Committee Information'),
        # Part 4 became Part 5 somewhere between 1999 and 2001
        # Seems like the use of the old and new versions of the forms overlapped slightly
        # https://gist.github.com/gordonje/fb858960bc249cf9a2a581212eccbb8b
        ('4a', 'Part 4a: Officeholder or Candidate Controlled Committee'),
        ('4A', 'Part 4a: Officeholder or Candidate Controlled Committee'),
        ('4b', 'Part 4b: Related Committees Not Included in this Statement'),
        ('4B', 'Part 4b: Related Committees Not Included in this Statement'),
        ('5a', 'Part 5a: Officeholder or Candidate Controlled Committee'),
        ('5A', 'Part 5a: Officeholder or Candidate Controlled Committee'),
        ('5b', 'Part 5b: Related Committees Not Included in this Statement'),
        ('5B', 'Part 5b: Related Committees Not Included in this Statement'),
        # On the 1999 Form...
        ('6', 'Part 6: Primarily Formed Committee'),
        # On 2001 form...
        ('6a', 'Part 6a: Name of Ballot Measure'),
        ('6A', 'Part 6a: Name of Ballot Measure'),
        ('6b', 'Part 6b: Name of Officeholder, Candidate, or Proponent'),
        ('6B', 'Part 6b: Name of Officeholder, Candidate, or Proponent'),
        ('7', 'Part 7: Primarily Formed Committee'),
    )
    f460_part = fields.CharField(
        max_length=2,
        db_column='F460_PART',
        blank=True,
        choices=F460_PART_CHOICES,
        help_text="Part of 460 cover page coded on ths cvr2 record",
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=32),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=24),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=32),
        ]
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
    )
    FORM_TYPE_CHOICES = tuple([(f.form.id, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        choices=FORM_TYPE_CHOICES,
        max_length=4,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=23),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=31),
        ]
    )
    JURIS_CD_CHOICES = get_sorted_choices(choices.JURIS_CODES) + (
        ('sen', choices.JURIS_CODES['SEN']),
        # looks like the Arlie Ricasa Campaign was consistently making this mis-write
        ('SD', choices.JURIS_CODES['ASM']),
        # ditto for Kevin de Leon Believing in A Better California
        ('se', choices.JURIS_CODES['SEN']),
        # ditto for Friends of Bob Dutton
        ('F', choices.JURIS_CODES['ASM']),
        # ditto for Friends To Re-Elect Tonia For 7th District
        ('LBC', choices.JURIS_CODES['CIT']),
        # Several different filers have made this mis-write
        # Usually they mean Statewide, but sometimes they mean State Assembly or City
        ('CA', choices.JURIS_CODES['STW']),
    )
    juris_cd = fields.CharField(
        max_length=3,
        db_column='JURIS_CD',
        blank=True,
        help_text="Office jurisdiction code",
        choices=JURIS_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=24),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=33),
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=35),
        ]
    )
    juris_dscr = fields.CharField(
        max_length=40,
        db_column='JURIS_DSCR',
        blank=True,
        help_text="Office jurisdiction description"
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    # mail_adr1 = fields.CharField(
    #     max_length=55, db_column='MAIL_ADR1', blank=True
    # )
    # mail_adr2 = fields.CharField(
    #     max_length=55, db_column='MAIL_ADR2', blank=True
    # )
    mail_city = fields.CharField(
        max_length=30,
        db_column='MAIL_CITY',
        blank=True,
        help_text="Filer's mailing city"
    )
    mail_st = fields.CharField(
        max_length=2,
        db_column='MAIL_ST',
        blank=True,
        help_text="Filer's mailing state"
    )
    mail_zip4 = fields.CharField(
        max_length=10,
        db_column='MAIL_ZIP4',
        blank=True,
        help_text="Filer's mailing ZIP Code"
    )
    OFF_S_H_CD_CHOICES = (
        ('S', choices.OFF_S_H_CODES['S']),
        ('H', choices.OFF_S_H_CODES['H']),
        ('s', choices.OFF_S_H_CODES['S']),
        # Bob Dutton meant 'Sought'
        ("F", choices.OFF_S_H_CODES['S']),
        # This one actually says 'Held'. Maybe a mis-read?
        ("T", choices.OFF_S_H_CODES['H']),
    )
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text='Office is sought or held code',
        choices=OFF_S_H_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=35),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=24),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=34),
        ]
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office sought description"
    )
    OFFICE_CD_CHOICES = get_sorted_choices(choices.OFFICE_CODES) + (
        # looks like the Richard Alarcon for Assembly made this mis-write
        ('CIT', choices.OFFICE_CODES['ASM']),
        # ditto for Isadore Hall for Assembly
        ('CTL', choices.OFFICE_CODES['ASM']),
        # ditto for Friends of Bob Dutton
        ('F', choices.OFFICE_CODES['ASM']),
        # ditto for Henry Perea
        ('ST', choices.OFFICE_CODES['ASM']),
        # This one is all over the board
        ('PAC', 'Unknown'),
    )
    office_cd = fields.CharField(
        db_column='OFFICE_CD',
        max_length=3,
        blank=True,
        verbose_name="office code",
        help_text="Identifies the office being sought",
        choices=OFFICE_CD_CHOICES,
        documentcloud_pages=choices.DOCS['office_codes'],
    )
    REC_TYPE_CHOICES = (
        ("CVR2", "Cover, Page 2"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        help_text="Record Type Value: CVR2",
        documentcloud_pages=[
            DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=41),
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=32),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=23),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=31),
        ]
    )
    SUP_OPP_CD_CHOICES = (
        ('S', choices.SUP_OPP_CODES['S']),
        ('O', choices.SUP_OPP_CODES['O']),
        ('s', choices.SUP_OPP_CODES['S']),
        ('o', choices.SUP_OPP_CODES['O']),
    )
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text="Support or opposition code",
        choices=SUP_OPP_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=41),
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=35),
        ]
    )
    title = fields.CharField(
        max_length=90,
        db_column='TITLE',
        blank=True,
        help_text="Official title of filing officer. Applies to the form 465."
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )
    tres_namf = fields.CharField(
        max_length=45,
        db_column='TRES_NAMF',
        blank=True,
        help_text="Treasurer or responsible officer's first name"
    )
    tres_naml = fields.CharField(
        max_length=200,
        db_column='TRES_NAML',
        blank=True,
        help_text="Treasurer or responsible officer's last name"
    )
    tres_nams = fields.CharField(
        max_length=10,
        db_column='TRES_NAMS',
        blank=True,
        help_text="Treasurer or responsible officer's suffix"
    )
    tres_namt = fields.CharField(
        max_length=10,
        db_column='TRES_NAMT',
        blank=True,
        help_text="Treasurer or responsible officer's prefix or title"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'CVR2_CAMPAIGN_DISCLOSURE_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class Cvr3VerificationInfoCd(CalAccessBaseModel):
    """
    Verification information from campaign-disclosure forms.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=46, end_page=47),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=41, end_page=42),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=25),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=50),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=34),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=64),
    ]
    FILING_FORMS = [
        get_filing_form('F400').get_section('P5'),
        get_filing_form('F401').get_section('CVR'),
        get_filing_form('F402').get_section('VER'),
        get_filing_form('F410').get_section('P3'),
        get_filing_form('F425').get_section('P3'),
        get_filing_form('F450').get_section('P4'),
        get_filing_form('F460').get_section('CVR'),
        get_filing_form('F461').get_section('P4'),
        get_filing_form('F465').get_section('P6'),
        get_filing_form('F511'),
        get_filing_form('F900'),
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
        ("CVR3", "Cover Page 3, Verification Information"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        help_text="Record Type Value: CVR3",
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=25),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=50),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=34),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=64),
        ]
    )
    FORM_TYPE_CHOICES = (
        ('F400', get_filing_form('F400').get_section('P5').full_title),
        ('F401', get_filing_form('F401').get_section('CVR').full_title),
        ('F402', get_filing_form('F402').get_section('VER').full_title),
        ('F410', get_filing_form('F410').get_section('P3').full_title),
        ('F425', get_filing_form('F425').get_section('P3').full_title),
        ('F450', get_filing_form('F450').get_section('P4').full_title),
        ('F460', get_filing_form('F460').get_section('CVR').full_title),
        ('F461', get_filing_form('F461').get_section('P4').full_title),
        ('F465', get_filing_form('F465').get_section('P6').full_title),
        ('F511', get_filing_form('F511').full_title),
        ('F900', get_filing_form('F900').full_title),
    )
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=4,
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=50),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=64),
        ]
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )
    ENTITY_CD_CHOICES = (
        # Codes explicitly allowed for this field, according to documentation
        ('ATR', choices.CAMPAIGN_ENTITY_CODES['ATR']),
        ('CAO', choices.CAMPAIGN_ENTITY_CODES['CAO']),
        ('TRE', choices.CAMPAIGN_ENTITY_CODES['TRE']),
        ('OFF', choices.CAMPAIGN_ENTITY_CODES['OFF']),
        ('PRO', choices.CAMPAIGN_ENTITY_CODES['PRO']),
        ('SPO', choices.CAMPAIGN_ENTITY_CODES['SPO']),
        # Lower case versions of valid codes
        ('atr', choices.CAMPAIGN_ENTITY_CODES['TRE']),
        ('tre', choices.CAMPAIGN_ENTITY_CODES['ATR']),
        ('cao', choices.CAMPAIGN_ENTITY_CODES['CAO']),
        # Other known codes observed in this field
        ('MDI', choices.CAMPAIGN_ENTITY_CODES['MDI']),
        ('POF', choices.CAMPAIGN_ENTITY_CODES['POF']),
        ('RCP', choices.CAMPAIGN_ENTITY_CODES['RCP']),
        # Misspelling of 'CAO', 'Candidate/officeholder'
        ('COA', choices.CAMPAIGN_ENTITY_CODES['CAO']),
        # Other unknown values observed
        ('0', 'Unknown'),
        ('BBB', 'Unknown'),
        ('CON', 'Unknown'),
        ('MAI', 'Unknown'),
    )
    entity_cd = fields.CharField(
        db_column='ENTITY_CD',
        max_length=3,
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CD_CHOICES,
        help_text='Entity Code',  # describing verifier?
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=9),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=25),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=11),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=34),
        ]
    )
    sig_date = fields.DateField(
        verbose_name='signed date',
        db_column='SIG_DATE',
        blank=True,
        null=True,
        help_text='date when signed',
    )
    sig_loc = fields.CharField(
        verbose_name='signed location',
        db_column='SIG_LOC',
        max_length=39,
        blank=True,
        help_text='city and state where signed',
    )
    sig_naml = fields.CharField(
        verbose_name='last name',
        db_column='SIG_NAML',
        max_length=56,
        blank=True,
        help_text='last name of the signer',
    )
    sig_namf = fields.CharField(
        verbose_name='first name',
        db_column='SIG_NAMF',
        max_length=45,
        blank=True,
        help_text='first name of the signer',
    )
    sig_namt = fields.CharField(
        verbose_name='title',
        db_column='SIG_NAMT',
        max_length=10,
        blank=True,
        help_text='title of the signer',
    )
    sig_nams = fields.CharField(
        verbose_name='suffix',
        db_column='SIG_NAMS',
        max_length=8,
        blank=True,
        help_text='suffix of the signer',
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'CVR3_VERIFICATION_INFO_CD'
        ordering = ("-sig_date",)

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class DebtCd(CalAccessBaseModel):
    """
    Itemized campaign debts.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=47, end_page=49),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=49, end_page=48),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=33, end_page=34),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=45, end_page=46),
    ]
    FILING_FORMS = [
        get_filing_form('F460').get_section('F'),
    ]
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    amt_incur = fields.DecimalField(
        decimal_places=2,
        max_digits=14,
        db_column='AMT_INCUR',
        help_text='Amount incurred this period',
    )
    amt_paid = fields.DecimalField(
        decimal_places=2,
        max_digits=14,
        db_column='AMT_PAID',
        help_text='Amount paid this period.'
    )
    bakref_tid = fields.CharField(
        max_length=20,
        db_column='BAKREF_TID',
        blank=True,
        help_text='Back reference to a transaction identifier \
of a parent record.'
    )
    beg_bal = fields.DecimalField(
        decimal_places=2,
        max_digits=14,
        db_column='BEG_BAL',
        help_text='Outstanding balance at beginning of period',
    )
    cmte_id = fields.CharField(
        max_length=9,
        db_column='CMTE_ID',
        blank=True,
        help_text='Committee identification number',
    )
    end_bal = fields.DecimalField(
        decimal_places=2,
        max_digits=14,
        db_column='END_BAL',
        help_text='Outstanding balance at close of this period',
    )
    ENTITY_CD_CHOICES = (
        ('BNM', choices.CAMPAIGN_ENTITY_CODES['BNM']),
        ('COM', choices.CAMPAIGN_ENTITY_CODES['COM']),
        ('IND', choices.CAMPAIGN_ENTITY_CODES['IND']),
        ('OTH', choices.CAMPAIGN_ENTITY_CODES['OTH']),
        ('PTY', choices.CAMPAIGN_ENTITY_CODES['PTY']),
        ('RCP', choices.CAMPAIGN_ENTITY_CODES['RCP']),
        ('SCC', choices.CAMPAIGN_ENTITY_CODES['SCC']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CD_CHOICES,
        help_text='Entity code describing the payee',
        documentcloud_pages=choices.DOCS['entity_codes'] + [
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=33),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=45),
        ]
    )
    EXPN_CODE_CHOICES = get_sorted_choices(choices.EXPENSE_CODES) + (
        # alt cases of valid codes
        ('Fnd', choices.EXPENSE_CODES['FND']),
        ('ofc', choices.EXPENSE_CODES['OFC']),
        # printed this way on the pdfs, but probably meant consultant code
        ("'CN", choices.EXPENSE_CODES['CNS']),
        # Other codes observed in the table that are not documented by the state
        ("*", "Unknown"),
        ("AIR", "Unknown"),
        ("BUS", "Unknown"),
        ("C", "Unknown"),
        ("CAM", "Unknown"),
        ("CC", "Unknown"),
        ("COM", "Unknown"),
        ("CON", "Unknown"),
        ("CSN", "Unknown"),
        ("DEP", "Unknown"),
        ("EVE", "Unknown"),
        ("F", "Unknown"),
        ("FED", "Unknown"),
        ("fns", "Unknown"),
        ("G", "Unknown"),
        ("GGG", "Unknown"),
        ("HOT", "Unknown"),
        ("L", "Unknown"),
        ("LDF", "Unknown"),
        ("MEE", "Unknown"),
        ("N", "Unknown"),
        ("O", "Unknown"),
        ("OTH", "Unknown"),  # Other?
        ("P", "Unknown"),
        ("PEN", "Unknown"),
        ("S", "Unknown"),
        ("SPE", "Unknown"),
        ("STA", "Unknown"),
        ("T", "Unknown"),
        ("TAX", "Unknown"),
        ("TRA", "Unknown"),
        ("V", "Unknown"),
        ("X", "Unknown"),
    )
    expn_code = fields.CharField(
        max_length=3,
        db_column='EXPN_CODE',
        blank=True,
        verbose_name='expense code',
        help_text="Expense Code",
        choices=EXPN_CODE_CHOICES,
        documentcloud_pages=choices.DOCS['expense_codes']
    )
    expn_dscr = fields.CharField(
        max_length=400,
        db_column='EXPN_DSCR',
        blank=True,
        verbose_name="expense description",
        help_text='Purpose of expense and/or description/explanation',
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number of the parent filing",
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=1,
        db_column='FORM_TYPE',
        choices=FORM_TYPE_CHOICES,
        help_text='Schedule Name/ID: (F - Sched F / Accrued Expenses)',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=33),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=45),
        ]
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Record line item number",
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
        help_text='Reference to text contained in a TEXT record.'
    )
    # payee_adr1 = fields.CharField(
    #     max_length=55, db_column='PAYEE_ADR1', blank=True
    # )
    # payee_adr2 = fields.CharField(
    #     max_length=55, db_column='PAYEE_ADR2', blank=True
    # )
    payee_city = fields.CharField(
        max_length=30,
        db_column='PAYEE_CITY',
        blank=True,
        help_text='First line of the payee\'s street address',
    )
    payee_namf = fields.CharField(
        max_length=45,
        db_column='PAYEE_NAMF',
        blank=True,
        help_text='Payee\'s first name if the payee is an individual',
    )
    payee_naml = fields.CharField(
        max_length=200,
        db_column='PAYEE_NAML',
        help_text="Payee's business name or last name if the payee is an \
individual."
    )
    payee_nams = fields.CharField(
        max_length=10,
        db_column='PAYEE_NAMS',
        blank=True,
        help_text='Payee\'s name suffix if the payee is an individual',
    )
    payee_namt = fields.CharField(
        max_length=100,
        db_column='PAYEE_NAMT',
        blank=True,
        help_text='Payee\'s prefix or title if the payee is an individual',
    )
    payee_st = fields.CharField(
        max_length=2,
        db_column='PAYEE_ST',
        blank=True,
        help_text='Payee\'s state',
    )
    payee_zip4 = fields.CharField(
        max_length=10,
        db_column='PAYEE_ZIP4',
        blank=True,
        help_text='Payee\'s ZIP Code',
    )
    REC_TYPE_CHOICES = (
        ("DEBT", "DEBT"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        help_text='Record type value: DEBT',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=33, end_page=34),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=45, end_page=46),
        ]
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Transaction identifier - permanent value unique to \
this item',
    )
    # tres_adr1 = fields.CharField(
    #     max_length=55, db_column='TRES_ADR1', blank=True
    # )
    # tres_adr2 = fields.CharField(
    #     max_length=55, db_column='TRES_ADR2', blank=True
    # )
    tres_city = fields.CharField(
        max_length=30,
        db_column='TRES_CITY',
        blank=True,
        help_text='City portion of the treasurer or responsible \
officer\'s street address',
    )
    tres_namf = fields.CharField(
        max_length=45,
        db_column='TRES_NAMF',
        blank=True,
        help_text='Treasurer or responsible officer\'s first name'
    )
    tres_naml = fields.CharField(
        max_length=200,
        db_column='TRES_NAML',
        blank=True,
        help_text='Treasurer or responsible officer\'s last name'
    )
    tres_nams = fields.CharField(
        max_length=10,
        db_column='TRES_NAMS',
        blank=True,
        help_text='Treasurer or responsible officer\'s suffix',
    )
    tres_namt = fields.CharField(
        max_length=100,
        db_column='TRES_NAMT',
        blank=True,
        help_text='Treasurer or responsible officer\'s prefix or title',
    )
    tres_st = fields.CharField(
        max_length=2,
        db_column='TRES_ST',
        blank=True,
        help_text='State portion of the treasurer or responsible \
officer\'s address',
    )
    tres_zip4 = fields.CharField(
        max_length=10,
        db_column='TRES_ZIP4',
        blank=True,
        help_text='ZIP Code portion of the treasurer or responsible \
officer\'s address',
    )
    xref_match = fields.CharField(
        max_length=1,
        db_column='XREF_MATCH',
        blank=True,
        help_text='Related item on other schedule has same \
transaction identifier. /"X/" indicates this condition is true'
    )
    xref_schnm = fields.CharField(
        max_length=2, db_column='XREF_SCHNM', blank=True,
        help_text='Related record is included on Schedule C.'
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'DEBT_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class ExpnCd(CalAccessBaseModel):
    """
    Itemized campaign expenditures.
    """
    UNIQUE_KEY = (
        'FILING_ID',
        'AMEND_ID',
        'LINE_ITEM',
        'REC_TYPE',
        'FORM_TYPE'
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=8),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=53, end_page=56),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=45, end_page=48),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=31, end_page=32),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=42, end_page=44),
    ]
    FILING_FORMS = [
        get_filing_form('F450').get_section('P5'),
        get_filing_form('F460').get_section('D'),
        get_filing_form('F460').get_section('E'),
        get_filing_form('F460').get_section('G'),
        get_filing_form('F461').get_section('P5'),
        get_filing_form('F465').get_section('P3'),
        get_filing_form('F900'),
    ]
    agent_namf = fields.CharField(
        max_length=45,
        db_column='AGENT_NAMF',
        blank=True,
        help_text="Agent of Ind. Contractor's First name"
    )
    agent_naml = fields.CharField(
        max_length=200,
        db_column='AGENT_NAML',
        blank=True,
        help_text="Agent of Ind. Contractor's Last name (Sched G)"
    )
    agent_nams = fields.CharField(
        max_length=10,
        db_column='AGENT_NAMS',
        blank=True,
        help_text="Agent of Ind. Contractor's Suffix"
    )
    agent_namt = fields.CharField(
        max_length=10,
        db_column='AGENT_NAMT',
        blank=True,
        help_text="Agent of Ind. Contractor's Prefix or Title"
    )
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    amount = fields.DecimalField(
        decimal_places=2,
        max_digits=14,
        db_column='AMOUNT',
        help_text="Amount of Payment"
    )
    bakref_tid = fields.CharField(
        verbose_name='back reference transaction id',
        max_length=20,
        db_column='BAKREF_TID',
        blank=True,
        help_text="Back Reference to a Tran_ID of a 'parent' record"
    )
    bal_juris = fields.CharField(
        verbose_name='ballot measure jurisdiction',
        max_length=40,
        db_column='BAL_JURIS',
        blank=True,
        help_text="Ballot measure's jurisdiction"
    )
    bal_name = fields.CharField(
        verbose_name='ballot measure name',
        max_length=200,
        db_column='BAL_NAME',
        blank=True,
        help_text="Ballot Measure Name"
    )
    bal_num = fields.CharField(
        verbose_name='ballot measure number',
        max_length=7,
        db_column='BAL_NUM',
        blank=True,
        help_text="Ballot Number or Letter"
    )
    cand_namf = fields.CharField(
        max_length=45,
        db_column='CAND_NAMF',
        blank=True,
        help_text="Candidate's First name"
    )
    cand_naml = fields.CharField(
        max_length=200,
        db_column='CAND_NAML',
        blank=True,
        help_text="Candidate's Last name"
    )
    cand_nams = fields.CharField(
        max_length=10,
        db_column='CAND_NAMS',
        blank=True,
        help_text="Candidate's Suffix"
    )
    cand_namt = fields.CharField(
        max_length=10,
        db_column='CAND_NAMT',
        blank=True,
        help_text="Candidate's Prefix or Title"
    )
    cmte_id = fields.CharField(
        max_length=9,
        db_column='CMTE_ID',
        blank=True,
        help_text="Committee ID (If [COM|RCP] & no ID#, Treas info Req.)"
    )
    cum_oth = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='CUM_OTH',
        blank=True,
        help_text="Cumulative / 'Other' (No Cumulative on Sched E & G)"
    )
    cum_ytd = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='CUM_YTD',
        blank=True,
        help_text="Cumulative / Year-to-date amount \
        (No Cumulative on Sched E & G)"
    )
    dist_no = fields.CharField(
        max_length=3,
        db_column='DIST_NO',
        blank=True,
        help_text="Office District Number (Req. if Juris_Cd=[SEN|ASM|BOE]"
    )
    ENTITY_CD_CHOICES = (
        # Codes explicitly allowed for this field, according to documentation
        ('COM', choices.CAMPAIGN_ENTITY_CODES['COM']),
        ('IND', choices.CAMPAIGN_ENTITY_CODES['IND']),
        ('RCP', choices.CAMPAIGN_ENTITY_CODES['RCP']),
        ('OTH', choices.CAMPAIGN_ENTITY_CODES['OTH']),
        ('PTY', choices.CAMPAIGN_ENTITY_CODES['PTY']),
        ('SCC', choices.CAMPAIGN_ENTITY_CODES['SCC']),
        # Other known codes observed in this field
        ('BNM', choices.CAMPAIGN_ENTITY_CODES['BNM']),
        ('CAO', choices.CAMPAIGN_ENTITY_CODES['CAO']),
        ('MBR', choices.LOBBYING_ENTITY_CODES['MBR']),
        ('OFF', choices.CAMPAIGN_ENTITY_CODES['OFF']),
        # Unknown codes observed in this field
        ('0', 'Unknown'),
        ('PTH', 'Unknown'),
        ('RFD', 'Unknown'),  # 'RFD' from EXPN_CD? Request For Development?
    )
    entity_cd = fields.CharField(
        choices=ENTITY_CD_CHOICES,
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        help_text='Entity Code describing payee',
        documentcloud_pages=choices.DOCS['entity_codes'] + [
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=31),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=42),
        ]
    )
    expn_chkno = fields.CharField(
        max_length=20,
        db_column='EXPN_CHKNO',
        blank=True,
        help_text="Check Number (Optional)"
    )
    EXPN_CODE_CHOICES = get_sorted_choices(choices.EXPENSE_CODES) + (
        ('ctb', choices.EXPENSE_CODES['CTB']),
        ('ikd', choices.EXPENSE_CODES['IKD']),
        ('Mon', choices.EXPENSE_CODES['MON']),
        ('ofc', choices.EXPENSE_CODES['OFC']),
        ('OFc', choices.EXPENSE_CODES['OFC']),
        ('Ofc', choices.EXPENSE_CODES['OFC']),
        # Codes observed in this field, but not found in docs
        ("", "Unknown"),
        ("*", "Unknown"),
        ("0", "Unknown"),
        ("001", "Unknown"),
        ("011", "Unknown"),
        ("200", "Unknown"),
        ("401", "Unknown"),
        ("ADV", "Unknown"),
        ("ANN", "Unknown"),
        ("APR", "Unknown"),
        ("AUG", "Unknown"),
        ("AUT", "Unknown"),
        ("Ban", "Unknown"),
        ("BAN", "Unknown"),
        ("BOO", "Unknown"),
        ("BOX", "Unknown"),
        ("C", "Unknown"),
        ("CAT", "Unknown"),
        ("CC", "Unknown"),
        ("CHE", "Unknown"),
        ("CIV", "Unknown"),
        ("CNT", "Unknown"),
        ("CON", "Unknown"),
        ("COP", "Unknown"),
        ("CRE", "Unknown"),
        ("CSN", "Unknown"),
        ("CT", "Unknown"),
        (",CT", "Unknown"),
        (".CT", "Unknown"),
        ("CTN", "Unknown"),
        ("CVD", "Unknown"),
        ("DAT", "Unknown"),
        ("DEC", "Unknown"),
        ("Dem", "Unknown"),
        ("DIN", "Unknown"),
        ("Don", "Unknown"),
        ("DON", "Unknown"),
        ("Ear", "Unknown"),
        ("EIM", "Unknown"),
        ("EMP", "Unknown"),
        ("F", "Unknown"),
        ("FAX", "Unknown"),
        ("FDN", "Unknown"),
        ("FED", "Unknown"),
        ("FEE", "Unknown"),
        ("FIN", "Unknown"),
        ("Fun", "Unknown"),
        ("FUN", "Unknown"),
        ("G", "Unknown"),
        ("GEN", "Unknown"),
        ("GGG", "Unknown"),
        ("GOT", "Unknown"),
        ("IEs", "Unknown"),
        ("IN-", "Unknown"),
        ("Ina", "Unknown"),
        ("INK", "Unknown"),  # Misspelling of 'IKD' ('In-kind')?
        ("INS", "Unknown"),
        ("ITE", "Unknown"),
        ("JAN", "Unknown"),
        ("JUL", "Unknown"),
        ("JUN", "Unknown"),
        ("KIC", "Unknown"),
        ("L", "Unknown"),
        ("LEV", "Unknown"),
        ("Lit", "Unknown"),
        ("LN#", "Unknown"),
        ("LOG", "Unknown"),
        ("M", "Unknown"),
        ("MAI", "Unknown"),
        ("Mar", "Unknown"),
        ("MAR", "Unknown"),
        ("MAY", "Unknown"),
        ("MED", "Unknown"),
        ("MEE", "Unknown"),
        ("MGT", "Unknown"),
        ("Mis", "Unknown"),
        ("MRB", "Unknown"),
        ("NGP", "Unknown"),  # Nathaniel G. Pearlman?
        ("NON", "Unknown"),
        ("NOT", "Unknown"),
        ("NOV", "Unknown"),
        ("O", "Unknown"),
        ("OCT", "Unknown"),
        (".OF", "Unknown"),
        ("OFF", "Unknown"),  # Misspelling 'OFC' ('Office expenses')?
        ("OPE", "Unknown"),
        ("OTH", "Unknown"),  # Other?
        ("P", "Unknown"),
        ("Pac", "Unknown"),
        ("PAI", "Unknown"),
        ("PAR", "Unknown"),
        ("PAY", "Unknown"),
        ("PEN", "Unknown"),
        ("PMT", "Unknown"),
        (".PO", "Unknown"),
        ("Pos", "Unknown"),
        ("PRE", "Unknown"),
        ("PRI", "Unknown"),
        ("PRP", "Unknown"),
        ("R", "Unknown"),
        (".Re", "Unknown"),
        (".RE", "Unknown"),
        ("REF", "Unknown"),
        ("REI", "Unknown"),
        ("RFP", "Unknown"),
        ("S", "Unknown"),
        ("S-A", "Unknown"),
        ("SA", "Unknown"),
        ("Sal", "Unknown"),
        ("S C", "Unknown"),
        ("S.C", "Unknown"),
        ("SCU", "Unknown"),
        ("SEE", "Unknown"),
        ("SEN", "Unknown"),
        ("SEP", "Unknown"),
        ("S.M.", "Unknown"),
        ("SOF", "Unknown"),
        ("SWI", "Unknown"),
        ("T", "Unknown"),
        ("TAX", "Unknown"),
        ("TB", "Unknown"),
        ("TB,", "Unknown"),
        ("TIC", "Unknown"),
        ("Tor", "Unknown"),
        ("TRA", "Unknown"),
        ("TRF", "Unknown"),
        ("TRV", "Unknown"),
        ("UN", "Unknown"),
        ("UTI", "Unknown"),
        ("V", "Unknown"),
        ("VEN", "Unknown"),
        ("-VO", "Unknown"),
        ("VOI", "Unknown"),
        ("VOY", "Unknown"),
        ("WI", "Unknown"),
        ("x", "Unknown"),
        ("X", "Unknown"),
        ('S-6', 'Unknown'),
        ('S.M', 'Unknown'),
        ('S-4', 'Unknown'),
        ('SA:', 'Unknown'),
        ('100', 'Unknown'),
        ('RFN', 'Unknown'),
        ('REN', 'Unknown'),
        ('003', 'Unknown'),
        ('S-1', 'Unknown'),
        ('08', 'Unknown'),
    )
    expn_code = fields.CharField(
        max_length=3,
        db_column='EXPN_CODE',
        blank=True,
        choices=EXPN_CODE_CHOICES,
        verbose_name="expense code",
        help_text="The type of expenditure",
        documentcloud_pages=choices.DOCS['expense_codes']
    )
    expn_date = fields.DateField(
        null=True,
        db_column='EXPN_DATE',
        blank=True,
        verbose_name="expense date",
        help_text="Date of Expenditure (Note: Date not on Sched E & G)"
    )
    expn_dscr = fields.CharField(
        max_length=400,
        db_column='EXPN_DSCR',
        verbose_name="expense description",
        blank=True,
        help_text="Purpose of expense and/or description/explanation"
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        choices=FORM_TYPE_CHOICES,
        max_length=6,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=31),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=42),
        ]
    )
    g_from_e_f = fields.CharField(
        max_length=1,
        db_column='G_FROM_E_F',
        blank=True,
        help_text="Back Reference from Sched G to Sched 'E' or 'F'?"
    )
    JURIS_CD_CHOICES = get_sorted_choices(choices.JURIS_CODES) + (
        # alt casing of valid values
        ('Cit', choices.JURIS_CODES['CIT']),
        ('sen', choices.JURIS_CODES['SEN']),
        ('Sen', choices.JURIS_CODES['SEN']),
        ('stw', choices.JURIS_CODES['STW']),
        # statewide office codes
        ('APP', choices.JURIS_CODES['STW']),
        ('ASR', choices.JURIS_CODES['CTY']),
        ('ATT', choices.JURIS_CODES['STW']),
        ('GOV', choices.JURIS_CODES['STW']),
        ('LTG', choices.JURIS_CODES['STW']),
        ('SOS', choices.JURIS_CODES['STW']),
        ('SUP', choices.JURIS_CODES['STW']),
        ('TRE', choices.JURIS_CODES['STW']),
        # county office codes
        ('BSU', choices.JURIS_CODES['CTY']),
        ('CSU', choices.JURIS_CODES['CTY']),
        # city office codes
        ('ES', choices.JURIS_CODES['CIT']),
        ('SM', choices.JURIS_CODES['CIT']),
        # "other" office codes
        ('BED', choices.JURIS_CODES['OTH']),
        ('CCB', choices.JURIS_CODES['OTH']),
        ('CCM', choices.JURIS_CODES['OTH']),
        ('PDR', choices.JURIS_CODES['OTH']),
        # state senate districts
        ('12', choices.JURIS_CODES['SEN']),
        # Ballot Propositions
        ('4', choices.JURIS_CODES['STW']),
        ('8', choices.JURIS_CODES['STW']),
        ('27', choices.JURIS_CODES['STW']),
        ('93', choices.JURIS_CODES['STW']),
        ('98', choices.JURIS_CODES['STW']),
        # Community College Board, except that one time where it's City Council
        ('CLB', 'Unknown'),
        # Sometimes these are Assembly Members, sometimes State Senators,
        # sometimes Public Employees Retirement System
        ('PER', 'Unknown'),
        # Misprint
        ('Boa', choices.JURIS_CODES['BOE']),
        # Usually Assembly Member except for those two times when it's governor and attorney general
        ('Sta', 'Unknown'),
        ('STA', 'Unknown'),
        # All over the board
        ('CA', 'Unknown'),
        ('SAN', 'Unknown'),
        ('ES ', 'Unknown'),
        ('CON', 'Unknown'),
        ('LA', 'Unknown'),
        ('LBC', 'Unknown'),
        ('OR', 'Unknown'),
        ('SB', 'Unknown'),
        ('WES', 'Unknown'),
        ('BM', 'Unknown'),
        ('(Lo', 'Unknown'),
        ('(Ci', 'Unknown'),
        ('vty', 'Unknown'),
        ('OC', 'Unknown'),
        ('SM ', 'Unknown'),
        ('ASS', 'Unknown'),
        ('JR', 'Unknown'),
        ('O', 'Unknown'),
        ('ADM', 'Unknown'),
        ('SAC', 'Unknown'),
        ('US', 'Unknown'),
        ('J', 'Unknown'),
        ('LOS', 'Unknown'),
        ('IRV', 'Unknown'),
        ('CO', 'Unknown'),
        ('JRS', 'Unknown'),
        ('NEV', 'Unknown'),
        ('IB', 'Unknown'),
        ('A', 'Unknown'),
        ('Ass', 'Unknown'),
        ('SD', 'Unknown'),
        ('D', 'Unknown'),
        ('SEC', 'Unknown'),
        ('SC', 'Unknown'),
        ('RB', 'Unknown'),
        ('GEN', 'Unknown'),
        ('CC', 'Unknown'),
        ('FED', 'Unknown'),
        ('FM', 'Unknown'),
        ('R', 'Unknown'),
    )
    juris_cd = fields.CharField(
        max_length=3,
        db_column='JURIS_CD',
        blank=True,
        choices=JURIS_CD_CHOICES,
        help_text="Office Jurisdiction Code",
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=32),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=44),
        ]
    )
    juris_dscr = fields.CharField(
        max_length=40,
        db_column='JURIS_DSCR',
        blank=True,
        help_text="Office Jurisdiction Description \
        (Req. if Juris_Cd=[CIT|CTY|LOC|OTH]"
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
        help_text="Memo Amount? (Date/Amount are informational only). For Form"
                  " 460 filings, this indicates the record is a sub-item and "
                  "its amount is included in another item reported on the "
                  "filing."
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text="Reference to text contained in a TEXT record."
    )
    OFF_S_H_CD_CHOICES = get_sorted_choices(choices.OFF_S_H_CODES) + (
        ('s', choices.OFF_S_H_CODES['S']),
        ('h', choices.OFF_S_H_CODES['H']),
        # The codes below appear in the database but are undocumented
        ('A', 'UNKNOWN'),
        ('a', 'UNKNOWN'),
        ('8', 'UNKNOWN'),
        ('O', 'UNKNOWN'),
    )
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text='Office is sought or held code',
        choices=OFF_S_H_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=32),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=44),
        ]
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office Sought Description (Req. if Office_Cd=OTH)"
    )
    OFFICE_CD_CHOICES = get_sorted_choices(choices.OFFICE_CODES) + (
        # alt cases for valid codes
        ('Cou', choices.OFFICE_CODES['COU']),
        ('sen', choices.OFFICE_CODES['SEN']),
        ('AtT', choices.OFFICE_CODES['ATT']),
        ('May', choices.OFFICE_CODES['MAY']),
        ('Sen', choices.OFFICE_CODES['SEN']),
        ('asm', choices.OFFICE_CODES['ASM']),
        ('gov', choices.OFFICE_CODES['GOV']),
        ('Gov', choices.OFFICE_CODES['GOV']),
        # unknown codes
        ('LA', 'Unknown'),
        ('HOU', 'Unknown'),
        ('LAD', 'Unknown'),
        ('11A', 'Unknown'),
        ('001', 'Unknown'),
        ('BM', 'Unknown'),
        ('AS1', 'Unknown'),
        ('ASS', 'Unknown'),
        ('73', 'Unknown'),
        ('CIT', 'Unknown'),
        ('HSE', 'Unknown'),
        ('LT', 'Unknown'),
        ('CTY', 'Unknown'),
        ('STA', 'Unknown'),
        ('GO', 'Unknown'),
        ('CO', 'Unknown'),
        ('A', 'Unknown'),
        ('PAC', 'Unknown'),
        ('REP', 'Unknown'),
        ('OFF', 'Unknown'),
        ('SE', 'Unknown'),
        ('031', 'Unknown'),
        ('COM', 'Unknown'),
        ('ASB', 'Unknown'),
        ('OT', 'Unknown'),
        ('NAT', 'Unknown'),
        ('CC', 'Unknown'),
        ('SWE', 'Unknown'),
        ('FED', 'Unknown'),
        ('STE', 'Unknown'),
        ('H', 'Unknown'),
        ('DA', 'Unknown'),
        ('S', 'Unknown'),
        ('AS', 'Unknown'),
        ('OF', 'Unknown'),
        ('LEG', 'Unknown'),
        ('STW', 'Unknown'),
        ('ST', 'Unknown'),
        ('PRE', 'Unknown'),
        ('/S', 'Unknown'),
        ('U S', 'Unknown'),
        ('O', 'Unknown'),
        ('8', 'Unknown'),
        ('C:S', 'Unknown'),
    )
    office_cd = fields.CharField(
        db_column='OFFICE_CD',
        max_length=3,
        blank=True,
        verbose_name="office code",
        help_text="Identifies the office being sought",
        choices=OFFICE_CD_CHOICES,
        documentcloud_pages=choices.DOCS['office_codes']
    )
    # payee_adr1 = fields.CharField(
    #     max_length=55,
    #     db_column='PAYEE_ADR1',
    #     blank=True,
    #     help_text="Address of Payee"
    # )
    # payee_adr2 = fields.CharField(
    #     max_length=55,
    #     db_column='PAYEE_ADR2',
    #     blank=True,
    #     help_text="Optional 2nd line of Address"
    # )
    payee_city = fields.CharField(
        max_length=30,
        db_column='PAYEE_CITY',
        blank=True,
        help_text="Payee City"
    )
    payee_namf = fields.CharField(
        max_length=45,
        db_column='PAYEE_NAMF',
        blank=True,
        help_text="Payee's First name"
    )
    payee_naml = fields.CharField(
        max_length=200,
        db_column='PAYEE_NAML',
        blank=True,
        help_text="Payee's Last name"
    )
    payee_nams = fields.CharField(
        max_length=10,
        db_column='PAYEE_NAMS',
        blank=True,
        help_text="Payee's Suffix"
    )
    payee_namt = fields.CharField(
        max_length=10,
        db_column='PAYEE_NAMT',
        blank=True,
        help_text="Payee's Prefix or Title"
    )
    payee_st = fields.CharField(
        max_length=2,
        db_column='PAYEE_ST',
        blank=True,
        help_text="State code"
    )
    payee_zip4 = fields.CharField(
        max_length=10,
        db_column='PAYEE_ZIP4',
        blank=True,
        help_text="Zip+4"
    )
    REC_TYPE_CHOICES = (
        ("EXPN", "Expense"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        help_text='Record Type Value: EXPN',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=31),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=42),
        ]
    )
    SUP_OPP_CD_CHOICES = get_sorted_choices(choices.SUP_OPP_CODES) + (
        ('s', choices.SUP_OPP_CODES['S']),
        ('o', choices.SUP_OPP_CODES['O']),
        ('H', 'UNKNOWN'),
        ('N', 'UNKNOWN'),
        ('X', 'UNKNOWN'),
        ('Y', 'UNKNOWN'),
    )
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text="Support or opposition code",
        choices=SUP_OPP_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=32),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=44),
        ]
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )
    # tres_adr1 = fields.CharField(
    #     max_length=55,
    #     db_column='TRES_ADR1',
    #     blank=True,
    #     help_text="Treasurer Street 1(Req if [COM|RCP] & no ID#)"
    # )
    # tres_adr2 = fields.CharField(
    #     max_length=55,
    #     db_column='TRES_ADR2',
    #     blank=True,
    #     help_text="Treasurer Street 2"
    # )
    tres_city = fields.CharField(
        max_length=30,
        db_column='TRES_CITY',
        blank=True,
        help_text="Treasurer City"
    )
    tres_namf = fields.CharField(
        max_length=45,
        db_column='TRES_NAMF',
        blank=True,
        help_text="Treasurer's First name (Req if [COM|RCP] & no ID#)"
    )
    tres_naml = fields.CharField(
        max_length=200,
        db_column='TRES_NAML',
        blank=True,
        help_text="Treasurer's Last name (Req if [COM|RCP] & no ID#)"
    )
    tres_nams = fields.CharField(
        max_length=10,
        db_column='TRES_NAMS',
        blank=True,
        help_text="Treasurer's Suffix"
    )
    tres_namt = fields.CharField(
        max_length=10,
        db_column='TRES_NAMT',
        blank=True,
        help_text="Treasurer's Prefix or Title"
    )
    tres_st = fields.CharField(
        max_length=2,
        db_column='TRES_ST',
        blank=True,
        help_text="Treasurer State"
    )
    tres_zip4 = fields.CharField(
        max_length=10,
        db_column='TRES_ZIP4',
        blank=True,
        help_text="Treasurer ZIP+4"
    )
    xref_match = fields.CharField(
        max_length=1,
        db_column='XREF_MATCH',
        blank=True,
        help_text="X = Related item on other Sched has same Tran_ID"
    )
    xref_schnm = fields.CharField(
        max_length=2,
        db_column='XREF_SCHNM',
        blank=True,
        help_text="Related item is included on Sched 'C' or 'H2'"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'EXPN_CD'
        ordering = ("-expn_date",)

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class LoanCd(CalAccessBaseModel):
    """
    Itemized campaign loans.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=87, end_page=90),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=60, end_page=63),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=35, end_page=39),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=47, end_page=50),
    ]
    FILING_FORMS = [
        get_filing_form('F460').get_section('B1'),
        get_filing_form('F460').get_section('B2'),
        get_filing_form('F460').get_section('B3'),
        get_filing_form('F460').get_section('H'),
        get_filing_form('F460').get_section('H1'),
        get_filing_form('F460').get_section('H2'),
        get_filing_form('F460').get_section('H3'),
    ]
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
        help_text="Back Reference to transaction identifier of parent record"
    )
    cmte_id = fields.CharField(
        max_length=9,
        db_column='CMTE_ID',
        blank=True,
        verbose_name="Committee ID",
        help_text="Committee identification number"
    )
    ENTITY_CD_CHOICES = (
        ('COM', choices.CAMPAIGN_ENTITY_CODES['COM']),
        ('IND', choices.CAMPAIGN_ENTITY_CODES['IND']),
        ('OTH', choices.CAMPAIGN_ENTITY_CODES['OTH']),
        ('PTY', choices.CAMPAIGN_ENTITY_CODES['PTY']),
        ('RCP', choices.CAMPAIGN_ENTITY_CODES['RCP']),
        ('SCC', choices.CAMPAIGN_ENTITY_CODES['SCC']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name="entity code",
        help_text="Entity code describing the lender",
        choices=ENTITY_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=35),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=47),
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
        max_length=2,
        db_column='FORM_TYPE',
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=35),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=47),
        ]
    )
    # intr_adr1 = fields.CharField(
    #     max_length=55, db_column='INTR_ADR1', blank=True
    # )
    # intr_adr2 = fields.CharField(
    #     max_length=55, db_column='INTR_ADR2', blank=True
    # )
    intr_city = fields.CharField(
        max_length=30,
        db_column='INTR_CITY',
        blank=True,
        help_text="Intermediary's city"
    )
    intr_namf = fields.CharField(
        max_length=45,
        db_column='INTR_NAMF',
        blank=True,
        help_text="Intermediary's first name"
    )
    intr_naml = fields.CharField(
        max_length=200,
        db_column='INTR_NAML',
        blank=True,
        help_text="Intermediary's last name"
    )
    intr_nams = fields.CharField(
        max_length=10,
        db_column='INTR_NAMS',
        blank=True,
        help_text="Intermediary's suffix"
    )
    intr_namt = fields.CharField(
        max_length=10,
        db_column='INTR_NAMT',
        blank=True,
        help_text="Intermediary's title or prefix"
    )
    intr_st = fields.CharField(
        max_length=2,
        db_column='INTR_ST',
        blank=True,
        help_text="Intermediary's state"
    )
    intr_zip4 = fields.CharField(
        max_length=10,
        db_column='INTR_ZIP4',
        blank=True,
        help_text="Intermediary's ZIP Code"
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    lndr_namf = fields.CharField(
        max_length=45,
        db_column='LNDR_NAMF',
        blank=True,
        help_text="Lender's first name"
    )
    lndr_naml = fields.CharField(
        max_length=200,
        db_column='LNDR_NAML',
        help_text="Lender's last name or business name"
    )
    lndr_nams = fields.CharField(
        max_length=10,
        db_column='LNDR_NAMS',
        blank=True,
        help_text="Lender's suffix"
    )
    lndr_namt = fields.CharField(
        max_length=10,
        db_column='LNDR_NAMT',
        blank=True,
        help_text="Lender's title or prefix"
    )
    # loan_adr1 = fields.CharField(
    #     max_length=55, db_column='LOAN_ADR1', blank=True
    # )
    # loan_adr2 = fields.CharField(
    #     max_length=55, db_column='LOAN_ADR2', blank=True
    # )
    loan_amt1 = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='LOAN_AMT1',
        blank=True,
        help_text="Repaid or forgiven amount; Original loan amount. The \
content of this column varies based on the \
schedule/part that the record applies to. See the CAL \
document for a description of the value of this field."
    )
    loan_amt2 = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='LOAN_AMT2',
        blank=True,
        help_text="Outstanding Principal; unpaid balance. The content of \
this column varies based on the schedule/part that the \
record applies to. See the CAL document for a \
description of the value of this field."
    )
    loan_amt3 = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='LOAN_AMT3',
        blank=True,
        help_text="Interest Paid; Unpaid interest; Interest received. The \
content of this column varies based on the \
schedule/part that the record applies to. See the CAL \
document for a description of the value of this field."
    )
    loan_amt4 = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='LOAN_AMT4',
        blank=True,
        help_text="Cumulative Amount/Other. The content of this column \
varies based on the schedule/part that the record \
applies to. See the CAL document for a description of the \
value of this field."
    )
    loan_amt5 = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='LOAN_AMT5',
        blank=True,
        help_text="This field is undocumented"
    )
    loan_amt6 = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='LOAN_AMT6',
        blank=True,
        help_text="This field is undocumented"
    )
    loan_amt7 = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='LOAN_AMT7',
        blank=True,
        help_text="This field is undocumented"
    )
    loan_amt8 = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='LOAN_AMT8',
        blank=True,
        help_text="This field is undocumented"
    )
    loan_city = fields.CharField(
        max_length=30,
        db_column='LOAN_CITY',
        blank=True,
        help_text="Lender's city"
    )
    loan_date1 = fields.DateField(
        db_column='LOAN_DATE1',
        null=True,
        help_text="Date the loan was made or received. The content of this \
column varies based on the schedule/part that the \
record applies to. See the CAL document for a description of the value."
    )
    loan_date2 = fields.DateField(
        null=True,
        db_column='LOAN_DATE2',
        blank=True,
        help_text="Date repaid/forgiven; date loan due. The content of this \
column varies based on the schedule/part that the \
record applies to. See the CAL document for a \
description of the value of this field."
    )
    loan_emp = fields.CharField(
        max_length=200,
        db_column='LOAN_EMP',
        blank=True,
        help_text="Loan employer. Applies to the Form 460 Schedule B \
Part 1."
    )
    loan_occ = fields.CharField(
        max_length=60,
        db_column='LOAN_OCC',
        blank=True,
        help_text="Loan occupation. Applies to the Form 460 Schedule B \
Part 1."
    )
    loan_rate = fields.CharField(
        max_length=30,
        db_column='LOAN_RATE',
        blank=True,
        help_text="Interest Rate. The content of this column varies based \
on the schedule/part that the record applies to. See the \
CAL document for a description of the value of this field."
    )
    loan_self = fields.CharField(
        max_length=1,
        db_column='LOAN_SELF',
        blank=True,
        help_text="Self-employed checkbox"
    )
    loan_st = fields.CharField(
        max_length=2,
        db_column='LOAN_ST',
        blank=True,
        help_text="Lender's state"
    )
    LOAN_TYPE_CHOICES = (
        ("H2T", "Third party payment"),
        ("H2F", "Forgiven"),
        ("H2R", "Repay"),
        ("B2T", "Third party payment"),
        ("B2F", "Forgiven"),
        ("B2R", "Repay"),
        ("B1G", "Guarantor"),
        ("B1L", "Lender"),
    )
    loan_type = fields.CharField(
        max_length=3,
        db_column='LOAN_TYPE',
        blank=True,
        choices=LOAN_TYPE_CHOICES,
        help_text="Type of loan",
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=35),
            # this field may no longer be in use, CAL format v2 instructs to leave NULL
            DocumentCloud(id='2712034-Cal-Format-201', start_page=47),
        ]
    )
    loan_zip4 = fields.CharField(
        max_length=10,
        db_column='LOAN_ZIP4',
        blank=True,
        help_text="Lender's ZIP Code"
    )
    memo_code = fields.CharField(
        max_length=1,
        db_column='MEMO_CODE',
        blank=True,
        help_text="Memo amount flag"
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text="Reference to text contained in a TEXT record"
    )
    REC_TYPE_CHOICES = (
        ("LOAN", "LOAN"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        help_text='Record Type Value: LOAN',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=35),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=47),
        ]
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )
    # tres_adr1 = fields.CharField(
    #     max_length=55, db_column='TRES_ADR1', blank=True
    # )
    # tres_adr2 = fields.CharField(
    #     max_length=55, db_column='TRES_ADR2', blank=True
    # )
    tres_city = fields.CharField(
        max_length=30,
        db_column='TRES_CITY',
        blank=True,
        help_text="Treasurer or responsible officer's city"
    )
    tres_namf = fields.CharField(
        max_length=45,
        db_column='TRES_NAMF',
        blank=True,
        help_text="Treasurer or responsible officer's first name"
    )
    tres_naml = fields.CharField(
        max_length=200,
        db_column='TRES_NAML',
        blank=True,
        help_text="Treasurer or responsible officer's last name"
    )
    tres_nams = fields.CharField(
        max_length=10,
        db_column='TRES_NAMS',
        blank=True,
        help_text="Treasurer or responsible officer's suffix"
    )
    tres_namt = fields.CharField(
        max_length=10,
        db_column='TRES_NAMT',
        blank=True,
        help_text="Treasurer or responsible officer's title or prefix"
    )
    tres_st = fields.CharField(
        max_length=2,
        db_column='TRES_ST',
        blank=True,
        help_text="Treasurer or responsible officer's street address"
    )
    tres_zip4 = fields.CharField(
        max_length=10,
        db_column='TRES_ZIP4',
        blank=True,
        help_text="Treasurer or responsible officer's ZIP Code"
    )
    xref_match = fields.CharField(
        max_length=1,
        db_column='XREF_MATCH',
        blank=True,
        help_text='Related item on other schedule has same transaction \
identifier. "X" indicates this condition is true.'
    )
    xref_schnm = fields.CharField(
        max_length=2,
        db_column='XREF_SCHNM',
        blank=True,
        help_text="Related record is included on Form 460 Schedule 'A' or 'E'"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOAN_CD'
        ordering = ("-loan_date1",)

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class RcptCd(CalAccessBaseModel):
    """
    Itemized campaign contributions.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=13),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=118, end_page=121),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=71, end_page=75),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=29, end_page=30),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=37, end_page=41),
    ]
    FILING_FORMS = [
        get_filing_form('E530'),
        get_filing_form('F900'),
        get_filing_form('F401').get_section('A'),
        get_filing_form('F460').get_section('A'),
        get_filing_form('F460').get_section('A-1'),
        get_filing_form('F460').get_section('C'),
        get_filing_form('F460').get_section('I'),
        get_filing_form('F496').get_section('P3'),
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
        max_digits=14,
        db_column='AMOUNT',
        help_text="Amount Received (Monetary, In-kind, Promise)"
    )
    bakref_tid = fields.CharField(
        max_length=20,
        db_column='BAKREF_TID',
        blank=True,
        help_text="Back Reference to a transaction identifier of a parent \
record"
    )
    bal_juris = fields.CharField(
        max_length=40,
        db_column='BAL_JURIS',
        blank=True,
        help_text="Jurisdiction of ballot measure. Used on the Form 401 \
Schedule A"
    )
    bal_name = fields.CharField(
        max_length=200,
        db_column='BAL_NAME',
        blank=True,
        help_text="Ballot measure name. Used on the Form 401 Schedule A"
    )
    bal_num = fields.CharField(
        max_length=7,
        db_column='BAL_NUM',
        blank=True,
        help_text="Ballot measure number or letter. Used on the Form 401 \
Schedule A"
    )
    cand_namf = fields.CharField(
        max_length=45,
        db_column='CAND_NAMF',
        blank=True,
        help_text="Candidate/officeholder's first name. Used on the Form \
401 Schedule A"
    )
    cand_naml = fields.CharField(
        max_length=200,
        db_column='CAND_NAML',
        blank=True,
        help_text="Candidate/officeholder's last name. Used on the Form \
401 Schedule A"
    )
    cand_nams = fields.CharField(
        max_length=10,
        db_column='CAND_NAMS',
        blank=True,
        help_text="Candidate/officeholder's name suffix. Used on the Form \
401 Schedule A"
    )
    cand_namt = fields.CharField(
        max_length=10,
        db_column='CAND_NAMT',
        blank=True,
        help_text="Candidate/officeholder's name prefix or title. Used on \
the Form 401 Schedule A"
    )
    cmte_id = fields.CharField(
        max_length=9,
        db_column='CMTE_ID',
        blank=True,
        help_text="Committee Identification number"
    )
    # ctrib_adr1 = fields.CharField(
    #     max_length=55,
    #     db_column='CTRIB_ADR1',
    #     blank=True,
    #     default="",
    #     help_text="First line of the contributor's street address"
    # )
    # ctrib_adr2 = fields.CharField(
    #     max_length=55,
    #     db_column='CTRIB_ADR2',
    #     blank=True,
    #     help_text="Second line of the contributor's street address"
    # )
    ctrib_city = fields.CharField(
        max_length=30,
        db_column='CTRIB_CITY',
        blank=True,
        help_text="Contributor's City"
    )
    ctrib_dscr = fields.CharField(
        max_length=90,
        db_column='CTRIB_DSCR',
        blank=True,
        help_text="Description of goods/services received"
    )
    ctrib_emp = fields.CharField(
        max_length=200,
        db_column='CTRIB_EMP',
        blank=True,
        help_text="Employer"
    )
    ctrib_namf = fields.CharField(
        max_length=45,
        db_column='CTRIB_NAMF',
        blank=True,
        help_text="Contributor's First Name"
    )
    ctrib_naml = fields.CharField(
        max_length=200,
        db_column='CTRIB_NAML',
        help_text="Contributor's last name or business name"
    )
    ctrib_nams = fields.CharField(
        max_length=10,
        db_column='CTRIB_NAMS',
        blank=True,
        help_text="Contributor's Suffix"
    )
    ctrib_namt = fields.CharField(
        max_length=10,
        db_column='CTRIB_NAMT',
        blank=True,
        help_text="Contributor's Prefix or Title"
    )
    ctrib_occ = fields.CharField(
        max_length=60,
        db_column='CTRIB_OCC',
        blank=True,
        help_text="Occupation"
    )
    ctrib_self = fields.CharField(
        max_length=1,
        db_column='CTRIB_SELF',
        blank=True,
        help_text="Self Employed Check-box"
    )
    ctrib_st = fields.CharField(
        max_length=2,
        db_column='CTRIB_ST',
        blank=True,
        help_text="Contributor's State"
    )
    ctrib_zip4 = fields.CharField(
        max_length=10,
        db_column='CTRIB_ZIP4',
        blank=True,
        help_text="Contributor's ZIP+4"
    )
    cum_oth = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='CUM_OTH',
        blank=True,
        help_text="Cumulative Other (Sched A, A-1)"
    )
    cum_ytd = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='CUM_YTD',
        blank=True,
        help_text="Cumulative year to date amount (Form 460 Schedule A \
and Form 401 Schedule A, A-1)"
    )
    date_thru = fields.DateField(
        null=True,
        db_column='DATE_THRU',
        blank=True,
        help_text="End of date range for items received"
    )
    dist_no = fields.CharField(
        max_length=3,
        db_column='DIST_NO',
        blank=True,
        help_text="Office District Number (used on F401A)"
    )
    ENTITY_CD_CHOICES = (
        # Codes explicitly allowed for this field, according to documentation
        ('COM', choices.CAMPAIGN_ENTITY_CODES['COM']),
        ('IND', choices.CAMPAIGN_ENTITY_CODES['IND']),
        ('PTY', choices.CAMPAIGN_ENTITY_CODES['PTY']),
        ('OTH', choices.CAMPAIGN_ENTITY_CODES['OTH']),
        ('RCP', choices.CAMPAIGN_ENTITY_CODES['RCP']),
        ('SCC', choices.CAMPAIGN_ENTITY_CODES['SCC']),
        ('Com', choices.CAMPAIGN_ENTITY_CODES['COM']),
        # Other known codes observed in this field
        ('CAO', choices.CAMPAIGN_ENTITY_CODES['CAO']),
        ('BNM', choices.CAMPAIGN_ENTITY_CODES['BNM']),
        ('OFF', choices.CAMPAIGN_ENTITY_CODES['OFF']),
        # Other unknown values observed
        ('0', "Unknown"),
        ('PTH', 'Unknown'),
        ('RFD', 'Unknown'),  # Request for Development?
        ('MBR', 'Unknown'),  # Member?
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        help_text="Entity Code describing the contributor",
        choices=ENTITY_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=71),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=29),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=37),
        ] + choices.DOCS['entity_codes']
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        choices=FORM_TYPE_CHOICES,
        max_length=9,
        db_index=True,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=29),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=37),
        ]
    )
    int_rate = fields.CharField(
        max_length=9,
        db_column='INT_RATE',
        blank=True,
        help_text="This field is undocumented. The observed values look like "
                  "filer_ids taken from section 5, cover page 2 of Form 460 "
                  "(Related Committees Not Included in this Statement)."
    )
    # intr_adr1 = fields.CharField(
    #     max_length=55,
    #     db_column='INTR_ADR1',
    #     blank=True,
    #     help_text="First line of the intermediary's street address."
    # )
    # intr_adr2 = fields.CharField(
    #     max_length=55,
    #     db_column='INTR_ADR2',
    #     blank=True,
    #     help_text="Second line of the Intermediary's street address."
    # )
    intr_city = fields.CharField(
        max_length=30,
        db_column='INTR_CITY',
        blank=True,
        help_text="Intermediary's City"
    )
    intr_cmteid = fields.CharField(
        max_length=9,
        db_column='INTR_CMTEID',
        blank=True,
        help_text="This field is undocumented"
    )
    intr_emp = fields.CharField(
        max_length=200,
        db_column='INTR_EMP',
        blank=True,
        help_text="Intermediary's Employer"
    )
    intr_namf = fields.CharField(
        max_length=45,
        db_column='INTR_NAMF',
        blank=True,
        help_text="Intermediary's First Name"
    )
    intr_naml = fields.CharField(
        max_length=200,
        db_column='INTR_NAML',
        blank=True,
        help_text="Intermediary's Last Name"
    )
    intr_nams = fields.CharField(
        max_length=10,
        db_column='INTR_NAMS',
        blank=True,
        help_text="Intermediary's Suffix"
    )
    intr_namt = fields.CharField(
        max_length=10,
        db_column='INTR_NAMT',
        blank=True,
        help_text="Intermediary's Prefix or Title"
    )
    intr_occ = fields.CharField(
        max_length=60,
        db_column='INTR_OCC',
        blank=True,
        help_text="Intermediary's Occupation"
    )
    intr_self = fields.CharField(
        max_length=1,
        db_column='INTR_SELF',
        blank=True,
        help_text="Intermediary's self employed check box"
    )
    intr_st = fields.CharField(
        max_length=2,
        db_column='INTR_ST',
        blank=True,
        help_text="Intermediary's state"
    )
    intr_zip4 = fields.CharField(
        max_length=10,
        db_column='INTR_ZIP4',
        blank=True,
        help_text="Intermediary's zip code"
    )
    JURIS_CD_CHOICES = get_sorted_choices(choices.JURIS_CODES) + (
        # "other" office codes
        ('BED', choices.JURIS_CODES['OTH']),
        ('CLB', choices.JURIS_CODES['OTH']),
        # misprint
        ('COU', choices.JURIS_CODES['CTY']),
        # Office Code for this one record is Superior Court Judge
        ('CO', choices.JURIS_CODES['OTH']),
        ('SAC', 'Unknown'),
        ('PER', 'Unknown'),
        ('SF', 'Unknown'),
        ('OR', 'Unknown'),
        ('AL', 'Unknown'),
        ('4', 'Unknown'),
        ('CA', 'Unknown'),
    )
    juris_cd = fields.CharField(
        max_length=3,
        db_column='JURIS_CD',
        blank=True,
        choices=JURIS_CD_CHOICES,
        help_text="Office jurisdiction code. See the CAL document for the \
list of legal values. Used on Form 401 Schedule A",
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=74),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=30),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=40),
        ]
    )
    juris_dscr = fields.CharField(
        max_length=40,
        db_column='JURIS_DSCR',
        blank=True,
        help_text="Office Jurisdiction Description (used on F401A)"
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
        help_text="Memo amount flag (Date/Amount are informational only)"
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text="Reference to text contained in a TEXT record"
    )
    OFF_S_H_CD_CHOICES = (
        ('S', choices.OFF_S_H_CODES['S']),
        ('H', choices.OFF_S_H_CODES['H']),
    )
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text='Office is sought or held code',
        choices=OFF_S_H_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=75),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=30),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=40),
        ]
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office Sought Description (used on F401A)"
    )
    OFFICE_CD_CHOICES = get_sorted_choices(choices.OFFICE_CODES) + (
        # alt cases for valid codes
        ('asm', choices.OFFICE_CODES['ASM']),
        ('gov', choices.OFFICE_CODES['GOV']),
        ('OTh', choices.OFFICE_CODES['OTH']),
        ('oth', choices.OFFICE_CODES['OTH']),
        ('csu', choices.OFFICE_CODES['CSU']),
        # invalid codes
        ('H', 'Unknown'),
        ('HOU', 'Unknown'),
        ('ASS', 'Unknown'),
    )
    office_cd = fields.CharField(
        db_column='OFFICE_CD',
        max_length=3,
        blank=True,
        verbose_name="office code",
        help_text="Identifies the office being sought",
        choices=OFFICE_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=10),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=12),
            DocumentCloud(id='2712032-Cal-Errata-201', start_page=2),
        ],
    )
    rcpt_date = fields.DateField(
        db_column='RCPT_DATE',
        null=True,
        help_text="Date item received"
    )
    REC_TYPE_CHOICES = (
        ('E530', get_filing_form('E530').full_title),
        ("RCPT", "Receipt"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        help_text="Record Type Value: CVR",
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=71),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=37),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=29),
        ]
    )
    SUP_OPP_CD_CHOICES = (
        # Codes explicitly allowed for this field, according to documentation
        ('S', choices.SUP_OPP_CODES['S']),
        ('O', choices.SUP_OPP_CODES['O']),
        # Other unknown values observed
        ('F', 'Unknown'),
    )
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text="Support or opposition code",
        choices=SUP_OPP_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=74),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=30),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=40),
        ]
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )
    TRAN_TYPE_CHOICES = [
        # Codes explicitly allowed for this field, according to documentation
        ('F', 'Forgiven Loan'),
        ('I', 'Intermediary'),
        ('R', 'Returned (Negative Amount?)'),
        ('T', 'Third Party Repayment'),
        ('X', 'Transfer'),
        # Other unknown values observed
        ('0', 'Unknown'),
        ('I', 'Unknown'),
        ('M', 'Unknown'),
        ('N', 'Unknown'),
        ('R', 'Unknown'),
        ('T', 'Unknown'),
    ]
    tran_type = fields.CharField(
        max_length=1,
        db_column='TRAN_TYPE',
        blank=True,
        choices=TRAN_TYPE_CHOICES,
        help_text="Transaction Type",
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=72),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=29),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=38),
        ]
    )
#     tres_adr1 = fields.CharField(
#         max_length=55,
#         db_column='TRES_ADR1',
#         blank=True,
#         help_text="First line of the treasurer or responsible officer's \
# street address"
#     )
#     tres_adr2 = fields.CharField(
#         max_length=55,
#         db_column='TRES_ADR2',
#         blank=True,
#         help_text="Second line of the treasurer or responsible officer's \
# street address"
#     )
    tres_city = fields.CharField(
        max_length=30,
        db_column='TRES_CITY',
        blank=True,
        help_text="City portion of the treasurer or responsible officer's \
street address"
    )
    tres_namf = fields.CharField(
        max_length=45,
        db_column='TRES_NAMF',
        blank=True,
        help_text="Treasurer or responsible officer's first name"
    )
    tres_naml = fields.CharField(
        max_length=200,
        db_column='TRES_NAML',
        blank=True,
        help_text="Treasurer or responsible officer's last name"
    )
    tres_nams = fields.CharField(
        max_length=10,
        db_column='TRES_NAMS',
        blank=True,
        help_text="Treasurer or responsible officer's suffix"
    )
    tres_namt = fields.CharField(
        max_length=10,
        db_column='TRES_NAMT',
        blank=True,
        help_text="Treasurer or responsible officer's prefix or title"
    )
    tres_st = fields.CharField(
        max_length=2,
        db_column='TRES_ST',
        blank=True,
        help_text="State portion of the treasurer or responsible officer's \
address"
    )
    tres_zip4 = fields.CharField(
        null=True,
        max_length=10,
        blank=True,
        db_column='TRES_ZIP4',
        help_text="Zip code portion of the treasurer or responsible officer's \
address"
    )
    xref_match = fields.CharField(
        max_length=1,
        db_column='XREF_MATCH',
        blank=True,
        help_text="Related item on other schedule has same transaction \
identifier. 'X' indicates this condition is true"
    )
    xref_schnm = fields.CharField(
        max_length=2,
        db_column='XREF_SCHNM',
        blank=True,
        help_text="Related record is included on Sched 'B2' or 'F'"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'RCPT_CD'
        ordering = ("-rcpt_date",)

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class S401Cd(CalAccessBaseModel):
    """
    Payments and other disclosures made by slate-mailer organizations.
    """
    UNIQUE_KEY = (
        'FILING_ID',
        'AMEND_ID',
        'LINE_ITEM',
        'REC_TYPE',
        'FORM_TYPE'
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=123, end_page=124),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=76, end_page=78),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=39),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=51, end_page=52),
    ]
    FILING_FORMS = [
        get_filing_form('F401').get_section('B'),
        get_filing_form('F401').get_section('B-1'),
        get_filing_form('F401').get_section('C'),
        get_filing_form('F401').get_section('D'),
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
        ("S401", "S401"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        help_text="Record Type Value: S401",
        choices=REC_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=39),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=51),
        ]
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        blank=True,
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=39),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=51),
        ]
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )
    agent_naml = fields.CharField(
        max_length=200,
        db_column='AGENT_NAML',
        blank=True,
        help_text="Agent or independent contractor's last name"
    )
    agent_namf = fields.CharField(
        max_length=45,
        db_column='AGENT_NAMF',
        blank=True,
        help_text="Agent or independent contractor's first name"
    )
    agent_namt = fields.CharField(
        max_length=200,
        db_column='AGENT_NAMT',
        blank=True,
        help_text="Agent or independent contractor's title or prefix"
    )
    agent_nams = fields.CharField(
        max_length=10,
        db_column='AGENT_NAMS',
        blank=True,
        help_text="Agent or independent contractor's suffix"
    )
    payee_naml = fields.CharField(
        max_length=200,
        db_column='PAYEE_NAML',
        blank=True,
        help_text="Payee's business name or last name if the payee is an \
individual"
    )
    payee_namf = fields.CharField(
        max_length=45,
        db_column='PAYEE_NAMF',
        blank=True,
        help_text="Payee's first name if the payee is an individual"
    )
    payee_namt = fields.CharField(
        max_length=10,
        db_column='PAYEE_NAMT',
        blank=True,
        help_text="Payee's title or prefix if the payee is an individual"
    )
    payee_nams = fields.CharField(
        max_length=10,
        db_column='PAYEE_NAMS',
        blank=True,
        help_text="Payee's suffix if the payee is an individual"
    )
    payee_city = fields.CharField(
        max_length=30,
        db_column='PAYEE_CITY',
        blank=True,
        help_text="Payee's city address"
    )
    payee_st = fields.CharField(
        max_length=2,
        db_column='PAYEE_ST',
        blank=True,
        help_text="Payee state address"
    )
    payee_zip4 = fields.CharField(
        max_length=10,
        db_column='PAYEE_ZIP4',
        blank=True,
        help_text="Payee ZIP Code"
    )
    amount = fields.DecimalField(
        max_digits=16,
        decimal_places=2,
        db_column='AMOUNT',
        help_text="Amount (Sched F401B, 401B-1, 401C)"
    )
    aggregate = fields.DecimalField(
        max_digits=16,
        decimal_places=2,
        db_column='AGGREGATE',
        help_text="Aggregate year-to-date amount (Sched 401C)"
    )
    expn_dscr = fields.CharField(
        max_length=90,
        db_column='EXPN_DSCR',
        blank=True,
        help_text="Purpose of expense and/or description/explanation"
    )
    cand_naml = fields.CharField(
        max_length=200,
        db_column='CAND_NAML',
        blank=True,
        help_text="Candidate/officeholder last name"
    )
    cand_namf = fields.CharField(
        max_length=45,
        db_column='CAND_NAMF',
        blank=True,
        help_text="Candidate/officeholder first name"
    )
    cand_namt = fields.CharField(
        max_length=10,
        db_column='CAND_NAMT',
        blank=True,
        help_text="Candidate/officeholder title or prefix"
    )
    cand_nams = fields.CharField(
        max_length=10,
        db_column='CAND_NAMS',
        blank=True,
        help_text="Candidate/officeholder suffix"
    )
    OFFICE_CD_CHOICES = get_sorted_choices(choices.OFFICE_CODES) + (
        # alt cases for valid codes
        ('asm', choices.OFFICE_CODES['ASM']),
        ('ltg', choices.OFFICE_CODES['LTG']),
        ('OTh', choices.OFFICE_CODES['OTH']),
        ('att', choices.OFFICE_CODES['ATT']),
        ('oth', choices.OFFICE_CODES['OTH']),
        ('tre', choices.OFFICE_CODES['TRE']),
        ('con', choices.OFFICE_CODES['CON']),
        ('boe', choices.OFFICE_CODES['BOE']),
        ('sos', choices.OFFICE_CODES['SOS']),
        ('sup', choices.OFFICE_CODES['SUP']),
        # invalid codes
        ('H', 'Unknown'),
    )
    office_cd = fields.CharField(
        db_column='OFFICE_CD',
        max_length=3,
        blank=True,
        verbose_name="office code",
        help_text="Identifies the office being sought",
        choices=OFFICE_CD_CHOICES,
        documentcloud_pages=choices.DOCS['office_codes'],
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office sought description"
    )
    JURIS_CD_CHOICES = get_sorted_choices(choices.JURIS_CODES) + (
        ('SAC', 'Unknown'),
        ('CT', 'Unknown'),
        ('ca', 'Unknown'),
        ('CAL', 'Unknown'),
        ('OR', 'Unknown'),
        ('AL', 'Unknown'),
        ('CA', 'Unknown'),
        ('10', 'Unknown'),
    )
    juris_cd = fields.CharField(
        max_length=3,
        choices=JURIS_CD_CHOICES,
        db_column='JURIS_CD',
        blank=True,
        help_text="Office jurisdiction code",
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=77),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=39),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=52),
        ]
    )
    juris_dscr = fields.CharField(
        max_length=40,
        db_column='JURIS_DSCR',
        blank=True,
        help_text="Office jurisdiction description"
    )
    dist_no = fields.CharField(
        max_length=3,
        db_column='DIST_NO',
        blank=True,
        help_text="District number for the office being sought. Populated \
for Senate, Assembly, or Board of Equalization races."
    )
    OFF_S_H_CD_CHOICES = (
        ('S', choices.OFF_S_H_CODES['S']),
        ('H', choices.OFF_S_H_CODES['H']),
    )
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text='Office is sought or held code',
        choices=OFF_S_H_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=39),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=52),
        ]
    )
    bal_name = fields.CharField(
        max_length=200,
        db_column='BAL_NAME',
        blank=True,
        help_text="Ballot measure name"
    )
    bal_num = fields.CharField(
        max_length=7,
        db_column='BAL_NUM',
        blank=True,
        help_text="Ballot measure number or letter"
    )
    bal_juris = fields.CharField(
        max_length=40,
        db_column='BAL_JURIS',
        blank=True,
        help_text="Ballot measure jurisdiction"
    )
    SUP_OPP_CD_CHOICES = (
        ('S', choices.SUP_OPP_CODES['S']),
        ('O', choices.SUP_OPP_CODES['O']),
    )
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text="Support or opposition code",
        choices=SUP_OPP_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=39),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=52),
        ]
    )
    memo_code = fields.CharField(
        max_length=1,
        db_column='MEMO_CODE',
        blank=True,
        help_text="Memo amount flag"
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text="Reference to text contained in the TEXT record"
    )
    bakref_tid = fields.CharField(
        max_length=20,
        db_column='BAKREF_TID',
        blank=True,
        help_text="Back reference to transaction identifier of parent record"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'S401_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class F495P2Cd(CalAccessBaseModel):
    """
    Supplemental pre-election campaign statements.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=56, end_page=57),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=49),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=26),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=35),
    ]
    FILING_FORMS = [
        get_filing_form('F450'),
        get_filing_form('F460'),
        get_filing_form('F495'),
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
        ('F495', 'F495'),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        help_text='Record Type Value: F495',
        choices=REC_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=26),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=35),
        ]
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=4,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=26),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=35),
        ],
        help_text='Name of the source filing form to which the Form 495 is \
attached (must equal Form_Type in CVR record)',
    )
    elect_date = fields.DateField(
        db_column='ELECT_DATE',
        blank=True,
        null=True,
        help_text="Date of the General Election This date will be the same \
as on the filing's cover (CVR) record."
    )
    electjuris = fields.CharField(
        db_column='ELECTJURIS',
        max_length=40,
        help_text="Jurisdiction of the election"
    )
    contribamt = fields.FloatField(
        db_column='CONTRIBAMT',
        help_text="Contribution amount (For the period of 6 months prior to \
17 days before the election)"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'F495P2_CD'
        ordering = ("-elect_date",)

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class S496Cd(CalAccessBaseModel):
    """
    Itemized independent expenditures made in the 90 days before an election.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=12),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=124, end_page=125),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=79),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=40),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=53),
    ]
    FILING_FORMS = [
        get_filing_form('F496')
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
        ('S496', 'S496'),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        max_length=4,
        db_column='REC_TYPE',
        db_index=True,
        choices=REC_TYPE_CHOICES,
        help_text="Record Type Value: S496",
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=40),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=53),
        ]
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=4,
        db_column='FORM_TYPE',
        blank=True,
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=40),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=53),
        ]
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )
    amount = fields.DecimalField(
        max_digits=16,
        decimal_places=2,
        db_column='AMOUNT',
        help_text="Expenditure amount"
    )
    exp_date = fields.DateField(
        db_column='EXP_DATE',
        null=True,
        help_text="Expenditure dates"
    )
    expn_dscr = fields.CharField(
        max_length=90,
        db_column='EXPN_DSCR',
        blank=True,
        help_text="Purpose of expense and/or description/explanation"
    )
    memo_code = fields.CharField(
        max_length=1,
        db_column='MEMO_CODE',
        blank=True,
        help_text="Memo amount flag"
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text="Reference to text contained in a TEXT record"
    )
    date_thru = fields.DateField(
        db_column='DATE_THRU',
        null=True,
        help_text="End of date range for items paid"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'S496_CD'
        ordering = ("-exp_date",)

    def __str__(self):
        return "{} Filing {}, Amendment {}".format(
            self.form_type,
            self.filing_id,
            self.amend_id
        )


@python_2_unicode_compatible
class S497Cd(CalAccessBaseModel):
    """
    Campaign contributions made or received in the 90 days before an election.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=12),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=125, end_page=127),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=80, end_page=82),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=41, end_page=42),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=54, end_page=55),
    ]
    FILING_FORMS = [
        get_filing_form('F497').get_section('P1'),
        get_filing_form('F497').get_section('P2'),
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
        ("S497", "S497"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        help_text="Record Type Value: S497",
        choices=REC_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=41),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=54),
        ]
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=6,
        db_column='FORM_TYPE',
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=41),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=54),
        ]
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )
    ENTITY_CD_CHOICES = (
        ('BNM', choices.CAMPAIGN_ENTITY_CODES['BNM']),
        ('CAO', choices.CAMPAIGN_ENTITY_CODES['CAO']),
        ('CTL', choices.CAMPAIGN_ENTITY_CODES['CTL']),
        ('COM', choices.CAMPAIGN_ENTITY_CODES['COM']),
        ('com', choices.CAMPAIGN_ENTITY_CODES['COM']),
        ('IND', choices.CAMPAIGN_ENTITY_CODES['IND']),
        ('OFF', choices.CAMPAIGN_ENTITY_CODES['OFF']),
        ('OTH', choices.CAMPAIGN_ENTITY_CODES['OTH']),
        ('PTY', choices.CAMPAIGN_ENTITY_CODES['PTY']),
        ('RCP', choices.CAMPAIGN_ENTITY_CODES['RCP']),
        ('SCC', choices.CAMPAIGN_ENTITY_CODES['SCC']),
        ('0', 'Unknown'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        help_text='Entity Code describing the Contributor/Recipient',
        choices=ENTITY_CD_CHOICES,
        documentcloud_pages=choices.DOCS['entity_codes'] + [
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=41),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=54),
        ]
    )
    enty_naml = fields.CharField(
        max_length=200,
        db_column='ENTY_NAML',
        blank=True,
        help_text="Last name of Contributor/Recipient",
    )
    enty_namf = fields.CharField(
        max_length=45,
        db_column='ENTY_NAMF',
        blank=True,
        help_text="First name of Contributor/Recipient",
    )
    enty_namt = fields.CharField(
        max_length=10,
        db_column='ENTY_NAMT',
        blank=True,
        help_text="Name title or prefix of Contributor/Recipient",
    )
    enty_nams = fields.CharField(
        max_length=10,
        db_column='ENTY_NAMS',
        blank=True,
        help_text="Name suffix of Contributor/Recipient",
    )
    enty_city = fields.CharField(
        max_length=30,
        db_column='ENTY_CITY',
        blank=True,
        help_text="City address of Contributor/Recipient",
    )
    enty_st = fields.CharField(
        max_length=2,
        db_column='ENTY_ST',
        blank=True,
        help_text="State address of Contributor/Recipient",
    )
    enty_zip4 = fields.CharField(
        max_length=10,
        db_column='ENTY_ZIP4',
        blank=True,
        help_text="ZIP Code of Contributor/Recipient",
    )
    ctrib_emp = fields.CharField(
        max_length=200,
        db_column='CTRIB_EMP',
        blank=True,
        help_text="Employer of Contributor (populated for some Recipients as well)",
    )
    ctrib_occ = fields.CharField(
        max_length=60,
        db_column='CTRIB_OCC',
        blank=True,
        help_text="Occupation of Contributor (populated for some Recipients as well)"
    )
    ctrib_self = fields.CharField(
        max_length=1,
        db_column='CTRIB_SELF',
        blank=True,
        verbose_name="Contributor self-employed checkbox",
        help_text='Contributor self-employed checkbox. "X" indicates the contributor is \
self-employed.'
    )
    elec_date = fields.DateField(
        db_column='ELEC_DATE',
        null=True,
        help_text="Date of election"
    )
    ctrib_date = fields.DateField(
        db_column='CTRIB_DATE',
        null=True,
        help_text="Date item received/made"
    )
    date_thru = fields.DateField(
        db_column='DATE_THRU',
        null=True,
        help_text="End of date range for items received"
    )
    amount = fields.DecimalField(
        max_digits=16,
        decimal_places=2,
        db_column='AMOUNT',
        help_text="Amount received/made"
    )
    cmte_id = fields.CharField(
        max_length=9,
        db_column='CMTE_ID',
        blank=True,
        verbose_name="Committee ID",
        help_text="Committee identification number"
    )
    cand_naml = fields.CharField(
        max_length=200,
        db_column='CAND_NAML',
        blank=True,
        help_text="Candidate/officeholder's last name"
    )
    cand_namf = fields.CharField(
        max_length=45,
        db_column='CAND_NAMF',
        blank=True,
        help_text="Candidate/officeholder's first name"
    )
    cand_namt = fields.CharField(
        max_length=10,
        db_column='CAND_NAMT',
        blank=True,
        help_text="Candidate/officeholder's title or prefix"
    )
    cand_nams = fields.CharField(
        max_length=10,
        db_column='CAND_NAMS',
        blank=True,
        help_text="Candidate/officeholder's suffix"
    )
    OFFICE_CD_CHOICES = get_sorted_choices(choices.OFFICE_CODES) + (
        # alt cases of valid codes
        ('asm', choices.OFFICE_CODES['ASM']),
        ('sen', choices.OFFICE_CODES['SEN']),
        ('Asm', choices.OFFICE_CODES['ASM']),
        ('May', choices.OFFICE_CODES['MAY']),
        ('ASm', choices.OFFICE_CODES['ASM']),
        ('oth', choices.OFFICE_CODES['OTH']),
        ('csu', choices.OFFICE_CODES['CSU']),
        ('Oth', choices.OFFICE_CODES['OTH']),
        # invalid codes
        ('H', 'Unknown'),
        ('S', 'Unknown'),
        ('OF', 'Unknown'),
        ('HOU', 'Unknown'),
        ('LOC', 'Unknown'),
        ('LEG', 'Unknown'),
        ('STW', 'Unknown'),
        ('P', 'Unknown'),
        ('LTV', 'Unknown'),
        ('LT', 'Unknown'),
        ('CTY', 'Unknown'),
        ('OFF', 'Unknown'),
        ('REP', 'Unknown'),
        ('COM', 'Unknown'),
        ('N/A', 'Unknown'),
    )
    office_cd = fields.CharField(
        db_column='OFFICE_CD',
        max_length=3,
        blank=True,
        verbose_name="office code",
        help_text="Identifies the office being sought",
        choices=OFFICE_CD_CHOICES,
        documentcloud_pages=choices.DOCS['office_codes']
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office sought description"
    )
    JURIS_CD_CHOICES = get_sorted_choices(choices.JURIS_CODES) + (
        ('asm', choices.JURIS_CODES['ASM']),
        ('sen', choices.JURIS_CODES['SEN']),
        ('cit', choices.JURIS_CODES['CIT']),
        ('GOV', choices.JURIS_CODES['STW']),
        # city office codes
        ('MAY', choices.JURIS_CODES['CIT']),
        # county office codes
        ('BSU', choices.JURIS_CODES['CTY']),
        ('CSU', choices.JURIS_CODES['CTY']),
        # statewide office codes
        ('SUP', choices.JURIS_CODES['STW']),
        # other office codes
        ('BED', choices.JURIS_CODES['OTH']),
        ('CCB', choices.JURIS_CODES['OTH']),
        ('CCM', choices.JURIS_CODES['OTH']),
        ('CLB', choices.JURIS_CODES['OTH']),
        # These are all for City Council Member offices
        ('IRV', choices.JURIS_CODES['CIT']),
        ('Fon', choices.JURIS_CODES['CIT']),
        # For Arnold's Gov campaign
        ('JRS', choices.JURIS_CODES['STW']),
        # County Supervisor office
        ('CO', choices.JURIS_CODES['CTY']),
        ('Riv', choices.JURIS_CODES['CTY']),
        # misspelling
        ('SNE', choices.JURIS_CODES['SEN']),
        # This is for Prop 83
        ('83', choices.JURIS_CODES['STW']),
        # Sometimes Assembly Member, sometimes Public Employees Retirement System
        ('PER', 'Unknown'),
        # These look like contributions to federal campaigns (e.g., President, Congress)
        ('FED', 'Unknown'),
        # Sometimes for Assembly Members, sometimes Statewide offices, kinda all over
        ('CA', 'Unknown'),
        ('JR', 'Unknown'),
    )
    juris_cd = fields.CharField(
        max_length=3,
        db_column='JURIS_CD',
        blank=True,
        verbose_name="jurisdiction code",
        help_text="Jurisdiction code describing the office being sought",
        choices=JURIS_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=42),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=55),
        ]
    )
    juris_dscr = fields.CharField(
        max_length=40,
        db_column='JURIS_DSCR',
        blank=True,
        help_text="Office jurisdiction description"
    )
    dist_no = fields.CharField(
        max_length=3,
        db_column='DIST_NO',
        blank=True,
        help_text="District number for the office being sought. Populated \
for Senate, Assembly, or Board of Equalization races."
    )
    OFF_S_H_CD_CHOICES = get_sorted_choices(choices.OFF_S_H_CODES) + (
        ('s', choices.OFF_S_H_CODES['S']),
        ('h', choices.OFF_S_H_CODES['H']),
        # The codes below appear in the database but are undocumented
        ('F', 'UNKNOWN'),
        ('T', 'UNKNOWN'),
    )
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text='Office is sought or held code',
        choices=OFF_S_H_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=42),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=55),
        ]
    )
    bal_name = fields.CharField(
        max_length=200,
        db_column='BAL_NAME',
        blank=True,
        help_text="Ballot measure name"
    )
    bal_num = fields.CharField(
        max_length=7,
        db_column='BAL_NUM',
        blank=True,
        help_text="Ballot measure number"
    )
    bal_juris = fields.CharField(
        max_length=40,
        db_column='BAL_JURIS',
        blank=True,
        help_text="Ballot measure jurisdiction"
    )
    memo_code = fields.CharField(
        max_length=1,
        db_column='MEMO_CODE',
        blank=True,
        help_text="Memo amount flag"
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text="Reference to text contained in TEXT code"
    )
    bal_id = fields.CharField(
        max_length=9,
        db_column='BAL_ID',
        blank=True,
        help_text="This field is undocumented"
    )
    cand_id = fields.CharField(
        max_length=9,
        db_column='CAND_ID',
        blank=True,
        help_text="This field is undocumented"
    )
    sup_off_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OFF_CD',
        blank=True,
        help_text="This field is undocumented"
    )
    SUP_OPP_CD_CHOICES = get_sorted_choices(choices.SUP_OPP_CODES)
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text="Support or opposition code",
        choices=SUP_OPP_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=82),
        ]
    )

    def __str__(self):
        return "{} Filing {}, Amendment {}".format(
            self.get_form_type_display(),
            self.filing_id,
            self.amend_id
        )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'S497_CD'
        ordering = ("-ctrib_date",)


@python_2_unicode_compatible
class S498Cd(CalAccessBaseModel):
    """
    Payments received by slate-mailer organizations in the 90 days before an election.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE",
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=12),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=127, end_page=129),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=83, end_page=85),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=43, end_page=44),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=56, end_page=57),
    ]
    FILING_FORMS = [
        get_filing_form('F498').get_section('A'),
        get_filing_form('F498').get_section('R'),
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
        ("S498", "S498"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        help_text="Record Type Value: S498",
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=43),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=56),
        ]
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        max_length=9,
        db_column='FORM_TYPE',
        blank=True,
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=43),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=56),
        ]
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )
    ENTITY_CD_CHOICES = (
        ('CAO', choices.CAMPAIGN_ENTITY_CODES['CAO']),
        ('COM', choices.CAMPAIGN_ENTITY_CODES['COM']),
        ('IND', choices.CAMPAIGN_ENTITY_CODES['IND']),
        ('OTH', choices.CAMPAIGN_ENTITY_CODES['OTH']),
        ('RCP', choices.CAMPAIGN_ENTITY_CODES['RCP']),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        help_text="Entity code",
        choices=ENTITY_CD_CHOICES,
        documentcloud_pages=choices.DOCS['entity_codes'] + [
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=43),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=56),
        ]
    )
    cmte_id = fields.CharField(
        max_length=9,
        db_column='CMTE_ID',
        blank=True,
        verbose_name="Committee ID",
        help_text="Committee identification number"
    )
    payor_naml = fields.CharField(
        max_length=200,
        db_column='PAYOR_NAML',
        blank=True,
        help_text="Payor's last name or business name"
    )
    payor_namf = fields.CharField(
        max_length=45,
        db_column='PAYOR_NAMF',
        blank=True,
        help_text="Payor's first name."
    )
    payor_namt = fields.CharField(
        max_length=10,
        db_column='PAYOR_NAMT',
        blank=True,
        help_text="Payor's Prefix or title."
    )
    payor_nams = fields.CharField(
        max_length=10,
        db_column='PAYOR_NAMS',
        blank=True,
        help_text="Payor's suffix."
    )
    payor_city = fields.CharField(
        max_length=30,
        db_column='PAYOR_CITY',
        blank=True,
        help_text="Payor's city."
    )
    payor_st = fields.CharField(
        max_length=2,
        db_column='PAYOR_ST',
        blank=True,
        help_text="Payor's State."
    )
    payor_zip4 = fields.CharField(
        max_length=10,
        db_column='PAYOR_ZIP4',
        blank=True,
        help_text="Payor's zip code"
    )
    date_rcvd = fields.DateField(
        db_column='DATE_RCVD',
        null=True,
        help_text="Date received"
    )
    amt_rcvd = fields.DecimalField(
        max_digits=16,
        decimal_places=2,
        db_column='AMT_RCVD',
        help_text="Amount received"
    )
    cand_naml = fields.CharField(
        max_length=200,
        db_column='CAND_NAML',
        blank=True,
        help_text="Candidate/officerholder last name"
    )
    cand_namf = fields.CharField(
        max_length=45,
        db_column='CAND_NAMF',
        blank=True,
        help_text="Candidate/officerholder first name"
    )
    cand_namt = fields.CharField(
        max_length=10,
        db_column='CAND_NAMT',
        blank=True,
        help_text="Candidate/officerholder title or prefix"
    )
    cand_nams = fields.CharField(
        max_length=10,
        db_column='CAND_NAMS',
        blank=True,
        help_text="Candidate/officerholder suffix"
    )
    OFFICE_CD_CHOICES = get_sorted_choices(choices.OFFICE_CODES) + (
        ('gov', choices.OFFICE_CODES['GOV']),
        ('oth', choices.OFFICE_CODES['OTH']),
    )
    office_cd = fields.CharField(
        db_column='OFFICE_CD',
        max_length=4,
        blank=True,
        verbose_name="office code",
        choices=OFFICE_CD_CHOICES,
        help_text="Identifies the office being sought",
        documentcloud_pages=choices.DOCS['office_codes'],
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Description of office sought"
    )
    JURIS_CD_CHOICES = get_sorted_choices(choices.JURIS_CODES) + (
        ('GOV', choices.JURIS_CODES['STW']),
        ('COU', choices.JURIS_CODES['CTY']),
    )
    juris_cd = fields.CharField(
        max_length=3,
        db_column='JURIS_CD',
        blank=True,
        choices=JURIS_CD_CHOICES,
        help_text="Office jurisdiction code",
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=43),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=57),
        ]
    )
    juris_dscr = fields.CharField(
        max_length=40,
        db_column='JURIS_DSCR',
        blank=True,
        help_text="Office jurisdiction description"
    )
    dist_no = fields.CharField(
        max_length=3,
        db_column='DIST_NO',
        blank=True,
        help_text="District number for the office being sought. \
Populated for Senate, Assembly, or Board of Equalization races."
    )
    OFF_S_H_CD_CHOICES = get_sorted_choices(choices.OFF_S_H_CODES)
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text='Office is sought or held code',
        choices=OFF_S_H_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=44),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=57),
        ]
    )
    bal_name = fields.CharField(
        max_length=200,
        db_column='BAL_NAME',
        blank=True,
        help_text="Ballot measure name"
    )
    bal_num = fields.CharField(
        max_length=7,
        db_column='BAL_NUM',
        blank=True,
        help_text="Ballot measure number or letter."
    )
    bal_juris = fields.CharField(
        max_length=40,
        db_column='BAL_JURIS',
        blank=True,
        help_text="Jurisdiction of ballot measure"
    )
    SUP_OPP_CD_CHOICES = get_sorted_choices(choices.SUP_OPP_CODES)
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text="Support or opposition code",
        choices=SUP_OPP_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=43),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=57),
        ]
    )
    amt_attrib = fields.DecimalField(
        max_digits=16,
        decimal_places=2,
        db_column='AMT_ATTRIB',
        help_text="Amount attributed (only if Form_type = 'F498-A')"
    )
    memo_code = fields.CharField(
        max_length=1,
        db_column='MEMO_CODE',
        blank=True,
        help_text="Memo amount flat"
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text='Reference text contained in TEXT record'
    )
    employer = fields.CharField(
        max_length=200,
        db_column='EMPLOYER',
        blank=True,
        help_text="This field is undocumented"
    )
    occupation = fields.CharField(
        max_length=60,
        db_column='OCCUPATION',
        blank=True,
        help_text='This field is undocumented'
    )
    selfemp_cb = fields.CharField(
        max_length=1,
        db_column='SELFEMP_CB',
        blank=True,
        help_text='Self-employed checkbox'
    )

    def __str__(self):
        return str(self.filing_id)

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'S498_CD'
        ordering = ("-date_rcvd",)


@python_2_unicode_compatible
class F501502Cd(CalAccessBaseModel):
    """
    Candidate intention statements.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=8),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=57, end_page=59),
    ]
    FILING_FORMS = [
        get_filing_form('F501'),
        get_filing_form('F502'),
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
        ("CVR", "CVR"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        help_text="Record Type",
        documentcloud_pages=[
            DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=58),
        ]
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=4,
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=58),
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
    committee_id = fields.CharField(
        db_column='COMMITTEE_ID',
        max_length=9,
        blank=True,
        verbose_name="Committee ID",
        help_text='Committee identification number'
    )
    ENTITY_CD_CHOICES = get_sorted_choices(choices.CAMPAIGN_ENTITY_CODES) + (
        ('8', 'Unknown'),
    )
    entity_cd = fields.CharField(
        db_column='ENTITY_CD',
        choices=ENTITY_CD_CHOICES,
        blank=True,
        max_length=9,
        help_text='Entity code',  # Not clear which values are valid
        documentcloud_pages=choices.DOCS['entity_codes'],
    )
    report_num = fields.CharField(
        db_column='REPORT_NUM',
        blank=True,
        null=True,
        max_length=3,
        help_text='Report Number; 000 Original; 001-999 Amended'
    )
    rpt_date = fields.DateField(
        db_column='RPT_DATE',
        blank=True,
        null=True,
        help_text='date this report is filed'
    )
    STMT_TYPE_CHOICES = (
        (10001, 'ORIGINAL/INITIAL'),
        (10002, 'AMENDMENT'),
        (10003, 'TERMINATION'),
        (10004, 'REDESIGNATE THE ACCOUNT FOR FUTURE ELECTION TO THE SAME OFFICE'),
        (10005, 'LOG'),
        (10006, 'LOG/AMENDMENT'),
        (10007, 'AS FILED BY COMMITTEE')
    )
    stmt_type = fields.IntegerField(
        db_column='STMT_TYPE',
        verbose_name="statement type",
        choices=STMT_TYPE_CHOICES,
        help_text='Type of statement',
        documentcloud_pages=[
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=6)
        ],
    )
    from_date = fields.CharField(
        db_column='FROM_DATE',
        max_length=32,
        blank=True,
        help_text='Reporting period from date'
    )
    thru_date = fields.CharField(
        db_column='THRU_DATE',
        max_length=32,
        blank=True,
        help_text="Reporting period through date"
    )
    elect_date = fields.CharField(
        db_column='ELECT_DATE',
        max_length=32,
        blank=True,
        help_text='Date of election'
    )
    cand_naml = fields.CharField(
        db_column='CAND_NAML',
        max_length=200,
        blank=True,
        help_text="Candidate/officerholder last name"
    )
    cand_namf = fields.CharField(
        db_column='CAND_NAMF',
        max_length=45,
        blank=True,
        help_text="Candidate/officerholder first name"
    )
    can_namm = fields.CharField(
        db_column='CAN_NAMM',
        max_length=20,
        blank=True,
        help_text='Candidate/officeholder middle name'
    )
    cand_namt = fields.CharField(
        db_column='CAND_NAMT',
        max_length=100,
        blank=True,
        help_text="Candidate/officerholder title or prefix"
    )
    cand_nams = fields.CharField(
        db_column='CAND_NAMS',
        max_length=10,
        blank=True,
        help_text="Candidate/officeholder suffix"
    )
    moniker_pos = fields.CharField(
        db_column='MONIKER_POS',
        max_length=32,
        blank=True,
        help_text="Location of the candidate/officeholder's moniker"
    )
    moniker = fields.CharField(
        db_column='MONIKER',
        max_length=20,
        blank=True,
        help_text="Candidate/officeholder's moniker"
    )
    cand_city = fields.CharField(
        db_column='CAND_CITY',
        max_length=30,
        blank=True,
        help_text="Candidate/officerholder city"
    )
    cand_st = fields.CharField(
        db_column='CAND_ST',
        max_length=4,
        blank=True,
        help_text='Candidate/officeholder state'
    )
    cand_zip4 = fields.CharField(
        db_column='CAND_ZIP4',
        max_length=10,
        blank=True,
        help_text='Candidate/officeholder zip +4'
    )
    cand_phon = fields.CharField(
        db_column='CAND_PHON',
        max_length=20,
        blank=True,
        help_text='Candidate/officeholder phone number'
    )
    cand_fax = fields.CharField(
        db_column='CAND_FAX',
        max_length=20,
        blank=True,
        help_text="Candidate/officerholder fax"
    )
    cand_email = fields.CharField(
        db_column='CAND_EMAIL',
        max_length=60,
        blank=True,
        help_text='Candidate/officeholder email address'
    )
    fin_naml = fields.CharField(
        db_column='FIN_NAML',
        max_length=200,
        blank=True,
        help_text="Financial institution's business name"
    )
    fin_namf = fields.CharField(
        db_column='FIN_NAMF',
        max_length=45,
        blank=True,
        help_text="Unused. Financial institution's first name."
    )
    fin_namt = fields.CharField(
        db_column='FIN_NAMT',
        max_length=100,
        blank=True,
        help_text="Unused. Financial institution's title."
    )
    fin_nams = fields.CharField(
        db_column='FIN_NAMS',
        max_length=32,
        blank=True,
        help_text="Unused. Financial institution's suffix."
    )
    fin_city = fields.CharField(
        db_column='FIN_CITY',
        max_length=30,
        blank=True,
        help_text="Financial institution's city."
    )
    fin_st = fields.CharField(
        db_column='FIN_ST',
        max_length=4,
        blank=True,
        help_text="Financial institution's state."
    )
    fin_zip4 = fields.CharField(
        db_column='FIN_ZIP4',
        max_length=10,
        blank=True,
        help_text="Financial institution's zip code."
    )
    fin_phon = fields.CharField(
        db_column='FIN_PHON',
        max_length=20,
        blank=True,
        help_text="Financial institution's phone number."
    )
    fin_fax = fields.CharField(
        db_column='FIN_FAX',
        max_length=20,
        blank=True,
        help_text="Financial institution's FAX Number."
    )
    fin_email = fields.CharField(
        db_column='FIN_EMAIL',
        max_length=60,
        blank=True,
        help_text="Financial institution's e-mail address."
    )
    OFFICE_CD_CHOICES = (
        (0, "N/A"),
        (30001, "PRESIDENT"),
        (30002, "GOVERNOR"),
        (30003, "LIEUTENANT GOVERNOR"),
        (30004, "SECRETARY OF STATE"),
        (30005, "CONTROLLER"),
        (30006, "TREASURER"),
        (30007, "ATTORNEY GENERAL"),
        (30008, "SUPERINTENDENT OF PUBLIC INSTRUCTION"),
        (30009, "MEMBER BOARD OF EQUALIZATION"),
        (30010, "OXNARD HARBOR COMMISSIONER"),
        (30011, "CITY CONTROLLER"),
        (30012, "STATE SENATE"),
        (30013, "ASSEMBLY"),
        (30014, "INSURANCE COMMISSIONER"),
        (30015, "JUDGE"),
        (30016, "BOARD MEMBER"),
        (30017, "TAX COLLECTOR"),
        (30018, "TRUSTEE"),
        (30019, "SUPERVISOR"),
        (30020, "SHERIFF"),
        (30021, "CORONER"),
        (30022, "MARSHALL"),
        (30023, "CITY CLERK"),
        (30024, "SCHOOL BOARD"),
        (30025, "HARBOR COMMISSIONER"),
        (30026, "DISTRICT ATTORNEY"),
        (30027, "COUNTY CLERK"),
        (30028, "AUDITOR"),
        (30029, "MAYOR"),
        (30030, "CITY ATTORNEY"),
        (30031, "DEMOCRATIC COUNTY CENTRAL COMMITTEE"),
        (30032, "TOWN COUNCIL"),
        (30033, "ASSESSOR"),
        (30034, "CITY TREASURER"),
        (30035, "CITY COUNCIL"),
        (30036, "COMMISSIONER"),
        (30037, "REPUBLICAN COUNTY CENTRAL COMMITTEE"),
        (30038, "DIRECTOR"),
        (30039, "DIRECTOR OF ZONE 7"),
        (30040, "COMMUNITY COLLEGE BOARD"),
        (30041, "POLICE CHIEF"),
        (30042, "CHIEF OF POLICE"),
        (30043, "CENTRAL COMMITTEE"),
        (30044, "BOARD OF EDUCATION"),
        (30045, "BOARD OF DIRECTORS"),
        (30046, "COLLEGE BOARD"),
        (30047, "BART BOARD DIRECTOR"),
        (30048, "BOARD OF TRUSTEES"),
        (30049, "IRRIGATION"),
        (30050, "WATER BOARD"),
        (30051, "COMMUNITY PLANNING GROUP"),
        (30052, "BOARD OF SUPERVISORS"),
        (30053, "SUPERIOR COURT JUDGE"),
        (30054, "DISTRICT ATTORNEY/PUBLIC DEFENDER"),
        (30055, "MEASURE"),
        (30056, "CITY PROSECUTOR"),
        (30057, "SUPREME COURT JUDGE"),
        (30058, "PUBLIC EMPLOYEES RETIREMENT BOARD"),
        (30059, "APPELLATE COURT JUDGE"),
        (50001, "Ag"),
        (50002, "Assembly"),
        (50003, "Assessor"),
        (50004, "Assessor/Clerk/Recorder"),
        (50005, "Assessor/County Clerk/Recorder"),
        (50006, "Assessor/Recorder"),
        (50007, "Associate Justice"),
        (50008, "Auditor"),
        (50009, "Auditor/Controller"),
        (50010, "Auditor/Controller/Clerk/Recorder"),
        (50011, "Auditor/Controller/Recorder"),
        (50012, "Auditor/Controller/Treasurer/Tax Collector"),
        (50013, "Auditor/Recorder"),
        (50014, "Board Member"),
        (50015, "Board Of Director"),
        (50016, "Board Of Supervisor"),
        (50017, "Boe"),
        (50018, "Chief Justice"),
        (50019, "City"),
        (50020, "City Attorney"),
        (50021, "City Auditor"),
        (50022, "City Clerk"),
        (50023, "City Council"),
        (50024, "City Of Los Angeles"),
        (50025, "City Of South El Monte"),
        (50026, "City Prosecutor"),
        (50027, "City Treasurer"),
        (50028, "Clerk/Auditor"),
        (50029, "Clerk/Record/Public Admin"),
        (50030, "Clerk/Recorder"),
        (50031, "Clerk/Recorder/Registar"),
        (50032, "Clerk/Recorder/Registrar"),
        (50033, "Commissioner"),
        (50034, "Controller"),
        (50035, "Costa Mesa"),
        (50036, "Council Member"),
        (50037, "County Clerk"),
        (50038, "County Clerk/Auditor"),
        (50039, "County Clerk/Auditor/Controller"),
        (50040, "County Clerk/Recorder"),
        (50041, "County Clerk/Recorder/Assessor"),
        (50042, "County Clerk/Recorder/Public Admin"),
        (50043, "Democratic County Central Committee"),
        (50044, "Director"),
        (50045, "District Attorney"),
        (50046, "District Attorney/Public Administrator"),
        (50047, "Gccc"),
        (50048, "Governor"),
        (50049, "Harbor Commissioner"),
        (50050, "Ic"),
        (50051, "Irrigation Dist"),
        (50052, "Judge"),
        (50053, "Justice"),
        (50054, "Legislature"),
        (50055, "Lieutenant Governor"),
        (50056, "Mayor"),
        (50057, "N/A"),
        (50058, "Placentia"),
        (50059, "Public Administrator"),
        (50060, "Public Administrator/Guardian"),
        (50061, "Rent Stabilization Board"),
        (50062, "Republican Central Committee"),
        (50063, "San Francisco Dccc"),
        (50064, "Sanger"),
        (50065, "School Board"),
        (50066, "Secretary Of State"),
        (50067, "Senator"),
        (50068, "Sheriff"),
        (50069, "Sheriff/Coroner"),
        (50070, "Sheriff/Coroner/Marshall"),
        (50071, "Sheriff/Coroner/Public Administrator"),
        (50072, "Solana Beach"),
        (50073, "Superintendent"),
        (50074, "Supervisor"),
        (50075, "Supt Of Schools"),
        (50076, "Tax Collector"),
        (50077, "Town Council"),
        (50078, "Treasurer"),
        (50079, "Treasurer/Tax Collector"),
        (50080, "Treasurer/Tax Collector/Clerk"),
        (50081, "Treasurer/Tax Collector/Public Administrator"),
        (50082, "Treasurer/Tax Collector/Public Administrator/County Clerk"),
        (50083, "Treasurer/Tax Collector/Recorder"),
        (50084, "Trustee"),
        (50085, "Weed Recreation Board Member"),
    )
    office_cd = fields.IntegerField(
        db_column='OFFICE_CD',
        verbose_name="office code",
        help_text="Identifies the office being sought",
        choices=OFFICE_CD_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=20, end_page=22),
        ]
    )
    offic_dscr = fields.CharField(
        db_column='OFFIC_DSCR',
        max_length=80,
        blank=True,
        help_text="Office sought description"
    )
    agency_nam = fields.CharField(
        db_column='AGENCY_NAM',
        max_length=200,
        blank=True,
        help_text="Agency name"
    )
    JURIS_CD_CHOICES = (
        (0, "N/A"),
        (40501, "LOCAL"),
        (40502, "STATE"),
        (40503, "COUNTY"),
        (40504, "MULTI-COUNTY"),
        (40505, "CITY"),
        (40507, "SUPERIOR COURT JUDGE"),
    )
    juris_cd = fields.IntegerField(
        db_column='JURIS_CD',
        blank=True,
        null=True,
        choices=JURIS_CD_CHOICES,
        help_text='Office jurisdiction code',
        documentcloud_pages=[
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=19, end_page=20),
        ]
    )
    juris_dscr = fields.CharField(
        db_column='JURIS_DSCR',
        max_length=30,
        blank=True,
        help_text='office jurisdiction description'
    )
    dist_no = fields.CharField(
        db_column='DIST_NO',
        max_length=4,
        blank=True,
        help_text='District number for the office being sought. \
Populated for Senate, Assembly or Board of Equalization races.'
    )
    party = fields.CharField(
        db_column='PARTY',
        max_length=200,
        blank=True,
        help_text="Political party"
    )
    yr_of_elec = fields.IntegerField(
        db_column='YR_OF_ELEC',
        blank=True,
        null=True,
        help_text='Year of election'
    )
    ELEC_TYPE_CHOICES = (
        (0, 'N/A'),
        (3001, "GENERAL"),
        (3002, "PRIMARY"),
        (3003, "RECALL"),
        (3004, "SPECIAL ELECTION"),
        (3005, "OFFICEHOLDER"),
        (3006, "SPECIAL RUNOFF"),
        # Observed in this field, but not documented
        (3007, "UNKNOWN"),
    )
    elec_type = fields.IntegerField(
        db_column='ELEC_TYPE',
        blank=True,
        null=True,
        verbose_name="Election type",
        choices=ELEC_TYPE_CHOICES,
        help_text="Election type",
        documentcloud_pages=[
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=3, end_page=4),
        ]
    )
    execute_dt = fields.DateField(
        db_column='EXECUTE_DT',
        blank=True,
        null=True,
        help_text='Execution date'
    )
    can_sig = fields.CharField(
        db_column='CAN_SIG',
        max_length=200,
        blank=True,
        help_text='Candidate signature'
    )
    account_no = fields.CharField(
        db_column='ACCOUNT_NO',
        max_length=32,
        blank=True,
        help_text='Account number'
    )
    acct_op_dt = fields.DateField(
        db_column='ACCT_OP_DT',
        blank=True,
        null=True,
        help_text='Account open date'
    )
    PARTY_CD_CHOICES = (
        (0, 'N/A'),
        (16001, 'DEMOCRATIC'),
        (16002, 'REPUBLICAN'),
        (16003, 'GREEN PARTY'),
        (16004, 'REFORM PARTY'),
        (16005, 'AMERICAN INDEPENDENT PARTY'),
        (16006, 'PEACE AND FREEDOM'),
        (16007, 'INDEPENDENT'),
        (16008, 'LIBERTARIAN'),
        (16009, 'NON PARTISAN'),
        (16010, 'NATURAL LAW'),
        (16011, 'UNKNOWN'),
        (16012, 'NO PARTY PREFERENCE'),
        (16013, 'AMERICANS ELECT'),
        (16014, 'UNKNOWN'),
        (16020, 'PEACE AND FREEDOM'),
    )
    party_cd = fields.IntegerField(
        db_column='PARTY_CD',
        blank=True,
        null=True,
        choices=PARTY_CD_CHOICES,
        help_text="Party code",
        documentcloud_pages=[
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=10, end_page=11),
        ]
    )
    DISTRICT_CD_CHOICES = (
        (0, 'N/A'),
        (17001, '01'),
        (17002, '13'),
        (17003, '24'),
        (17004, '35'),
        (17005, '46'),
        (17006, '57'),
        (17007, '68'),
        (17008, '79'),
        (17009, '02'),
        (17010, '05'),
        (17011, '04'),
        (17013, '06'),
        (17014, '07'),
        (17015, '08'),
        (17016, '19'),
        (17017, '10'),
        (17018, '11'),
        (17019, '12'),
        (17020, '14'),
        (17021, '15'),
        (17022, '16'),
        (17023, '17'),
        (17024, '18'),
        (17026, '20'),
        (17027, '21'),
        (17028, '22'),
        (17029, '23'),
        (17030, '25'),
        (17031, '26'),
        (17032, '27'),
        (17033, '28'),
        (17034, '29'),
        (17035, '30'),
        (17036, '31'),
        (17037, '32'),
        (17038, '33'),
        (17039, '34'),
        (17040, '36'),
        (17041, '37'),
        (17042, '38'),
        (17043, '39'),
        (17044, '40'),
        (17045, '41'),
        (17046, '42'),
        (17047, '43'),
        (17048, '44'),
        (17049, '45'),
        (17050, '47'),
        (17051, '48'),
        (17052, '49'),
        (17053, '50'),
        (17054, '51'),
        (17055, '52'),
        (17056, '53'),
        (17057, '54'),
        (17058, '55'),
        (17059, '56'),
        (17060, '03'),
        (17061, '59'),
        (17062, '60'),
        (17063, '61'),
        (17064, '62'),
        (17065, '63'),
        (17066, '64'),
        (17067, '65'),
        (17068, '66'),
        (17069, '67'),
        (17070, '69'),
        (17071, '70'),
        (17072, '71'),
        (17073, '72'),
        (17074, '73'),
        (17075, '74'),
        (17076, '75'),
        (17077, '76'),
        (17078, '77'),
        (17079, '78'),
        (17080, '80'),
        (17081, '09'),
        (17090, '58'),
        (17012, 'Unknown'),
        (17082, 'Unknown'),
        (17025, 'Unknown'),
    )
    district_cd = fields.IntegerField(
        db_column='DISTRICT_CD',
        blank=True,
        null=True,
        choices=DISTRICT_CD_CHOICES,
        help_text='District number for the office being sought. \
Populated for Senate, Assembly, or Board of Equalization races.',
        documentcloud_pages=[
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=11, end_page=13),
        ]
    )
    accept_limit_yn = fields.IntegerField(
        db_column='ACCEPT_LIMIT_YN',
        blank=True,
        null=True,
        help_text='This field is undocumented'
    )
    did_exceed_dt = fields.DateField(
        db_column='DID_EXCEED_DT',
        blank=True,
        null=True,
        help_text='This field is undocumented'
    )
    cntrb_prsnl_fnds_dt = fields.DateField(
        db_column='CNTRB_PRSNL_FNDS_DT',
        blank=True,
        null=True,
        help_text="This field is undocumented"
    )

    def __str__(self):
        return str(self.filing_id)

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'F501_502_CD'
        ordering = ("-rpt_date",)
