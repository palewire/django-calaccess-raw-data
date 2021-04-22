#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utilities for representing and interacting with CAL-ACCESS reference documents and forms.
"""
# Helpers
import os
import csvkit

# Annotations data
from . import choices
from .forms import FilingForm, FilingFormSection
from .documents import DocumentCloud, DocumentCloudPage


def load_forms():
    """
    Load all the FilingForm objects from the source CSV.
    """
    this_dir = os.path.dirname(__file__)

    # Read in forms
    form_path = os.path.join(this_dir, 'forms.csv')
    with open(form_path, 'r') as form_obj:
        form_reader = csvkit.DictReader(form_obj)
        form_list = [FilingForm(**row) for row in form_reader]

    # Read in sections
    section_path = os.path.join(this_dir, 'sections.csv')
    with open(section_path, 'r') as section_obj:
        section_reader = csvkit.DictReader(section_obj)
        for section in section_reader:
            form = next((x for x in form_list if x.id == section['form_id']))
            form.add_section(**section)

    # Pass it out
    return form_list


# Boot up all the forms from our source CSV files
FORMS = load_forms()


def get_form(id):
    """
    Takes an id for a filing form and returns a FilingForm object.
    """
    return next((x for x in FORMS if x.id == id.upper()), None)


def sort_choices(codes_dict):
    """
    Returns a tuple of tuples, sorted by the given codes_dict's key.
    """
    return tuple(sorted(codes_dict.items(), key=lambda x: x[0]))


__all__ = (
    "DocumentCloud",
    "DocumentCloudPage",
    "FilingForm",
    "FilingFormSection",
    'FORMS',
    'get_form',
    'choices',
    "sort_choices"
)
