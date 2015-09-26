from __future__ import unicode_literals
from calaccess_raw import fields
from django.utils.encoding import python_2_unicode_compatible
from .base import CalAccessBaseModel


@python_2_unicode_compatible
class AcronymsCd(CalAccessBaseModel):
    """
    Contains acronyms and their meaning.
    """
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
    election_date = fields.DateTimeField(
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
    filing_date = fields.DateTimeField(
        db_column='FILING_DATE',
        null=True,
        help_text="This field is undocumented"
    )
    filingstatus = fields.IntegerField(
        db_column='FILINGSTATUS',
        help_text="This field is undocumented"
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
    FORM_TYPE_CHOICES = (
        ('BADFORMAT 253', ''),
        ('F400', ''),
        ('F401', ''),
        ('F402', ''),
        ('F410', ''),
        ('F425', ''),
        ('F450', ''),
        ('F460', ''),
        ('F461', ''),
        ('F465', ''),
        ('F496', ''),
        ('F497', ''),
        ('F498', ''),
        ('F601', ''),
        ('F602', ''),
        ('F603', ''),
        ('F604', ''),
        ('F606', ''),
        ('F607', ''),
        ('F615', ''),
        ('F625', ''),
        ('F635', ''),
        ('F645', ''),
        ('form', ''),
    )
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=250,
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
    )
    error_no = fields.CharField(
        db_column='ERROR_NO',
        max_length=250,
        help_text="This field is undocumented"
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
    effect_dt = fields.DateTimeField(
        db_column='EFFECT_DT',
        blank=True,
        null=True,
        help_text="Address effective date",
        verbose_name='Effective date'
    )
    add_type = fields.IntegerField(
        db_column='ADD_TYPE',
        blank=True,
        null=True,
        verbose_name="Address type"
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
    ethics_date = fields.DateTimeField(
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
    interest_cd = fields.IntegerField(
        db_column='INTEREST_CD',
        blank=True,
        null=True,
        verbose_name="interest code"
    )
    effect_date = fields.DateTimeField(
        db_column='EFFECT_DATE',
        null=True,
        verbose_name="Effective date"
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
        (-12019, '-12019'),
        (-12018, '-12018'),
        (-12016, '-12016'),
        (-12015, '-12015'),
        (-12014, '-12014'),
        (-12013, '-12013'),
        (-12011, '-12011'),
        (-12008, '-12008'),
        (-12005, '-12005'),
        (-12004, '-12004'),
        (-12002, '-12002'),
        (-12001, '-12001'),
        (0, '0'),
        (12001, '12001'),
        (12002, '12002'),
        (12004, '12004'),
        (12005, '12005'),
        (12008, '12008'),
        (12011, '12011'),
        (12013, '12013'),
        (12014, '12014'),
        (12015, '12015'),
        (12016, '12016'),
        (12018, '12018'),
        (12019, '12019'),
    )
    link_type = fields.IntegerField(
        choices=LINK_TYPE_CHOICES,
        db_column='LINK_TYPE',
        help_text='Denotes the type of the link',
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
        help_text="Termination effective date"
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
    This is an undocumented model.
    """
    UNIQUE_KEY = "STATUS_TYPE"
    status_type = fields.CharField(
        max_length=11,
        db_column='STATUS_TYPE',
        help_text='This field is undocumented'
    )
    status_desc = fields.CharField(
        max_length=11,
        db_column='STATUS_DESC',
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
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
        db_column='FILER_ID',
    )
    filer_type = fields.IntegerField(
        help_text="Filer type identification number",
        db_column='FILER_TYPE',
    )
    active = fields.CharField(
        max_length=1,
        help_text="Indicates if the filer is currently active",
        db_column='ACTIVE',
    )
    race = fields.IntegerField(
        null=True,
        blank=True,
        help_text="If applicable indicates the race in which the filer is \
running",
        db_column='RACE',
    )
    session_id = fields.IntegerField(
        verbose_name='session ID',
        db_column='SESSION_ID',
        help_text='Legislative session identification number',
        null=True,
    )
    category = fields.IntegerField(
        null=True,
        blank=True,
        help_text="Defines the filer's category such as controlled, jointly \
controlled, etc. (subset of filer's type)",
        db_column='CATEGORY',
    )
    category_type = fields.IntegerField(
        null=True,
        blank=True,
        help_text="When applicable, the category type specifies additional \
information about the category. (e.g. state, local, etc.)",
        db_column='CATEGORY_TYPE',
    )
    sub_category = fields.IntegerField(
        null=True,
        blank=True,
        help_text="When applicable specifies general purpose, primarily \
formed, etc.",
        db_column='SUB_CATEGORY',
    )
    effect_dt = fields.DateField(
        null=True,
        help_text="The date the filer assumed the current class or type",
        db_column='EFFECT_DT',
    )
    sub_category_type = fields.IntegerField(
        null=True,
        blank=True,
        help_text="When applicable specifies broad based or small contributor",
        db_column='SUB_CATEGORY_TYPE',
    )
    election_type = fields.IntegerField(
        null=True,
        blank=True,
        help_text="Indicates type of election (general, primary, special)",
        db_column='ELECTION_TYPE',
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
    party_cd = fields.IntegerField(
        null=True,
        blank=True,
        help_text="Filer's political party",
        db_column='PARTY_CD',
    )
    county_cd = fields.IntegerField(
        null=True,
        blank=True,
        help_text="Filer's county code",
        db_column='COUNTY_CD',
    )
    district_cd = fields.IntegerField(
        null=True,
        blank=True,
        help_text="Filer's district number for the office being sought. \
Populated for Senate, Assembly or Board of Equalization races",
        db_column='DISTRICT_CD',
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
    filer_type = fields.IntegerField(
        db_column='FILER_TYPE',
        help_text="Filer type identification number"
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
    identification numbers.
    """
    UNIQUE_KEY = ['FILER_ID', 'XREF_ID']
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
        verbose_name="Effective date"
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
    UNIQUE_KEY = "PERIOD_ID"
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
    period_type = fields.IntegerField(
        db_column='PERIOD_TYPE',
        help_text='This field is undocumented'
    )
    per_grp_type = fields.IntegerField(
        db_column='PER_GRP_TYPE',
        help_text="Period group type"
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
    This lookup table stores group type information.
    """
    UNIQUE_KEY = "GRP_ID"
    grp_id = fields.IntegerField(
        db_column='GRP_ID',
        verbose_name="Group ID",
        help_text="Group identification number"
    )
    grp_name = fields.CharField(
        db_column='GRP_NAME',
        max_length=28,
        blank=True,
        verbose_name="Group name"
    )
    grp_desc = fields.CharField(
        db_column='GRP_DESC',
        max_length=32,
        blank=True,
        verbose_name="Group description"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'GROUP_TYPES_CD'
        verbose_name = 'GROUP_TYPES_CD'
        verbose_name_plural = 'GROUP_TYPES_CD'

    def __str__(self):
        return str(self.grp_id)


@python_2_unicode_compatible
class HeaderCd(CalAccessBaseModel):
    """
    Lookup table used to report form 460 information in the AMS.
    """
    UNIQUE_KEY = ("LINE_NUMBER", "FORM_ID", "REC_TYPE")
    line_number = fields.IntegerField(
        db_column='LINE_NUMBER',
        help_text="This field is undocumented"
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
class HdrCd(CalAccessBaseModel):
    """
    Electronic filing record header data
    """
    UNIQUE_KEY = ("FILING_ID", "AMEND_ID")
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
class ImageLinksCd(CalAccessBaseModel):
    """
    This table links images to filers and accounts.
    """
    UNIQUE_KEY = ("IMG_LINK_ID", "IMG_ID")
    img_link_id = fields.IntegerField(
        db_column='IMG_LINK_ID',
        verbose_name="Image link ID",
        help_text="Image link identification number"
    )
    img_link_type = fields.IntegerField(
        db_column='IMG_LINK_TYPE',
        verbose_name="Image link type"
    )
    img_id = fields.IntegerField(
        db_column='IMG_ID',
        verbose_name="Image ID",
        help_text="Image identification number"
    )
    img_type = fields.IntegerField(
        db_column='IMG_TYPE',
        verbose_name="Image type"
    )
    img_dt = fields.DateField(
        db_column='IMG_DT',
        null=True,
        verbose_name="Image date"
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
class LobbyingChgLogCd(CalAccessBaseModel):
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
        help_text="The type of filer"
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
        help_text="Filer full name"
    )
    filer_city = fields.CharField(
        max_length=200,
        db_column="FILER_CITY",
        help_text="Filer city"
    )
    filer_st = fields.CharField(
        max_length=200,
        db_column="FILER_ST",
        help_text="Filer state"
    )
    filer_zip = fields.IntegerField(
        db_column="FILER_ZIP",
        null=True,
        help_text="Filer ZIP Code"
    )
    filer_phone = fields.CharField(
        db_column="FILER_PHONE",
        null=True,
        max_length=12,
        help_text="Filer phone number"
    )
    entity_type = fields.IntegerField(
        db_column="ENTITY_TYPE",
        null=True,
        help_text="Type of entity"
    )
    entity_name = fields.CharField(
        max_length=500,
        db_column="ENTITY_NAME",
        help_text="Entity name"
    )
    entity_city = fields.CharField(
        max_length=500,
        db_column="ENTITY_CITY",
        help_text="Entity city"
    )
    entity_st = fields.CharField(
        max_length=500,
        db_column="ENTITY_ST",
        help_text="Entity state"
    )
    entity_zip = fields.CharField(
        db_column="ENTITY_ZIP",
        blank=True,
        max_length=10,
        help_text="Entity ZIP Code"
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
        help_text="Effective date"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYING_CHG_LOG_CD'
        verbose_name = 'LOBBYING_CHG_LOG_CD'
        verbose_name_plural = 'LOBBYING_CHG_LOG_CD'

    def __str__(self):
        return str(self.filer_id)


@python_2_unicode_compatible
class LobbyistContributions1Cd(CalAccessBaseModel):
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
    This is an undocumented model.
    """
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
    This is an undocumented model.
    """
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
    This is an undocumented model.
    """
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
    This is an undocumented model.
    """
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
    This is an undocumented model.
    """
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
        db_table = 'LOBBYIST_FIRM1_CD'
        verbose_name = 'LOBBYIST_FIRM1_CD'
        verbose_name_plural = 'LOBBYIST_FIRM1_CD'

    def __str__(self):
        return str(self.firm_id)


@python_2_unicode_compatible
class LobbyistFirm2Cd(CalAccessBaseModel):
    """
    This is an undocumented model.
    """
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
    This is an undocumented model.
    """
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
    This is an undocumented model.
    """
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
    It's an undocumented model.
    """
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
class LookupCode(CalAccessBaseModel):
    """
    The description of all lookup codes in the system.
    """
    UNIQUE_KEY = ("CODE_ID", "CODE_TYPE")
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
    form_id = fields.CharField(
        db_column='FORM_ID',
        max_length=4,
        blank=True,
        help_text="Form identification code"
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
