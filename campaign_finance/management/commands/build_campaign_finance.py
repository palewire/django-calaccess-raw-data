from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
try:
    from calaccess.models import FilernameCd,  FilerFilingsCd, FilerLinksCd, ExpnCd, RcptCd, SmryCd,  FilersCd, FilerTypesCd, FilerToFilerTypeCd
except:
    print 'you need to load the raw calaccess data app in order to populate this one'
from campaign_finance.models import  Committee, Contribution, Cycle, Expenditure, Filer, Filing, Stats, Summary
from django.db import connection, transaction
from dateutil.relativedelta import relativedelta
from django.db.models import Sum
from django.db.models import Q
import csv


def insert_cmte(filer_obj, filer_id_raw):
    insert_cmtee = Committee()
    insert_cmtee.filer = filer_obj # tie all candidate committees to the CAL-ACCESS candidate filer
    insert_cmtee.filer_id_raw = filer_id_raw # preserve the CAL-ACCESS filer_id for the committee here, but don't add it to our Filer model. So can distinguish PAC from Cand Cmtee
    insert_cmtee.committee_type = filer_obj.filer_type
    try:
        filer_name_obj = FilernameCd.objects.filter(filer_id=filer_id_raw)[0]
        insert_cmtee.name = (filer_name_obj.namt + ' ' + filer_name_obj.namf + '' + filer_name_obj.naml + ' ' + filer_name_obj.nams).strip()
        insert_cmtee.xref_filer_id = filer_name_obj.xref_filer_id
    except:
        insert_cmtee.name = None
    insert_cmtee.save() 

class Command(BaseCommand):
    help = 'Break out the recipient committee campaign finance data from the CAL-ACCESS dump'
    
    def handle(self, *args, **options):
        self.load_filers()
        self.load_filings()
        self.load_summary()
        self.load_contributions()
        self.load_expenditures()
    
    def load_filers(self):
        '''
            Take a look in the Filings table and just load up the filers that have filed a 460 or a 450
        '''
        #filer_type_dict = {}
        #for f in FilerTypesCd.objects.all():
        #    filer_type_dict[f.filer_type] = f.description
        '''
            {0L: u' NOT DEFINED',
            1L: u'CLIENT',
            2L: u'EMPLOYER',
            3L: u'FIRM',
            4L: u'LOBBYIST',
            5L: u'PAYMENT TO INFLUENCE',
            6L: u'ALL FILERS',
            8L: u'CANDIDATE/OFFICEHOLDER',
            10L: u'MAJOR DONOR/INDEPENDENT EXPENDITURE COMMITTEE',
            12L: u'SLATE MAILER ORGANIZATIONS',
            14L: u'PROPONENT',
            16L: u'RECIPIENT COMMITTEE',
            17L: u'PROPOSITION ',
            19L: u'INITIATIVE',
            20L: u'TREASURER/RESPONSIBLE OFFICER',
            21L: u'FEDERAL',
            100L: u'PREPAID ACCOUNT',
            101L: u'INDIVIDUAL'}
        '''
        # there's a lot of orphaned junk in this database
        # i winnow down the filers we care about like so
        ## get a list of all the recipient committees that filed a dislosure
        ## get a list of all those filings that have any summary info to report
        ## take the list of those filers and load them up
        ## this method should cut through all the crap like
        ### this candidate filer has no committees
        ### or this candidate committee has no associated candidate filer and no name of the committee in FilerNameCD
        
        all_filings = FilerFilingsCd.objects.filter(Q(form_id='F460') | Q(form_id='F450')).values_list('filing_id', flat=True).distinct()
        all_filings_with_data = SmryCd.objects.filter(filing_id__in=all_filings).values_list('filing_id', flat=True).distinct()
        all_filers_with_data = FilerFilingsCd.objects.filter(filing_id__in=all_filings_with_data).values_list('filer_id', flat=True).distinct() # if you swap filing_id for filer_id in the values clause you get the same count of filings as in all_filings_with_data
        
        for filer_id in all_filers_with_data:
            qs_linked = FilerLinksCd.objects.filter(filer_id_b=filer_id)
            if qs_linked.count() == 0:
                filer_id_type = 'pac'
                insert_pac = Filer()
                insert_pac.filer_id = filer_id
                insert_pac.filer_type = filer_id_type
                try:
                    filer_name_obj = FilernameCd.objects.filter(filer_id=filer_id)[0]
                    insert_pac.name = (filer_name_obj.namt + ' ' + filer_name_obj.namf + ' ' + filer_name_obj.naml + ' ' + filer_name_obj.nams).strip()
                    insert_pac.xref_filer_id = filer_name_obj.xref_filer_id
                except:
                    insert_pac.name = None
                    insert_pac.xref_filer_id = None
                insert_pac.save()
                insert_cmte(insert_pac, filer_id)
                
            elif qs_linked.count() == 1:
                filer_id_type = 'cand'
                filer_cand_id = qs_linked[0].filer_id_a
                qs_candidate_linked = FilerLinksCd.objects.filter(filer_id_a=filer_cand_id)
                if qs_candidate_linked.values_list('filer_id_a', flat=True).distinct().count() == 1:
                    try:
                        filer_name_obj = FilernameCd.objects.filter(filer_id=filer_cand_id)[0]
                        name = (filer_name_obj.namt + ' ' + filer_name_obj.namf + ' ' + filer_name_obj.naml + ' ' + filer_name_obj.nams).strip()
                        xref_filer_id = filer_name_obj.xref_filer_id
                    except:
                        name = None
                        xref_filer_id = None
                    filer_obj, created = Filer.objects.get_or_create(
                        filer_id = filer_cand_id,
                        filer_type = filer_id_type,
                        name = name,
                        xref_filer_id = xref_filer_id,
                    )
                    insert_cmte(filer_obj, filer_cand_id)
                else:
                    print 'filer_id %s might not be a candidate, take a look' % filer_id
                    break
            elif qs_linked.count() > 1:
                filer_id_type = 'linked-pac'
                if qs_linked.values_list('filer_id_b').distinct().count() == 1:
                    linked_pac_id = qs_linked.values_list('filer_id_b', flat=True).distinct()[0]
                    insert_pac_linked = Filer()
                    insert_pac_linked.filer_id = linked_pac_id
                    insert_pac_linked.filer_type = filer_id_type
                    try:
                        filer_name_obj = FilernameCd.objects.filter(filer_id=linked_pac_id)[0]
                        insert_pac_linked.name = (filer_name_obj.namt + ' ' + filer_name_obj.namf + ' ' + filer_name_obj.naml + ' ' + filer_name_obj.nams).strip()
                        insert_pac_linked.xref_filer_id = filer_name_obj.xref_filer_id
                    except:
                        insert_pac_linked.name = None
                        insert_pac_linked.xref_filer_id = None
                    insert_pac_linked.save()
                    insert_cmte(insert_pac_linked, linked_pac_id)
                else:
                    print 'linked pac filer_id_b not unique for filer_id %s' % filer_id
                    break
        print 'loaded filers'
    
    
    def load_filings(self):
        insert_obj_list = []
        
        for c in Committee.objects.all():
            qs_filings = FilerFilingsCd.objects.filter(Q(form_id='F460') | Q(form_id='F450'), filer_id=c.filer_id_raw)
            for f_id in qs_filings.values_list('filing_id', flat=True).distinct():
                current_filing = qs_filings.filter(filing_id=f_id).order_by('-filing_sequence')[0]
                
                insert = Filing()
                if current_filing.session_id % 2 == 0:
                    cycle_year = current_filing.session_id
                else:
                    cycle_year = current_filing.session_id + 1
                insert.cycle, created = Cycle.objects.get_or_create(name=cycle_year)
                insert.committee = c
                insert.filing_id_raw = current_filing.filing_id
                insert.amend_id = current_filing.filing_sequence
                insert.form_id = current_filing.form_id
                if current_filing.rpt_start:
                    insert.start_date = current_filing.rpt_start.isoformat()
                if current_filing.rpt_end:
                    insert.end_date = current_filing.rpt_end.isoformat()
                insert_obj_list.append(insert)
            if len(insert_obj_list) == 10000:
                Filing.objects.bulk_create(insert_obj_list)
                insert_obj_list = []
        
        if len(insert_obj_list) > 0:
            Filing.objects.bulk_create(insert_obj_list)
        
        print 'loaded filings'
    
    def load_summary(self):
        '''
            Currently using a dictonary to parse the summary information by form type, schedule and line number.
        '''
        summary_form_dict = {
            'F460': {
                #'name': 'Recipient Committee Campaign Statement',
                'itemized_monetary_contribs': {'sked': 'A', 'line_item': 1},
                'unitemized_monetary_contribs': {'sked': 'A', 'line_item': 2},
                'total_monetary_contribs': {'sked': 'A', 'line_item': 3},
                'non_monetary_contribs': {'sked': 'F460', 'line_item': 4},
                'total_contribs': {'sked': 'F460', 'line_item': 5},
                'itemized_expenditures': {'sked': 'E', 'line_item': 1},
                'unitemized_expenditures': {'sked': 'E', 'line_item': 2},
                'total_expenditures': {'sked': 'E', 'line_item': 4},
                'ending_cash_balance': {'sked': 'F460', 'line_item': 16},
                'outstanding_debts': {'sked': 'F460', 'line_item': 19},
            },
            'F450': {
                #'name': 'Recipient Committee Campaign Statement -- Short Form',
                'itemized_monetary_contribs': None,
                'unitemized_monetary_contribs': None,
                'total_monetary_contribs': {'sked': 'F450', 'line_item': 7},
                'non_monetary_contribs': {'sked': 'F450', 'line_item': 8},
                'total_contribs': {'sked': '450', 'line_item': 10},
                'itemized_expenditures': {'sked': 'F450', 'line_item': 1},
                'unitemized_expenditures': {'sked': 'F450', 'line_item': 2},
                'total_expenditures': {'sked': 'E', 'line_item': 6},
                'ending_cash_balance': {'sked': 'F460', 'line_item': 15},
                'outstanding_debts': None,
            }
        }
        insert_obj_list = []
        for f in Filing.objects.all():
            qs = SmryCd.objects.filter(filing_id=f.filing_id_raw, amend_id=f.amend_id)
            if qs.count() == 0:
                print 'no SmryCd data for Committee %s Filing %s Amend %s' % (f.committee.filer_id, f.filing_id_raw, f.amend_id)
            else:
                query_dict = summary_form_dict[f.form_id]
                insert = Summary()
                insert.committee = f.committee
                insert.cycle = f.cycle
                insert.form_type = f.form_id
                insert.filing = f
                for k,v in query_dict.items():
                    try:
                        insert.__dict__[k] = qs.get(form_type=v['sked'], line_item=v['line_item']).amount_a
                    except:
                        insert.__dict__[k] = 0
                insert_obj_list.append(insert)
            if len(insert_obj_list) == 10000:
                Summary.objects.bulk_create(insert_obj_list)
                insert_obj_list = []
        
        if len(insert_obj_list) == 10000:
            Summary.objects.bulk_create(insert_obj_list)
        
        print 'loaded summary'
    
    def load_expenditures(self):
        insert_stats = {}
        insert_obj_list = []
        for f in Filing.objects.all():
            qs = ExpnCd.objects.filter(filing_id=f.filing_id_raw, amend_id=f.amend_id)
            filing_key = '%s-%s' % (f.filing_id_raw, f.amend_id)
            insert_stats[filing_key] = qs.count()
            for q in qs:
                
                ## have to contruct the payee name from multiple fields
                if q.payee_naml == '':
                    bal_name = q.bal_name
                    cand_name = (q.cand_namt + ' ' + q.cand_namf + ' ' + q.cand_naml + ' ' + q.cand_nams).strip()
                    juris_name = q.juris_dscr
                    off_name = q.offic_dscr
                    name_list = [ bal_name, cand_name, juris_name, off_name, ]
                    recipient_name = ' '.join(name_list)
                else:
                    recipient_name = (q.payee_namt + ' ' + q.payee_namf + ' ' + q.payee_naml + ' ' + q.payee_nams).strip()
                
                insert = Expenditure()
                insert.cycle = f.cycle
                insert.committee = f.committee
                insert.filing = f
                insert.line_item = q.line_item
                insert.payee_namt = q.payee_namt
                insert.payee_namf = q.payee_namf
                insert.payee_naml = q.payee_naml
                insert.payee_nams = q.payee_nams
                insert.amend_id = q.amend_id
                insert.expn_dscr = q.expn_dscr
                insert.payee_zip4 = q.payee_zip4
                insert.g_from_e_f = q.g_from_e_f
                insert.payee_city = q.payee_city
                insert.amount = q.amount
                insert.memo_refno = q.memo_refno
                insert.expn_code = q.expn_code
                insert.memo_code = q.memo_code
                insert.entity_cd = q.entity_cd
                insert.bakref_tid = q.bakref_tid
                insert.payee_adr1 = q.payee_adr1
                insert.payee_adr2 = q.payee_adr2
                insert.expn_chkno = q.expn_chkno
                insert.form_type = q.form_type
                insert.cmte_id = q.cmte_id
                insert.xref_schnm = q.xref_schnm
                insert.xref_match = q.xref_match
                if q.expn_date:
                    insert.expn_date = q.expn_date.isoformat()
                insert.cum_ytd = q.cum_ytd
                insert.payee_st = q.payee_st
                insert.tran_id = q.tran_id
                
                insert.name = recipient_name.strip()
                insert_obj_list.append(insert)
                if len(insert_obj_list) == 10000:
                    Expenditure.objects.bulk_create(insert_obj_list)
                    insert_obj_list = []
        if len(insert_obj_list) > 0:
            Expenditure.objects.bulk_create(insert_obj_list)
        
        cnt = Expenditure.objects.count()
        if sum(insert_stats.values()) == cnt:
            print 'loaded %s expenditures' % cnt
        else:
            print 'loaded %s expenditures but %s records queried' % (cnt, sum(insert_stats.values()))
    
    def load_contributions(self):
        insert_stats = {}
        insert_obj_list = []
        for f in Filing.objects.all():
            qs = RcptCd.objects.filter(filing_id=f.filing_id_raw, amend_id=f.amend_id)
            filing_key = '%s-%s' % (f.filing_id_raw, f.amend_id)
            insert_stats[filing_key] = qs.count()
            for q in qs:
                insert = Contribution()
                insert.cycle = f.cycle
                insert.committee = f.committee
                insert.filing = f
                insert.ctrib_namt = q.ctrib_namt
                insert.ctrib_occ = q.ctrib_occ
                insert.ctrib_nams = q.ctrib_nams
                insert.line_item = q.line_item
                insert.amend_id = q.amend_id
                insert.rec_type = q.rec_type
                insert.ctrib_namf = q.ctrib_namf
                insert.date_thru = q.date_thru
                insert.ctrib_naml = q.ctrib_naml
                insert.ctrib_self = q.ctrib_self
                if q.rcpt_date:
                    insert.rcpt_date = q.rcpt_date
                insert.ctrib_zip4 = q.ctrib_zip4
                insert.ctrib_st = q.ctrib_st
                insert.ctrib_adr1 = q.ctrib_adr1
                insert.ctrib_adr2 = q.ctrib_adr2
                insert.memo_refno = q.memo_refno
                insert.intr_st = q.intr_st
                insert.memo_code = q.memo_code
                insert.intr_self = q.intr_self
                insert.intr_occ = q.intr_occ
                insert.intr_emp = q.intr_emp
                insert.entity_cd = q.entity_cd
                insert.intr_cmteid = q.intr_cmteid
                insert.ctrib_city = q.ctrib_city
                insert.bakref_tid = q.bakref_tid
                insert.tran_type = q.tran_type
                insert.intr_adr2 = q.intr_adr2
                insert.cum_ytd = q.cum_ytd
                insert.intr_adr1 = q.intr_adr1
                insert.form_type = q.form_type
                insert.intr_city = q.intr_city
                insert.cmte_id = q.cmte_id
                insert.xref_schnm = q.xref_schnm
                insert.ctrib_emp = q.ctrib_emp
                insert.xref_match = q.xref_match
                insert.cum_oth = q.cum_oth
                insert.ctrib_dscr = q.ctrib_dscr
                insert.intr_namt = q.intr_namt
                insert.intr_nams = q.intr_nams
                insert.amount = q.amount
                insert.intr_naml = q.intr_naml
                insert.intr_zip4 = q.intr_zip4
                insert.intr_namf = q.intr_namf
                insert.tran_id = q.tran_id
                insert.name = (q.ctrib_namt + ' '+ q.ctrib_namf + ' ' + q.ctrib_naml + ' ' + q.ctrib_nams).strip()
                insert_obj_list.append(insert)
                if len(insert_obj_list) == 10000:
                    Contribution.objects.bulk_create(insert_obj_list)
                    insert_obj_list = []
        if len(insert_obj_list) > 0:
            Contribution.objects.bulk_create(insert_obj_list)
        
        cnt = Contribution.objects.count()
        if sum(insert_stats.values()) == cnt:
            print 'loaded %s contributions' % cnt
        else:
            print 'loaded %s contributions but %s records queried' % (cnt, sum(insert_stats.values()))
