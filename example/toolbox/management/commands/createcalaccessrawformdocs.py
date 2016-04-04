#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.template.loader import render_to_string
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.calaccess_forms import CALACCESS_FORMS

class Command(CalAccessCommand):
    help = 'Generate documentation for CAL-ACCESS forms'

    def handle(self, *args, **kwargs):
        self.docs_dir = os.path.join(
            settings.REPO_DIR,
            'docs'
        )

        self.target_path = os.path.join(self.docs_dir, 'filingforms.rst')

        group_dict = {}

        for k in sorted(CALACCESS_FORMS):
            try:
                group_dict[CALACCESS_FORMS[k].group].append(CALACCESS_FORMS[k])
            except KeyError:
                group_dict[CALACCESS_FORMS[k].group] = [CALACCESS_FORMS[k]]

        group_list = sorted(group_dict.items(), key=lambda x:x[0])

        context = {
            'group_list': group_list,
        }
        
        rendered = render_to_string('toolbox/filingforms.rst', context)

        with open(self.target_path, 'w') as target_file:
            target_file.write(rendered)
