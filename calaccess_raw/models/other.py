from __future__ import unicode_literals
from django.db import models
from .base import CalAccessBaseModel


class AcronymsCd(CalAccessBaseModel):
    """
    Contains acronyms and their meaning.
    """
    acronym = models.CharField(max_length=40, db_column="ACRONYM")
    stands_for = models.CharField(max_length=4, db_column="STANDS_FOR")
    effect_dt = models.DateField(db_column="EFFECT_DT", null=True)
    a_desc = models.CharField(max_length=50, db_column="A_DESC")

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'ACRONYMS_CD'
        verbose_name = 'ACRONYMS_CD'
        verbose_name_plural = 'ACRONYMS_CD'
        ordering = ("acronym",)

    def __unicode__(self):
        return self.acronym


class AddressCd(CalAccessBaseModel):
    """
    This table holds all addresses for the system. This table can be used for address 
    based searches and formes the bases for address information desplayed by the AMS.
    """
    adrid = models.IntegerField(db_column="ADRID")
    city = models.CharField(max_length=500, db_column="CITY")
    st = models.CharField(max_length=500, db_column="ST")
    zip4 = models.CharField(db_column="ZIP4", null=True, max_length=10L)
    phon = models.CharField(db_column="PHON", null=True, max_length=20L)
    fax = models.CharField(db_column="FAX", null=True, max_length=20L)
    email = models.CharField(max_length=500, db_column="EMAIL")

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'ADDRESS_CD'
        verbose_name = 'ADDRESS_CD'
        verbose_name_plural = 'ADDRESS_CD'


class BallotMeasuresCd(CalAccessBaseModel):
    """ Ballot measures dates and times """
    election_date = models.DateTimeField(db_column='ELECTION_DATE', null=True)
    filer_id = models.IntegerField(db_column='FILER_ID')
    measure_no = models.CharField(db_column='MEASURE_NO', max_length=2)
    measure_name = models.CharField(db_column='MEASURE_NAME', max_length=163)
    measure_short_name = models.CharField(
        db_column='MEASURE_SHORT_NAME',
        max_length=50, blank=True
    )
    jurisdiction = models.CharField(db_column='JURISDICTION', max_length=9)

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


class EfsFilingLogCd(CalAccessBaseModel):
    filing_date = models.DateTimeField(db_column='FILING_DATE', null=True)
    filingstatus = models.IntegerField(db_column='FILINGSTATUS')
    vendor = models.CharField(db_column='VENDOR', max_length=250)
    filer_id = models.CharField(db_column='FILER_ID', max_length=250)
    form_type = models.CharField(db_column='FORM_TYPE', max_length=250)
    error_no = models.CharField(db_column='ERROR_NO', max_length=250)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'EFS_FILING_LOG_CD'
        verbose_name = 'EFS_FILING_LOG_CD'
        verbose_name_plural = 'EFS_FILING_LOG_CD'


class FilersCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID', db_index=True)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILERS_CD'
        verbose_name = 'FILERS_CD'
        verbose_name_plural = 'FILERS_CD'


class FilerAcronymsCd(CalAccessBaseModel):
    """
    links acronyms to filers
    """
    acronym = models.CharField(db_column='ACRONYM', max_length=32L)
    filer_id = models.IntegerField(db_column='FILER_ID')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_ACRONYMS_CD'
        verbose_name = 'FILER_ACRONYMS_CD'
        verbose_name_plural = 'FILER_ACRONYMS_CD'
        ordering = ("id",)

    def __unicode__(self):
        return self.acronym


class FilerAddressCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    adrid = models.IntegerField(db_column='ADRID')
    effect_dt = models.DateTimeField(
        db_column='EFFECT_DT', blank=True, null=True
    )
    add_type = models.IntegerField(db_column='ADD_TYPE', blank=True, null=True)
    session_id = models.IntegerField(
        db_column='SESSION_ID', blank=True, null=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_ADDRESS_CD'
        verbose_name = 'FILER_ADDRESS_CD'
        verbose_name_plural = 'FILER_ADDRESS_CD'


class FilerEthicsClassCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    ethics_date = models.DateTimeField(db_column='ETHICS_DATE', null=True)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_ETHICS_CLASS_CD'
        verbose_name = 'FILER_ETHICS_CLASS_CD'
        verbose_name_plural = 'FILER_ETHICS_CLASS_CD'


class FilerInterestsCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    interest_cd = models.IntegerField(db_column='INTEREST_CD')
    effect_date = models.DateTimeField(db_column='EFFECT_DATE', null=True)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_INTERESTS_CD'
        verbose_name = 'FILER_INTERESTS_CD'
        verbose_name_plural = 'FILER_INTERESTS_CD'


class FilerLinksCd(CalAccessBaseModel):
    """
    This table links filers to other filers in the system by their type of relationship.
    """
    filer_id_a = models.IntegerField(db_column='FILER_ID_A', db_index=True)
    filer_id_b = models.IntegerField(db_column='FILER_ID_B', db_index=True)
    active_flg = models.CharField(max_length=1L, db_column='ACTIVE_FLG')
    session_id = models.IntegerField(db_column='SESSION_ID')
    link_type = models.IntegerField(db_column='LINK_TYPE')
    link_desc = models.CharField(
        max_length=255L, db_column='LINK_DESC', blank=True
    )
    effect_dt = models.DateField(db_column='EFFECT_DT', null=True)
    dominate_filer = models.CharField(
        max_length=1L, db_column='DOMINATE_FILER', blank=True
    )
    termination_dt = models.DateField(
        null=True, db_column='TERMINATION_DT', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_LINKS_CD'
        verbose_name = 'FILER_LINKS_CD'
        verbose_name_plural = 'FILER_LINKS_CD'


class FilerStatusTypesCd(CalAccessBaseModel):
    status_type = models.CharField(
        max_length=11L,
        db_column='STATUS_TYPE',
    )
    status_desc = models.CharField(
        max_length=11L,
        db_column='STATUS_DESC'
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_STATUS_TYPES_CD'
        verbose_name = 'FILER_STATUS_TYPES_CD'
        verbose_name_plural = 'FILER_STATUS_TYPES_CD'
        ordering = ("status_type",)

    def __unicode__(self):
        return self.status_type


class FilerToFilerTypeCd(CalAccessBaseModel):
    filer_id = models.IntegerField(
        db_column='FILER_ID',
        help_text="Filer's unique identification number"
    )
    filer_type = models.IntegerField(
        db_column='FILER_TYPE',
        help_text="Filer type identification number"
    )
    active = models.CharField(
        max_length=1L,
        db_column='ACTIVE',
        help_text="Indicates if the filer is currently active"
    )
    race = models.IntegerField(
        null=True,
        db_column='RACE',
        blank=True,
        help_text="If applicable indicates the race in which the filer is \
running"
    )
    session_id = models.IntegerField(
        db_column='SESSION_ID',
        help_text="Legislative session identification number"
    )
    category = models.IntegerField(
        null=True,
        db_column='CATEGORY',
        blank=True,
        help_text="Defines the filer's category such as controlled, jointly \
controlled, etc. (subset of filer's type)"
    )
    category_type = models.IntegerField(
        null=True,
        db_column='CATEGORY_TYPE',
        blank=True,
        help_text="When applicable, the category type specifies additional \
information about the category. (e.g. state, local, etc.)"
    )
    sub_category = models.IntegerField(
        null=True,
        db_column='SUB_CATEGORY',
        blank=True,
        help_text="When applicable specifies general purpose, primarily \
formed, etc."
    )
    effect_dt = models.DateField(
        db_column='EFFECT_DT',
        null=True,
        help_text="The date the filer assumed the current class or type"
    )
    sub_category_type = models.IntegerField(
        null=True,
        db_column='SUB_CATEGORY_TYPE',
        blank=True,
        help_text="When applicable specifies broad based or small contributor"
    )
    election_type = models.IntegerField(
        null=True,
        db_column='ELECTION_TYPE',
        blank=True,
        help_text="Indicates type of election (general, primary, special)"
    )
    sub_category_a = models.CharField(
        max_length=1L,
        db_column='SUB_CATEGORY_A',
        blank=True,
        help_text="Indicates if sponsored or not"
    )
    nyq_dt = models.DateField(
        null=True,
        db_column='NYQ_DT',
        blank=True,
        help_text="Indicates the date when a committee reached its qualifying \
level of activity"
    )
    party_cd = models.IntegerField(
        null=True,
        db_column='PARTY_CD',
        blank=True,
        help_text="Filer's political party"
    )
    county_cd = models.IntegerField(
        null=True,
        db_column='COUNTY_CD',
        blank=True,
        help_text="Filer's county code"
    )
    district_cd = models.IntegerField(
        null=True,
        db_column='DISTRICT_CD',
        blank=True,
        help_text="Filer's district number for the office being sought. \
Populated for Senate, Assembly or Board of Equalization races"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_TO_FILER_TYPE_CD'
        verbose_name = 'FILER_TO_FILER_TYPE_CD'
        verbose_name_plural = 'FILER_TO_FILER_TYPE_CD'

    def __unicode__(self):
        return unicode(self.filer_id)


class FilerTypesCd(CalAccessBaseModel):
    """
    This lookup table describes filer types.
    """
    filer_type = models.IntegerField(
        db_column='FILER_TYPE',
        help_text="Filer type identification number"
    )
    description = models.CharField(
        max_length=255,
        db_column='DESCRIPTION',
        help_text="Description of the filer type"
    )
    grp_type = models.IntegerField(
        null=True,
        db_column='GRP_TYPE',
        blank=True,
        help_text="Group type assocated with the filer type"
    )
    calc_use = models.CharField(
        max_length=1,
        db_column='CALC_USE',
        blank=True,
        help_text="Use checkbox flag"
    )
    grace_period = models.CharField(
        max_length=12, db_column='GRACE_PERIOD', blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_TYPES_CD'
        verbose_name = 'FILER_TYPES_CD'
        verbose_name_plural = 'FILER_TYPES_CD'
        ordering = ("filer_type",)

    def __unicode__(self):
        return unicode(self.filer_type)


class FilerXrefCd(CalAccessBaseModel):
    """
    This table maps legacy filer identification numbers to the systems filer identification numbers.
    """
    filer_id = models.IntegerField(db_column='FILER_ID')
    xref_id = models.CharField(max_length=32L, db_column='XREF_ID')
    effect_dt = models.DateField(db_column='EFFECT_DT', null=True)
    migration_source = models.CharField(
        max_length=50L, db_column='MIGRATION_SOURCE'
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILER_XREF_CD'
        verbose_name = 'FILER_XREF_CD'
        verbose_name_plural = 'FILER_XREF_CD'


class FilingPeriodCd(CalAccessBaseModel):
    period_id = models.IntegerField(
        db_column='PERIOD_ID',
        help_text="Unique period identification number"
    )
    start_date = models.DateField(
        db_column='START_DATE',
        null=True,
        help_text="Starting date for period"
    )
    end_date = models.DateField(
        db_column='END_DATE',
        null=True,
        help_text="Ending date of period"
    )
    period_type = models.IntegerField(
        db_column='PERIOD_TYPE',
    )
    per_grp_type = models.IntegerField(
        db_column='PER_GRP_TYPE',
        help_text="Period group type"
    )
    period_desc = models.CharField(
        max_length=255,
        db_column='PERIOD_DESC',
        help_text="Period description"
    )
    deadline = models.DateField(
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


class GroupTypesCd(CalAccessBaseModel):
    """
    This lookup table stores group type information.
    """
    grp_id = models.IntegerField(db_column='GRP_ID')
    grp_name = models.CharField(
        db_column='GRP_NAME', max_length=28, blank=True
    )
    grp_desc = models.CharField(
        db_column='GRP_DESC', max_length=32, blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'GROUP_TYPES_CD'
        verbose_name = 'GROUP_TYPES_CD'
        verbose_name_plural = 'GROUP_TYPES_CD'


class HeaderCd(CalAccessBaseModel):
    """
    Lookup table used to report form 460 information in the AMS.
    """
    line_number = models.IntegerField(db_column='LINE_NUMBER')
    form_id = models.CharField(db_column='FORM_ID', max_length=5)
    rec_type = models.CharField(db_column='REC_TYPE', max_length=11)
    section_label = models.CharField(
        db_column='SECTION_LABEL', max_length=58, blank=True
    )
    comments1 = models.CharField(
        db_column='COMMENTS1', max_length=48, blank=True
    )
    comments2 = models.CharField(
        db_column='COMMENTS2', max_length=48, blank=True
    )
    label = models.CharField(db_column='LABEL', max_length=98)
    column_a = models.IntegerField(db_column='COLUMN_A', blank=True, null=True)
    column_b = models.IntegerField(db_column='COLUMN_B', blank=True, null=True)
    column_c = models.IntegerField(db_column='COLUMN_C', blank=True, null=True)
    show_c = models.IntegerField(db_column='SHOW_C', blank=True, null=True)
    show_b = models.IntegerField(db_column='SHOW_B', blank=True, null=True)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'HEADER_CD'
        verbose_name = 'HEADER_CD'
        verbose_name_plural = 'HEADER_CD'


class HdrCd(CalAccessBaseModel):
    """
    Electronic filing record header data
    """
    amend_id = models.IntegerField(db_column='AMEND_ID')
    cal_ver = models.CharField(max_length=4L, db_column='CAL_VER', blank=True)
    ef_type = models.CharField(max_length=3L, db_column='EF_TYPE', blank=True)
    filing_id = models.IntegerField(db_column='FILING_ID')
    hdr_comment = models.CharField(
        max_length=200L,
        db_column='HDRCOMMENT',
        blank=True
    )
    rec_type = models.CharField(
        max_length=3L,
        db_column='REC_TYPE',
        blank=True
    )
    soft_name = models.CharField(
        max_length=90L,
        db_column='SOFT_NAME',
        blank=True
    )
    soft_ver = models.CharField(
        max_length=16L,
        db_column='SOFT_VER',
        blank=True
    )
    state_cd = models.CharField(
        max_length=2L,
        db_column='STATE_CD',
        blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'HDR_CD'
        verbose_name = 'HDR_CD'
        verbose_name_plural = 'HDR_CD'


class ImageLinksCd(CalAccessBaseModel):
    img_link_id = models.IntegerField(db_column='IMG_LINK_ID')
    img_link_type = models.IntegerField(db_column='IMG_LINK_TYPE')
    img_id = models.IntegerField(db_column='IMG_ID')
    img_type = models.IntegerField(db_column='IMG_TYPE')
    img_dt = models.DateField(db_column='IMG_DT', null=True)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'IMAGE_LINKS_CD'
        verbose_name = 'IMAGE_LINKS_CD'
        verbose_name_plural = 'IMAGE_LINKS_CD'


class LegislativeSessionsCd(CalAccessBaseModel):
    """
    Legislative session, begin and end dates look up table.
    """
    session_id = models.IntegerField(db_column='SESSION_ID')
    begin_date = models.DateField(db_column='BEGIN_DATE', null=True)
    end_date = models.DateField(db_column='END_DATE', null=True)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LEGISLATIVE_SESSIONS_CD'
        verbose_name = 'LEGISLATIVE_SESSIONS_CD'
        verbose_name_plural = 'LEGISLATIVE_SESSIONS_CD'


class LobbyingChgLogCd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    change_no = models.IntegerField(db_column='CHANGE_NO')
    session_id = models.IntegerField(db_column='SESSION_ID', null=True)
    log_dt = models.DateField(db_column="LOG_DT", null=True)
    filer_type = models.IntegerField(db_column='FILER_TYPE')
    correction_flag = models.CharField(
        max_length=200,
        db_column="CORRECTION_FLG"
    )
    action = models.CharField(max_length=200, db_column="ACTION")
    attribute_changed = models.CharField(
        max_length=200,
        db_column="ATTRIBUTE_CHANGED"
    )
    ethics_dt = models.DateField(db_column="ETHICS_DT", null=True)
    interests = models.CharField(max_length=200, db_column="INTERESTS")
    filer_full_name = models.CharField(
        max_length=200,
        db_column="FILER_FULL_NAME"
    )
    filer_city = models.CharField(max_length=200, db_column="FILER_CITY")
    filer_st = models.CharField(max_length=200, db_column="FILER_ST")
    filer_zip = models.IntegerField(db_column="FILER_ZIP", null=True)
    filer_phone = models.CharField(
        db_column="FILER_PHONE", null=True, max_length=12L
    )
    entity_type = models.IntegerField(db_column="ENTITY_TYPE", null=True)
    entity_name = models.CharField(max_length=500, db_column="ENTITY_NAME")
    entity_city = models.CharField(max_length=500, db_column="ENTITY_CITY")
    entity_st = models.CharField(max_length=500, db_column="ENTITY_ST")
    entity_zip = models.CharField(
        db_column="ENTITY_ZIP", blank=True, max_length=10L
    )
    entity_phone = models.CharField(
        db_column="ENTITY_PHONE", null=True, max_length=12L
    )
    entity_id = models.IntegerField(db_column="ENTITY_ID", null=True)
    responsible_officer = models.CharField(
        max_length=500, db_column="RESPONSIBLE_OFFICER"
    )
    effect_dt = models.DateField(db_column="EFFECT_DT", null=True)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYING_CHG_LOG_CD'
        verbose_name = 'LOBBYING_CHG_LOG_CD'
        verbose_name_plural = 'LOBBYING_CHG_LOG_CD'


class LobbyistContributions1Cd(CalAccessBaseModel):
    filer_id = models.IntegerField(db_column='FILER_ID')
    filing_period_start_dt = models.DateField(
        null=True,
        db_column='FILING_PERIOD_START_DT'
    )
    filing_period_end_dt = models.DateField(
        db_column='FILING_PERIOD_END_DT',
        null=True
    )
    contribution_dt = models.CharField(
        db_column='CONTRIBUTION_DT', max_length=32, blank=True
    )
    recipient_name = models.CharField(
        db_column='RECIPIENT_NAME', max_length=106, blank=True
    )
    recipient_id = models.IntegerField(
        db_column='RECIPIENT_ID', blank=True, null=True
    )
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_CONTRIBUTIONS1_CD'
        verbose_name = 'LOBBYIST_CONTRIBUTIONS1_CD'
        verbose_name_plural = 'LOBBYIST_CONTRIBUTIONS1_CD'


class LobbyistContributions2Cd(CalAccessBaseModel):
    """
    Lobbyist contribution disclosure table. Temporary table used to generate disclosure table (Lobbyist Contributions 3)
    """
    filer_id = models.IntegerField(db_column='FILER_ID')
    filing_period_start_dt = models.DateField(
        db_column='FILING_PERIOD_START_DT',
        null=True
    )
    filing_period_end_dt = models.DateField(
        db_column='FILING_PERIOD_END_DT',
        null=True
    )
    contribution_dt = models.CharField(
        db_column='CONTRIBUTION_DT', max_length=32, blank=True
    )
    recipient_name = models.CharField(
        db_column='RECIPIENT_NAME', max_length=106, blank=True
    )
    recipient_id = models.IntegerField(
        db_column='RECIPIENT_ID', blank=True, null=True
    )
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_CONTRIBUTIONS2_CD'
        verbose_name = 'LOBBYIST_CONTRIBUTIONS2_CD'
        verbose_name_plural = 'LOBBYIST_CONTRIBUTIONS2_CD'


class LobbyistContributions3Cd(CalAccessBaseModel):
    """
    Lobbyist contribution disclosure table.
    """
    filer_id = models.IntegerField(db_column='FILER_ID')
    filing_period_start_dt = models.DateField(
        db_column='FILING_PERIOD_START_DT',
        null=True
    )
    filing_period_end_dt = models.DateField(
        db_column='FILING_PERIOD_END_DT',
        null=True
    )
    contribution_dt = models.CharField(
        db_column='CONTRIBUTION_DT', max_length=32, blank=True
    )
    recipient_name = models.CharField(
        db_column='RECIPIENT_NAME', max_length=106, blank=True
    )
    recipient_id = models.IntegerField(
        db_column='RECIPIENT_ID', blank=True, null=True
    )
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_CONTRIBUTIONS3_CD'
        verbose_name = 'LOBBYIST_CONTRIBUTIONS3_CD'
        verbose_name_plural = 'LOBBYIST_CONTRIBUTIONS3_CD'


class LobbyistEmployer1Cd(CalAccessBaseModel):
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=162)
    current_qtr_amt = models.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = models.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = models.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    interest_cd = models.IntegerField(
        db_column='INTEREST_CD', blank=True, null=True
    )
    interest_name = models.CharField(
        db_column='INTEREST_NAME', max_length=24, blank=True
    )
    session_yr_1 = models.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = models.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = models.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = models.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = models.FloatField(db_column='QTR_1')
    qtr_2 = models.FloatField(db_column='QTR_2')
    qtr_3 = models.FloatField(db_column='QTR_3')
    qtr_4 = models.FloatField(db_column='QTR_4')
    qtr_5 = models.FloatField(db_column='QTR_5')
    qtr_6 = models.FloatField(db_column='QTR_6')
    qtr_7 = models.FloatField(db_column='QTR_7')
    qtr_8 = models.FloatField(db_column='QTR_8')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMPLOYER1_CD'
        verbose_name = 'LOBBYIST_EMPLOYER1_CD'
        verbose_name_plural = 'LOBBYIST_EMPLOYER1_CD'


class LobbyistEmployer2Cd(CalAccessBaseModel):
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=162)
    current_qtr_amt = models.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = models.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = models.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    interest_cd = models.IntegerField(
        db_column='INTEREST_CD', blank=True, null=True
    )
    interest_name = models.CharField(
        db_column='INTEREST_NAME', max_length=24, blank=True
    )
    session_yr_1 = models.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = models.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = models.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = models.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = models.FloatField(db_column='QTR_1')
    qtr_2 = models.FloatField(db_column='QTR_2')
    qtr_3 = models.FloatField(db_column='QTR_3')
    qtr_4 = models.FloatField(db_column='QTR_4')
    qtr_5 = models.FloatField(db_column='QTR_5')
    qtr_6 = models.FloatField(db_column='QTR_6')
    qtr_7 = models.FloatField(db_column='QTR_7')
    qtr_8 = models.FloatField(db_column='QTR_8')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMPLOYER2_CD'
        verbose_name = 'LOBBYIST_EMPLOYER2_CD'
        verbose_name_plural = 'LOBBYIST_EMPLOYER2_CD'


class LobbyistEmployer3Cd(CalAccessBaseModel):
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=162)
    current_qtr_amt = models.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = models.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = models.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    interest_cd = models.IntegerField(
        db_column='INTEREST_CD', blank=True, null=True
    )
    interest_name = models.CharField(
        db_column='INTEREST_NAME', max_length=24, blank=True
    )
    session_yr_1 = models.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = models.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = models.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = models.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = models.FloatField(db_column='QTR_1')
    qtr_2 = models.FloatField(db_column='QTR_2')
    qtr_3 = models.FloatField(db_column='QTR_3')
    qtr_4 = models.FloatField(db_column='QTR_4')
    qtr_5 = models.FloatField(db_column='QTR_5')
    qtr_6 = models.FloatField(db_column='QTR_6')
    qtr_7 = models.FloatField(db_column='QTR_7')
    qtr_8 = models.FloatField(db_column='QTR_8')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMPLOYER3_CD'
        verbose_name = 'LOBBYIST_EMPLOYER3_CD'
        verbose_name_plural = 'LOBBYIST_EMPLOYER3_CD'


class LobbyistEmployerFirms1Cd(CalAccessBaseModel):
    """
    This is an undocumented model.
    """
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    firm_id = models.IntegerField(db_column='FIRM_ID')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=117)
    session_id = models.IntegerField(db_column='SESSION_ID')
    termination_dt = models.CharField(
        db_column='TERMINATION_DT', max_length=32, blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMPLOYER_FIRMS1_CD'
        verbose_name = 'LOBBYIST_EMPLOYER_FIRMS1_CD'
        verbose_name_plural = 'LOBBYIST_EMPLOYER_FIRMS1_CD'


class LobbyistEmployerFirms2Cd(CalAccessBaseModel):
   
    """ 
    This groups terminations by lobby firms.

    """

    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    firm_id = models.IntegerField(db_column='FIRM_ID')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=117)
    session_id = models.IntegerField(db_column='SESSION_ID')
    termination_dt = models.CharField(
        db_column='TERMINATION_DT', max_length=32, blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMPLOYER_FIRMS2_CD'
        verbose_name = 'LOBBYIST_EMPLOYER_FIRMS2_CD'
        verbose_name_plural = 'LOBBYIST_EMPLOYER_FIRMS2_CD'


class LobbyistEmpLobbyist1Cd(CalAccessBaseModel):
    lobbyist_id = models.IntegerField(db_column='LOBBYIST_ID')
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    lobbyist_last_name = models.CharField(
        db_column='LOBBYIST_LAST_NAME', max_length=17
    )
    lobbyist_first_name = models.CharField(
        db_column='LOBBYIST_FIRST_NAME', max_length=17
    )
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=117)
    session_id = models.IntegerField(db_column='SESSION_ID')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMP_LOBBYIST1_CD'
        verbose_name = 'LOBBYIST_EMP_LOBBYIST1_CD'
        verbose_name_plural = 'LOBBYIST_EMP_LOBBYIST1_CD'


class LobbyistEmpLobbyist2Cd(CalAccessBaseModel):
    """
    This is an undocumented model.
    """
    lobbyist_id = models.IntegerField(db_column='LOBBYIST_ID')
    employer_id = models.IntegerField(db_column='EMPLOYER_ID')
    lobbyist_last_name = models.CharField(
        db_column='LOBBYIST_LAST_NAME', max_length=17
    )
    lobbyist_first_name = models.CharField(
        db_column='LOBBYIST_FIRST_NAME', max_length=17
    )
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=117)
    session_id = models.IntegerField(db_column='SESSION_ID')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_EMP_LOBBYIST2_CD'
        verbose_name = 'LOBBYIST_EMP_LOBBYIST2_CD'
        verbose_name_plural = 'LOBBYIST_EMP_LOBBYIST2_CD'


class LobbyistFirm1Cd(CalAccessBaseModel):
    firm_id = models.IntegerField(db_column='FIRM_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=60)
    current_qtr_amt = models.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = models.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = models.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    session_yr_1 = models.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = models.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = models.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = models.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = models.FloatField(db_column='QTR_1')
    qtr_2 = models.FloatField(db_column='QTR_2')
    qtr_3 = models.FloatField(db_column='QTR_3')
    qtr_4 = models.FloatField(db_column='QTR_4')
    qtr_5 = models.FloatField(db_column='QTR_5')
    qtr_6 = models.FloatField(db_column='QTR_6')
    qtr_7 = models.FloatField(db_column='QTR_7')
    qtr_8 = models.FloatField(db_column='QTR_8')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM1_CD'
        verbose_name = 'LOBBYIST_FIRM1_CD'
        verbose_name_plural = 'LOBBYIST_FIRM1_CD'


class LobbyistFirm2Cd(CalAccessBaseModel):
    """
    This is an undocumented model.
    """
    firm_id = models.IntegerField(db_column='FIRM_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=60)
    current_qtr_amt = models.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = models.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = models.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    session_yr_1 = models.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = models.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = models.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = models.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = models.FloatField(db_column='QTR_1')
    qtr_2 = models.FloatField(db_column='QTR_2')
    qtr_3 = models.FloatField(db_column='QTR_3')
    qtr_4 = models.FloatField(db_column='QTR_4')
    qtr_5 = models.FloatField(db_column='QTR_5')
    qtr_6 = models.FloatField(db_column='QTR_6')
    qtr_7 = models.FloatField(db_column='QTR_7')
    qtr_8 = models.FloatField(db_column='QTR_8')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM2_CD'
        verbose_name = 'LOBBYIST_FIRM2_CD'
        verbose_name_plural = 'LOBBYIST_FIRM2_CD'


class LobbyistFirm3Cd(CalAccessBaseModel):
    firm_id = models.IntegerField(db_column='FIRM_ID')
    session_id = models.IntegerField(db_column='SESSION_ID')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=60)
    current_qtr_amt = models.FloatField(db_column='CURRENT_QTR_AMT')
    session_total_amt = models.FloatField(db_column='SESSION_TOTAL_AMT')
    contributor_id = models.IntegerField(
        db_column='CONTRIBUTOR_ID', blank=True, null=True
    )
    session_yr_1 = models.IntegerField(db_column='SESSION_YR_1')
    session_yr_2 = models.IntegerField(db_column='SESSION_YR_2')
    yr_1_ytd_amt = models.FloatField(db_column='YR_1_YTD_AMT')
    yr_2_ytd_amt = models.FloatField(db_column='YR_2_YTD_AMT')
    qtr_1 = models.FloatField(db_column='QTR_1')
    qtr_2 = models.FloatField(db_column='QTR_2')
    qtr_3 = models.FloatField(db_column='QTR_3')
    qtr_4 = models.FloatField(db_column='QTR_4')
    qtr_5 = models.FloatField(db_column='QTR_5')
    qtr_6 = models.FloatField(db_column='QTR_6')
    qtr_7 = models.FloatField(db_column='QTR_7')
    qtr_8 = models.FloatField(db_column='QTR_8')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM3_CD'
        verbose_name = 'LOBBYIST_FIRM3_CD'
        verbose_name_plural = 'LOBBYIST_FIRM3_CD'


class LobbyistFirmEmployer1Cd(CalAccessBaseModel):
    '''
    This is an undocumented model (Ask Matt)
    '''
    firm_id = models.IntegerField(db_column='FIRM_ID')
    filing_id = models.IntegerField(db_column='FILING_ID')
    filing_sequence = models.IntegerField(db_column='FILING_SEQUENCE')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=58)
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=75)
    rpt_start = models.DateField(db_column='RPT_START', null=True)
    rpt_end = models.DateField(db_column='RPT_END', null=True)
    per_total = models.FloatField(db_column='PER_TOTAL')
    cum_total = models.FloatField(db_column='CUM_TOTAL')
    lby_actvty = models.CharField(
        db_column='LBY_ACTVTY', max_length=182, blank=True
    )
    ext_lby_actvty = models.CharField(
        db_column='EXT_LBY_ACTVTY', max_length=32, blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM_EMPLOYER1_CD'
        verbose_name = 'LOBBYIST_FIRM_EMPLOYER1_CD'
        verbose_name_plural = 'LOBBYIST_FIRM_EMPLOYER1_CD'


class LobbyistFirmEmployer2Cd(CalAccessBaseModel):
    """
    This is an undocumented model
    """
    firm_id = models.IntegerField(db_column='FIRM_ID')
    filing_id = models.IntegerField(db_column='FILING_ID')
    filing_sequence = models.IntegerField(db_column='FILING_SEQUENCE')
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=58)
    employer_name = models.CharField(db_column='EMPLOYER_NAME', max_length=75)
    rpt_start = models.DateField(db_column='RPT_START', null=True)
    rpt_end = models.DateField(db_column='RPT_END', null=True)
    per_total = models.FloatField(db_column='PER_TOTAL')
    cum_total = models.FloatField(db_column='CUM_TOTAL')
    lby_actvty = models.CharField(
        db_column='LBY_ACTVTY', max_length=182, blank=True
    )
    ext_lby_actvty = models.CharField(
        db_column='EXT_LBY_ACTVTY', max_length=32, blank=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM_EMPLOYER2_CD'
        verbose_name = 'LOBBYIST_FIRM_EMPLOYER2_CD'
        verbose_name_plural = 'LOBBYIST_FIRM_EMPLOYER2_CD'


class LobbyistFirmLobbyist1Cd(CalAccessBaseModel):
    """
    It's an undocumented model.
    """
    lobbyist_id = models.IntegerField(db_column='LOBBYIST_ID')
    firm_id = models.IntegerField(db_column='FIRM_ID')
    lobbyist_last_name = models.CharField(
        db_column='LOBBYIST_LAST_NAME', max_length=15
    )
    lobbyist_first_name = models.CharField(
        db_column='LOBBYIST_FIRST_NAME', max_length=17
    )
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=60)
    session_id = models.IntegerField(db_column='SESSION_ID')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM_LOBBYIST1_CD'
        verbose_name = 'LOBBYIST_FIRM_LOBBYIST1_CD'
        verbose_name_plural = 'LOBBYIST_FIRM_LOBBYIST1_CD'


class LobbyistFirmLobbyist2Cd(CalAccessBaseModel):
    lobbyist_id = models.IntegerField(db_column='LOBBYIST_ID')
    firm_id = models.IntegerField(db_column='FIRM_ID')
    lobbyist_last_name = models.CharField(
        db_column='LOBBYIST_LAST_NAME', max_length=15
    )
    lobbyist_first_name = models.CharField(
        db_column='LOBBYIST_FIRST_NAME', max_length=17
    )
    firm_name = models.CharField(db_column='FIRM_NAME', max_length=60)
    session_id = models.IntegerField(db_column='SESSION_ID')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOBBYIST_FIRM_LOBBYIST2_CD'
        verbose_name = 'LOBBYIST_FIRM_LOBBYIST2_CD'
        verbose_name_plural = 'LOBBYIST_FIRM_LOBBYIST2_CD'


class LookupCode(CalAccessBaseModel):
    code_type = models.IntegerField(db_column='CODE_TYPE')
    code_id = models.IntegerField(db_column='CODE_ID')
    code_desc = models.CharField(
        db_column='CODE_DESC',
        max_length=100,
        null=True
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOOKUP_CODES_CD'
        verbose_name = 'LOOKUP_CODES_CD'
        verbose_name_plural = 'LOOKUP_CODES_CD'


class NamesCd(CalAccessBaseModel):
    namid = models.IntegerField(db_column='NAMID')
    naml = models.CharField(max_length=200L, db_column='NAML')
    namf = models.CharField(max_length=50L, db_column='NAMF')
    namt = models.CharField(max_length=100L, db_column='NAMT', blank=True)
    nams = models.CharField(max_length=30L, db_column='NAMS', blank=True)
    moniker = models.CharField(max_length=30L, db_column='MONIKER', blank=True)
    moniker_pos = models.CharField(
        max_length=9L, db_column='MONIKER_POS', blank=True
    )
    namm = models.CharField(max_length=20L, db_column='NAMM', blank=True)
    fullname = models.CharField(max_length=200L, db_column='FULLNAME')
    naml_search = models.CharField(max_length=200L, db_column='NAML_SEARCH')

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'NAMES_CD'
        verbose_name = 'NAMES_CD'
        verbose_name_plural = 'NAMES_CD'


class ReceivedFilingsCd(CalAccessBaseModel):
    """
    This is undocumented. J M needs to describe this table.
    """
    filer_id = models.IntegerField(db_column='FILER_ID')
    filing_file_name = models.CharField(
        db_column='FILING_FILE_NAME', max_length=14
    )
    received_date = models.DateField(db_column='RECEIVED_DATE', null=True)
    filing_directory = models.CharField(
        db_column='FILING_DIRECTORY', max_length=45
    )
    filing_id = models.IntegerField(
        db_column='FILING_ID', blank=True, null=True
    )
    form_id = models.CharField(db_column='FORM_ID', max_length=4, blank=True)
    receive_comment = models.CharField(
        db_column='RECEIVE_COMMENT', max_length=51
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'RECEIVED_FILINGS_CD'
        verbose_name = 'RECEIVED_FILINGS_CD'
        verbose_name_plural = 'RECEIVED_FILINGS_CD'


class ReportsCd(CalAccessBaseModel):
    """
    This is an undocumented model.
    """
    rpt_id = models.IntegerField(db_column='RPT_ID', help_text="Unique identification number")
    rpt_name = models.CharField(db_column='RPT_NAME', max_length=74, help_text="Name of the report")
    rpt_desc_field = models.CharField(
        db_column='RPT_DESC_', max_length=32, blank=True, help_text="Description of the report")
    path = models.CharField(db_column='PATH', max_length=32, blank=True, help_text="Reportpath")
    data_object = models.CharField(db_column='DATA_OBJECT', max_length=38)
    parms_flg_y_n = models.IntegerField(
        db_column='PARMS_FLG_Y_N', blank=True, null=True, help_text="Parameters indication flag"
    )
    rpt_type = models.IntegerField(db_column='RPT_TYPE', help_text="Type of the report")
    parm_definition = models.IntegerField(db_column='PARM_DEFINITION', help_text="Parameter definition")

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'REPORTS_CD'
        verbose_name = 'REPORTS_CD'
        verbose_name_plural = 'REPORTS_CD'
