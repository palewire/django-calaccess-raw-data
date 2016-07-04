#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Print table and record counts from the CAL-ACCESS raw database.
"""
from __future__ import unicode_literals
from calaccess_raw import get_model_list
from calaccess_raw.management.commands import CalAccessCommand
from django.contrib.humanize.templatetags.humanize import intcomma


class Command(CalAccessCommand):
    """
    Print table and record counts from the CAL-ACCESS raw database.
    """
    help = "Print table and record counts from the CAL-ACCESS raw database"

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)
        self.header("Totaling CAL-ACCESS tables and rows")
        model_list = get_model_list()
        self.log(" %s total tables" % len(model_list))
        record_count = 0
        for m in model_list:
            record_count += m.objects.count()
        self.log(" %s total records" % intcomma(record_count))
