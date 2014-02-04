try:
    from calaccess.models import FilernameCd, FilerLinksCd
except:
    print 'you need to load the raw calaccess data app in order to populate this one'
from campaign_finance.models import Filer, Committee

def filer_id_to_name(filer_id):
    from calaccess.models import FilernameCd, FilerLinksCd
    try:
        obj = FilernameCd.objects.filter(filer_id=filer_id)[0]
        name = (obj.namt + ' ' + obj.namf + ' ' + obj.naml + ' ' + obj.nams).strip()
    except:
        name = ''
    return name

def filer_type_to_committee_type(filer_type):
    if filer_type == 'MAJOR DONOR/INDEPENDENT EXPENDITURE COMMITTEE':
        t = 'mdid'
    elif filer_type == 'SLATE MAILER ORGANIZATIONS':
        t = 'sm'
    elif filer_type in [ 'INITIATIVE', 'PROPOSITION', ]:
        t = 'bi'
    elif filer_type == 'RECIPIENT COMMITTEE':
        t = 'cc'
    return t

def load():
    type_list = [
        'MAJOR DONOR/INDEPENDENT EXPENDITURE COMMITTEE',
        'SLATE MAILER ORGANIZATIONS',
        'RECIPIENT COMMITTEE',
        'CANDIDATE/OFFICEHOLDER',
        'INITIATIVE',
        'PROPOSITION',
    ]
    for f in FilernameCd.objects.filter(filer_type__in=type_list).values_list('filer_id', 'xref_filer_id', 'filer_type').distinct():
        if f[2] == 'CANDIDATE/OFFICEHOLDER':
            insert_filer_cand = Filer()
            insert_filer_cand.xref_filer_id = f[1]
            insert_filer_cand.filer_id = f[0]
            insert_filer_cand.filer_type = 'cand'
            insert_filer_cand.name = filer_id_to_name(f[0])
            insert_filer_cand.save()
            print '%s' % insert_filer_cand.name
            qs = FilerLinksCd.objects.filter(filer_id_a=f[0])
            for q in qs:
                insert_cc_cmte = Committee()
                insert_cc_cmte.filer = insert_filer_cand
                insert_cc_cmte.filer_id_raw = q.filer_id_b
                insert_cc_cmte.name = filer_id_to_name(q.filer_id_b)
                insert_cc_cmte.committee_type = 'cc'
                insert_cc_cmte.save()
                print '%s' % insert_cc_cmte.name
            
        else:
            insert_filer_pac = Filer()
            insert_filer_pac.xref_filer_id = f[1]
            insert_filer_pac.filer_id = f[0]
            insert_filer_pac.filer_type = 'pac'
            insert_filer_pac.name = filer_id_to_name(f[0])
            insert_filer_pac.save()
            print '%s' % insert_filer_pac.name
            
            insert_cmte = Committee()
            insert_cmte.filer = insert_filer_pac
            insert_cmte.filer_id_raw = f[0]
            insert_cmte.name = insert_filer_pac.name
            insert_cmte.committee_type = filer_type_to_committee_type(f[2].strip())
            insert_cmte.save()
            
