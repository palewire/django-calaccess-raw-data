import datetime
from haystack import indexes
from campaign_finance.models import Filer

class FilerIndex(indexes.SearchIndex, indexes.Indexable):
  text = indexes.CharField(document=True, use_template=True)
  name = indexes.CharField(model_attr='name')

  def get_model(self):
    return Filer

  # def index_queryset(self, using=None):
  #   """used when the entire index for model is updated"""
  #   return self.get_model().objects.filter