from __future__ import unicode_literals
from calaccess_raw import fields
from django.utils.encoding import python_2_unicode_compatible
from .base import CalAccessBaseModel


@python_2_unicode_compatible
class CvrSoCd(CalAccessBaseModel):
    """
    Cover page for a statement of organization creation or termination
    form filed by a slate-mailer organization or recipient committee.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE",
    )
    acct_opendt = fields.DateTimeField(
        db_column="ACCT_OPENDT",
        null=True,
        help_text='This field is undocumented',
    )
    ACTIVITY_LEVEL_CHOICES = (
        ("CI", "City"),
        ("CO", "County"),
        ("ST", "State"),
        ("", "Unknown"),
    )
    actvty_lvl = fields.CharField(
        max_length=2,
        db_column="ACTVTY_LVL",
        blank=True,
        choices=ACTIVITY_LEVEL_CHOICES,
        verbose_name="Activity level",
        help_text="Organization's level of activity"
    )
    amend_id = fields.IntegerField(
        db_column='AMEND_ID',
        db_index=True,
        help_text="Amendment identification number. A number of 0 is the \
original filing and 1 to 999 amendments.",
        verbose_name="amendment ID"
    )
    bank_adr1 = fields.CharField(
        max_length=55,
        db_column="BANK_ADR1",
        blank=True,
        help_text='This field is undocumented',
    )
    bank_adr2 = fields.CharField(
        max_length=55,
        db_column="BANK_ADR2",
        blank=True,
        help_text='This field is undocumented',
    )
    bank_city = fields.CharField(
        max_length=30,
        db_column="BANK_CITY",
        blank=True,
        help_text='This field is undocumented',
    )
    bank_nam = fields.CharField(
        max_length=200,
        db_column="BANK_NAM",
        blank=True,
        help_text='This field is undocumented',
    )
    bank_phon = fields.CharField(
        max_length=20,
        db_column="BANK_PHON",
        blank=True,
        help_text='This field is undocumented',
    )
    bank_st = fields.CharField(
        max_length=2,
        db_column="BANK_ST",
        blank=True,
        help_text='This field is undocumented',
    )
    bank_zip4 = fields.CharField(
        max_length=10,
        db_column="BANK_ZIP4",
        blank=True,
        help_text='This field is undocumented',
    )
    brdbase_cb = fields.CharField(
        max_length=1,
        db_column="BRDBASE_CB",
        blank=True,
        help_text='This field is undocumented',
    )
    city = fields.CharField(
        max_length=30,
        db_column="CITY",
        blank=True,
        help_text='This field is undocumented',
    )
    cmte_email = fields.CharField(
        max_length=60,
        db_column="CMTE_EMAIL",
        blank=True,
        help_text='This field is undocumented',
    )
    cmte_fax = fields.CharField(
        max_length=20,
        db_column="CMTE_FAX",
        blank=True,
        help_text='This field is undocumented',
    )
    com82013id = fields.CharField(
        max_length=9,
        db_column="COM82013ID",
        blank=True,
        help_text='This field is undocumented',
    )
    com82013nm = fields.CharField(
        max_length=200,
        db_column="COM82013NM",
        blank=True,
        help_text='This field is undocumented',
    )
    com82013yn = fields.CharField(
        max_length=1,
        db_column="COM82013YN",
        blank=True,
        help_text='This field is undocumented',
    )
    control_cb = fields.CharField(
        max_length=1,
        db_column="CONTROL_CB",
        blank=True,
        help_text='This field is undocumented',
    )
    county_act = fields.CharField(
        max_length=20,
        db_column="COUNTY_ACT",
        blank=True,
        help_text='This field is undocumented',
    )
    county_res = fields.CharField(
        max_length=20,
        db_column="COUNTY_RES",
        blank=True,
        help_text='This field is undocumented',
    )
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('BMC', 'Ballot measure committee'),
        ('CAO', 'Candidate/officeholder'),
        ('COM', 'Committee'),
        ('CTL', 'Controlled committee'),
        ('RCP', 'Recipient committee'),
        ('SMO', 'Slate-mailer organization'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column="ENTITY_CD",
        blank=True,
        choices=ENTITY_CODE_CHOICES,
        verbose_name="Entity code"
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
        verbose_name="Filer first name"
    )
    filer_naml = fields.CharField(
        max_length=200,
        db_column="FILER_NAML",
        blank=True,
        verbose_name="Filer last name"
    )
    filer_nams = fields.CharField(
        max_length=10,
        db_column="FILER_NAMS",
        blank=True,
        verbose_name="Filer name suffix"
    )
    filer_namt = fields.CharField(
        max_length=10,
        db_column="FILER_NAMT",
        blank=True,
        verbose_name="Filer name title"
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = (
        ('F400', 'Form 400 (Statement of organization, \
slate mailer organization)'),
        ('F402', 'Form 402 (Statement of termination, \
slate mailer organization'),
        ('F410', 'Form 410 (Statement of organization, recipient committee)'),
    )
    form_type = fields.CharField(
        max_length=4,
        db_column="FORM_TYPE",
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule'
    )
    genpurp_cb = fields.CharField(
        max_length=1,
        db_column="GENPURP_CB",
        blank=True,
        help_text='This field is undocumented',
    )
    gpc_descr = fields.CharField(
        max_length=300,
        db_column="GPC_DESCR",
        blank=True,
        help_text='This field is undocumented',
    )
    mail_city = fields.CharField(
        max_length=30,
        db_column="MAIL_CITY",
        blank=True,
        help_text='This field is undocumented',
    )
    mail_st = fields.CharField(
        max_length=2,
        db_column="MAIL_ST",
        blank=True,
        help_text='This field is undocumented',
    )
    mail_zip4 = fields.CharField(
        max_length=10,
        db_column="MAIL_ZIP4",
        blank=True,
        help_text='This field is undocumented',
    )
    phone = fields.CharField(
        max_length=20,
        db_column="PHONE",
        blank=True,
        help_text='This field is undocumented',
    )
    primfc_cb = fields.CharField(
        max_length=1,
        db_column="PRIMFC_CB",
        blank=True,
        help_text='This field is undocumented',
    )
    qualfy_dt = fields.DateTimeField(
        db_column="QUALFY_DT",
        null=True,
        verbose_name="Date qualified",
        help_text="Date qualified as an organization"
    )
    qual_cb = fields.CharField(
        max_length=1,
        db_column="QUAL_CB",
        blank=True,
        help_text='This field is undocumented',
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
        db_column="REPORT_NUM",
        blank=True,
        help_text='This field is undocumented',
    )
    rpt_date = fields.DateTimeField(
        db_column="RPT_DATE",
        null=True,
        help_text='This field is undocumented',
    )
    smcont_qualdt = fields.DateTimeField(
        db_column="SMCONT_QUALDT",
        null=True,
        help_text='This field is undocumented',
    )
    sponsor_cb = fields.CharField(
        max_length=1,
        db_column="SPONSOR_CB",
        blank=True,
        help_text='This field is undocumented',
    )
    st = fields.CharField(
        max_length=2,
        db_column="ST",
        blank=True,
        help_text='This field is undocumented',
    )
    surplusdsp = fields.CharField(
        max_length=90,
        db_column="SURPLUSDSP",
        blank=True,
        help_text='This field is undocumented',
    )
    term_date = fields.DateTimeField(
        db_column="TERM_DATE",
        null=True,
        help_text='This field is undocumented',
    )
    tres_city = fields.CharField(
        max_length=30,
        db_column="TRES_CITY",
        blank=True,
        verbose_name="Treasurer's city"
    )
    tres_namf = fields.CharField(
        max_length=45,
        db_column="TRES_NAMF",
        blank=True,
        verbose_name="Treasurer's first name"
    )
    tres_naml = fields.CharField(
        max_length=200,
        db_column="TRES_NAML",
        blank=True,
        verbose_name="Treasurer's last name"
    )
    tres_nams = fields.CharField(
        max_length=10,
        db_column="TRES_NAMS",
        blank=True,
        verbose_name="Treasurer's name suffix"
    )
    tres_namt = fields.CharField(
        max_length=10,
        db_column="TRES_NAMT",
        blank=True,
        verbose_name="Treasurer's name title"
    )
    tres_phon = fields.CharField(
        max_length=20,
        db_column="TRES_PHON",
        blank=True,
        verbose_name="Treasurer's phone number"
    )
    tres_st = fields.CharField(
        max_length=2,
        db_column="TRES_ST",
        blank=True,
        verbose_name="Treasurer's street",
    )
    tres_zip4 = fields.CharField(
        max_length=10,
        db_column="TRES_ZIP4",
        blank=True,
        help_text="Treasurer's ZIP Code"
    )
    zip4 = fields.CharField(
        max_length=10,
        db_column="ZIP4",
        blank=True,
        help_text='This field is undocumented',
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = "CVR_SO_CD"
        verbose_name = 'CVR_SO_CD'
        verbose_name_plural = 'CVR_SO_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class Cvr2SoCd(CalAccessBaseModel):
    """
    Additional names and committees information included on the second page
    of a statement of organization creation form filed
    by a slate-mailer organization or recipient committee.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
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
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    FORM_TYPE_CHOICES = (
        ('F400', 'Form 400 (Statement of organization, \
slate mailer organization)'),
        ('F410', 'Form 410 (Statement of organization, recipient committee)'),
    )
    form_type = fields.CharField(
        choices=FORM_TYPE_CHOICES,
        db_column='FORM_TYPE',
        max_length=4,
        help_text='Name of the source filing form or schedule'
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
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('ATH', 'Authorizing individual'),
        ('ATR', 'Assistant treasurer'),
        ('BMN', 'BMN (Unknown)'),
        ('BNM', 'Ballot measure\'s name/title'),
        ('CAO', 'Candidate/officeholder'),
        ('COM', 'Committee'),
        ('CTL', 'Controlled committee'),
        ('OFF', 'Officer'),
        ('POF', 'Principal officer'),
        ('PRO', 'Proponent'),
        ('SPO', 'Sponsor'),
    )
    entity_cd = fields.CharField(
        db_column='ENTITY_CD',
        max_length=3,
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
    )
    enty_naml = fields.CharField(
        db_column='ENTY_NAML',
        max_length=194,
        blank=True,
        help_text="Entity's business name or last name if the entity is an \
individual"
    )
    enty_namf = fields.CharField(
        db_column='ENTY_NAMF',
        max_length=34,
        blank=True,
        help_text="Entity's first name if the entity is an individual"
    )
    enty_namt = fields.CharField(
        db_column='ENTY_NAMT',
        max_length=9,
        blank=True,
        help_text="Entity's name prefix or title if the entity is an \
individual"
    )
    enty_nams = fields.CharField(
        db_column='ENTY_NAMS',
        max_length=10,
        blank=True,
        help_text="Entity's name suffix if the entity is an individual"
    )
    item_cd = fields.CharField(
        db_column='ITEM_CD',
        max_length=4,
        blank=True,
        help_text="Section of the Statement of Organization this \
itemization relates to. See CAL document for the definition \
of legal values for this column."
    )
    mail_city = fields.CharField(
        db_column='MAIL_CITY',
        max_length=25,
        blank=True,
        help_text="City portion of the entity's mailing address"
    )
    mail_st = fields.CharField(
        db_column='MAIL_ST',
        max_length=4,
        blank=True,
        help_text="State portion of the entity's mailing address"
    )
    mail_zip4 = fields.CharField(
        db_column='MAIL_ZIP4',
        max_length=10,
        blank=True,
        help_text="Zipcode portion of the entity's mailing address"
    )
    day_phone = fields.CharField(
        db_column='DAY_PHONE',
        max_length=20,
        blank=True,
        help_text="Entity's daytime phone number"
    )
    fax_phone = fields.CharField(
        db_column='FAX_PHONE',
        max_length=20,
        blank=True,
        help_text="Entity's fax number"
    )
    email_adr = fields.CharField(
        db_column='EMAIL_ADR',
        max_length=40,
        blank=True,
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
        max_length=87,
        blank=True,
        help_text="Industry group/affiliation description"
    )
    office_cd = fields.CharField(
        db_column='OFFICE_CD',
        max_length=4,
        blank=True,
        help_text="Code that identifies the office being sought. See \
CAL document for a list of valid codes."
    )
    offic_dscr = fields.CharField(
        db_column='OFFIC_DSCR',
        max_length=40,
        blank=True,
        help_text="Office sought description used if the office sought code \
(OFFICE_CD) equals other (OTH)."
    )
    juris_cd = fields.CharField(
        db_column='JURIS_CD',
        max_length=4,
        blank=True,
        help_text="Office jurisdiction code. See CAL document for a \
list of legal values."
    )
    juris_dscr = fields.CharField(
        db_column='JURIS_DSCR',
        max_length=40,
        blank=True,
        help_text="Office jurisdiction description provided if the \
        jurisdiction code (JURIS_CD) equals other (OTH)."
    )
    dist_no = fields.CharField(
        db_column='DIST_NO',
        max_length=4,
        blank=True,
        help_text="Office district number for Senate, Assembly, and Board \
of Equalization districts."
    )
    off_s_h_cd = fields.CharField(
        db_column='OFF_S_H_CD',
        max_length=4,
        blank=True,
        help_text="Office sought/held code. Legal values are 'S' for sought \
and 'H' for held."
    )
    non_pty_cb = fields.CharField(
        db_column='NON_PTY_CB',
        max_length=4,
        blank=True,
        help_text="Non-partisan check-box. Legal values are 'X' and null."
    )
    party_name = fields.CharField(
        db_column='PARTY_NAME',
        max_length=63,
        blank=True,
        help_text="Name of party (if partisan)"
    )
    bal_num = fields.CharField(
        db_column='BAL_NUM',
        max_length=7,
        blank=True,
        help_text="Ballot measure number or letter"
    )
    bal_juris = fields.CharField(
        db_column='BAL_JURIS',
        max_length=40,
        blank=True,
        help_text="Jurisdiction of ballot measure"
    )
    sup_opp_cd = fields.CharField(
        db_column='SUP_OPP_CD',
        max_length=4,
        blank=True,
        help_text="Support/oppose code (S/O). Legal values are 'S' for \
support and 'O' for oppose."
    )
    year_elect = fields.CharField(
        db_column='YEAR_ELECT',
        max_length=4,
        blank=True,
        help_text="Year of election"
    )
    pof_title = fields.CharField(
        db_column='POF_TITLE',
        max_length=44,
        blank=True,
        help_text="Position/title of the principal officer"
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR2_SO_CD'
        verbose_name = 'CVR2_SO_CD'
        verbose_name_plural = 'CVR2_SO_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class CvrCampaignDisclosureCd(CalAccessBaseModel):
    """
    Cover page information from campaign disclosure forms
    """
    UNIQUE_KEY = ['filing_id', 'amend_id']
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
        help_text="This field is undocumented"
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
    # bus_adr1 = fields.CharField(
    #     max_length=55, db_column='BUS_ADR1', blank=True
    # )
    # bus_adr2 = fields.CharField(
    #     max_length=55, db_column='BUS_ADR2', blank=True
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
    # cand_adr1 = fields.CharField(
    #     max_length=55, db_column='CAND_ADR1', blank=True
    # )
    # cand_adr2 = fields.CharField(
    #     max_length=55, db_column='CAND_ADR2', blank=True
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
        help_text="This field is not documented"
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
    cmtte_type = fields.CharField(
        max_length=1,
        db_column='CMTTE_TYPE',
        blank=True,
        verbose_name="Committee type",
        help_text="Type of Recipient Committee. Applies to the 450/460."
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
    elect_date = fields.DateTimeField(
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
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('BMC', 'Ballot measure committee'),
        ('CAO', 'Candidate/officeholder'),
        ('COM', 'Committee'),
        ('CTL', 'Controlled committee'),
        ('IND', 'Person (Spending > $5,000)'),
        ('MDI', 'Major donor/independent expenditure'),
        ('OTH', 'Other'),
        ('PTY', 'Political party'),
        ('RCP', 'Recipient committee'),
        ('SCC', 'Small contributor committee'),
        ('SMO', 'Slate mailer organization'),
    )
    entity_cd = fields.CharField(
        max_length=4,
        db_column='ENTITY_CD',
        blank=True,
        choices=ENTITY_CODE_CHOICES,
        verbose_name='entity code'
    )
    file_email = fields.CharField(
        max_length=60,
        db_column='FILE_EMAIL',
        blank=True,
        help_text="Filer's email address"
    )
    # filer_adr1 = fields.CharField(
    #     max_length=55, db_column='FILER_ADR1', blank=True
    # )
    # filer_adr2 = fields.CharField(
    #     max_length=55, db_column='FILER_ADR2', blank=True
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
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = (
        ('F511', 'Form 511 (Paid spokesman report)'),
        ('F900', 'Form 900 (Public employee\'s retirement board, \
candidate campaign statement)'),
        ('F425', 'Form 425 (Semi-annual statement of no activity, \
non-controlled recipient committee)'),
        ('F450', 'Form 450 (Recipient committee campaign statement, \
short form)'),
        ('F401', 'Form 401 (Slate mailer organization campaign statement)'),
        ('F498', 'Form 498 (Late payment report, slate mailer organizations'),
        ('F465', 'Form 465 (Supplemental independent expenditure report'),
        ('F496', 'Form 496 (Late independent expenditure report)'),
        ('F461', 'Form 461 (Independent expenditure committee \
and major donor committee campaign statement)'),
        ('F460', 'Form 460 (Recipient committee campaign statement)'),
        ('F497', 'Form 497 (Late contribution report)')
    )
    form_type = fields.CharField(
        choices=FORM_TYPE_CHOICES,
        max_length=4,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule'
    )
    from_date = fields.DateTimeField(
        null=True,
        db_column='FROM_DATE',
        blank=True,
        help_text="Reporting period from date"
    )
    juris_cd = fields.CharField(
        max_length=3,
        db_column='JURIS_CD',
        blank=True,
        help_text="Office jurisdiction code"
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
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text='Office Sought/Held Code. Legal values are "S" for \
sought and "H" for held.'
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office sought description if the field OFFICE_CD is set \
to other (OTH)"
    )
    office_cd = fields.CharField(
        max_length=3,
        db_column='OFFICE_CD',
        blank=True,
        verbose_name="Office code",
        help_text="Code that identifies the office being sought"
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
        ("CVR", "Cover"),
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
        help_text="Amendment number, as reported by the filer \
Report Number 000 represents an original filing. 001-999 are amendments."
    )
    reportname = fields.CharField(
        max_length=3,
        db_column='REPORTNAME',
        blank=True,
        help_text="Attached campaign disclosure statement type. Legal \
values are 450, 460, and 461."
    )
    rpt_att_cb = fields.CharField(
        max_length=4,
        db_column='RPT_ATT_CB',
        blank=True,
        help_text="Committee Report Attached check-box. Legal values \
are 'X' or null. This field applies to the form 401."
    )
    rpt_date = fields.DateTimeField(
        db_column='RPT_DATE',
        null=True,
        help_text="Date this report was filed, according to the filer"
    )
    rptfromdt = fields.DateTimeField(
        null=True,
        db_column='RPTFROMDT',
        blank=True,
        help_text="Attached campaign disclosure statement - Period from \
date."
    )
    rptthrudt = fields.DateTimeField(
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
        help_text="Self employed check-box"
    )
    sponsor_yn = fields.IntegerField(
        null=True,
        db_column='SPONSOR_YN',
        blank=True,
        help_text="Sponsored Committee (yes/no) checkbox. Legal values \
are 'Y' or 'N'."
    )
    stmt_type = fields.CharField(
        max_length=2,
        db_column='STMT_TYPE',
        blank=True,
        help_text='Type of statement'
    )
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text='Support/oppose code. Legal values are "S" for support \
or "O" for oppose.'
    )
    thru_date = fields.DateTimeField(
        null=True,
        db_column='THRU_DATE',
        blank=True,
        help_text='Reporting period through date'
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR_CAMPAIGN_DISCLOSURE_CD'
        verbose_name = 'CVR_CAMPAIGN_DISCLOSURE_CD'
        verbose_name_plural = 'CVR_CAMPAIGN_DISCLOSURE_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class Cvr2CampaignDisclosureCd(CalAccessBaseModel):
    """
    Record used to carry additional names for the campaign
    disclosure forms below.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
        )

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
        help_text="Commitee identification number, when the entity \
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
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('ATR', 'Assistant treasurer'),
        ('BNM', 'Ballot measure\'s name/title'),
        ('CAO', 'Candidate/officeholder'),
        ('CTL', 'Controlled committee'),
        ('COM', 'Committee'),
        ('FIL', 'Candidate filing/ballot fees'),
        ('OFF', 'Officer (Responsible)'),
        ('PEX', 'PEX (Unknown)'),
        ('POF', 'Principal officer'),
        ('PRO', 'Proponent'),
        ('RCP', 'Recipient committee'),
        ('RDP', 'RDP (Unknown)'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
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
    f460_part = fields.CharField(
        max_length=2,
        db_column='F460_PART',
        blank=True,
        help_text="Part of 460 cover page coded on ths cvr2 record. Legal \
values are 3, 4a, 4b, 5a, 5b, or 6."
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = (
        ('F425', 'Form 425 (Semi-annual statement of no activity, \
non-controlled committees)'),
        ('F450', 'Form 450 (Recipient committee campaign statement, \
short form)'),
        ('F460', 'Form 460 (Recipient committee campaign statement)'),
        ('F465', 'Form 465 (Supplemental independent expenditure report)'),
    )
    form_type = fields.CharField(
        choices=FORM_TYPE_CHOICES,
        max_length=4,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule'
    )
    juris_cd = fields.CharField(
        max_length=3,
        db_column='JURIS_CD',
        blank=True,
        help_text="Office jurisdiction code"
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
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text='Office sought/held code. Indicates if the candidate is an \
incumbent. Legal values are "S" for sought and "H" for held.'
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office sought description"
    )
    office_cd = fields.CharField(
        max_length=3,
        db_column='OFFICE_CD',
        blank=True,
        verbose_name="Office code",
        help_text="Code that identifies the office being sought"
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
    )
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text='Support/Oppose (S/O) code for the ballot measure. \
Legal values are "S" for support or "O" for oppose.'
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR2_CAMPAIGN_DISCLOSURE_CD'
        verbose_name = 'CVR2_CAMPAIGN_DISCLOSURE_CD'
        verbose_name_plural = 'CVR2_CAMPAIGN_DISCLOSURE_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class RcptCd(CalAccessBaseModel):
    """
    Receipts schedules for the following forms.

        Form 460 (Recipient Committee Campaign Statement)
        Schedules A, C, I, and A-1.

        Form 401 (Slate Mailer Organization Campaign Statement) Schedule A.
    """
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
        help_text="Amount Received (Monetary, Inkkind, Promise)"
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
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ("", "None"),
        ("0", "0 (Unknown)"),
        ("BNM", "Ballot measure\'s name/title"),
        ("COM", "Committee"),
        ("IND", "Individual"),
        ("OFF", "Officer (Responsible)"),
        ("OTH", "Other"),
        ("PTY", "Political party"),
        ("RCP", "Recipient commmittee"),
        ("SCC", "Small contributor committee"),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        help_text="Entity code: Values [CMO|RCP|IND|OTH]",
        choices=ENTITY_CODE_CHOICES
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = (
        ('F900', 'Form 900 (Public employee\'s retirement board, \
candidate campaign statement): Schedule A'),
        ('A-1', 'Form 460: Schedule A-1, contributions transferred \
to special election committees'),
        ('E530', 'Form E530 (Issue advocacy receipts)'),
        ('F496P3', 'Form 496 (Late independent expenditure): \
Part 3, contributions > $100 received'),
        ('F401A', 'Form 401 (Slate mailer organization): Schedule A, \
payments received'),
        ('I', 'Form 460 (Recipient committee campaign statement): \
Schedule I, miscellanous increases to cash'),
        ('C', 'Form 460 (Recipient committee campaign statement): \
Schedule C, non-monetary contributions received'),
        ('A', 'Form 460 (Recipient committee campaign statement): \
Schedule A, monetary contributions received')
    )
    form_type = fields.CharField(
        choices=FORM_TYPE_CHOICES,
        max_length=9,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule'
    )
    int_rate = fields.CharField(
        max_length=9,
        db_column='INT_RATE',
        blank=True,
        help_text="This field is undocumented"
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
    juris_cd = fields.CharField(
        max_length=3,
        db_column='JURIS_CD',
        blank=True,
        help_text="Office jurisdiction code. See the CAL document for the \
list of legal values. Used on Form 401 Schedule A"
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
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text="Office Sought/Held Code. Used on the Form 401 \
Schedule A. Legal values are 'S' for sought and 'H' for \
held"
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office Sought Description (used on F401A)"
    )
    office_cd = fields.CharField(
        max_length=3,
        db_column='OFFICE_CD',
        blank=True,
        help_text="Code that identifies the office being sought. See the \
CAL document for a list of valid codes. Used on the \
Form 401 Schedule A)"
    )
    rcpt_date = fields.DateField(
        db_column='RCPT_DATE',
        null=True,
        help_text="Date item received"
    )
    REC_TYPE_CHOICES = (
        ("E530", "E530"),
        ("RCPT", "RCPT"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text="Support/oppose code. Legal values are 'S' for support \
or 'O' for oppose. Used on Form 401 Sechedule A. \
Transaction identifier - permanent value unique to this item"
    )
    tran_id = fields.CharField(
        verbose_name='transaction ID',
        max_length=20,
        db_column='TRAN_ID',
        blank=True,
        help_text='Permanent value unique to this item',
    )
    tran_type = fields.CharField(
        max_length=1,
        db_column='TRAN_TYPE',
        blank=True,
        help_text="Transaction Type: Values T- third party | F Forgiven \
loan | R Returned (Negative amount)"
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'RCPT_CD'
        verbose_name = 'RCPT_CD'
        verbose_name_plural = 'RCPT_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class Cvr3VerificationInfoCd(CalAccessBaseModel):
    """
    Cover page verification information from campaign disclosure forms
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
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
        ("CVR3", "CVR3"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    FORM_TYPE_CHOICES = (
        ('F400', 'Form 400 (Statement of organization, \
slate mailer organization)'),
        ('F401', 'Form 401 (Slate mailer organization campaign statement)'),
        ('F402', 'Form 402 (Statement of termination, \
slate mailer organization'),
        ('F410', 'Form 410 (Statement of organization, recipient committee)'),
        ('F425', 'Form 425 (Semi-annual statement of no activity, \
non-controlled committees)'),
        ('F450', 'Form 450 (Recipient committee campaign statement, \
short form)'),
        ('F460', 'Form 460 (Recipient committee campaign statement)'),
        ('F461', 'Form 461 (Independent expenditure and major donor \
committee campaign statement)'),
        ('F465', 'Form 465 (Supplemental independent expenditure report)'),
        ('F511', 'Form 511 (Paid spokesman report)'),
        ('F900', 'Form 900 (Public employee\'s retirement board, \
candidate campaign statement)'),
    )
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=4,
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
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
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('0', '0 (Unknown)'),
        ('ATR', 'Assistant treasurer'),
        ('BBB', 'BBB (Unknown)'),
        ('COA', 'COA (Unknown)'),
        ('CAO', 'Candidate/officeholder'),
        ('CON', 'State controller'),
        ('MAI', 'MAI (Unknown)'),
        ('MDI', 'Major donor/independent expenditure'),
        ('OFF', 'Officer (Responsible)'),
        ('POF', 'Principal officer'),
        ('PRO', 'Proponent'),
        ('RCP', 'Recipient committee'),
        ('SPO', 'Sponsor'),
        ('TRE', 'Treasurer'),
    )
    entity_cd = fields.CharField(
        db_column='ENTITY_CD',
        max_length=3,
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR3_VERIFICATION_INFO_CD'
        verbose_name = 'CVR3_VERIFICATION_INFO_CD'
        verbose_name_plural = 'CVR3_VERIFICATION_INFO_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class LoanCd(CalAccessBaseModel):
    """
    Loans received and made
    """
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
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('COM', "Committee"),
        ("IND", "Person (spending > $5,000)"),
        ("OTH", "Other"),
        ("PTY", "Political party"),
        ('RCP', 'Recipient committee'),
        ('SCC', 'Small contributor committee'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name="entity code",
        choices=ENTITY_CODE_CHOICES,
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = (
        ('B1', 'Form 460 (Recipient committee campaign statement): \
Schedule B1'),
        ('B2', 'Form 460 (Recipient committee campaign statement): \
Schedule B2'),
        ('B3', 'Form 460 (Recipient committee campaign statement): \
Schedule B3'),
        ('H', 'Form 460 (Recipient committee campaign statement): \
Schedule H'),
        ('H1', 'Form 460 (Recipient committee campaign statement): \
Schedule H1'),
        ('H2', 'Form 460 (Recipient committee campaign statement): \
Schedule H2'),
        ('H3', 'Form 460 (Recipient committee campaign statement): \
Schedule H3'),
    )
    form_type = fields.CharField(
        max_length=2,
        db_column='FORM_TYPE',
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule'
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
        help_text="Date the loan was made or recieved. The content of this \
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
    loan_type = fields.CharField(
        max_length=3,
        db_column='LOAN_TYPE',
        blank=True,
        help_text="Type of loan"
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'LOAN_CD'
        verbose_name = 'LOAN_CD'
        verbose_name_plural = 'LOAN_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class S401Cd(CalAccessBaseModel):
    """
    This table contains Form 401 (Slate Mailer Organization) payment and other
    disclosure schedule (F401B, F401B-1, F401C, F401D) information.
    """
    UNIQUE_KEY = ['FILING_ID', 'AMEND_ID', 'LINE_ID', 'REC_TYPE', 'FORM_TYPE']
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
        ("S401", "S401"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    FORM_TYPE_CHOICES = (
        ('F401B', 'Form 401 (Slate mailer organization campaign statement): \
Schedule B, payments made'),
        ('F401B-1', 'Form 401 (Slate mailer organization campaign statement): \
Schedule B-1, payments made by agent or independent contractor'),
        ('F401C', 'Form 401 (Slate mailer organization campaign statement): \
Schedule C, persons receiving $1,000 or more'),
        ('F401D', 'Form 401 (Slate mailer organization campaign statement): \
Schedule D, candidates or measures supported or opposed with < $100 payment'),
    )
    form_type = fields.CharField(
        max_length=7,
        db_column='FORM_TYPE',
        blank=True,
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule'
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
    office_cd = fields.CharField(
        max_length=3,
        db_column='OFFICE_CD',
        blank=True,
        verbose_name="Office code",
        help_text="Code that identifies the office being sought"
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office sought description"
    )
    juris_cd = fields.CharField(
        max_length=3,
        db_column='JURIS_CD',
        blank=True,
        help_text="Office jurisdiction code"
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
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text="Office sought/held code"
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
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text='Support/oppose code. Legal values are "S" for support \
or "O" for oppose. Used on Form 401.'
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'S401_CD'
        verbose_name = 'S401_CD'
        verbose_name_plural = 'S401_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class ExpnCd(CalAccessBaseModel):
    """
    Campaign expenditures from a variety of forms
    """
    UNIQUE_KEY = (
        'FILING_ID',
        'AMEND_ID',
        'LINE_ITEM',
        'REC_TYPE',
        'FORM_TYPE'
    )
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
        max_length=20,
        db_column='BAKREF_TID',
        blank=True,
        help_text="Back Reference to a Tran_ID of a 'parent' record"
    )
    bal_juris = fields.CharField(
        max_length=40,
        db_column='BAL_JURIS',
        blank=True,
        help_text="Jurisdiction"
    )
    bal_name = fields.CharField(
        max_length=200,
        db_column='BAL_NAME',
        blank=True,
        help_text="Ballot Measure Name"
    )
    bal_num = fields.CharField(
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
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('0', '0 (Unknown)'),
        ('COM', 'Committee'),
        ('RCP', 'Recipient Committee'),
        ('IND', 'Person (spending > $5,000)'),
        ('OTH', 'Other'),
        ('PTY', 'Political party'),
        ('SCC', 'Small contributor committee'),
        ('BNM', 'Ballot measure\'s name/title'),
        ('CAO', 'Candidate/officeholder'),
        ('OFF', 'Officer'),
        ('PTH', 'PTH (Unknown)'),
        ('RFD', 'RFD (Unknown)'),
        ('MBR', 'MBR (Unknown)'),
    )
    entity_cd = fields.CharField(
        choices=ENTITY_CODE_CHOICES,
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
    )
    expn_chkno = fields.CharField(
        max_length=20,
        db_column='EXPN_CHKNO',
        blank=True,
        help_text="Check Number (Optional)"
    )
    expn_code = fields.CharField(
        max_length=3,
        db_column='EXPN_CODE',
        blank=True,
        help_text="Expense Code - Values: (Refer to list in Overview) \
Note: CTB & IND need explanation & listing on Sched D TRC & TRS require \
explanation."
    )
    expn_date = fields.DateField(
        null=True,
        db_column='EXPN_DATE',
        blank=True,
        help_text="Date of Expenditure (Note: Date not on Sched E & G)"
    )
    expn_dscr = fields.CharField(
        max_length=400,
        db_column='EXPN_DSCR',
        blank=True,
        help_text="Purpose of Expense and/or Description/explanation"
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
    FORM_TYPE_CHOICES = (
        ('D', 'Form 460 (Recipient committee campaign statement): \
Schedule D, summary of expenditure supporting/opposing other candidates, \
measures and committees'),
        ('E', 'Form 460 (Recipient committee campaign statement): \
Schedule E, payments made'),
        ('G', 'Form 460 (Recipient committee campaign statement): \
Schedule G, payments made by agent of independent contractor'),
        ('F450P5', 'Form 450 (Recipient Committee Campaign Statement \
Short Form): Part 5, payments made'),
        ('F461P5', 'Form 461 (Independent expenditure and major donor \
committee campaign statement): Part 5, contributions and expenditures made'),
        ('F465P3', 'Form 465 (Supplemental independent expenditure \
report): Part 3, independent expenditures made'),
        ('F900', 'Form 900 (Public Employee\'s Retirement Board Candidate \
Campaign Statement), Schedule B, expenditures made'),
    )
    form_type = fields.CharField(
        choices=FORM_TYPE_CHOICES,
        max_length=6,
        db_column='FORM_TYPE',
        help_text='Name of the source filing form or schedule'
    )
    g_from_e_f = fields.CharField(
        max_length=1,
        db_column='G_FROM_E_F',
        blank=True,
        help_text="Back Reference from Sched G to Sched 'E' or 'F'?"
    )
    juris_cd = fields.CharField(
        max_length=3,
        db_column='JURIS_CD',
        blank=True,
        help_text="Office Jurisdiction Code Values: STW=Statewide; \
        SEN=Senate District; ASM=Assembly District; \
        BOE=Board of Equalization District; \
        CIT=City; CTY=County; LOC=Local; OTH=Other"
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
        help_text="Memo Amount? (Date/Amount are informational only)"
    )
    memo_refno = fields.CharField(
        max_length=20,
        db_column='MEMO_REFNO',
        blank=True,
        help_text="Reference to text contained in a TEXT record."
    )
    OFF_S_H_CD_CHOICES = (
        ('H', 'Office Held'),
        ('S', 'Office Sought'),
        ('A', 'A - Unknown'),
        ('8', '8 - Unknown'),
        ('O', 'O - Unknown'),
    )
    off_s_h_cd = fields.CharField(
        choices=OFF_S_H_CD_CHOICES,
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text="Office Sought/Held Code: H=Held; S=Sought"
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office Sought Description (Req. if Office_Cd=OTH)"
    )
    office_cd = fields.CharField(
        max_length=3,
        db_column='OFFICE_CD',
        blank=True,
        help_text="Office Sought (See table of code in Overview)"
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
        ("EXPN", "EXPN"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text="Support/Oppose? Values: S; O (F450, F461)"
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'EXPN_CD'
        verbose_name = 'EXPN_CD'
        verbose_name_plural = 'EXPN_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class F495P2Cd(CalAccessBaseModel):
    """
    F495 Supplemental Preelection Campaign Statement

    It's attatchment to the forms below

        F450 Recipient Committee Campaign Statement Short Form
        F460 Recipient Committee Campaign Statement

    Form 495 is for use by a recipient committee that
    makes contributions totaling $10,000 or more in
    connection with an election for which the committee
    is not required to file regular preelection reports.
    Form 495 is filed as an attachment to a campaign
    disclosure statement (Form 450 or 460). On the
    Form 450 or 460, the committee will report all
    contributions received and expenditures made since
    its last report.
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_ITEM",
        "FORM_TYPE"
    )
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
        ('F495', 'F495'),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    FORM_TYPE_CHOICES = (
        ('F450', 'Form 450 (Recipient committee campaign statement, \
short form)'),
        ('F460', 'Form 460 (Recipient committee campaign statement)'),
    )
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=4,
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule'
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'F495P2_CD'
        verbose_name = 'F495P2_CD'
        verbose_name_plural = 'F495P2_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class DebtCd(CalAccessBaseModel):
    """
    Form 460 (Recipient Committee Campaign Statement)
    Schedule (F) Accrued Expenses (Unpaid Bills) records
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
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
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('BNM', 'Ballot measure\'s name/title'),
        ('COM', 'Committee'),
        ('IND', 'Person (spending > $5,000)'),
        ('OTH', 'Other'),
        ('PTY', 'Political party'),
        ('RCP', 'Recipient Committee'),
        ('SCC', 'Small contributor committee'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
        help_text='Entity code of the payee',
    )
    expn_code = fields.CharField(
        max_length=3,
        db_column='EXPN_CODE',
        blank=True,
        help_text='Expense code',
    )
    expn_dscr = fields.CharField(
        max_length=400,
        db_column='EXPN_DSCR',
        blank=True,
        help_text='Purpose of expense and/or description/explanation',
    )
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number of the parent filing",
    )
    FORM_TYPE_CHOICES = (
       ('F', 'Form 460 (Recipient committee campaign statement): \
Schedule F, accrued expenses (unpaid bills)'),
    )
    form_type = fields.CharField(
        max_length=1,
        db_column='FORM_TYPE',
        choices=FORM_TYPE_CHOICES,
        help_text='Schedule Name/ID: (F - Sched F / Accrued Expenses)'
    )
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Record line item number",
        db_index=True,
    )
    memo_code = fields.CharField(
        max_length=1, db_column='MEMO_CODE', blank=True,
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'DEBT_CD'
        verbose_name = 'DEBT_CD'
        verbose_name_plural = 'DEBT_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class S496Cd(CalAccessBaseModel):
    """
    Form 496 Late Independent Expenditures
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
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
        ('S496', 'S496'),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        max_length=4,
        db_column='REC_TYPE',
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    FORM_TYPE_CHOICES = (
        ('F496', 'F496 (Late independent expenditure report)'),
    )
    form_type = fields.CharField(
        max_length=4, db_column='FORM_TYPE', blank=True,
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule'
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'S496_CD'
        verbose_name = 'S496_CD'
        verbose_name_plural = 'S496_CD'

    def __str__(self):
        return "{} Filing {}, Amendment {}".format(
            self.form_type,
            self.filing_id,
            self.amend_id
        )


@python_2_unicode_compatible
class SpltCd(CalAccessBaseModel):
    """
    Split records
    """
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
class S497Cd(CalAccessBaseModel):
    """
    Form 497: Late Contributions Received/Made
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE"
    )
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
        ("S497", "S497"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    FORM_TYPE_CHOICES = (
        ('F497P1', 'Form 497 (Late contribution report): \
Part 1, late contributions received'),
        ('F497P2', 'Form 497 (Late contribution report): \
Part 2, late contributions made')
    )
    form_type = fields.CharField(
        max_length=6,
        db_column='FORM_TYPE',
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule'
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
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('0', '0 (Unknown)'),
        ('BNM', 'Ballot measure\'s name/title'),
        ('CAO', 'Candidate/officerholder'),
        ('CTL', 'Controlled committee'),
        ('COM', 'Committee'),
        ('IND', 'Person (spending > $5,000)'),
        ('OFF', 'Officer'),
        ('OTH', 'Other'),
        ('PTY', 'Political party'),
        ('RCP', 'Recipient Committee'),
        ('SCC', 'Small contributor committee'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
    )
    enty_naml = fields.CharField(
        max_length=200,
        db_column='ENTY_NAML',
        blank=True,
        help_text="Entity's last name or business name"
    )
    enty_namf = fields.CharField(
        max_length=45,
        db_column='ENTY_NAMF',
        blank=True,
        help_text="Entity's first name"
    )
    enty_namt = fields.CharField(
        max_length=10,
        db_column='ENTY_NAMT',
        blank=True,
        help_text="Entity's title or prefix"
    )
    enty_nams = fields.CharField(
        max_length=10,
        db_column='ENTY_NAMS',
        blank=True,
        help_text="Entity's suffix"
    )
    enty_city = fields.CharField(
        max_length=30,
        db_column='ENTY_CITY',
        blank=True,
        help_text="Filing committee's city address"
    )
    enty_st = fields.CharField(
        max_length=2,
        db_column='ENTY_ST',
        blank=True,
        help_text="Filing committee's state address"
    )
    enty_zip4 = fields.CharField(
        max_length=10,
        db_column='ENTY_ZIP4',
        blank=True,
        help_text="Filing committee's ZIP Code"
    )
    ctrib_emp = fields.CharField(
        max_length=200,
        db_column='CTRIB_EMP',
        blank=True,
        help_text="Employer"
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
        help_text='Self employed checkbox. "X" indicates the contributor is \
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
    office_cd = fields.CharField(
        max_length=3,
        db_column='OFFICE_CD',
        blank=True,
        verbose_name="Office code",
        help_text="Office sought code"
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Office sought description"
    )
    juris_cd = fields.CharField(
        max_length=3,
        db_column='JURIS_CD',
        blank=True,
        verbose_name="Jurisdiction code"
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
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text='Office Sought/Held Code. Legal values are "S" for \
sought and "H" for held.'
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
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text="This field is undocumented"
    )

    def __str__(self):
        return "{} Filing {}, Amendment {}".format(
            self.get_form_type_display(),
            self.filing_id,
            self.amend_id
        )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'S497_CD'
        verbose_name = 'S497_CD'
        verbose_name_plural = 'S497_CD'


@python_2_unicode_compatible
class F501502Cd(CalAccessBaseModel):
    """
    Candidate intention statement
    """
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
        ("CVR", "CVR"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    FORM_TYPE_CHOICES = (
        ('F501', 'Form 501 (Candidate intention statement)'),
        ('F502', 'Form 502 (Campaign bank account statement)')
    )
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=4,
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule'
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
        max_length=8,
        blank=True,
        verbose_name="Committee ID",
        help_text='Committee identification number'
    )
    entity_cd = fields.CharField(
        db_column='ENTITY_CD',
        blank=True,
        max_length=3,
        help_text='Entity code'
    )
    report_num = fields.IntegerField(
        db_column='REPORT_NUM',
        blank=True,
        null=True,
        help_text='Report Number; 000 Original; 001-999 Amended'
    )
    rpt_date = fields.DateTimeField(
        db_column='RPT_DATE',
        blank=True,
        null=True,
        help_text='date this report is filed'
    )
    stmt_type = fields.IntegerField(
        db_column='STMT_TYPE',
        help_text="Type of statement"
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
        max_length=81,
        blank=True,
        help_text="Candidate/officerholder last name"
    )
    cand_namf = fields.CharField(
        db_column='CAND_NAMF',
        max_length=25,
        blank=True,
        help_text="Candidate/officerholder first name"
    )
    can_namm = fields.CharField(
        db_column='CAN_NAMM',
        max_length=10,
        blank=True,
        help_text='Candidate/officeholder middle name'
    )
    cand_namt = fields.CharField(
        db_column='CAND_NAMT',
        max_length=7,
        blank=True,
        help_text="Candidate/officerholder title or prefix"
    )
    cand_nams = fields.CharField(
        db_column='CAND_NAMS',
        max_length=7,
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
        max_length=4,
        blank=True,
        help_text="Candidate/officeholder's moniker"
    )
    cand_city = fields.CharField(
        db_column='CAND_CITY',
        max_length=22,
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
        max_length=14,
        blank=True,
        help_text='Candidate/officeholder phone number'
    )
    cand_fax = fields.CharField(
        db_column='CAND_FAX',
        max_length=14,
        blank=True,
        help_text="Candidate/officerholder fax"
    )
    cand_email = fields.CharField(
        db_column='CAND_EMAIL',
        max_length=37,
        blank=True,
        help_text='Candidate/officeholder email address'
    )
    fin_naml = fields.CharField(
        db_column='FIN_NAML',
        max_length=53,
        blank=True,
        help_text="Financial institution's business name"
    )
    fin_namf = fields.CharField(
        db_column='FIN_NAMF',
        max_length=32,
        blank=True,
        help_text="Unused. Financial institution's first name."
    )
    fin_namt = fields.CharField(
        db_column='FIN_NAMT',
        max_length=32,
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
        max_length=20,
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
        max_length=9,
        blank=True,
        help_text="Financial institution's zip code."
    )
    fin_phon = fields.CharField(
        db_column='FIN_PHON',
        max_length=14,
        blank=True,
        help_text="Financial institution's phone number."
    )
    fin_fax = fields.CharField(
        db_column='FIN_FAX',
        max_length=10,
        blank=True,
        help_text="Financial institution's FAX Number."
    )
    fin_email = fields.CharField(
        db_column='FIN_EMAIL',
        max_length=15,
        blank=True,
        help_text="Financial institution's e-mail address."
    )
    office_cd = fields.IntegerField(
        db_column='OFFICE_CD',
        help_text="Office sought code"
    )
    offic_dscr = fields.CharField(
        db_column='OFFIC_DSCR',
        max_length=50,
        blank=True,
        help_text="Office sought description"
    )
    agency_nam = fields.CharField(
        db_column='AGENCY_NAM',
        max_length=63,
        blank=True,
        help_text="Agency name"
    )
    juris_cd = fields.IntegerField(
        db_column='JURIS_CD',
        blank=True,
        null=True,
        help_text='Office jurisdiction code'
    )
    juris_dscr = fields.CharField(
        db_column='JURIS_DSCR',
        max_length=14,
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
        max_length=20,
        blank=True,
        help_text="Political party"
    )
    yr_of_elec = fields.IntegerField(
        db_column='YR_OF_ELEC',
        blank=True,
        null=True,
        help_text='Year of election'
    )
    elec_type = fields.IntegerField(
        db_column='ELEC_TYPE',
        blank=True,
        null=True,
        verbose_name="Election type"
    )
    execute_dt = fields.DateTimeField(
        db_column='EXECUTE_DT',
        blank=True,
        null=True,
        help_text='Execution date'
    )
    can_sig = fields.CharField(
        db_column='CAN_SIG',
        max_length=13,
        blank=True,
        help_text='Candidate signature'
    )
    account_no = fields.CharField(
        db_column='ACCOUNT_NO',
        max_length=22,
        blank=True,
        help_text='Account number'
    )
    acct_op_dt = fields.DateField(
        db_column='ACCT_OP_DT',
        blank=True,
        null=True,
        help_text='Account open date'
    )
    party_cd = fields.IntegerField(
        db_column='PARTY_CD',
        blank=True,
        null=True,
        help_text="Party code"
    )
    district_cd = fields.IntegerField(
        db_column='DISTRICT_CD',
        blank=True,
        null=True,
        help_text='District number for the office being sought. \
Populated for Senate, Assembly, or Board of Equalization races.'
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'F501_502_CD'
        verbose_name = 'F501_502_CD'
        verbose_name_plural = 'F501_502_CD'


@python_2_unicode_compatible
class S498Cd(CalAccessBaseModel):
    """
    Form 498: Slate Mailer Late Independent Expenditures Made
    """
    UNIQUE_KEY = (
        "FILING_ID",
        "AMEND_ID",
        "LINE_ITEM",
        "REC_TYPE",
        "FORM_TYPE",
    )
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
        ("S498", "S498"),
    )
    rec_type = fields.CharField(
        verbose_name='record type',
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
    )
    FORM_TYPE_CHOICES = (
        ('F498-A', 'Form 498 (Slate mailer late payment report): \
Part A: late payments attributed to'),
        ('F498-R', 'Form 498 (Slate mailer late payment report): \
Part R: late payments received from')
    )
    form_type = fields.CharField(
        max_length=9,
        db_column='FORM_TYPE',
        blank=True,
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule'
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
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
        ('CAO', 'Candidate/officerholder'),
        ('COM', 'Committee'),
        ('IND', 'Person (spending > $5,000)'),
        ('OTH', 'Other'),
        ('RCP', 'Recipient Committee'),
    )
    entity_cd = fields.CharField(
        max_length=3,
        db_column='ENTITY_CD',
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES,
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
    office_cd = fields.CharField(
        max_length=3,
        db_column='OFFICE_CD',
        blank=True,
        verbose_name='Office code',
        help_text="Code that identifies the office being sought"
    )
    offic_dscr = fields.CharField(
        max_length=40,
        db_column='OFFIC_DSCR',
        blank=True,
        help_text="Description of office sought"
    )
    juris_cd = fields.CharField(
        max_length=3,
        db_column='JURIS_CD',
        blank=True,
        help_text="Office jurisdiction code"
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
    off_s_h_cd = fields.CharField(
        max_length=1,
        db_column='OFF_S_H_CD',
        blank=True,
        help_text='Office Sought/Held Code. Legal values are "S" for \
sought and "H" for held'
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
    sup_opp_cd = fields.CharField(
        max_length=1,
        db_column='SUP_OPP_CD',
        blank=True,
        help_text='Support/oppose code. Legal values are "S" for support \
or "O" for oppose.'
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

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'S498_CD'
        verbose_name = 'S498_CD'
        verbose_name_plural = 'S498_CD'
