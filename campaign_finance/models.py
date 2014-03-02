from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models import Sum

# Create your models here.
class Filer(models.Model):
    FILER_TYPE_OPTIONS =(
        ('pac', 'Political Action Committee'),
        ('cand', 'Candidate'),
    )
    # straight out of the filer tables.
    filer_id = models.IntegerField()
    status = models.CharField(max_length=255, null=True)
    filer_type = models.CharField(max_length=10L, choices=FILER_TYPE_OPTIONS)
    
    ## fields updated by other tables
    xref_filer_id = models.CharField(max_length=32L, null=True)
    name = models.CharField(max_length=255L, null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('filer_detail', args=[str(self.slug), str(self.pk)])

    def _create_slug(self):
        return slugify(self.name)

    slug = property(_create_slug)

    def _total_contributions(self):

        qs = Filing.objects.filter(committee__filer=self)
        total = Summary.objects.filter(filing__in=qs).aggregate(tot=Sum('total_contribs'))['tot']
        return total

    total_contributions = property(_total_contributions) 


class Committee(models.Model):
    '''
        If a Candidate controls the committee, the filer is associated with the Candidate Filer record, not the committee Filer record
        But the committee Filer record can still be accessed using filer_id_raw
        So candidate filers potentially link to multiple committes, and committee filers that are not candidate controlled link back to one, committee filer
        If there's a better way I'm open to suggestions
    '''
    CMTE_TYPE_OPTIONS = (
        ('cand', 'Candidate Committee'),
        ('pac', 'Non-Candidate Committee'),
        ('linked-pac', 'Non-Candidate Committee, linked to other committees'),
    )
    filer = models.ForeignKey(Filer)
    filer_id_raw = models.IntegerField()
    name = models.CharField(max_length=255, null=True)
    committee_type = models.CharField(max_length=50, choices=CMTE_TYPE_OPTIONS)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('committee_detail', args=[str(self.pk)])

    def _total_contributions(self):
        qs = Filing.objects.filter(committee=self)
        total = Summary.objects.filter(filing__in=qs).aggregate(tot=Sum('total_contribs'))['tot']
        return total

    total_contributions = property(_total_contributions) 


class Cycle(models.Model):
    name = models.IntegerField()

class Filing(models.Model):
    cycle = models.ForeignKey(Cycle)
    committee = models.ForeignKey(Committee)
    filing_id = models.IntegerField()
    amend_id = models.IntegerField()
    form_id = models.CharField(max_length=7)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

class Summary(models.Model):
    FORM_TYPE_CHOICES = (
        ('F460', 'Recipient Committee Campaign Statement'),
        ('F450', 'Recipient Committee Campaign Statement -- Short Form'),
    )
    cycle = models.ForeignKey(Cycle)
    committee = models.ForeignKey(Committee)
    filing = models.ForeignKey(Filing)
    form_type = models.CharField(max_length=10, choices=FORM_TYPE_CHOICES)
    itemized_monetary_contribs = models.DecimalField(max_digits=16, decimal_places=2)
    unitemized_expenditures = models.DecimalField(max_digits=16, decimal_places=2)
    total_expenditures = models.DecimalField(max_digits=16, decimal_places=2)
    total_monetary_contribs = models.DecimalField(max_digits=16, decimal_places=2)
    unitemized_monetary_contribs = models.DecimalField(max_digits=16, decimal_places=2)
    non_monetary_contribs = models.DecimalField(max_digits=16, decimal_places=2)
    itemized_expenditures = models.DecimalField(max_digits=16, decimal_places=2)
    total_contribs = models.DecimalField(max_digits=16, decimal_places=2)
    outstanding_debts = models.DecimalField(max_digits=16, decimal_places=2)
    ending_cash_balance = models.DecimalField(max_digits=16, decimal_places=2)
    

class Expenditure(models.Model):
    '''
    This is a condensed version of the Raw CAL-ACCESS EXPN_CD table
    It leaves out a lot of the supporting information for the expense
    Like jurisdiction info, ballot initiative info, treasurer info, support/opposition info, etc.
    This just pulls in who got paid and how much
    And tries to prep the data for categorization by orgs and individuals
    Data comes from calaccess.models.ExpnCd
    '''
    cycle = models.ForeignKey(Cycle)
    committee = models.ForeignKey(Committee)
    
    ## Raw data fields
    amend_id = models.IntegerField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    bakref_tid = models.CharField(max_length=50L, blank=True)
    cmte_id = models.CharField(max_length=9L, blank=True)
    cum_ytd = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    entity_cd = models.CharField(max_length=5L, blank=True)
    expn_chkno = models.CharField(max_length=20L, blank=True)
    expn_code = models.CharField(max_length=3L, blank=True)
    expn_date = models.DateField(null=True)
    expn_dscr = models.CharField(max_length=400L, blank=True)
    filing_id = models.IntegerField()
    form_type = models.CharField(max_length=6L, blank=True)
    g_from_e_f = models.CharField(max_length=1L, blank=True) # back reference from Form 460 Schedule G to Schedule E or F
    line_item = models.IntegerField()
    memo_code = models.CharField(max_length=1L, blank=True)
    memo_refno = models.CharField(max_length=20L, blank=True)
    payee_adr1 = models.CharField(max_length=55L, blank=True)
    payee_adr2 = models.CharField(max_length=55L, blank=True)
    payee_city = models.CharField(max_length=30L, blank=True)
    payee_namf = models.CharField(max_length=255L, blank=True)
    payee_naml = models.CharField(max_length=200L, blank=True)
    payee_nams = models.CharField(max_length=10L, blank=True)
    payee_namt = models.CharField(max_length=10L, blank=True)
    payee_st = models.CharField(max_length=2L, blank=True)
    payee_zip4 = models.CharField(max_length=10L, blank=True)
    tran_id = models.CharField(max_length=20L, blank=True)
    xref_match = models.CharField(max_length=1L, blank=True) # a related item on other schedule has the same transaction identifier. "X" indicates this condition is true
    xref_schnm = models.CharField(max_length=2L, blank=True) # Related record is included on Form 460 Schedules B2 or F
    
    ## Derived fields
    name = models.CharField(max_length=255) # derive like so (e.payee_namt + ' '+ e.payee_namf + ' ' + e.payee_naml + ' ' + e.payee_nams).strip()
    status = models.BooleanField(default=True) # False meanse they are duplicated, additional disclosure that shouldn't be used for summing up but provide addtional info on the transaction
    org_id = models.IntegerField(null=True)
    individual_id = models.IntegerField(null=True)
    
    def raw(self):
        try:
            from calaccess.models import ExpnCd
            obj = ExpnCd.objects.get(amend_id=self.amend_id, filing_id=self.filing_id, tran_id=self.tran_id, bakref_tid=self.bakref_tid)
        except:
            print 'Raw data not available. Install calaccess app to process and house raw data.'
            obj = None
        return obj

class Contribution(models.Model):
    cycle = models.ForeignKey(Cycle)
    committee = models.ForeignKey(Committee)
    
    ## Raw data fields
    amend_id = models.IntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=14, db_column='AMOUNT')
    bakref_tid = models.CharField(max_length=20L, blank=True)
    cmte_id = models.CharField(max_length=9L, blank=True)
    ctrib_adr1 = models.CharField(max_length=55L, blank=True)
    ctrib_adr2 = models.CharField(max_length=55L, blank=True)
    ctrib_city = models.CharField(max_length=30L, blank=True)
    ctrib_dscr = models.CharField(max_length=90L, blank=True)
    ctrib_emp = models.CharField(max_length=200L, blank=True)
    ctrib_namf = models.CharField(max_length=255L, blank=True)
    ctrib_naml = models.CharField(max_length=200L, )
    ctrib_nams = models.CharField(max_length=10L, blank=True)
    ctrib_namt = models.CharField(max_length=10L, blank=True)
    ctrib_occ = models.CharField(max_length=60L, blank=True)
    ctrib_self = models.CharField(max_length=1L, blank=True)
    ctrib_st = models.CharField(max_length=2L, blank=True)
    ctrib_zip4 = models.CharField(max_length=10L, blank=True)
    cum_oth = models.DecimalField(decimal_places=2, null=True, max_digits=14, blank=True)
    cum_ytd = models.DecimalField(decimal_places=2, null=True, max_digits=14, blank=True)
    date_thru = models.DateField(null=True, blank=True)
    entity_cd = models.CharField(max_length=3L)
    filing_id = models.IntegerField()
    form_type = models.CharField(max_length=9L)
    intr_adr1 = models.CharField(max_length=55L, blank=True)
    intr_adr2 = models.CharField(max_length=55L, blank=True)
    intr_city = models.CharField(max_length=30L, blank=True)
    intr_cmteid = models.CharField(max_length=9L, blank=True)
    intr_emp = models.CharField(max_length=200L, blank=True)
    intr_namf = models.CharField(max_length=255L, blank=True)
    intr_naml = models.CharField(max_length=200L, blank=True)
    intr_nams = models.CharField(max_length=10L, blank=True)
    intr_namt = models.CharField(max_length=10L, blank=True)
    intr_occ = models.CharField(max_length=60L, blank=True)
    intr_self = models.CharField(max_length=1L, blank=True)
    intr_st = models.CharField(max_length=2L, blank=True)
    intr_zip4 = models.CharField(max_length=10L, blank=True)
    line_item = models.IntegerField()
    memo_code = models.CharField(max_length=1L, blank=True)
    memo_refno = models.CharField(max_length=20L, blank=True)
    rcpt_date = models.DateField(null=True)
    rec_type = models.CharField(max_length=4L)
    tran_id = models.CharField(max_length=20L)
    tran_type = models.CharField(max_length=1L, blank=True)
    xref_match = models.CharField(max_length=1L, blank=True)
    xref_schnm = models.CharField(max_length=2L, blank=True)
    
    ## Derived fields
    name = models.CharField(max_length=255) # derive like so (r.ctrib_namt + ' '+ r.ctrib_namf + ' ' + r.ctrib_naml + ' ' + r.ctrib_nams).strip()
    status = models.BooleanField(default=True) # False meanse they are duplicated, additional disclosure that shouldn't be used for summing up but provide addtional info on the transaction
    org_id = models.IntegerField(null=True)
    individual_id = models.IntegerField(null=True)
    
    def raw(self):
        try:
            from calaccess.models import RcptCd
            obj = RcptCd.objects.get(amend_id=self.amend_id, filing_id=self.filing_id, tran_id=self.tran_id, bakref_tid=self.bakref_tid)
        except:
            print 'Raw data not available. Install calaccess app to process and house raw data.'
            obj = None
        return obj

class Stats(models.Model):
    '''
        Flexible model for housing aggregate stats
        Should be able to add any stat you like for a filer_type in the options list
        And record any notes about how it was calculated and why
        Should allow for speedier display of aggregate data
        If it end up not working, we can blow it up and try something else
    '''
    FILER_TYPE_CHOICES = (
        ('cand', 'Candidate'),
        ('pac', 'Political Action Committee'),
    )
    STAT_TYPE_CHOICES = (
        ('itemized_monetary_contribs', 'Itemized Monetary Contributions'),
        ('unitemized_monetary_contribs', 'Unitemized Monetary Contributions'),
        ('total_contribs', 'Total Contributions'),
        ('total_expenditures', 'Total Expenditures'),
        ('outstanding_debts', 'Outstanding Debt'),
        
    )
    filer_type = models.CharField(max_length=10, choices=FILER_TYPE_CHOICES)
    filer = models.ForeignKey(Filer)
    stat_type = models.CharField(max_length=50, choices=STAT_TYPE_CHOICES)
    notes = models.TextField(null=True, blank=True)
    int_year_span = models.IntegerField() # years in operation eg. 10
    str_year_span = models.CharField(max_length=100) # string description eg. 2000 - 2010
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    
    def __unicode__(self):
        name_str = '%s-%s' % (self.filer_type, self.stat_type)
        return name_str
    