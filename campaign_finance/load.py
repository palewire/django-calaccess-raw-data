try:
    from calaccess.models import FilernameCd,  FilerFilingsCd, FilerLinksCd, ExpnCd, RcptCd, SmryCd
except:
    print 'you need to load the raw calaccess data app in order to populate this one'
from campaign_finance.models import Cycle, Filer, Filing, Committee, Summary
from django.db import connection, transaction
from django.db.models import Q
import csv

def load_candidates():
    sql_candidate_filers = '''
        SELECT
        FILERS_CD.FILER_ID,
        FILER_TYPES_CD.DESCRIPTION
        FROM FILERS_CD INNER JOIN FILER_TO_FILER_TYPE_CD ON FILERS_CD.FILER_ID = FILER_TO_FILER_TYPE_CD.FILER_ID
                        INNER JOIN FILER_TYPES_CD ON FILER_TO_FILER_TYPE_CD.FILER_TYPE = FILER_TYPES_CD.FILER_TYPE 
        WHERE FILER_TYPES_CD.FILER_TYPE='8'
        GROUP BY 1,2
    '''
    c = connection.cursor()
    c.execute(sql_candidate_filers)
    rows = c.fetchall()
    for r in rows:
        insert = Filer()
        insert.filer_id = r[0]
        insert.status = r[1]
        insert.filer_type = 'cand'
        insert.save()
    
    candidate_name_errors = []
    for f in Filer.objects.all():
        # check to see if they ever filed a F450 or F460
        try:
            obj = FilernameCd.objects.filter(filer_id=f.filer_id)[0]
            f.name = (obj.namt + ' ' + obj.namf + ' ' + obj.naml + ' ' + obj.nams).strip()
            f.xref_filer_id = obj.xref_filer_id
            f.save()
        except:
            'CANDIDATE NAME INFO NOT IN FilernameCd for %s' % f.filer_id
            candidate_name_errors.append(f.filer_id)
        
        
        qs = FilerLinksCd.objects.filter(filer_id_a=f.filer_id)
        for q in qs:
            # check to see if linked committee ever filed a F450 or F460. If it hasn't, forget about it
            qs_filings = FilerFilingsCd.objects.filter(filer_id=q.filer_id_b)
            has_filings_we_care_about = False
            if qs_filings.filter(form_id='F460').count() > 0:
                has_filings_we_care_about = True
            elif qs_filings.filter(form_id='F450').count() > 0:
                has_filings_we_care_about = True
            
            # check to see if the committee is linked to multiple filers. If it is, forget about it
            linked_to_just_this_candidate = False
            if FilerLinksCd.objects.filter(filer_id_b=q.filer_id_b).values_list('filer_id_a', flat=True).distinct().count() == 1:
                linked_to_just_this_candidate = True
            
            # is the committee already in the Committee model?
            qs_existing_cmtees = Committee.objects.filter(filer_id_raw=q.filer_id_b)
            if qs_existing_cmtees.count() > 0:
                already_accounted_for = True
            else:
                already_accounted_for = False
            
            if already_accounted_for == False:
                if has_filings_we_care_about and linked_to_just_this_candidate == True:
                    qs_filer_name = FilernameCd.objects.filter(filer_id=q.filer_id_b)
                    if qs_filer_name.count() > 0:
                        insert = Committee()
                        insert.filer = f
                        insert.filer_id_raw = q.filer_id_b
                        filer_name_obj = FilernameCd.objects.filter(filer_id=q.filer_id_b)[0]
                        insert.name = (filer_name_obj.namt + ' ' + filer_name_obj.namf + ' ' + filer_name_obj.naml + ' ' + filer_name_obj.nams).strip()
                        insert.committee_type = 'ccrc'
                        insert.save()
                else:
                    print '%s is a no go' % q.filer_id_b
        
        # nuke filers with no filings
        if f.committee_set.count() == 0:
            print 'bye bye %s' % f.filer_id
            f.delete()
        
        # I should add something here that looks at the Statement of Organization or some other filing to get party affiliation and office sought that cycle
    return candidate_name_errors

def load_filings():
    for f in Filer.objects.all():
        for c in f.committee_set.all():
            # filer_id_raw preserves the CAL-ACCESS committee filer_id
            # the app accociates all candidate committees with the Candidate as the controlling filer for convenience
            # all PACs will have the same Filer.filing_id and Committee.filing_id_raw
            qs_filings = FilerFilingsCd.objects.filter(Q(form_id='F460') | Q(form_id='F450'), filer_id=c.filer_id_raw)
            for filing in qs_filings:
                qs_amends = qs_filings.filter(filing_id=filing.filing_id)
                if qs_amends.count() > 1:
                    current_filing = qs_amends.order_by('-filing_sequence')[0]
                    qs_check = Filing.objects.filter(committee=c, filing_id=current_filing.filing_id, amend_id=current_filing.filing_sequence)
                    if qs_check == 1:
                        print 'already accounted for filing'
                        continue
                else:
                    current_filing = filing
                    insert = Filing()
                    if current_filing.session_id % 2 == 0:
                        cycle_year = current_filing.session_id
                    else:
                        cycle_year = current_filing.session_id + 1
                    insert.cycle, created = Cycle.objects.get_or_create(name=cycle_year)
                    insert.committee = c
                    insert.filing_id = current_filing.filing_id
                    insert.amend_id = current_filing.filing_sequence
                    insert.form_id = current_filing.form_id
                    if current_filing.rpt_start:
                        insert.start_date = current_filing.rpt_start.isoformat()
                    if current_filing.rpt_end:
                        insert.end_date = current_filing.rpt_end.isoformat()
                    insert.save()

def load_summary():
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
    for f in Filing.objects.all():
        qs = SmryCd.objects.filter(filing_id=f.filing_id, amend_id=f.amend_id)
        if qs.count() == 0:
            print 'no SmryCd data for Committee %s Filing %s Amend %s' % (f.committee.filer_id, f.filing_id, f.amend_id)
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
            insert.save()

def load_expenditures():
    for f in Filing.objects.all():
        qs = ExpnCd.objects.filter(filing_id=f.filing_id, amend_id=f.amend_id)

def load_contributions():
    for f in Filing.objects.all():
        qs = RcptCd.objects.filer(filing_id=f.filing_id, amend_id=f.amend_id)


  
