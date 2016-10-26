#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Models for storing inactive and deprecated tables from the CAL-ACCESS database.
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
class BallotMeasuresCd(CalAccessBaseModel):
    """
    Ballot-measure dates and times.
    """
    UNIQUE_KEY = "FILER_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=7),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=19),
    ]
    election_date = fields.DateField(
        db_column='ELECTION_DATE',
        null=True,
        help_text="Ballot measure election date"
    )
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    measure_no = fields.CharField(
        db_column='MEASURE_NO',
        max_length=2,
        help_text="Ballot measure number"
    )
    measure_name = fields.CharField(
        db_column='MEASURE_NAME',
        max_length=163,
        help_text="Ballot measure full name"
    )
    measure_short_name = fields.CharField(
        db_column='MEASURE_SHORT_NAME',
        max_length=50,
        blank=True,
        help_text="Ballot measure short name"
    )
    jurisdiction = fields.CharField(
        db_column='JURISDICTION',
        max_length=9,
        help_text="This field is undocumented"
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'BALLOT_MEASURES_CD'
        ordering = (
            "-election_date",
            "measure_no",
            "measure_short_name",
            "measure_name"
        )

    def __str__(self):
        return self.measure_name


@python_2_unicode_compatible
class CvrF470Cd(CalAccessBaseModel):
    """
    The cover page for officeholder and candidate short and supplemental forms.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "REC_TYPE",
        "FORM_TYPE",
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=8),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=30, end_page=32),
        DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=15, end_page=16),
        DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=22),
        DocumentCloud(id='2712034-Cal-Format-201', start_page=29, end_page=30),
    ]
    FILING_FORMS = [
        get_filing_form('F470'),
    ]
    amend_id = fields.IntegerField(
        db_column="AMEND_ID",
        db_index=True,
        help_text="Amendment Identification number. A number of 0 is an original filing and 1 "
                  "to 999 amendments."
    )
    cand_adr1 = fields.CharField(
        db_column="CAND_ADR1",
        blank=True,
        max_length=55,
        help_text="First line of the filer's street address."
    )
    cand_adr2 = fields.CharField(
        db_column="CAND_ADR2",
        blank=True,
        max_length=55,
        help_text="Second line of the filer's street address. "
    )
    cand_city = fields.CharField(
        db_column="CAND_CITY",
        blank=True,
        max_length=30,
        help_text="Candidate/Officeholder's City."
    )
    cand_email = fields.CharField(
        db_column="CAND_EMAIL",
        blank=True,
        max_length=60,
        help_text="Candidate/Officeholder's EMail address. Not required by the form."
    )
    cand_fax = fields.CharField(
        db_column="CAND_FAX",
        blank=True,
        max_length=20,
        help_text="Candidate/Officeholder's FAX Phone Number. Not required by the form."
    )
    cand_phon = fields.CharField(
        db_column="CAND_PHON",
        blank=True,
        max_length=20,
        help_text="Candidate/Officeholder's phone number."
    )
    cand_st = fields.CharField(
        db_column="CAND_ST",
        blank=True,
        max_length=2,
        help_text="Filer's State"
    )
    cand_zip4 = fields.CharField(
        db_column="CAND_ZIP4",
        blank=True,
        max_length=10,
        help_text="Filer's zipcode"
    )
    date_1000 = fields.DateField(
        db_column="DATE_1000",
        help_text="Date contributions totaling $1,000 or more. (For the 470-S)"
    )
    dist_no = fields.CharField(
        db_column="DIST_NO",
        blank=True,
        max_length=3,
        help_text="District number for the office being sought. Populated for Senate, Assembly, "
                  "or Board of Equalization races."
    )
    elect_date = fields.DateField(
        db_column="ELECT_DATE",
        help_text="Date of the general election. Required for filings in even years."
    )
    ENTITY_CD_CHOICES = (
        ('CAO', choices.CAMPAIGN_ENTITY_CODES['CAO']),
    )
    entity_cd = fields.CharField(
        db_column="ENTITY_CD",
        blank=True,
        choices=ENTITY_CD_CHOICES,
        max_length=3,
        help_text="The filer's entity code. The value of this column will always be "
                  "Candidate/Office Holder (CAO) for this table.",
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=22),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=29)
        ]
    )
    filer_id = fields.CharField(
        db_column="FILER_ID",
        blank=True,
        max_length=9,
        help_text="Filer's unique identification number."
    )
    filer_namf = fields.CharField(
        db_column="FILER_NAMF",
        blank=True,
        max_length=45,
        help_text="Filer's First Name(s) - required for individuals"
    )
    filer_naml = fields.CharField(
        db_column="FILER_NAML",
        blank=True,
        max_length=200,
        help_text="Filer's Last Name/Committee name"
    )
    filer_nams = fields.CharField(
        db_column="FILER_NAMS",
        blank=True,
        max_length=10,
        help_text="Filer's Name Suffix"
    )
    filer_namt = fields.CharField(
        db_column="FILER_NAMT",
        blank=True,
        max_length=10,
        help_text="The filer's prefix or title that preceeds their name if they are an individual."
    )
    filing_id = fields.IntegerField(
        db_column="FILING_ID",
        db_index=True,
        help_text="Unique filing identification number."
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_type = fields.CharField(
        db_column="FORM_TYPE",
        choices=FORM_TYPE_CHOICES,
        db_index=True,
        max_length=4,
        help_text="Type of Filing or Formset. The value of this column will always "
                  "be equal to F470.",
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=22),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=29),
        ]
    )
    JURIS_CD_CHOICES = get_sorted_choices(choices.JURIS_CODES)
    juris_cd = fields.CharField(
        db_column="JURIS_CD",
        choices=JURIS_CD_CHOICES,
        blank=True,
        max_length=3,
        help_text="Office Jurisdiction Code",
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=22),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=29),
        ]
    )
    juris_dscr = fields.CharField(
        db_column="JURIS_DSCR",
        blank=True,
        max_length=40,
        help_text="Office jurisdiction description text reqired if the jurisdiction code "
                  "(Juris_cd) is equal to CIT, CTY, LOC, or OTH."
    )
    OFF_S_H_CD_CHOICES = get_sorted_choices(choices.OFF_S_H_CODES)
    off_s_h_cd = fields.CharField(
        db_column="OFF_S_H_CD",
        choices=OFF_S_H_CD_CHOICES,
        blank=True,
        max_length=1,
        help_text='Office Sought/Held code. Legal values are "S" for sought and "H" for held.',
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=22),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=30),
        ]
    )
    offic_dscr = fields.CharField(
        db_column="OFFIC_DSCR",
        blank=True,
        max_length=40,
        help_text="Office sought description used if the office code is other (OTH)."
    )
    OFFICE_CD_CODES = get_sorted_choices(choices.OFFICE_CODES)
    office_cd = fields.CharField(
        db_column="OFFICE_CD",
        choices=OFFICE_CD_CODES,
        blank=True,
        max_length=3,
        help_text="Code that identifies the office being sought. See the CAL document for "
                  "a list of valid codes.",
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=22),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=29),
        ]
    )
    REC_TYPE_CHOICES = (
        ('CVR', 'Cover Page'),
    )
    rec_type = fields.CharField(
        db_column="REC_TYPE",
        choices=REC_TYPE_CHOICES,
        blank=True,
        max_length=3,
        help_text="Type of CAL record. This column will always contain CVR.",
        documentcloud_pages=[
            DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=22),
            DocumentCloud(id='2712034-Cal-Format-201', start_page=29),
        ]
    )
    report_num = fields.CharField(
        db_column="REPORT_NUM",
        blank=True,
        max_length=3,
        help_text="Report Number; 000 Original; 001-999 Amended as reported in the filing."
    )
    rpt_date = fields.DateField(
        db_column="RPT_DATE",
        db_index=True,
        null=True,
        help_text="Date this report is filed as reported by the filer."
    )

    def __str__(self):
        return str(self.amend_id)

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'CVR_F470_CD'


@python_2_unicode_compatible
class FilerTypePeriodsCd(CalAccessBaseModel):
    """
    Undocumented.

    The table's official description contains this note: "J M needs to document. This is
    in his list of tables designed for future enhancements."
    """
    UNIQUE_KEY = (
        "ELECTION_TYPE",
        "FILER_TYPE",
        "PERIOD_ID",
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=8),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=71),
    ]
    ELECTION_TYPE_CHOICES = (
        (0, 'N/A'),
        (3001, 'GENERAL'),
        (3002, 'PRIMARY'),
        (3003, 'RECALL'),
        (3004, 'SPECIAL ELECTION'),
        (3005, 'OFFICEHOLDER'),
        (3006, 'SPECIAL RUNOFF'),
    )
    election_type = fields.IntegerField(
        db_column="ELECTION_TYPE",
        db_index=True,
        choices=ELECTION_TYPE_CHOICES,
        help_text="Election type",
        documentcloud_pages=[
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=3, end_page=4),
        ],
    )
    filer_type = fields.ForeignKeyField(
        'FilerTypesCd',
        related_name='filing_type_periods',
        db_constraint=False,
        db_column="FILER_TYPE",
        db_index=True,
        help_text="Foreign key referencing FilerTypesCd.filer_type",
    )
    period_id = fields.ForeignKeyField(
        'FilingPeriodCd',
        related_name='filing_type_periods',
        db_constraint=False,
        db_column="PERIOD_ID",
        db_index=True,
        help_text="Foreign key referencing FilingPeriodCd.period_id",
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'FILER_TYPE_PERIODS_CD'

    def __str__(self):
        return str(self.election_type)


@python_2_unicode_compatible
class LobbyistContributions1Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of campaign contributions made by lobbyists.

    This table is 95 percent identical to LOBBYIST_CONTRIBUTIONS2_CD and LOBBYIST_CONTRIBUTIONS3_CD.

    According to "Cal-Access Tables, Columns, Indexes", this is a temporary
    table used to generate the actual Lobbyist contribution disclosure table,
    which is LOBBYIST_CONTRIBUTIONS3_CD.

    Also, the most recent values observed in FILING_PERIOD_START_DT are for the
    April 2001, so probably this table is no longer in use.
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
        verbose_name='Filing period start date',
        help_text='Start date of filing period',
    )
    filing_period_end_dt = fields.DateField(
        db_column='FILING_PERIOD_END_DT',
        null=True,
        verbose_name='Filing period end date',
        help_text='End date of filing period',
    )
    contribution_dt = fields.CharField(
        db_column='CONTRIBUTION_DT',
        max_length=32,
        blank=True,
        verbose_name='Contribution date',
        help_text='Date of contribution',
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_CONTRIBUTIONS1_CD'
        ordering = ("-filing_period_start_dt",)

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class LobbyistContributions2Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of campaign contributions made by lobbyists.

    This table is 95 percent identical to LOBBYIST_CONTRIBUTIONS1_CD and LOBBYIST_CONTRIBUTIONS3_CD.

    According to "Cal-Access Tables, Columns, Indexes", this is a temporary
    table used to generate the actual Lobbyist contribution disclosure table,
    which is LOBBYIST_CONTRIBUTIONS3_CD.

    Also, the most recent values observed in FILING_PERIOD_START_DT are for the
    April 2001, so probably this table is no longer in use.
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
        verbose_name='Filing period start date',
        help_text='Start date of filing period',
    )
    filing_period_end_dt = fields.DateField(
        db_column='FILING_PERIOD_END_DT',
        null=True,
        verbose_name='Filing period end date',
        help_text='End date of filing period',
    )
    contribution_dt = fields.CharField(
        db_column='CONTRIBUTION_DT',
        max_length=32,
        blank=True,
        verbose_name='Contribution date',
        help_text='Date of contribution',
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_CONTRIBUTIONS2_CD'
        ordering = ("-filing_period_start_dt",)

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class LobbyistContributions3Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of campaign contributions made by lobbyists.

    This table is 95 percent identical to LOBBYIST_CONTRIBUTIONS1_CD and LOBBYIST_CONTRIBUTIONS2_CD.

    According to "Cal-Access Tables, Columns, Indexes", this is the actual
    Lobbyist contribution disclosure table generated from the other two
    temporary tables: LOBBYIST_CONTRIBUTIONS1_CD and LOBBYIST_CONTRIBUTIONS2_CD.

    Also, the most recent values observed in FILING_PERIOD_START_DT are for the
    April 2001, so probably this table is no longer in use.
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
        verbose_name='Filing period start date',
        help_text='Start date of filing period',
    )
    filing_period_end_dt = fields.DateField(
        db_column='FILING_PERIOD_END_DT',
        null=True,
        verbose_name='Filing period end date',
        help_text='End date of filing period',
    )
    contribution_dt = fields.CharField(
        db_column='CONTRIBUTION_DT',
        max_length=32,
        blank=True,
        verbose_name='Contribution date',
        help_text='Date of contribution',
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_CONTRIBUTIONS3_CD'
        ordering = ("-filing_period_start_dt",)

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class LobbyistEmpLobbyist1Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is identical to LOBBYIST_EMP_LOBBYIST2_CD.

    Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
    this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also, the distinct SESSION_ID values span from 1995 to 2001, so probably this
    table is no longer in use.
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_EMP_LOBBYIST1_CD'
        ordering = ("-session_id",)

    def __str__(self):
        return str(self.lobbyist_id)


@python_2_unicode_compatible
class LobbyistEmpLobbyist2Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is identical to LOBBYIST_EMP_LOBBYIST1_CD.

    Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
    this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also, the distinct SESSION_ID values span from 1995 to 2001, so probably this
    table is no longer in use.
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_EMP_LOBBYIST2_CD'
        ordering = ("-session_id",)

    def __str__(self):
        return str(self.lobbyist_id)


@python_2_unicode_compatible
class LobbyistEmployer1Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is 99 percent identical to LOBBYIST_EMPLOYER2_CD and LOBBYIST_EMPLOYER3_CD.

    All three tables are documented in "Cal-Access Tables, Columns, Indexes", but
    with this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also, the only value in observed in SESSION_YR_1 is 1999 and the only value
    observed in SESSION_YR_2 is 2000.
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
    INTEREST_CD_CHOICES = (
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
        choices=INTEREST_CD_CHOICES,
        blank=True,
        null=True,
        verbose_name="interest code",
        help_text='Interest Code',
        documentcloud_pages=[
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=19),
        ],
    )
    interest_name = fields.CharField(
        db_column='INTEREST_NAME',
        max_length=24,
        blank=True,
        verbose_name="Interest name",
        help_text="Interest name",
    )
    session_yr_1 = fields.IntegerField(
        db_column='SESSION_YR_1',
        verbose_name="Total amount of year 1 of the session",
        help_text="Total amount of year 1 of the session",
    )
    session_yr_2 = fields.IntegerField(
        db_column='SESSION_YR_2',
        verbose_name="Total amount of year 2 of the session",
        help_text="Total amount of year 2 of the session",
    )
    yr_1_ytd_amt = fields.FloatField(
        db_column='YR_1_YTD_AMT',
        verbose_name="Year 1 year-to-date-amount",
        help_text="Year 1 year-to-date-amount",
    )
    yr_2_ytd_amt = fields.FloatField(
        db_column='YR_2_YTD_AMT',
        verbose_name="Year 2 year-to-date-amount",
        help_text="Year 2 year-to-date-amount",
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_EMPLOYER1_CD'
        ordering = ("-session_id",)

    def __str__(self):
        return str(self.employer_id)


@python_2_unicode_compatible
class LobbyistEmployer2Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is 99 percent identical to LOBBYIST_EMPLOYER1_CD and LOBBYIST_EMPLOYER3_CD.

    All three tables are documented in "Cal-Access Tables, Columns, Indexes", but
    with this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also, the only value in observed in SESSION_YR_1 is 1999 and the only value
    observed in SESSION_YR_2 is 2000.
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
    INTEREST_CD_CHOICES = (
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
        choices=INTEREST_CD_CHOICES,
        verbose_name="interest code",
        help_text='Interest Code',
        documentcloud_pages=[
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=19),
        ],
    )
    interest_name = fields.CharField(
        db_column='INTEREST_NAME',
        max_length=24,
        blank=True,
        help_text="Interest name"
    )
    session_yr_1 = fields.IntegerField(
        db_column='SESSION_YR_1',
        verbose_name="Total amount of year 1 of the session",
        help_text="Total amount of year 1 of the session",
    )
    session_yr_2 = fields.IntegerField(
        db_column='SESSION_YR_2',
        verbose_name="Total amount of year 2 of the session",
        help_text="Total amount of year 2 of the session",
    )
    yr_1_ytd_amt = fields.FloatField(
        db_column='YR_1_YTD_AMT',
        verbose_name="Year 1 year-to-date-amount",
        help_text="Year 1 year-to-date-amount",
    )
    yr_2_ytd_amt = fields.FloatField(
        db_column='YR_2_YTD_AMT',
        verbose_name="Year 2 year-to-date-amount",
        help_text="Year 2 year-to-date-amount",
    )
    qtr_1 = fields.FloatField(
        db_column='QTR_1',
        verbose_name="Quarter 1",
        help_text="Quarter 1 total amount",
    )
    qtr_2 = fields.FloatField(
        db_column='QTR_2',
        verbose_name="Quarter 2",
        help_text="Quarter 2 total amount",
    )
    qtr_3 = fields.FloatField(
        db_column='QTR_3',
        verbose_name="Quarter 3",
        help_text="Quarter 3 total amount",
    )
    qtr_4 = fields.FloatField(
        db_column='QTR_4',
        verbose_name="Quarter 4",
        help_text="Quarter 4 total amount",
    )
    qtr_5 = fields.FloatField(
        db_column='QTR_5',
        verbose_name="Quarter 5",
        help_text="Quarter 5 total amount",
    )
    qtr_6 = fields.FloatField(
        db_column='QTR_6',
        verbose_name="Quarter 6",
        help_text="Quarter 6 total amount",
    )
    qtr_7 = fields.FloatField(
        db_column='QTR_7',
        verbose_name="Quarter 7",
        help_text="Quarter 7 total amount",
    )
    qtr_8 = fields.FloatField(
        db_column='QTR_8',
        verbose_name="Quarter 8",
        help_text="Quarter 8 total amount",
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_EMPLOYER2_CD'
        ordering = ("-session_id",)

    def __str__(self):
        return str(self.employer_id)


@python_2_unicode_compatible
class LobbyistEmployer3Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is 99 percent identical to LOBBYIST_EMPLOYER1_CD and LOBBYIST_EMPLOYER2_CD.

    All three tables are documented in "Cal-Access Tables, Columns, Indexes", but
    with this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also, the only value in observed in SESSION_YR_1 is 1999 and the only value
    observed in SESSION_YR_2 is 2000.
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
    INTEREST_CD_CHOICES = (
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
        choices=INTEREST_CD_CHOICES,
        verbose_name="interest code",
        help_text='Interest Code',
        documentcloud_pages=[
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=19),
        ],
    )
    interest_name = fields.CharField(
        db_column='INTEREST_NAME',
        max_length=24,
        blank=True,
        help_text="Interest name"
    )
    session_yr_1 = fields.IntegerField(
        db_column='SESSION_YR_1',
        verbose_name="Total amount of year 1 of the session",
        help_text="Total amount of year 1 of the session",
    )
    session_yr_2 = fields.IntegerField(
        db_column='SESSION_YR_2',
        verbose_name="Total amount of year 2 of the session",
        help_text="Total amount of year 2 of the session",
    )
    yr_1_ytd_amt = fields.FloatField(
        db_column='YR_1_YTD_AMT',
        verbose_name="Year 1 year-to-date-amount",
        help_text="Year 1 year-to-date-amount",
    )
    yr_2_ytd_amt = fields.FloatField(
        db_column='YR_2_YTD_AMT',
        verbose_name="Year 2 year-to-date-amount",
        help_text="Year 2 year-to-date-amount",
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_EMPLOYER3_CD'
        ordering = ("-session_id",)

    def __str__(self):
        return str(self.employer_id)


@python_2_unicode_compatible
class LobbyistEmployerFirms1Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is identical to LOBBYIST_EMPLOYER_FIRMS2_CD.

    Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
    this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also the distinct SESSION_ID values span from 1995 to 2001, so probably this
    table is no longer in use.
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_EMPLOYER_FIRMS1_CD'
        ordering = ("-session_id",)

    def __str__(self):
        return str(self.employer_id)


@python_2_unicode_compatible
class LobbyistEmployerFirms2Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is identical to LOBBYIST_EMPLOYER_FIRMS1_CD.

    Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
    this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also the distinct SESSION_ID values span from 1995 to 2001, so probably this
    table is no longer in use.
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_EMPLOYER_FIRMS2_CD'
        ordering = ("-session_id",)

    def __str__(self):
        return str(self.employer_id)


@python_2_unicode_compatible
class LobbyistEmployerHistoryCd(CalAccessBaseModel):
    """
    Undocumented.

    An empty file of the same name is included in the Secretary of State's daily CAL-ACCESS database exports.

    This table is documented in "Cal-Access Tables, Columns, Indexes", but with
    this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation
    on these tables. Cox 5/11/2000".

    Also, the columns on this table are identical to the columns on the
    LOBBYIST_EMPLOYER1_CD, LOBBYIST_EMPLOYER2_CD and LOBBYIST_EMPLOYER3_CD
    tables.
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
    INTEREST_CD_CHOICES = (
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
        db_column="INTEREST_CD",
        choices=INTEREST_CD_CHOICES,
        verbose_name='interest code',
        help_text='Interest Code',
        documentcloud_pages=[
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=19),
        ],
    )
    interest_name = fields.CharField(
        db_column="INTEREST_NAME",
        max_length=300,
        blank=True,
        verbose_name="Interest name.",
        help_text="Interest name.",
    )
    qtr_1 = fields.IntegerField(
        db_column="QTR_1",
        verbose_name="quarter 1 amount",
        help_text="Quarter 1 total amount.",
    )
    qtr_2 = fields.IntegerField(
        db_column="QTR_2",
        verbose_name="quarter 2 amount.",
        help_text="Quarter 2 total amount.",
    )
    qtr_3 = fields.IntegerField(
        db_column="QTR_3",
        verbose_name="quarter 3 amount",
        help_text="Quarter 3 total amount.",
    )
    qtr_4 = fields.IntegerField(
        db_column="QTR_4",
        verbose_name="quarter 4 amount",
        help_text="Quarter 4 total amount.",
    )
    qtr_5 = fields.IntegerField(
        db_column="QTR_5",
        verbose_name="quarter 5 amount5",
        help_text="Quarter 5 total amount.",
    )
    qtr_6 = fields.IntegerField(
        db_column="QTR_6",
        verbose_name="quarter 6 amount.",
        help_text="Quarter 6 total amount.",
    )
    qtr_7 = fields.IntegerField(
        db_column="QTR_7",
        verbose_name="quarter 7 amount.",
        help_text="Quarter 7 total amount.",
    )
    qtr_8 = fields.IntegerField(
        db_column="QTR_8",
        verbose_name="quarter 8 amount.",
        help_text="Quarter 8 total amount.",
    )
    session_id = fields.IntegerField(
        db_column="SESSION_ID",
        verbose_name="session identification number.",
        help_text="Session identification number.",
    )
    session_total_amt = fields.IntegerField(
        db_column="SESSION_TOTAL_AMT",
        verbose_name="session total amount",
        help_text="Total amount for the session.",
    )
    session_yr_1 = fields.IntegerField(
        db_column="SESSION_YR_1",
        verbose_name="session year 1",
        help_text="Total amount for year 1 of the session.",
    )
    session_yr_2 = fields.IntegerField(
        db_column="SESSION_YR_2",
        verbose_name="session year 2",
        help_text="Total amount for year 2 of the session.",
    )
    yr_1_ytd_amt = fields.IntegerField(
        db_column="YR_1_YTD_AMT",
        help_text="Year 1 year to date amount.",
    )
    yr_2_ytd_amt = fields.IntegerField(
        db_column="YR_2_YTD_AMT",
        help_text="Year 2 year to date amount.",
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_EMPLOYER_HISTORY_CD'

    def __str__(self):
        return str(self.contributor_id)


@python_2_unicode_compatible
class LobbyistFirm1Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is identical to LOBBYIST_FIRM2_CD and LOBBYIST_FIRM3_CD.

    All three tables are documented in "Cal-Access Tables, Columns, Indexes", but
    with this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also, the distinct SESSION_YR_1 values are 2001, and the distinct SESSION_YR_2
    are 2002.
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
        help_text="Year 1 year-to-date-amount",
    )
    yr_2_ytd_amt = fields.FloatField(
        db_column='YR_2_YTD_AMT',
        verbose_name="Year 2 year-to-date-amount",
        help_text="Year 2 year-to-date-amount",
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_FIRM1_CD'

    def __str__(self):
        return str(self.firm_id)


@python_2_unicode_compatible
class LobbyistFirm2Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is identical to LOBBYIST_FIRM1_CD and LOBBYIST_FIRM3_CD.

    All three tables are documented in "Cal-Access Tables, Columns, Indexes", but
    with this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also, the distinct SESSION_YR_1 values are 2001, and the distinct SESSION_YR_2
    are 2002.
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
        help_text="Year 1 year-to-date-amount",
    )
    yr_2_ytd_amt = fields.FloatField(
        db_column='YR_2_YTD_AMT',
        verbose_name="Year 2 year-to-date-amount",
        help_text="Year 2 year-to-date-amount",
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_FIRM2_CD'

    def __str__(self):
        return str(self.firm_id)


@python_2_unicode_compatible
class LobbyistFirm3Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is identical to LOBBYIST_FIRM1_CD and LOBBYIST_FIRM2_CD.

    All three tables are documented in "Cal-Access Tables, Columns, Indexes", but
    with this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also, the distinct SESSION_YR_1 values are 2001, and the distinct SESSION_YR_2
    are 2002.
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
        help_text="Year 1 year-to-date-amount",
    )
    yr_2_ytd_amt = fields.FloatField(
        db_column='YR_2_YTD_AMT',
        verbose_name="Year 2 year-to-date-amount",
        help_text="Year 2 year-to-date-amount",
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_FIRM3_CD'

    def __str__(self):
        return str(self.firm_id)


@python_2_unicode_compatible
class LobbyistFirmEmployer1Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is identical to LOBBYIST_FIRM_EMPLOYER2_CD.

    Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
    this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also RPT_START and RPT_END each contain only one distinct value, "2001-04-01"
    and "2001-06-30", respectively.
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
        help_text="Unique filing identification number"
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_FIRM_EMPLOYER1_CD'
        ordering = ("-rpt_start",)

    def __str__(self):
        return str(self.firm_id)


@python_2_unicode_compatible
class LobbyistFirmEmployer2Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is identical to LOBBYIST_FIRM_EMPLOYER1_CD.

    Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
    this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also RPT_START and RPT_END each contain only one distinct value, "2001-04-01"
    and "2001-06-30", respectively.
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
        help_text="Unique filing identification number"
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_FIRM_EMPLOYER2_CD'
        ordering = ("-rpt_start",)

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class LobbyistFirmHistoryCd(CalAccessBaseModel):
    """
    Undocumented.

    An empty file of the same name is included in the Secretary of State's daily CAL-ACCESS database exports.

    This table is documented in "Cal-Access Tables, Columns, Indexes", but with
    this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation
    on these tables. Cox 5/11/2000".

    Also, the columns on this table are identical to the columns on the
    LOBBYIST_FIRM1_CD, LOBBYIST_FIRM2_CD and LOBBYIST_FIRM3_CD tables.
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
        verbose_name="Year 1 year to date amount.",
        help_text="Year 1 year to date amount.",
    )
    yr_2_ytd_amt = fields.IntegerField(
        db_column="YR_2_YTD_AMT",
        verbose_name="Year 2 year to date amount",
        help_text="Year 2 year to date amount",
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_FIRM_HISTORY_CD'

    def __str__(self):
        return str(self.contributor_id)


@python_2_unicode_compatible
class LobbyistFirmLobbyist1Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is identical to LOBBYIST_FIRM_LOBBYIST2_CD.

    Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
    this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also, all rows have the same SESSION_ID value: 2001.
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_FIRM_LOBBYIST1_CD'
        ordering = ("-session_id",)

    def __str__(self):
        return str(self.lobbyist_id)


@python_2_unicode_compatible
class LobbyistFirmLobbyist2Cd(CalAccessBaseModel):
    """
    Deprecated table for the disclosure of lobbyist relationships.

    This table is identical to LOBBYIST_FIRM_LOBBYIST1_CD.

    Both tables are documented in "Cal-Access Tables, Columns, Indexes", but with
    this cryptic note: "Matt needs to describe the relationship between the
    multiple tables. Documentation should be cloned from D H's documentation on
    these tables. Cox 5/11/2000".

    Also, all rows have the same SESSION_ID value: 2001.
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

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'LOBBYIST_FIRM_LOBBYIST2_CD'
        ordering = ("-session_id",)

    def __str__(self):
        return str(self.lobbyist_id)


@python_2_unicode_compatible
class EfsFilingLogCd(CalAccessBaseModel):
    """
    Logs from the Electronic Filing Subsystem, which accepts and validates electronic filings.
    """
    UNIQUE_KEY = (
        "FILING_DATE",
        "VENDOR"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711624-Overview', start_page=1, end_page=2),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=49, end_page=50),
    ]
    FILING_FORMS = [
        get_filing_form('F400'),
        get_filing_form('F401'),
        get_filing_form('F402'),
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
        get_filing_form('F606'),
        get_filing_form('F607'),
        get_filing_form('F615'),
        get_filing_form('F625'),
        get_filing_form('F635'),
        get_filing_form('F645'),
    ]
    filing_date = fields.DateField(
        db_column='FILING_DATE',
        null=True,
        help_text="Date of filing"
    )
    filingstatus = fields.IntegerField(
        db_column='FILINGSTATUS',
        help_text="Status of filing. This field is described in the docs as being\
VARCHAR. However, its distinct values are 0, 1, 2 and 7.",
    )
    vendor = fields.CharField(
        db_column='VENDOR',
        max_length=250,
        help_text="Software vendor who submitted the electronic filing"
    )
    filer_id = fields.CharField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        max_length=250,
        blank=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    FORM_TYPE_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS]) + (
        ('BADFORMAT 253', 'Unknown'),
        ('form', 'Unknown'),
    )
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=250,
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        verbose_name="form type",
        documentcloud_pages=[
            DocumentCloud(id='2711624-Overview', start_page=4, end_page=8),
        ]
    )
    error_no = fields.CharField(
        db_column='ERROR_NO',
        max_length=250,
        help_text='Most records have a value of "ACCEPTED". Other records include "ERROR"\
or "BADFORMAT" and a three-digit number.',
    )

    class Meta(CalAccessBaseModel.Meta):
        """
        Meta model options.
        """
        db_table = 'EFS_FILING_LOG_CD'
        ordering = ("-filing_date",)

    def __str__(self):
        return "{} ({})".format(self.vendor, self.filing_date)
