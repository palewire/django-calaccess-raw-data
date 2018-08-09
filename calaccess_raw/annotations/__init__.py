#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utilities for representing and interacting with CAL-ACCESS reference documents and forms.
"""
from .documents import DocumentCloud, DocumentCloudPage
from .forms import FilingForm, FilingFormSection


def get_sorted_choices(codes_dict):
    """
    Returns a tuple of tuples, sorted by the given codes_dict's key.
    """
    return tuple(sorted(codes_dict.items(), key=lambda x: x[0]))


__all__ = (
    "DocumentCloud",
    "DocumentCloudPage",
    "FilingForm",
    "FilingFormSection",
    "get_sorted_choices",
)
