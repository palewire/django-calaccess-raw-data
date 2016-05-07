#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .base import CalAccessBaseModel
from calaccess_raw import fields
from calaccess_raw.annotations import DocumentCloud
from calaccess_raw.annotations.filing_forms import get_filing_form
from django.db.models import ForeignKey
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class AcronymsCd(CalAccessBaseModel):
    """
    Contains acronyms and their meaning.
    """
    UNIQUE_KEY = "ACRONYM"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=7),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=16),
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'ACRONYMS_CD'
        verbose_name = 'ACRONYMS_CD'
        verbose_name_plural = 'ACRONYMS_CD'
        ordering = ("acronym",)

    def __str__(self):
        return self.acronym


@python_2_unicode_compatible
class AddressCd(CalAccessBaseModel):
    """
    This table holds all addresses for the system. This table can be used
    for address-based searches and formes the bases for address information
    desplayed by the AMS.
    """
    UNIQUE_KEY = "ADRID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=7),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=16),
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'ADDRESS_CD'
        verbose_name = 'ADDRESS_CD'
        verbose_name_plural = 'ADDRESS_CD'

    def __str__(self):
        return str(self.adrid)


@python_2_unicode_compatible
class BallotMeasuresCd(CalAccessBaseModel):
    """
    Ballot measure dates and times
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'BALLOT_MEASURES_CD'
        verbose_name = 'BALLOT_MEASURES_CD'
        verbose_name_plural = 'BALLOT_MEASURES_CD'
        ordering = (
            "-election_date",
            "measure_no",
            "measure_short_name",
            "measure_name"
        )

    def __str__(self):
        return self.measure_name


@python_2_unicode_compatible
class EfsFilingLogCd(CalAccessBaseModel):
    """
    This is an undocumented model.
    """
    UNIQUE_KEY = (
        "FILING_DATE",
        "VENDOR"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=49, end_page=50)
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
        help_text="This field is undocumented"
    )
    filingstatus = fields.IntegerField(
        db_column='FILINGSTATUS',
        help_text="This field is undocumented",
    )
    vendor = fields.CharField(
        db_column='VENDOR',
        max_length=250,
        help_text="This field is undocumented"
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
    )
    error_no = fields.CharField(
        db_column='ERROR_NO',
        max_length=250,
        help_text="This field is undocumented",
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'EFS_FILING_LOG_CD'
        verbose_name = 'EFS_FILING_LOG_CD'
        verbose_name_plural = 'EFS_FILING_LOG_CD'

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class FilersCd(CalAccessBaseModel):
    """
    This table is the parent table from which all links and associations
    to a filer are derived.
    """
    UNIQUE_KEY = "FILER_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=9),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=73),
    ]
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILERS_CD'
        verbose_name = 'FILERS_CD'
        verbose_name_plural = 'FILERS_CD'

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class FilerAcronymsCd(CalAccessBaseModel):
    """
    Links acronyms to filers
    """
    UNIQUE_KEY = ("ACRONYM", "FILER_ID")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=9),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=61),
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_ACRONYMS_CD'
        verbose_name = 'FILER_ACRONYMS_CD'
        verbose_name_plural = 'FILER_ACRONYMS_CD'
        ordering = ("id",)

    def __str__(self):
        return self.acronym


@python_2_unicode_compatible
class FilerAddressCd(CalAccessBaseModel):
    """
    Links filers and addresses. This table maintains a history of when
    addresses change.
    """
    UNIQUE_KEY = ("FILER_ID", "ADRID")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=9),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=61, end_page=62),
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
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_ADDRESS_CD'
        verbose_name = 'FILER_ADDRESS_CD'
        verbose_name_plural = 'FILER_ADDRESS_CD'

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class FilerEthicsClassCd(CalAccessBaseModel):
    """
    This table stores lobbyist ethics training dates.
    """
    UNIQUE_KEY = "FILER_ID", "SESSION_ID", "ETHICS_DATE"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=9),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=64),
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_ETHICS_CLASS_CD'
        verbose_name = 'FILER_ETHICS_CLASS_CD'
        verbose_name_plural = 'FILER_ETHICS_CLASS_CD'

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class FilerInterestsCd(CalAccessBaseModel):
    """
    Links a filer to their interest codes.
    """
    UNIQUE_KEY = (
        "FILER_ID",
        "INTEREST_CD",
        "EFFECT_DATE",
        "SESSION_ID"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=9),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=66),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=19),
        ],
        choices=INTEREST_CD_CHOICES,
    )
    effect_date = fields.DateField(
        db_column='EFFECT_DATE',
        null=True,
        verbose_name="Effective date",
        help_text="Effective date",
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_INTERESTS_CD'
        verbose_name = 'FILER_INTERESTS_CD'
        verbose_name_plural = 'FILER_INTERESTS_CD'

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class FilerLinksCd(CalAccessBaseModel):
    """
    Links filers to each other and records their relationship type.
    """
    UNIQUE_KEY = (
        "FILER_ID_A",
        "FILER_ID_B",
        "ACTIVE_FLG",
        "SESSION_ID",
        "LINK_TYPE"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=9),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=67),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=6, end_page=7),
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_LINKS_CD'
        verbose_name = 'FILER_LINKS_CD'
        verbose_name_plural = 'FILER_LINKS_CD'

    def __str__(self):
        return str('%s-%s' % (self.filer_id_a, self.filer_id_b))


@python_2_unicode_compatible
class FilerStatusTypesCd(CalAccessBaseModel):
    """
    This is an undocumented model that contains a small number
    of codes and definitions that map to values in FILERNAME_CD.STATUS.
    """
    UNIQUE_KEY = "STATUS_TYPE"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=9),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=69),
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_STATUS_TYPES_CD'
        verbose_name = 'FILER_STATUS_TYPES_CD'
        verbose_name_plural = 'FILER_STATUS_TYPES_CD'
        ordering = ("status_type",)

    def __str__(self):
        return self.status_type


@python_2_unicode_compatible
class FilerToFilerTypeCd(CalAccessBaseModel):
    """
    This table links a filer to a set of characteristics that describe the
    filer. This table maintains a history of changes and allows the filer
    to change characteristics over time.
    """
    UNIQUE_KEY = (
        "FILER_ID",
        "FILER_TYPE",
        "SESSION_ID",
        "EFFECT_DT"
    )
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=9),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=69, end_page=70),
    ]
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
        db_column='FILER_ID',
    )
    filer_type = ForeignKey(
        'FilerTypesCd',
        related_name='filers',
        db_constraint=False,
        help_text="Filer type identification number. Foreign key referencing \
FilerTypesCd.FILER_TYPE",
        db_column='FILER_TYPE',
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=16, end_page=18),
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=20, end_page=22),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=18),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=19, end_page=20),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=18),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=18, end_page=19),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=3, end_page=4),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=10, end_page=11),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=13, end_page=15),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=11, end_page=13),
        ]
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_TO_FILER_TYPE_CD'
        verbose_name = 'FILER_TO_FILER_TYPE_CD'
        verbose_name_plural = 'FILER_TO_FILER_TYPE_CD'

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class FilerTypesCd(CalAccessBaseModel):
    """
    This lookup table describes filer types.
    """
    UNIQUE_KEY = "FILTER_TYPE"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=9),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=71, end_page=72),
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
    grp_type = fields.IntegerField(
        null=True,
        db_column='GRP_TYPE',
        blank=True,
        help_text="Group type assocated with the filer type"
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_TYPES_CD'
        verbose_name = 'FILER_TYPES_CD'
        verbose_name_plural = 'FILER_TYPES_CD'
        ordering = ("filer_type",)

    def __str__(self):
        return str(self.filer_type)


@python_2_unicode_compatible
class FilerXrefCd(CalAccessBaseModel):
    """
    This table maps legacy filer identification numbers to the system's filer
    identification numbers. Although 60 percent of the FILER_ID and XREF_ID values
    are equal.
    """
    UNIQUE_KEY = ("FILER_ID", "XREF_ID")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=9),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=72),
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_XREF_CD'
        verbose_name = 'FILER_XREF_CD'
        verbose_name_plural = 'FILER_XREF_CD'

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class FilingPeriodCd(CalAccessBaseModel):
    """
    An undocumented table that contains metadata for a variety
    of filing periods.
    """
    UNIQUE_KEY = "PERIOD_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=74, end_page=75),
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
        (1501, 'Non-standard period'),
    )
    period_type = fields.IntegerField(
        db_column='PERIOD_TYPE',
        choices=PERIOD_TYPE_CHOICES,
        help_text='Type of filing period',
        documentcloud_pages=[
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=3),
        ]
    )
    PER_GRP_TYPE_CHOICES = (
        (1500, 'STANDARD PERIOD'),
    )
    per_grp_type = fields.IntegerField(
        db_column='PER_GRP_TYPE',
        help_text="Period group type",
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILING_PERIOD_CD'
        verbose_name = 'FILING_PERIOD_CD'
        verbose_name_plural = 'FILING_PERIOD_CD'
        ordering = ("-end_date",)

    def __str__(self):
        return str(self.period_id)


@python_2_unicode_compatible
class GroupTypesCd(CalAccessBaseModel):
    """
    This lookup table stores group type information. Most (but not all) of the GRP_ID/
    GRP_NAME value pairs in this table match the FILER_TYPE/DESCRIPTION value pairs in
    the FILER_TYPE_CD table.
    """
    UNIQUE_KEY = "GRP_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=78, end_page=79),
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'GROUP_TYPES_CD'
        verbose_name = 'GROUP_TYPES_CD'
        verbose_name_plural = 'GROUP_TYPES_CD'

    def __str__(self):
        return str(self.grp_id)


@python_2_unicode_compatible
class ImageLinksCd(CalAccessBaseModel):
    """
    This table links images to filers and accounts.
    """
    UNIQUE_KEY = ("IMG_LINK_ID", "IMG_ID")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=80),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=5),
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
            DocumentCloud(id='2774529-Lookup-Codes-Cd', start_page=4),
        ],
    )
    img_dt = fields.DateField(
        db_column='IMG_DT',
        null=True,
        verbose_name="Image date",
        help_text="Image date",
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'IMAGE_LINKS_CD'
        verbose_name = 'IMAGE_LINKS_CD'
        verbose_name_plural = 'IMAGE_LINKS_CD'

    def __str__(self):
        return str(self.img_link_id)


@python_2_unicode_compatible
class LegislativeSessionsCd(CalAccessBaseModel):
    """
    Legislative session, begin and end dates look up table.
    """
    UNIQUE_KEY = "SESSION_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=10),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=84),
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LEGISLATIVE_SESSIONS_CD'
        verbose_name = 'LEGISLATIVE_SESSIONS_CD'
        verbose_name_plural = 'LEGISLATIVE_SESSIONS_CD'

    def __str__(self):
        return str(self.session_id)


@python_2_unicode_compatible
class LookupCodesCd(CalAccessBaseModel):
    """
    The description of some lookup codes in the system.
    """
    UNIQUE_KEY = ("CODE_ID", "CODE_TYPE")
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=12),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=106, end_page=106),
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOOKUP_CODES_CD'
        verbose_name = 'LOOKUP_CODES_CD'
        verbose_name_plural = 'LOOKUP_CODES_CD'

    def __str__(self):
        return str(self.code_id)


@python_2_unicode_compatible
class NamesCd(CalAccessBaseModel):
    """
    The name of all entities in the system. Used for searches when
    the name has an identification number.
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=13),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=112),
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'NAMES_CD'
        verbose_name = 'NAMES_CD'
        verbose_name_plural = 'NAMES_CD'

    def __str__(self):
        return str(self.namid)


@python_2_unicode_compatible
class ReceivedFilingsCd(CalAccessBaseModel):
    """
    This table is undocumented.
    """
    UNIQUE_KEY = False
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=13),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=121),
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
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    filing_file_name = fields.CharField(
        db_column='FILING_FILE_NAME',
        max_length=14,
        help_text="The field is undocumented"
    )
    received_date = fields.DateField(
        db_column='RECEIVED_DATE',
        null=True,
        help_text="Date received",
    )
    filing_directory = fields.CharField(
        db_column='FILING_DIRECTORY',
        max_length=45,
        help_text="This field is undocumented",
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number",
        null=True,
        blank=True,
    )
    FORM_ID_CHOICES = tuple([(f.db_value, f.full_title) for f in FILING_FORMS])
    form_id = fields.CharField(
        db_column='FORM_ID',
        max_length=4,
        blank=True,
        choices=FORM_ID_CHOICES,
        verbose_name="form identification code",
        help_text="Form identification code",
    )
    receive_comment = fields.CharField(
        db_column='RECEIVE_COMMENT',
        max_length=51,
        help_text="A comment"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'RECEIVED_FILINGS_CD'
        verbose_name = 'RECEIVED_FILINGS_CD'
        verbose_name_plural = 'RECEIVED_FILINGS_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class ReportsCd(CalAccessBaseModel):
    """
    This is an undocumented model.
    """
    UNIQUE_KEY = "RPT_ID"
    DOCUMENTCLOUD_PAGES = [
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=13),
        DocumentCloud(id='2711614-CalAccessTablesWeb', start_page=122),
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
    rpt_type = fields.IntegerField(
        db_column='RPT_TYPE',
        help_text="Type of the report"
    )
    parm_definition = fields.IntegerField(
        db_column='PARM_DEFINITION',
        help_text="Parameter definition"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'REPORTS_CD'
        verbose_name = 'REPORTS_CD'
        verbose_name_plural = 'REPORTS_CD'

    def __str__(self):
        return str(self.rpt_id)


@python_2_unicode_compatible
class FilerTypePeriodsCd(CalAccessBaseModel):
    """
    This table and its fields are listed in the official CAL-ACCESS documentation,
    but is not fully explained. The table's description contains this note: "J M needs
    to document. This is in his list of tables designed for future enhancements."
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
    election_type = fields.IntegerField(
        db_column="ELECTION_TYPE",
        db_index=True,
        help_text="Election type"
    )
    filer_type = fields.IntegerField(
        db_column="FILER_TYPE",
        db_index=True,
        help_text="Filer type identification number."
    )
    period_id = fields.IntegerField(
        db_column="PERIOD_ID",
        db_index=True,
        help_text="Period identification number."
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_TYPE_PERIODS_CD'
        verbose_name = 'FILER_TYPE_PERIODS_CD'
        verbose_name_plural = 'FILER_TYPE_PERIODS_CD'

    def __str__(self):
        return str(self.filer_type)
