from django.contrib import admin
from campaign_finance.models import Committee, Filer, CandidateCommittee

admin.site.register(Committee)
admin.site.register(Filer)
admin.site.register(CandidateCommittee)