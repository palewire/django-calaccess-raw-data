from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
try:
    from calaccess.models import CvrCampaignDisclosureCd, Cvr2CampaignDisclosureCd, DebtCd, ExpnCd, FilernameCd, FilersCd, FilerAcronymsCd, FilerFilingsCd
    from calaccess.models import FilerInterestsCd, FilerLinksCd, FilerStatusTypesCd, FilerToFilerTypeCd, FilerTypesCd, Filings, FilingPeriodCd, LoanCd
except:
    print 'You have to have the calaccess app up and running in order to build this app.'
