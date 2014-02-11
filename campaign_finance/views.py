# Create your views here.
from django.shortcuts import get_list_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from campaign_finance.models import *

class IndexView(generic.ListView):
  template_name = 'templates/campaign_finance/index.html'
  context_object_name = 'latest_campaigns'

  def get_queryset(self):
    return Committee.objects.order_by('-name')[:5]

class FilerView(generic.DetailView):
  model = Filer
  template = 'templates/campaign_finance/committee.html'