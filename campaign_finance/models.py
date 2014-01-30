from django.db import models

# Create your models here.
class Filer(models.Model):
    FILER_TYPE_OPTIONS =(
        ('pac', 'Political Action Committee'),
        ('cand', 'Candidate'),
    )
    filer_id = models.IntegerField()
    xref_filer_id = models.IntegerField()
    name = models.CharField(max_length=255L)
    filer_type = models.CharField(max_length=10L, options=FILER_TYPE_OPTIONS)

class Committee(models.Model):
    CMTE_TYPE_OPTIONS = (
        ('md', 'Major Donor'),
        ('id', 'Independent Expenditure'),
        ('sm', 'Slate Mailer'),
        ('bi', 'Ballot Initiative'),
        ('cm', 'Candidate Committee'),
    )
    filer_id = models.IntegerField()
    xref_filer_id = models.IntegerField()
    name = models.CharField(max_length=255)
    committee_type = models.CharField(max_length=2, options=CMTE_TYPE_OPTIONS)

class CandidateCommittee(models.Model):
    filer_id = models.IntegerField()
    xref_filer_id = models.IntegerField()
    name = models.CharField(max_length=255)
    models.ForeignKey(Committee)
    models.ForeignKey(Filer)

class Cycle(models.model):
    name = models.IntegerField()

class Expenditure(models.Model):
    '''
    This is a condensed version of the Raw CAL-ACCESS EXPN_CD table
    It leaves out a lot of the supporting information for the expense
    Like jurisdiction info, ballot initiative info, treasurer info, support/opposition info, etc.
    This just pulls in who got paid and how much
    And tries to prep the data for categorization by orgs and individuals
    '''
    cycle = models.ForeignKey(Cycle)
    committee = models.ForeignKey(Committee)
    
    ## Raw data fields
    amend_id = models.IntegerField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    bakref_tid = models.CharField(max_length=10L, blank=True)
    cmte_id = models.CharField(max_length=9L, blank=True)
    cum_other = models.DecimalField(max_digits=16, decimal_places=2)
    cum_ytd = models.DecimalField(max_digits=16, decimal_places=2)
    entity_cd = model.CharField(max_length=5L, blank=True)
    expn_chkno = model.CharField(max_length=20L, blank=True)
    expn_code = model.CharField(max_length=3L, blank=True)
    expn_date = models.DateField()
    expn_dscr = model.CharField(max_length=400L, blank=True)
    filing_id = models.IntegerField()
    form_type = model.CharField(max_length=6L, blank=True)
    g_from_e_f = models.CharField(max_length=1L, blank=True) # back reference from Form 460 Schedule G to Schedule E or F
    line_item = models.IntegerField()
    memo_code = model.CharField(max_length=1L, blank=True)
    memo_refno = model.CharField(max_length=20L, blank=True)
    payee_adr1 = model.CharField(max_length=55L, blank=True)
    payee_adr2 = model.CharField(max_length=55L, blank=True)
    payee_city = model.CharField(max_length=30L, blank=True)
    payee_namf = model.CharField(max_length=5L, blank=True)
    payee_naml = model.CharField(max_length=200L, blank=True)
    payee_nams = model.CharField(max_length=10L, blank=True)
    payee_namt = model.CharField(max_length=10L, blank=True)
    payee_namst = model.CharField(max_length=2L, blank=True)
    payee_zip4 = model.CharField(max_length=10L, blank=True)
    tran_id = models.CharField(max_length=20L, blank=True)
    xref_match = models.CharField(max_length=1L, blank=True) # a related item on other schedule has the same transaction identifier. "X" indicates this condition is true
    xref_schnm = models.CharField(max_length=2L, blank=True) # Related record is included on Form 460 Schedules B2 or F
    
    ## Derived fields
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True) # False meanse they are duplicated, additional disclosure that shouldn't be used for summing up but provide addtional info on the transaction
    