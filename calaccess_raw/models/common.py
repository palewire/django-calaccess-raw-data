from __future__ import unicode_literals
from calaccess_raw import fields
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import floatformat
from django.contrib.humanize.templatetags.humanize import intcomma
from .base import CalAccessBaseModel


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
        (' NOT DEFINED', 'Undefined'),
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
        choices=FILER_TYPE_CHOICES
    )
    STATUS_CHOICES = (
        ('', 'Undefined'),
        ('A', ''),
        ('ACTIVE', ''),
        ('INACTIVE', ''),
        ('P', ''),
        ('R', ''),
        ('S', ''),
        ('TERMINATED', ''),
        ('W', ''),
    )
    status = fields.CharField(
        max_length=10,
        db_column='STATUS',
        db_index=True,
        choices=STATUS_CHOICES,
        blank=True,
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
    adr1 = fields.CharField(max_length=200, db_column='ADR1', blank=True)
    adr2 = fields.CharField(max_length=200, db_column='ADR2', blank=True)
    city = fields.CharField(max_length=55, db_column='CITY', blank=True)
    st = fields.CharField(max_length=4, db_column='ST', blank=True)
    zip4 = fields.CharField(max_length=10, db_column='ZIP4', blank=True)
    phon = fields.CharField(max_length=60, db_column='PHON', blank=True)
    fax = fields.CharField(max_length=60, db_column='FAX', blank=True)
    email = fields.CharField(max_length=60, db_column='EMAIL', blank=True)

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
    FORM_ID_CHOICES = (
        ('E530', ''),
        ('F111', ''),
        ('F400', ''),
        ('F401', ''),
        ('F402', ''),
        ('F405', ''),
        ('F410', ''),
        ('F410 AT', ''),
        ('F410ATR', ''),
        ('F415', ''),
        ('F416', ''),
        ('F419', ''),
        ('F420', ''),
        ('F421', ''),
        ('F425', ''),
        ('F430', ''),
        ('F440', ''),
        ('F450', ''),
        ('F460', ''),
        ('F461', ''),
        ('F465', ''),
        ('F470', ''),
        ('F470S', ''),
        ('F480', ''),
        ('F490', ''),
        ('F495', ''),
        ('F496', ''),
        ('F497', ''),
        ('F498', ''),
        ('F500', ''),
        ('F501', ''),
        ('F501502', ''),
        ('F502', ''),
        ('F555', ''),
        ('F601', ''),
        ('F602', ''),
        ('F603', ''),
        ('F604', ''),
        ('F605', ''),
        ('F606', ''),
        ('F607', ''),
        ('F615', ''),
        ('F625', ''),
        ('F635', ''),
        ('F645', ''),
        ('F666', ''),
        ('F690', ''),
        ('F700', ''),
        ('F777', ''),
        ('F888', ''),
        ('F900', ''),
        ('F999', ''),
    )
    form_id = fields.CharField(
        max_length=7,
        db_column='FORM_ID',
        db_index=True,
        verbose_name='form type',
        choices=FORM_ID_CHOICES,
        help_text="Form identification code"
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
    STATEMENT_TYPE_CHOICES = (
        (0, ''),
        (10001, ''),
        (10002, ''),
        (10003, ''),
        (10004, ''),
        (10005, ''),
        (10006, ''),
        (10007, ''),
    )
    stmnt_type = fields.IntegerField(
        db_column='STMNT_TYPE',
        verbose_name="statement type",
        db_index=True,
        choices=STATEMENT_TYPE_CHOICES,
        help_text="Type of statement"
    )
    STATEMENT_STATUS_CHOICES = (
        (0, ''),
        (11001, ''),
        (11002, ''),
        (11003, ''),
    )
    stmnt_status = fields.IntegerField(
        db_column='STMNT_STATUS',
        db_index=True,
        help_text="The status of the statement. If the filing has been \
reviewed or not reviewed.",
        verbose_name='statement status',
        choices=STATEMENT_STATUS_CHOICES,
    )
    session_id = fields.IntegerField(
        db_column='SESSION_ID',
        help_text="Legislative session that the filing applies to"
    )
    user_id = fields.CharField(max_length=12, db_column='USER_ID')
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
        choices=FILING_TYPE_CHOICES
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
    filing_id = fields.IntegerField(
        db_column='FILING_ID',
        db_index=True,
        verbose_name='filing ID',
        help_text="Unique filing identificiation number"
    )
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
        choices=FILING_TYPE_CHOICES
    )

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'FILINGS_CD'
        verbose_name = 'FILINGS_CD'
        verbose_name_plural = 'FILINGS_CD'

    def __str__(self):
        return str("%s %s" % (self.filing_id, self.filing_type))


@python_2_unicode_compatible
class SmryCd(CalAccessBaseModel):
    """
    Summary totals from filings.
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
    FORM_TYPE_CHOICES = (
        ('401A', 'Form 401 (Slate mailer organization campaign statement): \
Schedule A, payments received'),
        ('401B', 'Form 401 (Slate mailer organization campaign statement): \
Schedule B, payments made'),
        ('401B-1', 'Form 401 (Slate mailer organization campaign statement): \
Schedule B1, payments made by agent or independent contractor'),
        ('A', 'Form 460 (Recipient committee campaign statement): \
Schedule A, '),
        ('B1', 'Form 460 (Recipient committee campaign statement): \
Schedule B1, '),
        ('B2', 'Form 460 (Recipient committee campaign statement): \
Schedule B2, '),
        ('B3', 'Form 460 (Recipient committee campaign statement): \
Schedule B3, '),
        ('C', 'Form 460 (Recipient committee campaign statement): \
Schedule C, '),
        ('D', 'Form 460 (Recipient committee campaign statement): \
Schedule D, '),
        ('E', 'Form 460 (Recipient committee campaign statement): \
Schedule E, '),
        ('F', 'Form 460 (Recipient committee campaign statement): \
Schedule F, '),
        ('G', 'Form 460 (Recipient committee campaign statement): \
Schedule G, '),
        ('H', 'Form 460 (Recipient committee campaign statement): \
Schedule H, '),
        ('H1', 'Form 460 (Recipient committee campaign statement): \
Schedule H1, '),
        ('H2', 'Form 460 (Recipient committee campaign statement): \
Schedule H2, '),
        ('H3', 'Form 460 (Recipient committee campaign statement): \
Schedule H3, '),
        ('I', 'Form 460 (Recipient committee campaign statement): \
Schedule I, '),
        ('F401', 'Form 401 (Slate mailer organization campaign statement)'),

        ('F450', 'Form 450 (Recipient committee campaign statement, \
short form)'),
        ('F460', 'Form 460 (Recipient committee campaign statement)'),
        ('F461', 'Form 461 (Independent expenditure and major donor \
committee campaign statement)'),
        ('F465', 'Form 465 ()'),
        ('F625', 'Form 625 (Report of lobbying firm)'),
        ('F625P2', 'Form 625 (Report of lobbying firm): \
Part 2, payments received in connection with lobbying activity'),
        ('F625P3A', 'Form 625 (Report of lobbying firm): \
Part 3A, payments for activity expenses made in connection with \
lobbying activities'),
        ('F625P3B', 'Form 625 (Report of lobbying firm): \
Part 3B, payments to other lobbying firms made in connection with \
lobbying activities'),
        ('F635', 'Form 635 (Report of lobbyist employer and lobbying \
coalition)'),
        ('F635P3A', 'Form 635 (Report of lobbyist employer and lobbying \
coalition): Part 3A, payments in in-house employee lobbyists'),
        ('F635P3B', 'Form 635 (Report of lobbyist employer and lobbying \
coalition): Part 3B, payments to lobbying firms'),
        ('F635P3C', 'Form 635 (Report of lobbyist employer and lobbying \
coalition): Part 3C, activity expenses'),
        ('F635P3D', 'Form 635 (Report of lobbyist employer and lobbying \
coalition): Part 3D, other payments to influence legislative or \
administrative action'),
        ('F635P3E', 'Form 635 (Report of lobbyist employer and lobbying \
coalition): Part 3E, payments in connection with administrative testimony \
in ratemaking proceedings before the California Public Utilities Commission'),
        ('F645', 'Form 645 (Report of person spending $5,000 or more to \
influence legislative or administrative action)'),
        ('F645P2A', 'Form 645 (Report of person spending $5,000 or more to \
influence legislative or administrative action): Part 2A, activity expenses'),
        ('F645P2B', 'Form 645 (Report of person spending $5,000 or more to \
influence legislative or administrative action): Part 2B, \
other payments to influence legislative or administrative action'),
        ('F645P2C', 'Form 645 (Report of person spending $5,000 or more to \
influence legislative or administrative action): Part 2C, \
payments in connection with administrative testimony in ratemaking \
proceedings before the California Public Utilities Commission'),
        ('F900', 'Form 900 (Form 900 (Public Employee\'s Retirement Board \
         Candidate Campaign Statement)'),
        ('S640', 'Form 640 (Governmental agencies reporting ther payments to \
influence legislative or administrative action attachment)'),
    )
    form_type = fields.CharField(
        max_length=8,
        db_column='FORM_TYPE',
        db_index=True,
        choices=FORM_TYPE_CHOICES,
        help_text='Name of the source filing form or schedule'
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
    This table method is undocumented in the print docs.
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
        ('E530', 'Form 530 (Issue advocacy report)'),
    )
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=4,
        db_index=True,
        help_text='Name of the source filing form or schedule',
        choices=FORM_TYPE_CHOICES,
    )
    ENTITY_CODE_CHOICES = (
        # Defined here:
        # http://www.documentcloud.org/documents/1308003-cal-access-cal-\
        # format.html#document/p9
        ('', 'Unknown'),
    )
    entity_cd = fields.CharField(
        db_column='ENTITY_CD',
        max_length=32,
        blank=True,
        verbose_name='entity code',
        choices=ENTITY_CODE_CHOICES
    )
    filer_naml = fields.CharField(db_column='FILER_NAML', max_length=200)
    filer_namf = fields.CharField(
        db_column='FILER_NAMF', max_length=4, blank=True
    )
    filer_namt = fields.CharField(
        db_column='FILER_NAMT', max_length=32, blank=True
    )
    filer_nams = fields.CharField(
        db_column='FILER_NAMS', max_length=32, blank=True
    )
    report_num = fields.CharField(
        db_column='REPORT_NUM', max_length=32, blank=True
    )
    rpt_date = fields.DateField(db_column='RPT_DATE', null=True)
    filer_city = fields.CharField(
        db_column='FILER_CITY', max_length=16, blank=True
    )
    filer_st = fields.CharField(db_column='FILER_ST', max_length=4, blank=True)
    filer_zip4 = fields.CharField(
        db_column='FILER_ZIP4', max_length=10, blank=True
    )
    occupation = fields.CharField(
        db_column='OCCUPATION', max_length=15, blank=True
    )
    employer = fields.CharField(
        db_column='EMPLOYER', max_length=13, blank=True
    )
    cand_naml = fields.CharField(db_column='CAND_NAML', max_length=46)
    cand_namf = fields.CharField(
        db_column='CAND_NAMF', max_length=21, blank=True
    )
    cand_namt = fields.CharField(
        db_column='CAND_NAMT', max_length=32, blank=True
    )
    cand_nams = fields.CharField(
        db_column='CAND_NAMS', max_length=32, blank=True
    )
    district_cd = fields.IntegerField(db_column='DISTRICT_CD')
    office_cd = fields.IntegerField(db_column='OFFICE_CD')
    pmnt_dt = fields.DateField(db_column='PMNT_DT', null=True)
    pmnt_amount = fields.FloatField(db_column='PMNT_AMOUNT')
    type_literature = fields.IntegerField(db_column='TYPE_LITERATURE')
    type_printads = fields.IntegerField(db_column='TYPE_PRINTADS')
    type_radio = fields.IntegerField(db_column='TYPE_RADIO')
    type_tv = fields.IntegerField(db_column='TYPE_TV')
    type_it = fields.IntegerField(db_column='TYPE_IT')
    type_billboards = fields.IntegerField(db_column='TYPE_BILLBOARDS')
    type_other = fields.IntegerField(db_column='TYPE_OTHER')
    other_desc = fields.CharField(db_column='OTHER_DESC', max_length=49)

    class Meta:
        app_label = 'calaccess_raw'
        db_table = 'CVR_E530_CD'
        verbose_name = 'CVR_E530_CD'
        verbose_name_plural = 'CVR_E530_CD'

    def __str__(self):
        return str(self.filing_id)


@python_2_unicode_compatible
class TextMemoCd(CalAccessBaseModel):
    """
    Text memos attached to electronic filings
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
    line_item = fields.IntegerField(
        db_column='LINE_ITEM',
        help_text="Line item number of this record",
        db_index=True,
    )
    REC_TYPE_CHOICES = (
        ('i', 'i'),
        ('MEMO', 'MEMO'),
        ('TEXT', 'TEXT'),
        ('trun', 'trun'),
        ('Unde', 'Unde'),
    )
    rec_type = fields.CharField(
        db_column='REC_TYPE',
        max_length=4,
        db_index=True,
        choices=REC_TYPE_CHOICES,
        verbose_name='record type'
    )
    FORM_TYPE_CHOICES = (
        (' E', ''),
        ('410', ''),
        ('460', ''),
        ('461', ''),
        ('465', ''),
        ('496', ''),
        ('497', ''),
        ('497P1', ''),
        ('497P2', ''),
        ('A', ''),
        ('A4', ''),
        ('A6', ''),
        ('B', ''),
        ('B1', ''),
        ('B2', ''),
        ('B3', ''),
        ('C', ''),
        ('COMMENTS', ''),
        ('CVR', ''),
        ('D', ''),
        ('DEBTF', ''),
        ('E', ''),
        ('EXPNT', ''),
        ('F', ''),
        ('F401', ''),
        ('F401A', ''),
        ('F401B', ''),
        ('F401B-1', ''),
        ('F405', ''),
        ('F410', ''),
        ('F425', ''),
        ('F450', ''),
        ('F450P5', ''),
        ('F460', ''),
        ('F461', ''),
        ('F461P1', ''),
        ('F461P2', ''),
        ('F461P5', ''),
        ('F465', ''),
        ('F465P3', ''),
        ('F496', ''),
        ('F496P3', ''),
        ('F497', ''),
        ('F497P1', ''),
        ('F497P2', ''),
        ('F498-A', ''),
        ('F498-R', ''),
        ('F601', ''),
        ('F601P2A', ''),
        ('F601P2B', ''),
        ('F602', ''),
        ('F603', ''),
        ('F604', ''),
        ('F605', ''),
        ('F606', ''),
        ('F607', ''),
        ('F615', ''),
        ('F615P1', ''),
        ('F615P2', ''),
        ('F625', ''),
        ('F625P2', ''),
        ('F625P3A', ''),
        ('F625P3B', ''),
        ('F625P4B', ''),
        ('F635', ''),
        ('F635P3B', ''),
        ('F635P3C', ''),
        ('F635P4B', ''),
        ('F645', ''),
        ('F645P2A', ''),
        ('F645P3B', ''),
        ('G', ''),
        ('H', ''),
        ('H1', ''),
        ('H2', ''),
        ('H3', ''),
        ('I', ''),
        ('PT5', ''),
        ('RCPTB1', ''),
        ('RCPTC', ''),
        ('RCPTI', ''),
        ('S497', ''),
        ('S630', ''),
        ('S635-C', ''),
        ('S635C', ''),
        ('S640', ''),
        ('SCH A', ''),
        ('SF', ''),
        ('SMRY', ''),
        ('SPLT', ''),
        ('SUM', ''),
        ('SUMMARY', ''),
    )
    form_type = fields.CharField(
        db_column='FORM_TYPE',
        max_length=8,
        help_text='Name of the source filing form or schedule',
        db_index=True,
        choices=FORM_TYPE_CHOICES
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
