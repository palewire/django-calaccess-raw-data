#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .base import CalAccessBaseModel
from calaccess_raw import fields
from calaccess_raw.annotations import DocumentCloud
from calaccess_raw.annotations.filing_forms import get_filing_form, all_filing_forms
from django.template.defaultfilters import floatformat
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.humanize.templatetags.humanize import intcomma


@python_2_unicode_compatible
class FilernameCd(CalAccessBaseModel):
    """
    A combination of CAL-ACCESS tables to provide the analyst with
    filer information.

    Full name of all PACs, firms, and employers are in the last
    name field.

    Major donors can be split between first and last name fields, but usually
    are contained in the last name field only. Individual names of lobbyists,
    candidates/officeholders, treasurers/responsible officers, and major donors
    (when they are only an individual's name) use both the first and last name
    fields in conjunction.
    """
    UNIQUE_KEY = ("FILER_ID", "NAMID")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=9),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=67, end_page=68),
        DocumentCloud(id='2711615-FAQ', start_page=2),
    ]
    xref_filer_id = fields.CharField(
        verbose_name='crossreference filer ID',
        max_length=15,
        db_column='XREF_FILER_ID',
        db_index=True,
        help_text="Alternative filer ID found on many forms"
    )
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        db_index=True,
        null=True,
        help_text="Filer's unique identification number"
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
            DocumentCloud(id='2774536-Filer-Types-Cd', start_page=1),
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
            DocumentCloud(id='2774537-Filer-Status-Types-Cd', start_page=1)
        ]
    )
    effect_dt = fields.DateField(
        db_column='EFFECT_DT',
        help_text="Effective date for status",
        null=True,
    )
    naml = fields.CharField(
        max_length=200, db_column='NAML',
        help_text="Last name, sometimes full name"
    )
    namf = fields.CharField(
        max_length=55, db_column='NAMF', blank=True,
        help_text="First name"
    )
    namt = fields.CharField(
        max_length=70, db_column='NAMT', blank=True,
        help_text="Name prefix or title"
    )
    nams = fields.CharField(
        max_length=32, db_column='NAMS', blank=True,
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
        verbose_name="State"
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILERNAME_CD'
        verbose_name = 'FILERNAME_CD'
        verbose_name_plural = 'FILERNAME_CD'
        ordering = ("naml", "namf",)

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class FilerFilingsCd(CalAccessBaseModel):
    """
    Key table that links filers to their paper, key data entry, legacy,
    and electronic filings. This table is used as an index to locate
    filing information.
    """
    UNIQUE_KEY = (
        "FILER_ID",
        "FILING_ID",
        "FORM_ID",
        "FILING_SEQUENCE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=8),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=64, end_page=66),
    ]
    FILING_FORMS = all_filing_forms
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
        help_text="Unique filing identificiation number"
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
        ('F470S', get_filing_form('F470').full_title),
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
            DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=65),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=6),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=6),
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
        (0, '0 (Unknown)'),
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
            DocumentCloud(id='2711615-FAQ', start_page=2),
        ],
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_FILINGS_CD'
        verbose_name = 'FILER_FILINGS_CD'
        verbose_name_plural = 'FILER_FILINGS_CD'

    def __str__(self):
        return str("%s %s" % (self.filer_id, self.filing_id))


@python_2_unicode_compatible
class FilingsCd(CalAccessBaseModel):
    """
    This table is the parent table from which all links and association to
    a filing are derived.
    """
    UNIQUE_KEY = "FILING_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=75),
    ]
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=75, end_page=75),
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
            DocumentCloud(id='2711615-FAQ', start_page=2),
        ],
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILINGS_CD'
        verbose_name = 'FILINGS_CD'
        verbose_name_plural = 'FILINGS_CD'

    def __str__(self):
        return str("%s %s" % (self.filing_id, self.filing_type))


@python_2_unicode_compatible
class HdrCd(CalAccessBaseModel):
    """
    Electronic filing record header data. Contains information
    identifying vendor and Cal Format version.
    """
    UNIQUE_KEY = ("FILING_ID", "AMEND_ID")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=79),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=1),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=51),
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
    ef_type = fields.CharField(
        max_length=3,
        db_column='EF_TYPE',
        blank=True,
        help_text='Electronic filing type. This will always have the \
        value of "CAL".'
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
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
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
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
    state_cd = fields.CharField(
        max_length=2,
        db_column='STATE_CD',
        blank=True,
        verbose_name='State code',
        help_text="The state code value entered in the electronic filing"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'HDR_CD'
        verbose_name = 'HDR_CD'
        verbose_name_plural = 'HDR_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class HeaderCd(CalAccessBaseModel):
    """
    Lookup table used to report Form 460 information in the AMS.
    """
    UNIQUE_KEY = ("LINE_NUMBER", "FORM_ID", "REC_TYPE")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=79, end_page=80),
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
        ('F450', get_filing_form('F450').full_title),
        ('F460', get_filing_form('F460').full_title),
        ('F461', get_filing_form('F461').full_title),
        ('FF490', 'Form 490, Part F'),
        ('HF490', 'Form 490, Part H'),
        ('IF490', 'Form 490, Part I'),
    )
    form_id = fields.CharField(
        db_column='FORM_ID',
        max_length=5,
        help_text="Form identification code",
        verbose_name="Form ID"
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'HEADER_CD'
        verbose_name = 'HEADER_CD'
        verbose_name_plural = 'HEADER_CD'

    def __str__(self):
        return str(self.form_id)


@python_2_unicode_compatible
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
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=131, end_page=132),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=86, end_page=87),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=27, end_page=28),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=59, end_page=60),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=35, end_page=37),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=72, end_page=74),
    ]
    FILING_FORMS = [
        get_filing_form('F401'),
        get_filing_form('F401').get_section('A'),
        get_filing_form('F401').get_section('B'),
        get_filing_form('F401').get_section('B-1'),
        get_filing_form('F450'),
        get_filing_form('F460'),
        get_filing_form('F460').get_section('A'),
        get_filing_form('F460').get_section('B1'),
        get_filing_form('F460').get_section('B2'),
        get_filing_form('F460').get_section('B3'),
        get_filing_form('F460').get_section('C'),
        get_filing_form('F460').get_section('D'),
        get_filing_form('F460').get_section('E'),
        get_filing_form('F460').get_section('F'),
        get_filing_form('F460').get_section('G'),
        get_filing_form('F460').get_section('H'),
        get_filing_form('F460').get_section('H1'),
        get_filing_form('F460').get_section('H2'),
        get_filing_form('F460').get_section('H3'),
        get_filing_form('F460').get_section('I'),
        get_filing_form('F461'),
        get_filing_form('F465'),
        get_filing_form('F625'),
        get_filing_form('F625').get_section('P2'),
        get_filing_form('F625').get_section('P3A'),
        get_filing_form('F625').get_section('P3B'),
        get_filing_form('F635'),
        get_filing_form('F635').get_section('P3A'),
        get_filing_form('F635').get_section('P3B'),
        get_filing_form('F635').get_section('P3C'),
        get_filing_form('F635').get_section('P3D'),
        get_filing_form('F635').get_section('P3E'),
        get_filing_form('S640'),
        get_filing_form('F645'),
        get_filing_form('F645').get_section('P2A'),
        get_filing_form('F645').get_section('P2B'),
        get_filing_form('F645').get_section('P2C'),
        get_filing_form('F900'),
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
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS]) + (
        ('401A', get_filing_form('F401').get_section('A')),
        ('401B', get_filing_form('F401').get_section('B')),
        ('401B-1', get_filing_form('F401').get_section('B-1')),
    )
    form_type = fields.CharField(
        max_length=8,
        db_column='FORM_TYPE',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule',
        documentcloud_pages=[
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=86),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=27, end_page=28),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=59, end_page=60),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=36, end_page=37),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=73, end_page=74),
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
        verbose_name='election date'
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'SMRY_CD'
        verbose_name = 'SMRY_CD'
        verbose_name_plural = 'SMRY_CD'
        ordering = ("filing_id", "-amend_id", 'form_type', "line_item")

    def __str__(self):
        return str(self.filing_id)

    def pretty_amount_a(self):
        if self.amount_a is None:
            return None
        return "$%s" % intcomma(floatformat(self.amount_a, 0))
    pretty_amount_a.short_description = 'amount A'

    def pretty_amount_b(self):
        if self.amount_b is None:
            return None
        return "$%s" % intcomma(floatformat(self.amount_b, 0))
    pretty_amount_b.short_description = 'amount B'

    def pretty_amount_c(self):
        if self.amount_c is None:
            return None
        return "$%s" % intcomma(floatformat(self.amount_c, 0))
    pretty_amount_c.short_description = 'amount C'


@python_2_unicode_compatible
class CvrE530Cd(CalAccessBaseModel):
    """
    This table method is undocumented.
    """
    UNIQUE_KEY = ("FILING_ID", "AMEND_ID")
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=29, end_page=30),
    ]
    FILING_FORMS = [
        get_filing_form('E530'),
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
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-format.html#document/p9
        ('', 'Unknown'),
    )
    entity_cd = fields.CharField(
        db_column='ENTITY_CD',
        max_length=32,
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES
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
        verbose_name='Filer state'
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
    district_cd = fields.IntegerField(
        db_column='DISTRICT_CD',
        help_text="This field is undocumented"
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
        choices=OFFICE_CODE_CHOICES
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR_E530_CD'
        verbose_name = 'CVR_E530_CD'
        verbose_name_plural = 'CVR_E530_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class SpltCd(CalAccessBaseModel):
    """
    Split Transaction Record - Used as a child record for schedules:
    A, B1, B2, C, D, H and/or F450P5 when disclosing Per Election to Date information.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "PFORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=132),
        DocumentCloud(id="2711616-MapCalFormat2Fields", start_page=88),
        DocumentCloud(id="2712034-Cal-Format-201", start_page=28),
    ]
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    elec_amount = fields.DecimalField(
        max_digits=16,
        decimal_places=2,
        db_column='ELEC_AMOUNT',
        help_text="This field is undocumented"
    )
    elec_code = fields.CharField(
        max_length=2,
        db_column='ELEC_CODE',
        blank=True,
        help_text='This field is undocumented',
    )
    elec_date = fields.DateField(
        db_column='ELEC_DATE',
        null=True,
        help_text="This field is undocumented"
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    PFORM_TYPE_CHOICES = (
        ('A', ''),
        ('B1', ''),
        ('B2', ''),
        ('C', ''),
        ('D', ''),
        ('F450P5', ''),
        ('H', ''),
    )
    pform_type = fields.CharField(
        max_length=7,
        db_column='PFORM_TYPE',
        db_index=True,
        choices=PFORM_TYPE_CHOICES,
        help_text='This field is undocumented',
    )
    ptran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=32,
        db_column='PTRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'SPLT_CD'
        verbose_name = 'SPLT_CD'
        verbose_name_plural = 'SPLT_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class TextMemoCd(CalAccessBaseModel):
    """
    Text memos attached to electronic filings
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=14),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=133, end_page=134),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=89, end_page=90),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=15, end_page=16),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=13),
    ]

    FILING_FORMS = [
        get_filing_form('F401'),
        get_filing_form('F405'),
        get_filing_form('F410'),
        get_filing_form('F425'),
        get_filing_form('F450'),
        get_filing_form('F460'),
        get_filing_form('F461'),
        get_filing_form('F465'),
        get_filing_form('F496'),
        get_filing_form('F497'),
        get_filing_form('F498'),
        get_filing_form('F601'),
        get_filing_form('F602'),
        get_filing_form('F603'),
        get_filing_form('F604'),
        get_filing_form('F605'),
        get_filing_form('F606'),
        get_filing_form('F607'),
        get_filing_form('F615'),
        get_filing_form('F625'),
        get_filing_form('F635'),
        get_filing_form('F645'),
        get_filing_form('S630'),
        get_filing_form('S635C'),
        get_filing_form('S640'),
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
        verbose_name='record type'
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS]) + (
        ('410', get_filing_form('F410').full_title),
        ('460', get_filing_form('F460').full_title),
        ('461', get_filing_form('F461').full_title),
        ('465', get_filing_form('F465').full_title),
        ('496', get_filing_form('F496').full_title),
        ('497', get_filing_form('F497').full_title),
        ('497P1', get_filing_form('F497').get_section('P1').full_title),
        ('497P2', get_filing_form('F497').get_section('P2').full_title),
        ('F401A', get_filing_form('F401').get_section('A').full_title),
        ('F401B', get_filing_form('F401').get_section('B').full_title),
        ('F401B-1', get_filing_form('F401').get_section('B-1').full_title),
        ('F450P5', get_filing_form('F450').get_section('P5').full_title),
        ('F461P1', get_filing_form('F461').get_section('P1').full_title),
        ('F461P2', get_filing_form('F461').get_section('P2').full_title),
        ('F461P5', get_filing_form('F461').get_section('P5').full_title),
        ('F465P3', get_filing_form('F465').get_section('P3').full_title),
        ('F496P3', get_filing_form('F496').get_section('P3').full_title),
        ('F497P1', get_filing_form('F497').get_section('P1').full_title),
        ('F497P2', get_filing_form('F497').get_section('P2').full_title),
        ('F498-A', get_filing_form('F498').get_section('A').full_title),
        ('F498-R', get_filing_form('F498').get_section('R').full_title),
        ('F601P2A', get_filing_form('F601').get_section('P2A').full_title),
        ('F601P2B', get_filing_form('F601').get_section('P2B').full_title),
        ('F615P1', get_filing_form('F615').get_section('P1').full_title),
        ('F615P2', get_filing_form('F615').get_section('P2').full_title),
        ('F625P2', get_filing_form('F625').get_section('P2').full_title),
        ('F625P3A', get_filing_form('F625').get_section('P3A').full_title),
        ('F625P3B', get_filing_form('F625').get_section('P3B').full_title),
        ('F625P4B', get_filing_form('F625').get_section('P4B').full_title),
        ('F635P3B', get_filing_form('F635').get_section('P3B').full_title),
        ('F635P3C', get_filing_form('F635').get_section('P3C').full_title),
        ('F635P4B', get_filing_form('F635').get_section('P4B').full_title),
        ('F645P2A', get_filing_form('F645').get_section('P2A').full_title),
        ('F645P3B', get_filing_form('F645').get_section('P3B').full_title),
        ('S497', get_filing_form('F497').full_title),
        ('S635C', get_filing_form('S635C').full_title),
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
        ('DEBTF', get_filing_form('F460').get_section('F').full_title),
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
            DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=90),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=16),
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=13),
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'TEXT_MEMO_CD'
        verbose_name = 'TEXT_MEMO_CD'
        verbose_name_plural = 'TEXT_MEMO_CD'

    def __str__(self):
        return str(self.filing_id)
