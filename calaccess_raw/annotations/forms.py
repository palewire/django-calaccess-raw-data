#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utilities for representing CAL-ACCESS forms.
"""
from .documents import DocumentCloud
from calaccess_raw import get_model_list
from django.utils.deconstruct import deconstructible


@deconstructible
class FilingForm(object):
    """
    A form used to collect information for the CAL-ACCESS database.
    """
    def __init__(self, id, title, **kwargs):
        """
        Create a new object by submitting a unique ID and title.
        """
        self.id = id
        self.title = title
        self.description = kwargs.get('description')
        self.group = kwargs.get('group')
        self.documentcloud_id = kwargs.get('documentcloud_id')
        self.db_value = kwargs.get('db_value', self.id)
        self.sections = []
        if self.documentcloud_id:
            self.documentcloud = DocumentCloud(self.documentcloud_id)
        else:
            self.documentcloud = None

    @property
    def type_and_num(self):
        """
        Returns a short title for the form that includes its type and number.
        """
        if self.id[0] == 'E':
            self._type_and_num = 'Electronic Form {}'.format(self.id[1:])
        elif self.id[0] == 'S':
            self._type_and_num = 'Schedule {}'.format(self.id[1:])
        else:
            self._type_and_num = 'Form {}'.format(self.id[1:])

        return self._type_and_num

    @property
    def full_title(self):
        """
        Returns the full title of the form.
        """
        self._full_title = '{0}: {1}'.format(self.type_and_num, self.title)
        return self._full_title

    def add_section(self, id, title, **kwargs):
        """
        Adds a Section with the provided title and options to this object.
        """
        new_section = FilingFormSection(
            form=self,
            id=id,
            title=title,
            db_value=kwargs.get('db_value', self.db_value),
            start_page=kwargs.get('start_page'),
            end_page=kwargs.get('end_page'),
            documentcloud_id=kwargs.get('documentcloud_id'),
        )
        self.sections.append(new_section)
        return new_section

    def get_section(self, id):
        """
        Returns the Section object with the given id.
        """
        section_dict = {i.id: i for i in self.sections}
        return section_dict[id]

    def get_models(self):
        """
        Returns all the CAL-ACCESS models connected with this form.
        """
        models = []
        for model in get_model_list():
            if self in [x[0] for x in model().get_filing_forms_w_sections()]:
                models.append(model)

        return models

    def __str__(self):
        return str(self.id)


@deconstructible
class FilingFormSection(object):
    """
    A section of a FilingForm (e.g., a cover page, summary sheet, schedule or part).
    """
    def __init__(self, form, id, title, **kwargs):
        """
        Create a new object by submitting a FilingForm parent with an ID and title.
        """
        self.form = form
        self.id = id
        self.title = title
        self.db_value = kwargs.get('db_value', form.db_value)
        self.start_page = kwargs.get('start_page')
        self.end_page = kwargs.get('end_page')
        self.documentcloud = DocumentCloud(
            self.form.documentcloud_id,
            self.start_page,
            self.end_page
        )

    @property
    def full_title(self):
        """
        Returns full title of the section, including the parent form's name.
        """
        self._full_title = '{0} ({1}): {2}'.format(
            self.form.type_and_num,
            self.form.title,
            self.title,
        )
        return self._full_title

    def __str__(self):
        return str(self.id)
