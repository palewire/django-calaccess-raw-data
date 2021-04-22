#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Models for storing common tables from the CAL-ACCESS database.
"""
# Models
from django.db import models
from calaccess_raw import fields
from .base import CalAccessBaseModel

# Annotations
from calaccess_raw import annotations
from calaccess_raw.annotations import DocumentCloud


class FilernameCd(CalAccessBaseModel):
    """
    A combination of CAL-ACCESS tables created by the state to consolidate filer information.
    """
    UNIQUE_KEY = ("FILER_ID",)
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711615', start_page=2),
    ]
    xref_filer_id = fields.CharField(
        verbose_name='crossreference filer ID',
        max_length=15,
        db_column='XREF_FILER_ID',
        db_index=True,
        help_text="alternative filer ID found on many forms"
    )
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        db_index=True,
        null=True,
        help_text="filer's unique identification number"
    )
    FILER_TYPE_CHOICES = (
        ('NOT DEFINED', 'Undefined'),
        ('ALL FILERS', 'All filers'),
        ('CANDIDATE/OFFICEHOLDER', 'Candidate/officeholder'),
        ('CLIENT', 'Client'),
        ('EMPLOYER', 'Employer'),
        ('FIRM', 'Firm'),
        ('INDIVIDUAL', 'Individual'),
        ('INITIATIVE', 'Initiative'),
        ('LOBBYIST', 'Lobbyist'),
        (
            'MAJOR DONOR/INDEPENDENT EXPENDITURE COMMITTEE',
            'Major donor or indenpendent expenditure committee'
        ),
        ('PAYMENT TO INFLUENCE', 'Payment to influence'),
        ('PREPAID ACCOUNT', 'Prepaid account'),
        ('PROPONENT', 'Proponent'),
        ('PROPOSITION', 'Proposition'),
        ('RECIPIENT COMMITTEE', 'Recipient committee'),
        ('SLATE MAILER ORGANIZATIONS', 'Slate mailer organization'),
        (
            'TREASURER/RESPONSIBLE OFFICER',
            'Treasurer/responsible officer'
        )
    )
    filer_type = fields.CharField(
        max_length=45,
        db_column='FILER_TYPE',
        db_index=True,
        choices=FILER_TYPE_CHOICES,
        help_text='The type of filer. These values are found FILER_TYPES_CD.DESCRIPTION',
        documentcloud_pages=[
            DocumentCloud(id='2774536', start_page=1),
        ],
    )
    STATUS_CHOICES = (
        ('', 'Undefined'),
        ('A', 'ACTIVE'),
        ('P', 'PENDING'),
        ('R', 'REVOKED'),
        ('S', 'SUSPENDED'),
        ('W', 'WITHDRAWN'),
        ('Y', 'ACTIVE'),
        ('N', 'INACTIVE'),
        ('T', 'TERMINATED'),
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE'),
        ('TERMINATED', 'TERMINATED'),
    )
    status = fields.CharField(
        max_length=10,
        db_column='STATUS',
        db_index=True,
        choices=STATUS_CHOICES,
        blank=True,
        help_text='The status of the filer. Includes a mixture of values found \
in the STATUS_TYPE and STATUS_DESC columns on FILER_STATUS_TYPES_CD',
        documentcloud_pages=[
            DocumentCloud(id='2774537', start_page=1)
        ]
    )
    effect_dt = fields.DateField(
        db_column='EFFECT_DT',
        help_text="effective date for status",
        null=True,
    )
    naml = fields.CharField(
        max_length=200,
        db_column='NAML',
        help_text="Last name, sometimes full name in the case of PACs, firms and employers. \
Major donors can be split between first and last name fields, but usually \
are contained in the last name field only. Individual names of lobbyists, \
politicans and officers tend to use both the first and last name."
    )
    namf = fields.CharField(
        max_length=55,
        db_column='NAMF',
        blank=True,
        help_text="First name"
    )
    namt = fields.CharField(
        max_length=70,
        db_column='NAMT',
        blank=True,
        help_text="Name prefix or title"
    )
    nams = fields.CharField(
        max_length=32,
        db_column='NAMS',
        blank=True,
        help_text="Name suffix"
    )
    adr1 = fields.CharField(
        max_length=200,
        db_column='ADR1',
        blank=True,
        help_text="First line of street address"
    )
    adr2 = fields.CharField(
        max_length=200,
        db_column='ADR2',
        blank=True,
        help_text="Second line of street address"
    )
    city = fields.CharField(
        max_length=55,
        db_column='CITY',
        blank=True,
        help_text="City address"
    )
    st = fields.CharField(
        max_length=4,
        db_column='ST',
        blank=True,
        help_text="State",
    )
    zip4 = fields.CharField(
        max_length=10,
        db_column='ZIP4',
        blank=True,
        help_text="ZIP Code"
    )
    phon = fields.CharField(
        max_length=60,
        db_column='PHON',
        blank=True,
        verbose_name="Phone",
        help_text="Phone number"
    )
    fax = fields.CharField(
        max_length=60,
        db_column='FAX',
        blank=True,
        help_text="Fax number"
    )
    email = fields.CharField(
        max_length=60,
        db_column='EMAIL',
        blank=True,
        help_text="Email address"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILERNAME_CD'
        ordering = ("naml", "namf",)

    def __str__(self):
        return str(self.filer_id)


class FilerFilingsCd(CalAccessBaseModel):
    """
    An index that links filers to their filings.
    """
    UNIQUE_KEY = (
        "FILER_ID",
        "FILING_ID",
        "FORM_ID",
        "FILING_SEQUENCE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=8),
        DocumentCloud(id='2711614', start_page=64, end_page=66),
    ]
    FILING_FORMS = annotations.FORMS
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        db_index=True,
        null=True,
        help_text="Filer's unique identification number"
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
    )
    period_id = fields.IntegerField(
        null=True,
        db_column='PERIOD_ID',
        blank=True,
        help_text="Identifies the period when the filing was recieved."
    )
    FORM_ID_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS]) + (
        # for unknown values see
        # https://github.com/california-civic-data-coalition/django-calaccess-raw-data/issues/1459
        ('F111', 'Unknown'),
        ('F410 AT', 'Unknown'),
        ('F410ATR', 'Unknown'),
        ('F421', 'Unknown'),
        ('F440', 'Unknown'),
        ('F470S', annotations.get_form('F470').full_title),
        ('F480', 'Unknown'),
        ('F500', 'Unknown'),
        ('F501502', 'Forms 501 and/or 502 (Candidate Intention and/or Bank Account Statements)'),
        ('F555', 'Unknown'),
        ('F666', 'Unknown'),
        ('F777', 'Unknown'),
        ('F888', 'Unknown'),
        ('F999', 'Unknown'),
    )
    form_id = fields.CharField(
        max_length=7,
        db_column='FORM_ID',
        db_index=True,
        verbose_name='form type',
        choices=FORM_ID_CHOICES,
        help_text="Form identification code",
        documentcloud_pages=[
            DocumentCloud(id='2711614', start_page=65),
        ]
    )
    filing_sequence = fields.IntegerField(
        db_column='FILING_SEQUENCE',
        db_index=True,
        help_text="Amendment number where 0 is an original filing and 1 to \
999 are amendments"
    )
    filing_date = fields.DateField(
        db_column='FILING_DATE',
        help_text="Date the filing entered into the system",
        null=True
    )
    STMNT_TYPE_CHOICES = (
        (0, 'N/A'),
        (10001, 'ORIGINAL/INITIAL'),
        (10002, 'AMENDMENT'),
        (10003, 'TERMINATION'),
        (10004, 'REDESIGNATE THE ACCOUNT FOR FUTURE ELECTION TO THE SAME OFFICE'),
        (10005, 'LOG'),
        (10006, 'LOG/AMENDMENT'),
        (10007, 'AS FILED BY COMMITTEE'),
    )
    stmnt_type = fields.IntegerField(
        db_column='STMNT_TYPE',
        verbose_name="statement type",
        db_index=True,
        choices=STMNT_TYPE_CHOICES,
        help_text="Type of statement",
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=6),
        ]
    )
    STMNT_STATUS_CHOICES = (
        (11001, 'COMPLETE'),
        (11002, 'INCOMPLETE'),
        (11003, 'NEEDS REVIEW'),
    )
    stmnt_status = fields.IntegerField(
        db_column='STMNT_STATUS',
        db_index=True,
        null=True,
        help_text="The status of the statement. If the filing has been \
reviewed or not reviewed.",
        verbose_name='statement status',
        choices=STMNT_STATUS_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=6),
        ]
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    user_id = fields.CharField(
        max_length=12,
        db_column='USER_ID',
        verbose_name="user ID",
        help_text="User identifier of the PRD user who logged the filing"
    )
    special_audit = fields.IntegerField(
        null=True,
        db_column='SPECIAL_AUDIT',
        blank=True,
        help_text="Denotes whether the filing has been audited for money \
laundering or other special condition."
    )
    fine_audit = fields.IntegerField(
        null=True,
        db_column='FINE_AUDIT',
        blank=True,
        help_text="Indicates whether a filing has been audited for a fine"
    )
    rpt_start = fields.DateField(
        null=True,
        db_column='RPT_START',
        blank=True,
        help_text="Starting date for the period the filing represents",
    )
    rpt_end = fields.DateField(
        null=True,
        db_column='RPT_END',
        blank=True,
        help_text="Ending date for the period the filing represents",
    )
    rpt_date = fields.DateField(
        null=True,
        db_column='RPT_DATE',
        blank=True,
        help_text="Date filing received",
    )
    FILING_TYPE_CHOICES = (
        (0, 'N/A'),
        (22001, 'Electronic'),
        (22006, 'Cal Online'),
    )
    filing_type = fields.IntegerField(
        db_column='FILING_TYPE',
        null=True,
        blank=True,
        choices=FILING_TYPE_CHOICES,
        help_text="The type of filing",
        documentcloud_pages=[
            DocumentCloud(id='2711615', start_page=2),
        ],
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILER_FILINGS_CD'

    def __str__(self):
        return str("%s %s" % (self.filer_id, self.filing_id))


class FilingsCd(CalAccessBaseModel):
    """
    All links and associations to a filing.
    """
    UNIQUE_KEY = "FILING_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=10),
        DocumentCloud(id='2711614', start_page=75),
    ]
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=75, end_page=75),
    ]
    FILING_TYPE_CHOICES = (
        (22001, 'Electronic'),
        (22002, 'Key data entry'),
        (22003, 'Historical lobby'),
        (22004, 'Historical campaign'),
        (22005, 'AMS'),
        (22006, 'Cal Online'),
    )
    filing_type = fields.IntegerField(
        db_column='FILING_TYPE',
        db_index=True,
        choices=FILING_TYPE_CHOICES,
        help_text="The type of filing",
        documentcloud_pages=[
            DocumentCloud(id='2711615', start_page=2),
        ],
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILINGS_CD'
        ordering = ("-filing_id",)

    def __str__(self):
        return str("{} ({})".format(self.filing_id, self.get_filing_type_display()))


class HdrCd(CalAccessBaseModel):
    """
    Electronic-filing headers with vendor and CalFormat version.
    """
    UNIQUE_KEY = ("FILING_ID", "AMEND_ID")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=10),
        DocumentCloud(id='2711614', start_page=79),
        DocumentCloud(id='2711616', start_page=1),
        DocumentCloud(id='2711616', start_page=51),
        DocumentCloud(id='2712033', start_page=4),
        DocumentCloud(id='2712034', start_page=5),
    ]
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    cal_ver = fields.CharField(
        max_length=4,
        db_column='CAL_VER',
        blank=True,
        help_text="CAL Version number the filing was made using"
    )
    EF_TYPE_CHOICES = (
        ('CAL', '.CAL format'),
    )
    ef_type = fields.CharField(
        max_length=3,
        choices=EF_TYPE_CHOICES,
        db_column='EF_TYPE',
        blank=True,
        help_text='Electronic filing type. This will always have the \
        value of "CAL".',
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=4),
            DocumentCloud(id='2712034', start_page=5),
        ]
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
    )
    hdr_comment = fields.CharField(
        max_length=200,
        db_column='HDRCOMMENT',
        blank=True,
        verbose_name="Header comment",
        help_text="Typically used for development and test filings"
    )
    REC_TYPE_CHOICES = (
        ("HDR", "HDR"),
    )
    rec_type = fields.CharField(
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        verbose_name='record type',
        help_text='Record Type. Value: HDR',
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=4),
            DocumentCloud(id='2712034', start_page=5),
        ]
    )
    soft_name = fields.CharField(
        max_length=90,
        db_column='SOFT_NAME',
        blank=True,
        help_text="Filing software name used to electronically file"
    )
    soft_ver = fields.CharField(
        max_length=16,
        db_column='SOFT_VER',
        blank=True,
        help_text="Filing software version number"
    )
    STATE_CD_CHOICES = (
        ('CA', 'California'),
    )
    state_cd = fields.CharField(
        max_length=2,
        db_column='STATE_CD',
        choices=STATE_CD_CHOICES,
        blank=True,
        verbose_name='State code',
        help_text="The state code value entered in the electronic filing",
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=4),
            DocumentCloud(id='2712034', start_page=5),
        ]
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'HDR_CD'
        ordering = ("-filing_id", "-amend_id")

    def __str__(self):
        return str(self.filing_id)


class HeaderCd(CalAccessBaseModel):
    """
    Lookup table used to report Form 460 information in the Agency Management System.
    """
    UNIQUE_KEY = ("LINE_NUMBER", "FORM_ID", "REC_TYPE")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=10),
        DocumentCloud(id='2711614', start_page=79, end_page=80),
    ]
    line_number = fields.IntegerField(
        db_column='LINE_NUMBER',
        help_text="This field is undocumented"
    )
    FORM_ID_CHOICES = (
        ('AF490', 'Form 490, Part A'),
        ('AP1', 'Allocation Part 1'),
        ('AP2', 'Allocation Part 2'),
        ('BF490', 'Form 490, Part B'),
        ('CF490', 'Form 490, Part C'),
        ('DF490', 'Form 490, Part D'),
        ('EF490', 'Form 490, Part E'),
        ('F450', annotations.get_form('F450').full_title),
        ('F460', annotations.get_form('F460').full_title),
        ('F461', annotations.get_form('F461').full_title),
        ('FF490', 'Form 490, Part F'),
        ('HF490', 'Form 490, Part H'),
        ('IF490', 'Form 490, Part I'),
    )
    form_id = fields.CharField(
        db_column='FORM_ID',
        max_length=5,
        help_text="Form identification code",
        verbose_name="Form ID",
        choices=FORM_ID_CHOICES,
    )
    REC_TYPE_CHOICES = (
        ("AP1", "AP1"),
        ("AP2", "AP2"),
        ("SMRY_HEADER", "SMRY_HEADER"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=11,
        db_index=True,
        help_text="Record Type",
        choices=REC_TYPE_CHOICES,
    )
    section_label = fields.CharField(
        db_column='SECTION_LABEL',
        max_length=58,
        blank=True,
        help_text="This field is undocumented"
    )
    comments1 = fields.CharField(
        db_column='COMMENTS1',
        max_length=48,
        blank=True,
        help_text="This field is undocumented"
    )
    comments2 = fields.CharField(
        db_column='COMMENTS2',
        max_length=48,
        blank=True,
        help_text="This field is undocumented"
    )
    label = fields.CharField(
        db_column='LABEL',
        max_length=98,
        help_text="This field is undocumented"
    )
    column_a = fields.IntegerField(
        db_column='COLUMN_A',
        blank=True,
        null=True,
        help_text="This field is undocumented"
    )
    column_b = fields.IntegerField(
        db_column='COLUMN_B',
        blank=True,
        null=True,
        help_text="This field is undocumented"
    )
    column_c = fields.IntegerField(
        db_column='COLUMN_C',
        blank=True,
        null=True,
        help_text="This field is undocumented"
    )
    show_c = fields.IntegerField(
        db_column='SHOW_C',
        blank=True,
        null=True,
        help_text="This field is undocumented"
    )
    show_b = fields.IntegerField(
        db_column='SHOW_B',
        blank=True,
        null=True,
        help_text="This field is undocumented"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'HEADER_CD'
        ordering = ("form_id", "line_number")

    def __str__(self):
        return str(self.form_id)


class SmryCd(CalAccessBaseModel):
    """
    Summary totals from filings.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE",
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=131, end_page=132),
        DocumentCloud(id='2711616', start_page=86, end_page=87),
        DocumentCloud(id='2712033', start_page=27, end_page=28),
        DocumentCloud(id='2712033', start_page=59, end_page=60),
        DocumentCloud(id='2712034', start_page=35, end_page=37),
        DocumentCloud(id='2712034', start_page=72, end_page=74),
    ]
    FILING_FORMS = [
        annotations.get_form('F401'),
        annotations.get_form('F401').get_section('A'),
        annotations.get_form('F401').get_section('B'),
        annotations.get_form('F401').get_section('B-1'),
        annotations.get_form('F450'),
        annotations.get_form('F460'),
        annotations.get_form('F460').get_section('A'),
        annotations.get_form('F460').get_section('B1'),
        annotations.get_form('F460').get_section('B2'),
        annotations.get_form('F460').get_section('B3'),
        annotations.get_form('F460').get_section('C'),
        annotations.get_form('F460').get_section('D'),
        annotations.get_form('F460').get_section('E'),
        annotations.get_form('F460').get_section('F'),
        annotations.get_form('F460').get_section('G'),
        annotations.get_form('F460').get_section('H'),
        annotations.get_form('F460').get_section('H1'),
        annotations.get_form('F460').get_section('H2'),
        annotations.get_form('F460').get_section('H3'),
        annotations.get_form('F460').get_section('I'),
        annotations.get_form('F461'),
        annotations.get_form('F465'),
        annotations.get_form('F625'),
        annotations.get_form('F625').get_section('P2'),
        annotations.get_form('F625').get_section('P3A'),
        annotations.get_form('F625').get_section('P3B'),
        annotations.get_form('F635'),
        annotations.get_form('F635').get_section('P3A'),
        annotations.get_form('F635').get_section('P3B'),
        annotations.get_form('F635').get_section('P3C'),
        annotations.get_form('F635').get_section('P3D'),
        annotations.get_form('F635').get_section('P3E'),
        annotations.get_form('S640'),
        annotations.get_form('F645'),
        annotations.get_form('F645').get_section('P2A'),
        annotations.get_form('F645').get_section('P2B'),
        annotations.get_form('F645').get_section('P2C'),
        annotations.get_form('F900'),
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
    line_item = fields.CharField(
        max_length=8,
        db_column='LINE_ITEM',
        db_index=True,
        help_text="Line item number of this record"
    )
    REC_TYPE_CHOICES = (
        ('SMRY', 'SMRY'),
    )
    rec_type = fields.CharField(
        max_length=4,
        db_column='REC_TYPE',
        db_index=True,
        choices=REC_TYPE_CHOICES,
        verbose_name='record type',
        help_text='Record Type Value: SMRY',
        documentcloud_pages=[
            DocumentCloud(id='2712033', start_page=27),
            DocumentCloud(id='2712033', start_page=59),
            DocumentCloud(id='2712034', start_page=35),
            DocumentCloud(id='2712034', start_page=72),
        ]
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS]) + (
        ('401A', annotations.get_form('F401').get_section('A')),
        ('401B', annotations.get_form('F401').get_section('B')),
        ('401B-1', annotations.get_form('F401').get_section('B-1')),
    )
    form_type = fields.CharField(
        max_length=8,
        db_column='FORM_TYPE',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2711616', start_page=86),
            DocumentCloud(id='2712033', start_page=27, end_page=28),
            DocumentCloud(id='2712033', start_page=59, end_page=60),
            DocumentCloud(id='2712034', start_page=36, end_page=37),
            DocumentCloud(id='2712034', start_page=73, end_page=74),
        ]
    )
    amount_a = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='AMOUNT_A',
        blank=True,
        help_text='Summary amount from column A',
        verbose_name='amount A'
    )
    amount_b = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='AMOUNT_B',
        blank=True,
        help_text='Summary amount from column B',
        verbose_name='amount B'
    )
    amount_c = fields.DecimalField(
        decimal_places=2,
        null=True,
        max_digits=14,
        db_column='AMOUNT_C',
        blank=True,
        help_text='Summary amount from column C',
        verbose_name='amount C'
    )
    elec_dt = fields.DateField(
        db_column='ELEC_DT',
        null=True,
        blank=True,
        verbose_name='election date',
        help_text='Election date',
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'SMRY_CD'
        ordering = ("filing_id", "-amend_id", 'form_type', "line_item")

    def __str__(self):
        return str(self.filing_id)


class CvrE530Cd(CalAccessBaseModel):
    """
    The cover page of Electronic Form 530.
    """
    UNIQUE_KEY = ("FILING_ID", "AMEND_ID")
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=29, end_page=30),
    ]
    FILING_FORMS = [
        annotations.get_form('E530'),
    ]
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
        help_text='Record Type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        verbose_name='form type',
        max_length=4,
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES,
    )
    ENTITY_CODE_CHOICES = annotations.sort_choices(annotations.choices.CAMPAIGN_ENTITY_CODES)
    entity_cd = fields.CharField(
        db_column='ENTITY_CD',
        max_length=32,
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
        help_text='entity code',
        documentcloud_pages=annotations.choices.DOCS['entity_codes'],
    )
    filer_naml = fields.CharField(
        db_column='FILER_NAML',
        max_length=200,
        help_text="Filer last name"
    )
    filer_namf = fields.CharField(
        db_column='FILER_NAMF',
        max_length=4,
        blank=True,
        help_text="Filer first name"
    )
    filer_namt = fields.CharField(
        db_column='FILER_NAMT',
        max_length=32,
        blank=True,
        help_text="Filer title or prefix"
    )
    filer_nams = fields.CharField(
        db_column='FILER_NAMS',
        max_length=32,
        blank=True,
        help_text="Filer suffix"
    )
    report_num = fields.CharField(
        db_column='REPORT_NUM',
        max_length=32,
        blank=True,
        help_text="This field is undocumented"
    )
    rpt_date = fields.DateField(
        db_column='RPT_DATE',
        null=True,
        help_text="This field is undocumented"
    )
    filer_city = fields.CharField(
        db_column='FILER_CITY',
        max_length=16,
        blank=True,
        help_text='Filer city'
    )
    filer_st = fields.CharField(
        db_column='FILER_ST',
        max_length=4,
        blank=True,
        help_text='Filer state'
    )
    filer_zip4 = fields.CharField(
        db_column='FILER_ZIP4',
        max_length=10,
        blank=True,
        help_text='Filer ZIP Code'
    )
    occupation = fields.CharField(
        db_column='OCCUPATION',
        max_length=15,
        blank=True,
        help_text="This field is undocumented"
    )
    employer = fields.CharField(
        db_column='EMPLOYER',
        max_length=13,
        blank=True,
        help_text="This field is undocumented"
    )
    cand_naml = fields.CharField(
        db_column='CAND_NAML',
        max_length=46,
        help_text="Candidate last name"
    )
    cand_namf = fields.CharField(
        db_column='CAND_NAMF',
        max_length=21,
        blank=True,
        help_text="Candidate first name"
    )
    cand_namt = fields.CharField(
        db_column='CAND_NAMT',
        max_length=32,
        blank=True,
        help_text="Candidate title or prefix"
    )
    cand_nams = fields.CharField(
        db_column='CAND_NAMS',
        max_length=32,
        blank=True,
        help_text="Candidate suffix"
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
    )
    district_cd = fields.IntegerField(
        db_column='DISTRICT_CD',
        choices=DISTRICT_CD_CHOICES,
        help_text="District Code",
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=11, end_page=13),
        ]
    )
    OFFICE_CODE_CHOICES = (
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
        choices=OFFICE_CODE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=16, end_page=18),
            DocumentCloud(id='2774529', start_page=20, end_page=22),
        ]
    )
    pmnt_dt = fields.DateField(
        db_column='PMNT_DT',
        null=True,
        help_text="This field is undocumented"
    )
    pmnt_amount = fields.FloatField(
        db_column='PMNT_AMOUNT',
        help_text="This field is undocumented"
    )
    type_literature = fields.IntegerField(
        db_column='TYPE_LITERATURE',
        help_text="This field is undocumented"
    )
    type_printads = fields.IntegerField(
        db_column='TYPE_PRINTADS',
        help_text="This field is undocumented"
    )
    type_radio = fields.IntegerField(
        db_column='TYPE_RADIO',
        help_text="This field is undocumented"
    )
    type_tv = fields.IntegerField(
        db_column='TYPE_TV',
        help_text="This field is undocumented"
    )
    type_it = fields.IntegerField(
        db_column='TYPE_IT',
        help_text="This field is undocumented"
    )
    type_billboards = fields.IntegerField(
        db_column='TYPE_BILLBOARDS',
        help_text="This field is undocumented"
    )
    type_other = fields.IntegerField(
        db_column='TYPE_OTHER',
        help_text="This field is undocumented"
    )
    other_desc = fields.CharField(
        db_column='OTHER_DESC',
        max_length=49,
        help_text="This field is undocumented"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'CVR_E530_CD'
        ordering = ("-pmnt_dt",)

    def __str__(self):
        return str(self.filing_id)


class SpltCd(CalAccessBaseModel):
    """
    Split transaction records used as a child record for a number of forms.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "PFORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=132),
        DocumentCloud(id="2711616", start_page=88),
        DocumentCloud(id="2712034", start_page=18),
    ]
    FILING_FORMS = [
        annotations.get_form('F460').get_section('A'),
        annotations.get_form('F460').get_section('B1'),
        annotations.get_form('F460').get_section('B2'),
        annotations.get_form('F460').get_section('C'),
        annotations.get_form('F460').get_section('D'),
        annotations.get_form('F450').get_section('P5'),
        annotations.get_form('F460').get_section('H'),
    ]
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    elec_amount = fields.DecimalField(
        max_digits=16,
        decimal_places=2,
        db_column='ELEC_AMOUNT',
        verbose_name="election amount",
        help_text="per election to date amount"
    )
    ELEC_CODE_CHOICES = (
        ('P', 'Primary'),
        ('G', 'General'),
        ('S', 'Special'),
        ('R', 'Runoff'),
        ('g', 'General'),
        ('p', 'primary'),
        # The values below are not parsing errors.
        # They are as they appear on sample filing forms.
        ('C', 'Unknown'),
        ('D', 'Unknown'),
        ('F', 'Unknown'),
        ('M', 'Unknown'),
        ('N', 'Unknown'),
        ('X', 'Unknown'),
        ('O', 'Unknown'),
        ('0', 'Unknown'),
        ('1', 'Unknown'),
        ('2', 'Unknown'),
    )
    elec_code = fields.CharField(
        max_length=2,
        choices=ELEC_CODE_CHOICES,
        db_column='ELEC_CODE',
        blank=True,
        verbose_name="election code",
        help_text='per election to date code',
        documentcloud_pages=[
            DocumentCloud(id="2712034", start_page=18),
        ]
    )
    elec_date = fields.DateField(
        db_column='ELEC_DATE',
        null=True,
        help_text="date of election"
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="unique filing identification number"
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="line item number of this record",
        db_index=True,
    )
    PFORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    pform_type = fields.CharField(
        max_length=7,
        db_column='PFORM_TYPE',
        db_index=True,
        choices=PFORM_TYPE_CHOICES,
        help_text='Parent Schedule Type',
        documentcloud_pages=[
            DocumentCloud(id="2712034", start_page=18),
        ]
    )
    ptran_id = fields.CharField(
        verbose_name='parent transaction ID',
        max_length=32,
        db_column='PTRAN_ID',
        blank=True,
        help_text='parent transaction ID',
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'SPLT_CD'

    def __str__(self):
        return str(self.filing_id)


class TextMemoCd(CalAccessBaseModel):
    """
    Text memos attached to electronic filings.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=14),
        DocumentCloud(id='2711614', start_page=133, end_page=134),
        DocumentCloud(id='2711616', start_page=89, end_page=90),
        DocumentCloud(id='2712034', start_page=15, end_page=16),
        DocumentCloud(id='2712033', start_page=13),
    ]

    FILING_FORMS = [
        annotations.get_form('F401'),
        annotations.get_form('F405'),
        annotations.get_form('F410'),
        annotations.get_form('F425'),
        annotations.get_form('F450'),
        annotations.get_form('F460'),
        annotations.get_form('F461'),
        annotations.get_form('F465'),
        annotations.get_form('F496'),
        annotations.get_form('F497'),
        annotations.get_form('F498'),
        annotations.get_form('F601'),
        annotations.get_form('F602'),
        annotations.get_form('F603'),
        annotations.get_form('F604'),
        annotations.get_form('F605'),
        annotations.get_form('F606'),
        annotations.get_form('F607'),
        annotations.get_form('F615'),
        annotations.get_form('F625'),
        annotations.get_form('F635'),
        annotations.get_form('F645'),
        annotations.get_form('S630'),
        annotations.get_form('S635C'),
        annotations.get_form('S640'),
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
        # this is only valid value
        ('TEXT', 'TEXT'),
        # More than 450 records with this value
        # Which is roughly equvalent to the one valid value
        ('MEMO', 'MEMO'),
        # Each of these values only occurs once
        # Records with this value have the same chars in the TEXT4000 field
        ('trun', 'Unknown'),
        ('Unde', 'Under'),
        ('am', 'Unknown'),
        ('sele', 'Unknown'),
        ('Term', 'Unknown'),
        # just noise
        ('re', 'Unknown'),
        ('i', 'Unknown'),
    )
    rec_type = fields.CharField(
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        verbose_name='record type',
        help_text="Record Type Value: TEXT",
        documentcloud_pages=[
            DocumentCloud(id='2712034', start_page=16),
            DocumentCloud(id='2712033', start_page=13),
        ]
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS]) + (
        ('410', annotations.get_form('F410').full_title),
        ('460', annotations.get_form('F460').full_title),
        ('461', annotations.get_form('F461').full_title),
        ('465', annotations.get_form('F465').full_title),
        ('496', annotations.get_form('F496').full_title),
        ('497', annotations.get_form('F497').full_title),
        ('497P1', annotations.get_form('F497').get_section('P1').full_title),
        ('497P2', annotations.get_form('F497').get_section('P2').full_title),
        ('F401A', annotations.get_form('F401').get_section('A').full_title),
        ('F401B', annotations.get_form('F401').get_section('B').full_title),
        ('F401B-1', annotations.get_form('F401').get_section('B-1').full_title),
        ('F450P5', annotations.get_form('F450').get_section('P5').full_title),
        ('F461P1', annotations.get_form('F461').get_section('P1').full_title),
        ('F461P2', annotations.get_form('F461').get_section('P2').full_title),
        ('F461P5', annotations.get_form('F461').get_section('P5').full_title),
        ('F465P3', annotations.get_form('F465').get_section('P3').full_title),
        ('F496P3', annotations.get_form('F496').get_section('P3').full_title),
        ('F497P1', annotations.get_form('F497').get_section('P1').full_title),
        ('F497P2', annotations.get_form('F497').get_section('P2').full_title),
        ('F498-A', annotations.get_form('F498').get_section('A').full_title),
        ('F498-R', annotations.get_form('F498').get_section('R').full_title),
        ('F601P2A', annotations.get_form('F601').get_section('P2A').full_title),
        ('F601P2B', annotations.get_form('F601').get_section('P2B').full_title),
        ('F615P1', annotations.get_form('F615').get_section('P1').full_title),
        ('F615P2', annotations.get_form('F615').get_section('P2').full_title),
        ('F625P2', annotations.get_form('F625').get_section('P2').full_title),
        ('F625P3A', annotations.get_form('F625').get_section('P3A').full_title),
        ('F625P3B', annotations.get_form('F625').get_section('P3B').full_title),
        ('F625P4B', annotations.get_form('F625').get_section('P4B').full_title),
        ('S635', annotations.get_form('F635').full_title),
        ('F635P3B', annotations.get_form('F635').get_section('P3B').full_title),
        ('F635P3C', annotations.get_form('F635').get_section('P3C').full_title),
        ('F635P4B', annotations.get_form('F635').get_section('P4B').full_title),
        ('F645P2A', annotations.get_form('F645').get_section('P2A').full_title),
        ('F645P3B', annotations.get_form('F645').get_section('P3B').full_title),
        ('S497', annotations.get_form('F497').full_title),
        ('S635C', annotations.get_form('S635C').full_title),
        ('A', 'Schedule A of any form (e.g., Forms 401 or 460)'),
        ('A4', 'Schedule A of any form (e.g., Forms 401 or 460)'),
        ('A6', 'Schedule A of any form (e.g., Forms 401 or 460)'),
        ('B', 'Schedule B of any form (e.g., Forms 401 or 460)'),
        ('B1', 'Schedule B, Part 1 of Forms 401 or 460'),
        ('B2', 'Schedule B, Part 2 of Forms 401 or 460'),
        ('B3', 'Schedule B, Part 3 of Forms 401 or 460'),
        ('C', 'Schedule C of any form (e.g., Forms 401 or F460)'),
        ('COMMENTS', 'Possibly comments by FPPC for any form?'),
        ('CVR', 'Cover page for any form (e.g., Forms 460, 461 or 497)'),
        ('D', 'Schedule D of any form (e.g., Forms 401, 460 or 461)'),
        ('DEBTF', annotations.get_form('F460').get_section('F').full_title),
        ('E', 'Schedule E of any form (e.g., Forms 460, 461 or 465)'),
        ('EXPNT', 'Expenditures outlined on any form (e.g. Form 460)'),
        ('F', 'Schedule F of any form (e.g., Form 460)'),
        ('G', 'Schedule G of any form (e.g., Form 460)'),
        ('H', 'Schedule H of any form (e.g., Form 460)'),
        ('H1', 'Schedule H, Part 1 of any form (e.g., Form 460)'),
        ('H2', 'Schedule H2, Part 2 of any form (e.g., Form 460)'),
        ('H3', 'Schedule H3, Part 3 of any form (e.g., Form 460)'),
        ('I', 'Schedule I of any form (e.g., Form 460)'),
        ('PT5', 'Part 5 of any form (e.g., Form 461'),
        ('RCPTB1', 'Schedule B, Part 1 of any form (e.g., Form 460'),
        ('RCPTC', 'Schedule C of any form (e.g., Form 460)'),
        ('RCPTI', 'Schedule I of any form (e.g., Form 460)'),
        ('SCH A', 'Schedule A of any form (e.g., Form 460)'),
        ('SF', 'Schedule F of any form (e.g., Form 460)'),
        ('SPLT', 'A memo that applies to multiple items?'),
        ('SMRY', 'Summary section of any form (e.g., Form 460)'),
        ('SUM', 'Summary section of any form (e.g., Form 460)'),
        ('SUMMARY', 'Summary section of any form (e.g., Form 460)'),
    )
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        verbose_name='form type',
        max_length=8,
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2711616', start_page=90),
            DocumentCloud(id='2712034', start_page=16),
            DocumentCloud(id='2712033', start_page=13),
        ]
    )
    ref_no = fields.CharField(
        db_column='REF_NO',
        max_length=20,
        blank=True,
        help_text='Links text memo to a specific record',
        verbose_name='reference number'
    )
    text4000 = fields.CharField(
        db_column='TEXT4000',
        max_length=4000,
        blank=True,
        help_text='Contents of the text memo',
        verbose_name='text'
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'TEXT_MEMO_CD'

    def __str__(self):
        return str(self.filing_id)


class AcronymsCd(CalAccessBaseModel):
    """
    Acronyms and their definitions.
    """
    UNIQUE_KEY = "ACRONYM"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=7),
        DocumentCloud(id='2711614', start_page=16),
    ]
    acronym = fields.CharField(
        max_length=40,
        db_column="ACRONYM",
        help_text='Acronym text value'
    )
    stands_for = fields.CharField(
        max_length=4,
        db_column="STANDS_FOR",
        help_text='Definition of the acronym'
    )
    effect_dt = fields.DateField(
        null=True,
        db_column="EFFECT_DT",
        help_text='Effective date for the acronym'
    )
    a_desc = fields.CharField(
        max_length=50,
        db_column="A_DESC",
        help_text='Description of the acronym'
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'ACRONYMS_CD'
        ordering = ("acronym",)

    def __str__(self):
        return self.acronym


class AddressCd(CalAccessBaseModel):
    """
    Addresses drawn from across the system.
    """
    UNIQUE_KEY = "ADRID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=7),
        DocumentCloud(id='2711614', start_page=16),
    ]
    adrid = fields.IntegerField(
        db_column="ADRID",
        verbose_name="Address ID",
        help_text='Address indentification number'
    )
    city = fields.CharField(
        max_length=500,
        db_column="CITY",
        help_text='Address city'
    )
    st = fields.CharField(
        max_length=500,
        db_column="ST",
        verbose_name='State',
        help_text='Address state'
    )
    zip4 = fields.CharField(
        db_column="ZIP4",
        null=True,
        max_length=10,
        help_text='Address ZIP Code'
    )
    phon = fields.CharField(
        db_column="PHON",
        null=True,
        max_length=20,
        verbose_name='Phone',
        help_text='Address phone number'
    )
    fax = fields.CharField(
        db_column="FAX",
        null=True,
        max_length=20,
        help_text='Address fax number'
    )
    email = fields.CharField(
        max_length=500,
        db_column="EMAIL",
        help_text='Address email'
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'ADDRESS_CD'

    def __str__(self):
        return str(self.adrid)


class FilersCd(CalAccessBaseModel):
    """
    All links and associations to a filer.
    """
    UNIQUE_KEY = "FILER_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=9),
        DocumentCloud(id='2711614', start_page=73),
    ]
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILERS_CD'
        ordering = ("-filer_id",)

    def __str__(self):
        return str(self.filer_id)


class FilerAcronymsCd(CalAccessBaseModel):
    """
    Links acronyms to filers.
    """
    UNIQUE_KEY = ("ACRONYM", "FILER_ID")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=9),
        DocumentCloud(id='2711614', start_page=61),
    ]
    acronym = fields.CharField(
        db_column='ACRONYM',
        max_length=32,
        help_text="AMS acronym"
    )
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILER_ACRONYMS_CD'
        ordering = ("acronym",)

    def __str__(self):
        return str(self.acronym)


class FilerAddressCd(CalAccessBaseModel):
    """
    Links filers and addresses.

    Maintains a history of when addresses change.
    """
    UNIQUE_KEY = ("FILER_ID", "ADRID")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=9),
        DocumentCloud(id='2711614', start_page=61, end_page=62),
    ]
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    adrid = fields.IntegerField(
        db_column='ADRID',
        verbose_name='Address ID',
        help_text="Address identification number"
    )
    effect_dt = fields.DateField(
        db_column='EFFECT_DT',
        blank=True,
        null=True,
        help_text="Address effective date",
        verbose_name='Effective date'
    )
    ADD_TYPE_CHOICES = (
        (51, 'PERMANENT'),
        (7026, 'BUSINESS'),
        (7027, 'HOME'),
        (7050, 'NOT IN USE'),
        (7051, 'PERMANENT'),
        (7082, 'MAILING ADDRESS'),
    )
    add_type = fields.IntegerField(
        choices=ADD_TYPE_CHOICES,
        db_column='ADD_TYPE',
        blank=True,
        null=True,
        verbose_name="Address type",
        help_text="Address type",
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=5),
        ]
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILER_ADDRESS_CD'

    def __str__(self):
        return str(self.filer_id)


class FilerEthicsClassCd(CalAccessBaseModel):
    """
    Ethics training events for lobbyists.
    """
    UNIQUE_KEY = "FILER_ID", "SESSION_ID", "ETHICS_DATE"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=9),
        DocumentCloud(id='2711614', start_page=64),
    ]
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    ethics_date = fields.DateField(
        db_column='ETHICS_DATE',
        null=True,
        help_text="Date ethics training was accomplished"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILER_ETHICS_CLASS_CD'
        ordering = ("-ethics_date",)

    def __str__(self):
        return str(self.filer_id)


class FilerInterestsCd(CalAccessBaseModel):
    """
    Links a filer to interest codes.
    """
    UNIQUE_KEY = (
        "FILER_ID",
        "INTEREST_CD",
        "EFFECT_DATE",
        "SESSION_ID"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=9),
        DocumentCloud(id='2711614', start_page=66),
    ]
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    INTEREST_CD_CHOICES = (
        (0, 'N/A'),
        (40301, 'AGRICULTURE'),
        (40302, 'EDUCATION'),
        (40303, 'ENTERTAINMENT/RECREATION'),
        (40304, 'FINANCE/INSURANCE'),
        (40305, 'GOVERNMENT'),
        (40306, 'HEALTH'),
        (40307, 'LABOR UNIONS'),
        (40308, 'LEGAL'),
        (40309, 'LODGING/RESTAURANTS'),
        (40310, 'MANUFACTURING/INDUSTRIAL'),
        (40311, 'MERCHANDISE/RETAIL'),
        (40312, 'MISCELLANEOUS'),
        (40313, 'OIL AND GAS'),
        (40314, 'POLITICAL ORGANIZATIONS'),
        (40315, 'PROFESSIONAL/TRADE'),
        (40316, 'PUBLIC EMPLOYEES'),
        (40317, 'REAL ESTATE'),
        (40318, 'TRANSPORTATION'),
        (40319, 'UTILITIES'),
    )
    interest_cd = fields.IntegerField(
        db_column='INTEREST_CD',
        blank=True,
        null=True,
        verbose_name="interest code",
        help_text="Interest code linked to the filer",
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=19),
        ],
        choices=INTEREST_CD_CHOICES,
    )
    effect_date = fields.DateField(
        db_column='EFFECT_DATE',
        null=True,
        verbose_name="Effective date",
        help_text="Effective date",
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILER_INTERESTS_CD'
        ordering = ("-effect_date",)

    def __str__(self):
        return str(self.filer_id)


class FilerLinksCd(CalAccessBaseModel):
    """
    Links filers to each other.
    """
    UNIQUE_KEY = (
        "FILER_ID_A",
        "FILER_ID_B",
        "ACTIVE_FLG",
        "SESSION_ID",
        "LINK_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=9),
        DocumentCloud(id='2711614', start_page=67),
    ]
    filer_id_a = fields.IntegerField(
        verbose_name='Filer ID A',
        db_column='FILER_ID_A',
        db_index=True,
        help_text='Unique identification number for the first filer \
in the relationship',
    )
    filer_id_b = fields.IntegerField(
        verbose_name='Filer ID B',
        db_column='FILER_ID_B',
        db_index=True,
        help_text='Unique identification number for the second filer \
in the relationship',
    )
    active_flg = fields.CharField(
        verbose_name='active flag',
        max_length=1,
        db_column='ACTIVE_FLG',
        help_text='Indicates if the link is active',
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    LINK_TYPE_CHOICES = (
        (-12019, 'CANDIDATE CONTROLLED CAUCUS COMMITTEE'),
        (-12018, 'PROPONENT'),
        (-12016, 'TREASURER/RESPONSIBLE OFFICER FOR'),
        (-12015, 'ASSOCIATED'),
        (-12014, 'SUPPORT'),
        (-12013, 'OPPOSE'),
        (-12011, 'CONTROLLING CANDIDATE'),
        (-12008, 'FIRM OF A LOBBYIST'),
        (-12005, 'FIRM OF A CLIENT (WHO IS ALSO A FIRM)'),
        (-12004, 'FIRM OF A CLIENT (WHO IS AN EMPLOYER)'),
        (-12002, 'EMPLOYER OF  AN IN-HOUSE LOBBYIST'),
        (-12001, 'CLIENT OF A FIRM'),
        (0, 'N/A'),
        (12001, 'FIRM OF A CLIENT'),
        (12002, 'IN-HOUSE LOBBYIST OF AN EMPLOYER'),
        (12004, 'CLIENT (WHO IS AN EMPLOYER) OF A FIRM'),
        (12005, 'CLIENT (WHO IS ALSO A FIRM) OF ANOTHER FIRM'),
        (12008, 'LOBBYIST OF A FIRM'),
        (12011, 'CANDIDATE CONTROLS THIS COMMITTEE'),
        (12013, 'OPPOSE'),
        (12014, 'SUPPORT'),
        (12015, 'ASSOCIATED'),
        (12016, 'TREASURER/RESPONSIBLE OFFICER'),
        (12018, 'PROPONENT'),
        (12019, 'CANDIDATE CONTROLLED CAUCUS COMMITTEE'),
    )
    link_type = fields.IntegerField(
        choices=LINK_TYPE_CHOICES,
        db_column='LINK_TYPE',
        verbose_name='link type',
        help_text='Denotes the type of the link',
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=6, end_page=7),
        ]
    )
    link_desc = fields.CharField(
        verbose_name='link description',
        max_length=255,
        db_column='LINK_DESC',
        blank=True,
        help_text='Unused',
    )
    effect_dt = fields.DateField(
        verbose_name='effective date',
        db_column='EFFECT_DT',
        null=True,
        help_text='Date the link became active',
    )
    dominate_filer = fields.CharField(
        max_length=1,
        db_column='DOMINATE_FILER',
        blank=True,
        help_text='Unused',
    )
    termination_dt = fields.DateField(
        verbose_name='termination date',
        db_column='TERMINATION_DT',
        null=True,
        blank=True,
        help_text="Termination effective date",
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILER_LINKS_CD'

    def __str__(self):
        return str('%s-%s' % (self.filer_id_a, self.filer_id_b))


class FilerStatusTypesCd(CalAccessBaseModel):
    """
    An undocumented table.

    Contains a small number of codes that map to FILERNAME_CD.STATUS.
    """
    UNIQUE_KEY = "STATUS_TYPE"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=9),
        DocumentCloud(id='2711614', start_page=69),
    ]
    status_type = fields.CharField(
        max_length=11,
        db_column='STATUS_TYPE',
        verbose_name='status type',
        help_text='This field is undocumented',
    )
    status_desc = fields.CharField(
        max_length=11,
        db_column='STATUS_DESC',
        verbose_name="status description",
        help_text='This field is undocumented'
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILER_STATUS_TYPES_CD'
        ordering = ("status_type",)

    def __str__(self):
        return self.status_type


class FilerToFilerTypeCd(CalAccessBaseModel):
    """
    Links a filer to a set of characteristics that describe the filer.

    Maintains a history of changes and allows the filer to change characteristics over time.
    """
    UNIQUE_KEY = (
        "FILER_ID",
        "FILER_TYPE",
        "SESSION_ID",
        "EFFECT_DT"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=9),
        DocumentCloud(id='2711614', start_page=69, end_page=70),
    ]
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
        db_column='FILER_ID',
    )
    filer_type = fields.ForeignKeyField(
        'FilerTypesCd',
        related_name='filers',
        db_constraint=False,
        help_text="Foreign key referencing FilerTypesCd.filer_type",
        db_column='FILER_TYPE',
        on_delete=models.CASCADE
    )
    active = fields.CharField(
        max_length=1,
        help_text="Indicates if the filer is currently active",
        db_column='ACTIVE',
    )
    RACE_CHOICES = (
        (0, 'N/A'),
        (30002, 'GOVERNOR'),
        (30003, 'LIEUTENANT GOVERNOR'),
        (30004, 'SECRETARY OF STATE'),
        (30005, 'CONTROLLER'),
        (30006, 'TREASURER'),
        (30007, 'ATTORNEY GENERAL'),
        (30008, 'SUPERINTENDENT OF PUBLIC INSTRUCTION'),
        (30009, 'MEMBER BOARD OF EQUALIZATION'),
        (30010, 'OXNARD HARBOR COMMISSIONER'),
        (30011, 'CITY CONTROLLER'),
        (30012, 'STATE SENATE'),
        (30013, 'ASSEMBLY'),
        (30014, 'INSURANCE COMMISSIONER'),
        (30015, 'JUDGE'),
        (30016, 'BOARD MEMBER'),
        (30017, 'TAX COLLECTOR'),
        (30018, 'TRUSTEE'),
        (30019, 'SUPERVISOR'),
        (30020, 'SHERIFF'),
        (30021, 'CORONER'),
        (30022, 'MARSHALL'),
        (30023, 'CITY CLERK'),
        (30024, 'SCHOOL BOARD'),
        (30025, 'HARBOR COMMISSIONER'),
        (30026, 'DISTRICT ATTORNEY'),
        (30027, 'COUNTY CLERK'),
        (30028, 'AUDITOR'),
        (30029, 'MAYOR'),
        (30030, 'CITY ATTORNEY'),
        (30031, 'DEMOCRATIC COUNTY CENTRAL COMMITTEE'),
        (30032, 'TOWN COUNCIL'),
        (30033, 'ASSESSOR'),
        (30034, 'CITY TREASURER'),
        (30035, 'CITY COUNCIL'),
        (30036, 'COMMISSIONER'),
        (30037, 'REPUBLICAN COUNTY CENTRAL COMMITTEE'),
        (30038, 'DIRECTOR'),
        (30039, 'DIRECTOR OF ZONE 7'),
        (30040, 'COMMUNITY COLLEGE BOARD'),
        (30041, 'POLICE CHIEF'),
        (30042, 'CHIEF OF POLICE'),
        (30043, 'CENTRAL COMMITTEE'),
        (30044, 'BOARD OF EDUCATION'),
        (30045, 'BOARD OF DIRECTORS'),
        (30046, 'COLLEGE BOARD'),
        (30047, 'BART BOARD DIRECTOR'),
        (30048, 'BOARD OF TRUSTEES'),
        (30049, 'IRRIGATION'),
        (30050, 'WATER BOARD'),
        (30051, 'COMMUNITY PLANNING GROUP'),
        (30052, 'BOARD OF SUPERVISORS'),
        (30053, 'SUPERIOR COURT JUDGE'),
        (30054, 'DISTRICT ATTORNEY/PUBLIC DEFENDER'),
        (30055, 'MEASURE'),
        (30056, 'CITY PROSECUTOR'),
        (30057, 'SUPREME COURT JUDGE'),
        (30058, 'PUBLIC EMPLOYEES RETIREMENT BOARD'),
        (30059, 'APPELLATE COURT JUDGE'),
        (50001, 'Ag'),
        (50002, 'Assembly'),
        (50003, 'Assessor'),
        (50004, 'Assessor/Clerk/Recorder'),
        (50005, 'Assessor/County Clerk/Recorder'),
        (50006, 'Assessor/Recorder'),
        (50007, 'Associate Justice'),
        (50008, 'Auditor'),
        (50009, 'Auditor/Controller'),
        (50010, 'Auditor/Controller/Clerk/Recorder'),
        (50011, 'Auditor/Controller/Recorder'),
        (50012, 'Auditor/Controller/Treasurer/Tax Collector'),
        (50013, 'Auditor/Recorder'),
        (50014, 'Board Member'),
        (50015, 'Board Of Director'),
        (50016, 'Board Of Supervisor'),
        (50017, 'Boe'),
        (50018, 'Chief Justice'),
        (50019, 'City'),
        (50020, 'City Attorney'),
        (50021, 'City Auditor'),
        (50022, 'City Clerk'),
        (50023, 'City Council'),
        (50024, 'City Of Los Angeles'),
        (50025, 'City Of South El Monte'),
        (50026, 'City Prosecutor'),
        (50027, 'City Treasurer'),
        (50028, 'Clerk/Auditor'),
        (50029, 'Clerk/Record/Public Admin'),
        (50030, 'Clerk/Recorder'),
        (50031, 'Clerk/Recorder/Registar'),
        (50032, 'Clerk/Recorder/Registrar'),
        (50033, 'Commissioner'),
        (50034, 'Controller'),
        (50035, 'Costa Mesa'),
        (50036, 'Council Member'),
        (50037, 'County Clerk'),
        (50038, 'County Clerk/Auditor'),
        (50039, 'County Clerk/Auditor/Controller'),
        (50040, 'County Clerk/Recorder'),
        (50041, 'County Clerk/Recorder/Assessor'),
        (50042, 'County Clerk/Recorder/Public Admin'),
        (50043, 'Democratic County Central Committee'),
        (50044, 'Director'),
        (50045, 'District Attorney'),
        (50046, 'District Attorney/Public Administrator'),
        (50047, 'Gccc'),
        (50048, 'Governor'),
        (50049, 'Harbor Commissioner'),
        (50050, 'Ic'),
        (50051, 'Irrigation Dist'),
        (50052, 'Judge'),
        (50053, 'Justice'),
        (50054, 'Legislature'),
        (50055, 'Lieutenant Governor'),
        (50056, 'Mayor'),
        (50057, 'N/A'),
        (50058, 'Placentia'),
        (50059, 'Public Administrator'),
        (50060, 'Public Administrator/Guardian'),
        (50061, 'Rent Stabilization Board'),
        (50062, 'Republican Central Committee'),
        (50063, 'San Francisco Dccc'),
        (50064, 'Sanger'),
        (50065, 'School Board'),
        (50066, 'Secretary Of State'),
        (50067, 'Senator'),
        (50068, 'Sheriff'),
        (50069, 'Sheriff/Coroner'),
        (50070, 'Sheriff/Coroner/Marshall'),
        (50071, 'Sheriff/Coroner/Public Administrator'),
        (50072, 'Solana Beach'),
        (50073, 'Superintendent'),
        (50074, 'Supervisor'),
        (50075, 'Supt Of Schools'),
        (50076, 'Tax Collector'),
        (50077, 'Town Council'),
        (50078, 'Treasurer'),
        (50079, 'Treasurer/Tax Collector'),
        (50080, 'Treasurer/Tax Collector/Clerk'),
        (50081, 'Treasurer/Tax Collector/Public Administrator'),
        (50082, 'Treasurer/Tax Collector/Public Administrator/County Clerk'),
        (50083, 'Treasurer/Tax Collector/Recorder'),
        (50084, 'Trustee'),
        (50085, 'Weed Recreation Board Member'),
    )
    race = fields.IntegerField(
        null=True,
        blank=True,
        db_column='RACE',
        choices=RACE_CHOICES,
        help_text="If applicable indicates the race in which the filer is \
running",
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=16, end_page=18),
            DocumentCloud(id='2774529', start_page=20, end_page=22),
        ]
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    CATEGORY_CHOICES = (
        (0, 'N/A'),
        (40000, 'CATEGORY'),
        (40001, 'JOINTLY CONTROLLED'),
        (40002, 'CONTROLLED'),
        (40003, 'CAUCUS COMMITTEE'),
        (40004, 'Unknown'),
    )
    category = fields.IntegerField(
        null=True,
        blank=True,
        choices=CATEGORY_CHOICES,
        help_text="Defines the filer's category such as controlled, jointly \
controlled, etc. (subset of filer's type)",
        db_column='CATEGORY',
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=18),
        ]
    )
    CATEGORY_TYPE_CHOICES = (
        (0, 'N/A'),
        (40501, 'LOCAL'),
        (40502, 'STATE'),
        (40503, 'COUNTY'),
        (40504, 'MULTI-COUNTY'),
        (40505, 'CITY'),
        (40506, 'FEDERAL'),
        (40507, 'SUPERIOR COURT JUDGE'),
    )
    category_type = fields.IntegerField(
        null=True,
        blank=True,
        choices=CATEGORY_TYPE_CHOICES,
        help_text="When applicable, the category type specifies additional \
information about the category. (e.g. state, local, etc.)",
        db_column='CATEGORY_TYPE',
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=19, end_page=20),
        ]
    )
    SUB_CATEGORY_CHOICES = (
        (0, 'N/A'),
        (40101, 'PRIMARILY FORMED MEASURE'),
        (40102, 'PRIMARILY FORMED CANDIDATE'),
        (40103, 'GENERAL PURPOSE'),
        (40104, 'GENERAL PURPOSE POLITICAL PARTY'),
        (40105, 'GENERAL PURPOSE MEASURE'),
        (40112, 'Unknown'),
    )
    sub_category = fields.IntegerField(
        null=True,
        blank=True,
        help_text="When applicable specifies general purpose, primarily \
formed, etc.",
        db_column='SUB_CATEGORY',
        choices=SUB_CATEGORY_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=18),
        ]
    )
    effect_dt = fields.DateField(
        null=True,
        help_text="The date the filer assumed the current class or type",
        db_column='EFFECT_DT',
    )
    SUB_CATEGORY_TYPE_CHOICES = (
        (0, 'N/A'),
        (40202, 'BROAD-BASED'),
        (40203, 'SMALL CONTRIBUTOR'),
        (40204, 'MPO - NON PROFIT'),
        (40205, 'MPO - NON PROFIT CY'),
        (40206, 'MPO - OTHER'),
        (40207, 'MPO - OTHER CY'),
        (40208, 'FEDERAL PAC'),
        (40209, 'OUT OF STATE PAC'),
    )
    sub_category_type = fields.IntegerField(
        null=True,
        blank=True,
        choices=SUB_CATEGORY_TYPE_CHOICES,
        help_text="When applicable specifies broad based or small contributor",
        db_column='SUB_CATEGORY_TYPE',
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=18, end_page=19),
        ],
    )
    ELECTION_TYPE_CHOICES = (
        (0, 'N/A'),
        (3001, 'GENERAL'),
        (3002, 'PRIMARY'),
        (3003, 'RECALL'),
        (3004, 'SPECIAL ELECTION'),
        (3005, 'OFFICEHOLDER'),
        (3006, 'SPECIAL RUNOFF'),
        (3010, 'Unknown'),
        (3007, 'Unknown'),
    )
    election_type = fields.IntegerField(
        null=True,
        blank=True,
        choices=ELECTION_TYPE_CHOICES,
        help_text="Indicates type of election (general, primary, special)",
        db_column='ELECTION_TYPE',
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=3, end_page=4),
        ],
    )
    sub_category_a = fields.CharField(
        max_length=1,
        blank=True,
        help_text="Indicates if sponsored or not",
        db_column='SUB_CATEGORY_A',
    )
    nyq_dt = fields.DateField(
        null=True,
        blank=True,
        help_text="Indicates the date when a committee reached its qualifying \
level of activity",
        db_column='NYQ_DT',
    )
    PARTY_CODE_CHOICES = (
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
        (16020, 'PEACE AND FREEDOM'),
        # The codes below occur in the database but are
        # undocumented in the lookup table
        (16014, 'UNKNOWN'),
        (0, 'UNKNOWN'),
        (None, 'NONE'),
    )
    party_cd = fields.IntegerField(
        null=True,
        blank=True,
        choices=PARTY_CODE_CHOICES,
        db_column='PARTY_CD',
        help_text="Filer's political party",
        verbose_name='party code',
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=10, end_page=11),
        ]
    )
    COUNTY_CD_CHOICES = (
        (0, 'N/A'),
        (18001, '01'),
        (18002, '12'),
        (18003, '23'),
        (18004, '34'),
        (18005, '45'),
        (18006, '55'),
        (18007, '56'),
        (18008, '57'),
        (18009, '58'),
        (18010, '02'),
        (18011, '03'),
        (18012, '04'),
        (18013, '05'),
        (18014, '06'),
        (18015, '07'),
        (18016, '08'),
        (18017, '09'),
        (18018, '10'),
        (18019, '11'),
        (18020, '13'),
        (18021, '14'),
        (18022, '15'),
        (18023, '16'),
        (18024, '17'),
        (18025, '18'),
        (18026, '19'),
        (18027, '20'),
        (18028, '21'),
        (18029, '22'),
        (18030, '24'),
        (18031, '25'),
        (18032, '26'),
        (18033, '27'),
        (18034, '28'),
        (18035, '29'),
        (18036, '30'),
        (18037, '31'),
        (18038, '32'),
        (18039, '33'),
        (18040, '35'),
        (18041, '36'),
        (18042, '37'),
        (18043, '38'),
        (18044, '39'),
        (18045, '40'),
        (18046, '41'),
        (18047, '42'),
        (18048, '43'),
        (18049, '44'),
        (18050, '46'),
        (18051, '47'),
        (18052, '48'),
        (18053, '49'),
        (18054, '50'),
        (18055, '51'),
        (18056, '52'),
        (18057, '53'),
        (18058, '54'),
    )
    county_cd = fields.IntegerField(
        null=True,
        blank=True,
        choices=COUNTY_CD_CHOICES,
        help_text="Filer's county code",
        verbose_name='county code',
        db_column='COUNTY_CD',
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=13, end_page=15),
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
        (17091, 'Unknown'),
        (17083, 'Unknown'),
        (17093, 'Unknown'),
        (17094, 'Unknown'),
        (17088, 'Unknown'),
        (17096, 'Unknown'),
        (17012, 'Unknown'),
        (17095, 'Unknown'),
        (17092, 'Unknown'),
        (17086, 'Unknown'),
        (17099, 'Unknown'),
        (17082, 'Unknown'),
        (17025, 'Unknown'),
        (17085, 'Unknown'),
        (17084, 'Unknown'),
        (17087, 'Unknown'),
        (17098, 'Unknown'),
        (17089, 'Unknown'),
    )
    district_cd = fields.IntegerField(
        null=True,
        blank=True,
        choices=DISTRICT_CD_CHOICES,
        verbose_name='county code',
        help_text="Filer's district number for the office being sought. \
Populated for Senate, Assembly or Board of Equalization races",
        db_column='DISTRICT_CD',
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=11, end_page=13),
        ]
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILER_TO_FILER_TYPE_CD'

    def __str__(self):
        return str(self.filer_id)


class FilerTypesCd(CalAccessBaseModel):
    """
    Lookup table describing filer types.
    """
    UNIQUE_KEY = "FILER_TYPE"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=9),
        DocumentCloud(id='2711614', start_page=71, end_page=72),
    ]
    filer_type = fields.IntegerField(
        db_column='FILER_TYPE',
        help_text="Filer type identification number",
        primary_key=True,
    )
    description = fields.CharField(
        max_length=255,
        db_column='DESCRIPTION',
        help_text="Description of the filer type"
    )
    GRP_TYPE_CHOICES = (
        (58, 'LOBBY PERIODS'),
        (59, 'CAMPAIGN PERIODS'),
        (60, 'DEFAULT PERIOD FOR ERRONEOUS DATA'),
        (61, 'Unknown'),
    )
    grp_type = fields.IntegerField(
        null=True,
        db_column='GRP_TYPE',
        blank=True,
        choices=GRP_TYPE_CHOICES,
        help_text="Group type assocated with the filer type",
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=4),
        ]
    )
    calc_use = fields.CharField(
        max_length=1,
        db_column='CALC_USE',
        blank=True,
        help_text="Use checkbox flag"
    )
    grace_period = fields.CharField(
        max_length=12,
        db_column='GRACE_PERIOD',
        blank=True,
        help_text="This field is undocumented"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILER_TYPES_CD'
        ordering = ("filer_type",)

    def __str__(self):
        return str(self.filer_type)


class FilerXrefCd(CalAccessBaseModel):
    """
    Maps legacy filer identification numbers to current filer identification numbers.
    """
    UNIQUE_KEY = ("FILER_ID", "XREF_ID")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=9),
        DocumentCloud(id='2711614', start_page=72),
    ]
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    xref_id = fields.CharField(
        verbose_name='crossreference filer ID',
        max_length=32,
        db_column='XREF_ID',
        db_index=True,
        help_text="Alternative filer ID found on many forms"
    )
    effect_dt = fields.DateField(
        db_column='EFFECT_DT',
        null=True,
        verbose_name="Effective date",
        help_text="Effective date",
    )
    migration_source = fields.CharField(
        max_length=50,
        db_column='MIGRATION_SOURCE',
        help_text="Source of the XREF_ID. Migration or generated by the AMS."
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILER_XREF_CD'

    def __str__(self):
        return str(self.filer_id)


class FilingPeriodCd(CalAccessBaseModel):
    """
    Metadata for filing periods.
    """
    UNIQUE_KEY = "PERIOD_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=10),
        DocumentCloud(id='2711614', start_page=74, end_page=75),
    ]
    period_id = fields.IntegerField(
        db_column='PERIOD_ID',
        help_text="Unique period identification number"
    )
    start_date = fields.DateField(
        db_column='START_DATE',
        null=True,
        help_text="Starting date for period"
    )
    end_date = fields.DateField(
        db_column='END_DATE',
        null=True,
        help_text="Ending date of period"
    )
    PERIOD_TYPE_CHOICES = (
        (1500, 'Standard period'),
    )
    period_type = fields.IntegerField(
        db_column='PERIOD_TYPE',
        choices=PERIOD_TYPE_CHOICES,
        help_text='Type of filing period',
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=3),
        ]
    )
    PER_GRP_TYPE_CHOICES = (
        (1500, 'STANDARD PERIOD'),
    )
    per_grp_type = fields.IntegerField(
        db_column='PER_GRP_TYPE',
        help_text="Period group type",
        choices=PER_GRP_TYPE_CHOICES,
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=3),
        ]
    )
    period_desc = fields.CharField(
        max_length=255,
        db_column='PERIOD_DESC',
        help_text="Period description"
    )
    deadline = fields.DateField(
        db_column='DEADLINE',
        null=True,
        help_text="Deadline date"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILING_PERIOD_CD'
        ordering = ("-end_date",)

    def __str__(self):
        return str(self.period_id)


class GroupTypesCd(CalAccessBaseModel):
    """
    Lookup table for group types.

    Most (but not all) of the GRP_ID/GRP_NAME value pairs in this table match
    the FILER_TYPE/DESCRIPTION value pairs in the FILER_TYPE_CD table.
    """
    UNIQUE_KEY = "GRP_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=10),
        DocumentCloud(id='2711614', start_page=78, end_page=79),
    ]
    grp_id = fields.IntegerField(
        db_column='GRP_ID',
        verbose_name="Group ID",
        help_text="Group identification number"
    )
    grp_name = fields.CharField(
        db_column='GRP_NAME',
        max_length=28,
        blank=True,
        verbose_name="Group name",
        help_text="Group name. Many of the values in this column are empty strings."
    )
    grp_desc = fields.CharField(
        db_column='GRP_DESC',
        max_length=32,
        blank=True,
        verbose_name="Group description",
        help_text="Group Description. This column contains only empty strings."
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'GROUP_TYPES_CD'
        ordering = ("grp_id",)

    def __str__(self):
        return str(self.grp_id)


class ImageLinksCd(CalAccessBaseModel):
    """
    Links images to filers and accounts.
    """
    UNIQUE_KEY = ("IMG_LINK_ID", "IMG_ID")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=10),
        DocumentCloud(id='2711614', start_page=80),
    ]
    img_link_id = fields.IntegerField(
        db_column='IMG_LINK_ID',
        verbose_name="Image link ID",
        help_text="Image link identification number"
    )
    IMG_LINK_TYPE_CHOICES = (
        (6501, 'FILING ID'),
        (6502, 'FILER ID'),
    )
    img_link_type = fields.IntegerField(
        choices=IMG_LINK_TYPE_CHOICES,
        db_column='IMG_LINK_TYPE',
        verbose_name="Image link type",
        help_text='Type of image link',
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=5),
        ]
    )
    img_id = fields.IntegerField(
        db_column='IMG_ID',
        verbose_name="Image ID",
        help_text="Image identification number"
    )
    IMG_TYPE_CHOICES = (
        (6001, 'FAX'),
        (6002, 'PERSONAL PHOTO'),
        (6004, 'SCANNED CHECK'),
        (6005, 'SCANNED LETTER'),
        (6007, 'IMAGE TYPES'),
    )
    img_type = fields.IntegerField(
        choices=IMG_TYPE_CHOICES,
        db_column='IMG_TYPE',
        verbose_name="Image type",
        help_text='Type of image',
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=4),
        ],
    )
    img_dt = fields.DateField(
        db_column='IMG_DT',
        null=True,
        verbose_name="Image date",
        help_text="Image date",
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'IMAGE_LINKS_CD'
        ordering = ("-img_dt",)

    def __str__(self):
        return str(self.img_link_id)


class LegislativeSessionsCd(CalAccessBaseModel):
    """
    Start and end dates for legislative sessions.
    """
    UNIQUE_KEY = "SESSION_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=10),
        DocumentCloud(id='2711614', start_page=84),
    ]

    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    begin_date = fields.DateField(
        db_column='BEGIN_DATE',
        null=True,
        help_text="Session start date"
    )
    end_date = fields.DateField(
        db_column='END_DATE',
        null=True,
        help_text="Session end date"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LEGISLATIVE_SESSIONS_CD'
        ordering = ("-begin_date",)

    def __str__(self):
        return str(self.session_id)


class LookupCodesCd(CalAccessBaseModel):
    """
    Definitions for some lookup codes.
    """
    UNIQUE_KEY = ("CODE_ID", "CODE_TYPE")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=12),
        DocumentCloud(id='2711614', start_page=106, end_page=106),
    ]
    code_type = fields.IntegerField(
        db_column='CODE_TYPE',
        help_text="This field is undocumented",
    )
    code_id = fields.IntegerField(
        db_column='CODE_ID',
        help_text="The code's identification number",
    )
    code_desc = fields.CharField(
        db_column='CODE_DESC',
        max_length=100,
        null=True,
        help_text="Code description",
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOOKUP_CODES_CD'

    def __str__(self):
        return str(self.code_id)


class NamesCd(CalAccessBaseModel):
    """
    A collection of names from across the database.

    Used for searches when the name has an identification number.
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=13),
        DocumentCloud(id='2711614', start_page=112),
    ]
    namid = fields.IntegerField(
        db_column='NAMID',
        help_text="Identification number unique to the name",
    )
    naml = fields.CharField(
        max_length=200,
        db_column='NAML',
        help_text="Last name",
    )
    namf = fields.CharField(
        max_length=50,
        db_column='NAMF',
        help_text="First name",
    )
    namt = fields.CharField(
        max_length=100,
        db_column='NAMT',
        blank=True,
        help_text="Name title or prefix",
    )
    nams = fields.CharField(
        max_length=30,
        db_column='NAMS',
        blank=True,
        help_text="Name suffix",
    )
    moniker = fields.CharField(
        max_length=30,
        db_column='MONIKER',
        blank=True,
        help_text="Entity's moniker",
    )
    moniker_pos = fields.CharField(
        max_length=9,
        db_column='MONIKER_POS',
        blank=True,
        help_text="Location of the entity's moniker",
    )
    namm = fields.CharField(
        max_length=20,
        db_column='NAMM',
        blank=True,
        help_text="Middle name",
    )
    fullname = fields.CharField(
        max_length=200,
        db_column='FULLNAME',
        help_text="Full name",
    )
    naml_search = fields.CharField(
        max_length=200,
        db_column='NAML_SEARCH',
        help_text="Last name",
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'NAMES_CD'
        ordering = ("naml", "namf")

    def __str__(self):
        return str(self.namid)


class ReceivedFilingsCd(CalAccessBaseModel):
    """
    Undocumented.
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=13),
        DocumentCloud(id='2711614', start_page=121),
    ]
    FILING_FORMS = [
        annotations.get_form('F400'),
        annotations.get_form('F401'),
        annotations.get_form('F402'),
        annotations.get_form('F410'),
        annotations.get_form('F425'),
        annotations.get_form('F450'),
        annotations.get_form('F460'),
        annotations.get_form('F461'),
        annotations.get_form('F465'),
        annotations.get_form('F496'),
        annotations.get_form('F497'),
        annotations.get_form('F498'),
        annotations.get_form('F601'),
        annotations.get_form('F602'),
        annotations.get_form('F603'),
        annotations.get_form('F604'),
        annotations.get_form('F606'),
        annotations.get_form('F607'),
        annotations.get_form('F615'),
        annotations.get_form('F625'),
        annotations.get_form('F635'),
        annotations.get_form('F645'),
    ]
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    filing_file_name = fields.CharField(
        db_column='FILING_FILE_NAME',
        max_length=60,
        help_text="The field is undocumented"
    )
    received_date = fields.DateField(
        db_column='RECEIVED_DATE',
        null=True,
        help_text="Date received",
    )
    filing_directory = fields.CharField(
        db_column='FILING_DIRECTORY',
        max_length=60,
        help_text="This field is undocumented",
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identification number",
        null=True,
        blank=True,
    )
    FORM_ID_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_id = fields.CharField(
        db_column='FORM_ID',
        max_length=7,
        blank=True,
        choices=FORM_ID_CHOICES,
        verbose_name="form identification code",
        help_text="Form identification code",
        documentcloud_pages=[
            DocumentCloud(id='2711624', start_page=4, end_page=8),
        ]
    )
    receive_comment = fields.CharField(
        db_column='RECEIVE_COMMENT',
        max_length=120,
        help_text="A comment"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'RECEIVED_FILINGS_CD'
        ordering = ("-received_date",)

    def __str__(self):
        return str(self.filing_id)


class ReportsCd(CalAccessBaseModel):
    """
    Undocumented.
    """
    UNIQUE_KEY = "RPT_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614', start_page=13),
        DocumentCloud(id='2711614', start_page=122),
    ]
    rpt_id = fields.IntegerField(
        db_column='RPT_ID',
        help_text="Unique identification number"
    )
    rpt_name = fields.CharField(
        db_column='RPT_NAME',
        max_length=74,
        help_text="Name of the report"
    )
    rpt_desc_field = fields.CharField(
        db_column='RPT_DESC_',
        max_length=32,
        blank=True,
        help_text="Description of the report"
    )
    path = fields.CharField(
        db_column='PATH',
        max_length=32,
        blank=True,
        help_text="Report path"
    )
    data_object = fields.CharField(
        db_column='DATA_OBJECT',
        max_length=38,
        help_text="This field is undocumented"
    )
    parms_flg_y_n = fields.IntegerField(
        db_column='PARMS_FLG_Y_N',
        blank=True,
        null=True,
        help_text="Parameters indication flag"
    )
    REPORT_TYPE_CHOICES = (
        (401, 'PUBLIC REPORTS'),
        (402, 'AUDITS'),
        (403, 'FINANCIAL REPORTS'),
        (404, 'AUDITS'),
        (405, 'MAILING LABELS'),
        (406, 'OTHER REPORTS'),
        (0, 'N/A'),
    )
    rpt_type = fields.IntegerField(
        choices=REPORT_TYPE_CHOICES,
        db_column='RPT_TYPE',
        help_text="Type of the report",
        documentcloud_pages=[
            DocumentCloud(id='2774529', start_page=2),
        ]
    )
    parm_definition = fields.IntegerField(
        db_column='PARM_DEFINITION',
        help_text="Parameter definition"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'REPORTS_CD'
        ordering = ("rpt_name",)

    def __str__(self):
        return str(self.rpt_id)
