import os
from django.conf import settings
from calaccess_raw import get_model_list
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand):
    help = 'Generate GitHub issues to add UNIQUE_KEY config for raw \
CAL-ACCESS database models'

    def handle(self, *args, **kwargs):
        model_list = sorted(get_model_list(), key=lambda x:x().klass_name)
        for m in model_list:
            print m().klass_name, m.UNIQUE_KEY
