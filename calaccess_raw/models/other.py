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
    adrid = fields.IntegerField(db_column="ADRID", help_text = 'Address indentification number')
    city = fields.CharField(max_length=500, db_column="CITY")
    st = fields.CharField(max_length=500, db_column="ST")
    zip4 = fields.CharField(db_column="ZIP4", null=True, max_length=10)
    phon = fields.CharField(db_column="PHON", null=True, max_length=20)
    fax = fields.CharField(db_column="FAX", null=True, max_length=20)
    email = fields.CharField(max_length=500, db_column="EMAIL")

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
        null=True
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
        max_length=2
    )
    measure_name = fields.CharField(
        db_column='MEASURE_NAME',
        max_length=163
    )
    measure_short_name = fields.CharField(
        db_column='MEASURE_SHORT_NAME',
        max_length=50, blank=True
    )
    jurisdiction = fields.CharField(
        db_column='JURISDICTION',
        max_length=9
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
    filing_date = fields.DateTimeField(db_column='FILING_DATE', null=True)
    filingstatus = fields.IntegerField(db_column='FILINGSTATUS')
    vendor = fields.CharField(db_column='VENDOR', max_length=250)
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
    error_no = fields.CharField(db_column='ERROR_NO', max_length=250)

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
    links acronyms to filers
    """
    acronym = fields.CharField(db_column='ACRONYM', max_length=32)
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
    adrid = fields.IntegerField(db_column='ADRID')
    effect_dt = fields.DateTimeField(
        db_column='EFFECT_DT',
        blank=True,
        null=True
    )
    add_type = fields.IntegerField(
        db_column='ADD_TYPE',
        blank=True,
        null=True
    )
    session_id = fields.IntegerField(
        db_column='SESSION_ID',
        blank=True,
        null=True
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
    filer_id = fields.IntegerField(
        verbose_name='filer ID',
        db_column='FILER_ID',
        null=True,
        db_index=True,
        help_text="Filer's unique identification number",
    )
    session_id = fields.IntegerField(db_column='SESSION_ID')
    ethics_date = fields.DateTimeField(db_column='ETHICS_DATE', null=True)

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
    session_id = fields.IntegerField(db_column='SESSION_ID')
    interest_cd = fields.IntegerField(db_column='INTEREST_CD')
    effect_date = fields.DateTimeField(db_column='EFFECT_DATE', null=True)

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
        help_text='Session identification number',
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
        help_text='Date the relationship was terminated',
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
    status_type = fields.CharField(
        max_length=11,
        db_column='STATUS_TYPE',
    )
    status_desc = fields.CharField(
        max_length=11,
        db_column='STATUS_DESC'
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
        help_text="Legislative session identification number",
        db_column='SESSION_ID',
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
        blank=True
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
    effect_dt = fields.DateField(db_column='EFFECT_DT', null=True)
    migration_source = fields.CharField(
        max_length=50,
        db_column='MIGRATION_SOURCE'
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
    grp_id = fields.IntegerField(db_column='GRP_ID')
    grp_name = fields.CharField(
        db_column='GRP_NAME',
        max_length=28,
        blank=True
    )
    grp_desc = fields.CharField(
        db_column='GRP_DESC',
        max_length=32,
        blank=True
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
    line_number = fields.IntegerField(db_column='LINE_NUMBER')
    form_id = fields.CharField(db_column='FORM_ID', max_length=5)
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
        blank=True
    )
    comments1 = fields.CharField(
        db_column='COMMENTS1',
        max_length=48,
        blank=True
    )
    comments2 = fields.CharField(
        db_column='COMMENTS2',
        max_length=48,
        blank=True
    )
    label = fields.CharField(db_column='LABEL', max_length=98)
    column_a = fields.IntegerField(
        db_column='COLUMN_A',
        blank=True,
        null=True
    )
    column_b = fields.IntegerField(
        db_column='COLUMN_B',
        blank=True,
        null=True
    )
    column_c = fields.IntegerField(
        db_column='COLUMN_C',
        blank=True,
        null=True)
    show_c = fields.IntegerField(db_column='SHOW_C', blank=True, null=True)
    show_b = fields.IntegerField(db_column='SHOW_B', blank=True, null=True)

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
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    cal_ver = fields.CharField(max_length=4, db_column='CAL_VER', blank=True)
    ef_type = fields.CharField(max_length=3, db_column='EF_TYPE', blank=True)
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    hdr_comment = fields.CharField(
        max_length=200,
        db_column='HDRCOMMENT',
        blank=True
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
        blank=True
    )
    soft_ver = fields.CharField(
        max_length=16,
        db_column='SOFT_VER',
        blank=True
    )
    state_cd = fields.CharField(
        max_length=2,
        db_column='STATE_CD',
        blank=True
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
    img_link_id = fields.IntegerField(db_column='IMG_LINK_ID')
    img_link_type = fields.IntegerField(db_column='IMG_LINK_TYPE')
    img_id = fields.IntegerField(db_column='IMG_ID')
    img_type = fields.IntegerField(db_column='IMG_TYPE')
    img_dt = fields.DateField(db_column='IMG_DT', null=True)

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
    session_id = fields.IntegerField(db_column='SESSION_ID')
    begin_date = fields.DateField(db_column='BEGIN_DATE', null=True)
    end_date = fields.DateField(db_column='END_DATE', null=True)

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
    change_no = fields.IntegerField(db_column='CHANGE_NO')
    session_id = fields.IntegerField(db_column='SESSION_ID', null=True)
    log_dt = fields.DateField(db_column="LOG_DT", null=True)
    filer_type = fields.IntegerField(db_column='FILER_TYPE')
    correction_flag = fields.CharField(
        max_length=200,
        db_column="CORRECTION_FLG"
    )
    action = fields.CharField(max_length=200, db_column="ACTION")
    attribute_changed = fields.CharField(
        max_length=200,
        db_column="ATTRIBUTE_CHANGED"
    )
    ethics_dt = fields.DateField(db_column="ETHICS_DT", null=True)
    interests = fields.CharField(max_length=200, db_column="INTERESTS")
    filer_full_name = fields.CharField(
        max_length=200,
        db_column="FILER_FULL_NAME"
    )
    filer_city = fields.CharField(max_length=200, db_column="FILER_CITY")
    filer_st = fields.CharField(max_length=200, db_column="FILER_ST")
    filer_zip = fields.IntegerField(db_column="FILER_ZIP", null=True)
    filer_phone = fields.CharField(
        db_column="FILER_PHONE",
        null=True,
        max_length=12
    )
    entity_type = fields.IntegerField(db_column="ENTITY_TYPE", null=True)
    entity_name = fields.CharField(max_length=500, db_column="ENTITY_NAME")
    entity_city = fields.CharField(max_length=500, db_column="ENTITY_CITY")
    entity_st = fields.CharField(max_length=500, db_column="ENTITY_ST")
    entity_zip = fields.CharField(
        db_column="ENTITY_ZIP",
        blank=True,
        max_length=10
    )
    entity_phone = fields.CharField(
        db_column="ENTITY_PHONE",
        null=True,
        max_length=12
    )
    entity_id = fields.IntegerField(db_column="ENTITY_ID", null=True)
    responsible_officer = fields.CharField(
        max_length=500,
        db_column="RESPONSIBLE_OFFICER"
    )
    effect_dt = fields.DateField(db_column="EFFECT_DT", null=True)

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
        db_column='FILING_PERIOD_START_DT'
    )
    filing_period_end_dt = fields.DateField(
        db_column='FILING_PERIOD_END_DT',
        null=True
    )
    contribution_dt = fields.CharField(
        db_column='CONTRIBUTION_DT',
        max_length=32,
        blank=True
    )
    recipient_name = fields.CharField(
        db_column='RECIPIENT_NAME',
        max_length=106,
        blank=True
    )
    recipient_id = fields.IntegerField(
        db_column='RECIPIENT_ID',
        blank=True,
        null=True
    )
    amount = fields.FloatField(db_column='AMOUNT', blank=True, null=True)

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
        db_column='FILING_PERIOD_START_DT',
        null=True
    )
    filing_period_end_dt = fields.DateField(
        db_column='FILING_PERIOD_END_DT',
        null=True
    )
    contribution_dt = fields.CharField(
        db_column='CONTRIBUTION_DT',
        max_length=32,
        blank=True
    )
    recipient_name = fields.CharField(
        db_column='RECIPIENT_NAME',
        max_length=106,
        blank=True
    )
    recipient_id = fields.IntegerField(
        db_column='RECIPIENT_ID',
        blank=True,
        null=True
    )
    amount = fields.FloatField(db_column='AMOUNT', blank=True, null=True)

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
        db_column='FILING_PERIOD_START_DT',
        null=True
    )
    filing_period_end_dt = fields.DateField(
        db_column='FILING_PERIOD_END_DT',
        null=True
    )
    contribution_dt = fields.CharField(
        db_column='CONTRIBUTION_DT',
        max_length=32,
        blank=True
    )
    recipient_name = fields.CharField(
        db_column='RECIPIENT_NAME',
        max_length=106,
        blank=True
    )
    recipient_id = fields.IntegerField(
        db_column='RECIPIENT_ID',
        blank=True,
        null=True
    )
    amount = fields.FloatField(db_column='AMOUNT', blank=True, null=True)

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
    employer_id = fields.IntegerField(db_column='EMPLOYER_ID')
    session_id = fields.IntegerField(db_column='SESSION_ID')
    employer_name = fields.CharField(db_column='EMPLOYER_NAME', max_length=162)
    current_qtr_amt = fields.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = fields.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = fields.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    interest_cd = fields.IntegerField(
        db_column='INTEREST_CD', blank=True, null=True
    )
    interest_name = fields.CharField(
        db_column='INTEREST_NAME', max_length=24, blank=True
    )
    session_yr_1 = fields.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = fields.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = fields.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = fields.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = fields.FloatField(db_column='QTR_1')
    qtr_2 = fields.FloatField(db_column='QTR_2')
    qtr_3 = fields.FloatField(db_column='QTR_3')
    qtr_4 = fields.FloatField(db_column='QTR_4')
    qtr_5 = fields.FloatField(db_column='QTR_5')
    qtr_6 = fields.FloatField(db_column='QTR_6')
    qtr_7 = fields.FloatField(db_column='QTR_7')
    qtr_8 = fields.FloatField(db_column='QTR_8')

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
    employer_id = fields.IntegerField(db_column='EMPLOYER_ID')
    session_id = fields.IntegerField(db_column='SESSION_ID')
    employer_name = fields.CharField(db_column='EMPLOYER_NAME', max_length=162)
    current_qtr_amt = fields.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = fields.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = fields.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    interest_cd = fields.IntegerField(
        db_column='INTEREST_CD', blank=True, null=True
    )
    interest_name = fields.CharField(
        db_column='INTEREST_NAME', max_length=24, blank=True
    )
    session_yr_1 = fields.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = fields.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = fields.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = fields.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = fields.FloatField(db_column='QTR_1')
    qtr_2 = fields.FloatField(db_column='QTR_2')
    qtr_3 = fields.FloatField(db_column='QTR_3')
    qtr_4 = fields.FloatField(db_column='QTR_4')
    qtr_5 = fields.FloatField(db_column='QTR_5')
    qtr_6 = fields.FloatField(db_column='QTR_6')
    qtr_7 = fields.FloatField(db_column='QTR_7')
    qtr_8 = fields.FloatField(db_column='QTR_8')

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
    employer_id = fields.IntegerField(db_column='EMPLOYER_ID')
    session_id = fields.IntegerField(db_column='SESSION_ID')
    employer_name = fields.CharField(db_column='EMPLOYER_NAME', max_length=162)
    current_qtr_amt = fields.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = fields.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = fields.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    interest_cd = fields.IntegerField(
        db_column='INTEREST_CD', blank=True, null=True
    )
    interest_name = fields.CharField(
        db_column='INTEREST_NAME', max_length=24, blank=True
    )
    session_yr_1 = fields.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = fields.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = fields.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = fields.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = fields.FloatField(db_column='QTR_1')
    qtr_2 = fields.FloatField(db_column='QTR_2')
    qtr_3 = fields.FloatField(db_column='QTR_3')
    qtr_4 = fields.FloatField(db_column='QTR_4')
    qtr_5 = fields.FloatField(db_column='QTR_5')
    qtr_6 = fields.FloatField(db_column='QTR_6')
    qtr_7 = fields.FloatField(db_column='QTR_7')
    qtr_8 = fields.FloatField(db_column='QTR_8')

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
    employer_id = fields.IntegerField(db_column='EMPLOYER_ID')
    firm_id = fields.IntegerField(db_column='FIRM_ID')
    firm_name = fields.CharField(db_column='FIRM_NAME', max_length=117)
    session_id = fields.IntegerField(db_column='SESSION_ID')
    termination_dt = fields.CharField(
        db_column='TERMINATION_DT',
        max_length=32,
        blank=True
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
    employer_id = fields.IntegerField(db_column='EMPLOYER_ID')
    firm_id = fields.IntegerField(db_column='FIRM_ID')
    firm_name = fields.CharField(db_column='FIRM_NAME', max_length=117)
    session_id = fields.IntegerField(db_column='SESSION_ID')
    termination_dt = fields.CharField(
        db_column='TERMINATION_DT',
        max_length=32,
        blank=True
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
    lobbyist_id = fields.IntegerField(db_column='LOBBYIST_ID')
    employer_id = fields.IntegerField(db_column='EMPLOYER_ID')
    lobbyist_last_name = fields.CharField(
        db_column='LOBBYIST_LAST_NAME',
        max_length=17
    )
    lobbyist_first_name = fields.CharField(
        db_column='LOBBYIST_FIRST_NAME',
        max_length=17
    )
    employer_name = fields.CharField(db_column='EMPLOYER_NAME', max_length=117)
    session_id = fields.IntegerField(db_column='SESSION_ID')

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
    lobbyist_id = fields.IntegerField(db_column='LOBBYIST_ID')
    employer_id = fields.IntegerField(db_column='EMPLOYER_ID')
    lobbyist_last_name = fields.CharField(
        db_column='LOBBYIST_LAST_NAME',
        max_length=17
    )
    lobbyist_first_name = fields.CharField(
        db_column='LOBBYIST_FIRST_NAME',
        max_length=17
    )
    employer_name = fields.CharField(db_column='EMPLOYER_NAME', max_length=117)
    session_id = fields.IntegerField(db_column='SESSION_ID')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMP_LOBBYIST2_CD'
        verbose_name = 'LOBBYIST_EMP_LOBBYIST2_CD'
        verbose_name_plural = 'LOBBYIST_EMP_LOBBYIST2_CD'

    def __str__(self):
        return str(self.lobbyist_id)


@python_2_unicode_compatible
class LobbyistFirm1Cd(CalAccessBaseModel):
    firm_id = fields.IntegerField(db_column='FIRM_ID')
    session_id = fields.IntegerField(db_column='SESSION_ID')
    firm_name = fields.CharField(db_column='FIRM_NAME', max_length=60)
    current_qtr_amt = fields.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = fields.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = fields.IntegerField(
        db_column='CONTRIBUTOR_ID',
        blank=True,
        null=True
    )
    session_yr_1 = fields.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = fields.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = fields.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = fields.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = fields.FloatField(db_column='QTR_1')
    qtr_2 = fields.FloatField(db_column='QTR_2')
    qtr_3 = fields.FloatField(db_column='QTR_3')
    qtr_4 = fields.FloatField(db_column='QTR_4')
    qtr_5 = fields.FloatField(db_column='QTR_5')
    qtr_6 = fields.FloatField(db_column='QTR_6')
    qtr_7 = fields.FloatField(db_column='QTR_7')
    qtr_8 = fields.FloatField(db_column='QTR_8')

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
    firm_id = fields.IntegerField(db_column='FIRM_ID')
    session_id = fields.IntegerField(db_column='SESSION_ID')
    firm_name = fields.CharField(db_column='FIRM_NAME', max_length=60)
    current_qtr_amt = fields.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = fields.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = fields.IntegerField(
        db_column='CONTRIBUTOR_ID',
        blank=True,
        null=True
    )
    session_yr_1 = fields.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = fields.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = fields.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = fields.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = fields.FloatField(db_column='QTR_1')
    qtr_2 = fields.FloatField(db_column='QTR_2')
    qtr_3 = fields.FloatField(db_column='QTR_3')
    qtr_4 = fields.FloatField(db_column='QTR_4')
    qtr_5 = fields.FloatField(db_column='QTR_5')
    qtr_6 = fields.FloatField(db_column='QTR_6')
    qtr_7 = fields.FloatField(db_column='QTR_7')
    qtr_8 = fields.FloatField(db_column='QTR_8')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM2_CD'
        verbose_name = 'LOBBYIST_FIRM2_CD'
        verbose_name_plural = 'LOBBYIST_FIRM2_CD'

    def __str__(self):
        return str(self.firm_id)


@python_2_unicode_compatible
class LobbyistFirm3Cd(CalAccessBaseModel):
    firm_id = fields.IntegerField(db_column='FIRM_ID')
    session_id = fields.IntegerField(db_column='SESSION_ID')
    firm_name = fields.CharField(db_column='FIRM_NAME', max_length=60)
    current_qtr_amt = fields.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = fields.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = fields.IntegerField(
        db_column='CONTRIBUTOR_ID',
        blank=True,
        null=True
    )
    session_yr_1 = fields.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = fields.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = fields.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = fields.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = fields.FloatField(db_column='QTR_1')
    qtr_2 = fields.FloatField(db_column='QTR_2')
    qtr_3 = fields.FloatField(db_column='QTR_3')
    qtr_4 = fields.FloatField(db_column='QTR_4')
    qtr_5 = fields.FloatField(db_column='QTR_5')
    qtr_6 = fields.FloatField(db_column='QTR_6')
    qtr_7 = fields.FloatField(db_column='QTR_7')
    qtr_8 = fields.FloatField(db_column='QTR_8')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM3_CD'
        verbose_name = 'LOBBYIST_FIRM3_CD'
        verbose_name_plural = 'LOBBYIST_FIRM3_CD'

    def __str__(self):
        return str(self.firm_id)


@python_2_unicode_compatible
class LobbyistFirmEmployer1Cd(CalAccessBaseModel):
    '''
    This is an undocumented model (Ask Matt)
    '''
    firm_id = fields.IntegerField(db_column='FIRM_ID')
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    filing_sequence = fields.IntegerField(db_column='FILING_SEQUENCE')
    firm_name = fields.CharField(db_column='FIRM_NAME', max_length=58)
    employer_name = fields.CharField(db_column='EMPLOYER_NAME', max_length=75)
    rpt_start = fields.DateField(db_column='RPT_START', null=True)
    rpt_end = fields.DateField(db_column='RPT_END', null=True)
    per_total = fields.FloatField(db_column='PER_TOTAL')
    cum_total = fields.FloatField(db_column='CUM_TOTAL')
    lby_actvty = fields.CharField(
        db_column='LBY_ACTVTY',
        max_length=182,
        blank=True
    )
    ext_lby_actvty = fields.CharField(
        db_column='EXT_LBY_ACTVTY',
        max_length=32,
        blank=True
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
    This is an undocumented model
    """
    firm_id = fields.IntegerField(db_column='FIRM_ID')
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    filing_sequence = fields.IntegerField(db_column='FILING_SEQUENCE')
    firm_name = fields.CharField(db_column='FIRM_NAME', max_length=58)
    employer_name = fields.CharField(db_column='EMPLOYER_NAME', max_length=75)
    rpt_start = fields.DateField(db_column='RPT_START', null=True)
    rpt_end = fields.DateField(db_column='RPT_END', null=True)
    per_total = fields.FloatField(db_column='PER_TOTAL')
    cum_total = fields.FloatField(db_column='CUM_TOTAL')
    lby_actvty = fields.CharField(
        db_column='LBY_ACTVTY',
        max_length=182,
        blank=True
    )
    ext_lby_actvty = fields.CharField(
        db_column='EXT_LBY_ACTVTY',
        max_length=32,
        blank=True
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
    lobbyist_id = fields.IntegerField(db_column='LOBBYIST_ID')
    firm_id = fields.IntegerField(db_column='FIRM_ID')
    lobbyist_last_name = fields.CharField(
        db_column='LOBBYIST_LAST_NAME',
        max_length=15
    )
    lobbyist_first_name = fields.CharField(
        db_column='LOBBYIST_FIRST_NAME',
        max_length=17
    )
    firm_name = fields.CharField(db_column='FIRM_NAME', max_length=60)
    session_id = fields.IntegerField(db_column='SESSION_ID')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM_LOBBYIST1_CD'
        verbose_name = 'LOBBYIST_FIRM_LOBBYIST1_CD'
        verbose_name_plural = 'LOBBYIST_FIRM_LOBBYIST1_CD'

    def __str__(self):
        return str(self.lobbyist_id)


@python_2_unicode_compatible
class LobbyistFirmLobbyist2Cd(CalAccessBaseModel):
    lobbyist_id = fields.IntegerField(db_column='LOBBYIST_ID')
    firm_id = fields.IntegerField(db_column='FIRM_ID')
    lobbyist_last_name = fields.CharField(
        db_column='LOBBYIST_LAST_NAME',
        max_length=15
    )
    lobbyist_first_name = fields.CharField(
        db_column='LOBBYIST_FIRST_NAME',
        max_length=17
    )
    firm_name = fields.CharField(db_column='FIRM_NAME', max_length=60)
    session_id = fields.IntegerField(db_column='SESSION_ID')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM_LOBBYIST2_CD'
        verbose_name = 'LOBBYIST_FIRM_LOBBYIST2_CD'
        verbose_name_plural = 'LOBBYIST_FIRM_LOBBYIST2_CD'

    def __str__(self):
        return str(self.lobbyist_id)


@python_2_unicode_compatible
class LookupCode(CalAccessBaseModel):
    code_type = fields.IntegerField(db_column='CODE_TYPE')
    code_id = fields.IntegerField(db_column='CODE_ID')
    code_desc = fields.CharField(
        db_column='CODE_DESC',
        max_length=100,
        null=True
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
    namid = fields.IntegerField(db_column='NAMID')
    naml = fields.CharField(max_length=200, db_column='NAML')
    namf = fields.CharField(max_length=50, db_column='NAMF')
    namt = fields.CharField(max_length=100, db_column='NAMT', blank=True)
    nams = fields.CharField(max_length=30, db_column='NAMS', blank=True)
    moniker = fields.CharField(max_length=30, db_column='MONIKER', blank=True)
    moniker_pos = fields.CharField(
        max_length=9,
        db_column='MONIKER_POS',
        blank=True
    )
    namm = fields.CharField(max_length=20, db_column='NAMM', blank=True)
    fullname = fields.CharField(max_length=200, db_column='FULLNAME')
    naml_search = fields.CharField(max_length=200, db_column='NAML_SEARCH')

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
    This is undocumented. J M needs to describe this table.
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
        max_length=14
    )
    received_date = fields.DateField(db_column='RECEIVED_DATE', null=True)
    filing_directory = fields.CharField(
        db_column='FILING_DIRECTORY',
        max_length=45
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number",
        null=True,
        blank=True,
    )
    form_id = fields.CharField(db_column='FORM_ID', max_length=4, blank=True)
    receive_comment = fields.CharField(
        db_column='RECEIVE_COMMENT',
        max_length=51
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
        help_text="Reportpath"
    )
    data_object = fields.CharField(
        db_column='DATA_OBJECT',
        max_length=38
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
