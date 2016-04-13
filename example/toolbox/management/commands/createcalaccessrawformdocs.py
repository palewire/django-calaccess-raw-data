#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.template.loader import render_to_string
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.annotations.filing_forms import all_filing_forms

class Command(CalAccessCommand):
    help = 'Generate documentation for CAL-ACCESS forms'

    def handle(self, *args, **kwargs):
        self.docs_dir = os.path.join(
            settings.REPO_DIR,
            'docs'
        )

        self.target_path = os.path.join(self.docs_dir, 'filingforms.rst')

        group_dict = {}

        for form in all_filing_forms:
            try:
                group_dict[form.group].append(form)
            except KeyError:
                group_dict[form.group] = [form]

        group_list = sorted(group_dict.items(), key=lambda x:x[0])

        context = {
            'group_list': group_list,
        }
        
        rendered = render_to_string('toolbox/filingforms.rst', context)

        with open(self.target_path, 'w') as target_file:
            target_file.write(rendered)
