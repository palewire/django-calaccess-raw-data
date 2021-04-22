#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests how thoroughly the CAL-ACCESS database has been documented.
"""
# Testing
from django.test import TestCase

# Stuff to test
from calaccess_raw import get_model_list
from calaccess_raw.fields import ForeignKeyField

# Text
import re
import agate

# Logging
import logging
logger = logging.getLogger(__name__)


class DocumentationTestCase(TestCase):
    """
    Tests the documentation of models, fields and values.
    """
    @classmethod
    def setUpClass(cls):
        """
        Load data into the database before running other tests.
        """
        super(DocumentationTestCase, cls).setUpClass()

    def attr_test_output(self, obj_type, attr_name, results):
        """
        Output test results to the console.
        """
        # Load the data
        table = agate.Table(results, ['group', obj_type, attr_name])

        # Count the number with no __str__
        fails = table.where(lambda row: row[attr_name] is False)
        if fails.rows:
            print("Fail: %s %ss are missing %s" % (
                len(fails.rows),
                obj_type,
                attr_name
            ))
            fails.select(["group", obj_type]).print_table(
                max_rows=None,
                max_column_width=50,
            )

    def test_model_str(self):
        """
        Verify that __str__ methods exist and work for all models.
        """
        results = []
        for m in get_model_list():
            # Test that works
            m().__str__()
            # Make sure that it is customized and not the Django defalult
            is_custom = m().__str__() != '%s object' % m.__name__
            results.append([m().klass_group, m.__name__, is_custom])
        self.attr_test_output("model", "__str__", results)

    def test_model_doc(self):
        """
        Verify that __doc__ methods exist and work for all models.
        """
        results = []
        for m in get_model_list():
            if m().__doc__.startswith(m.__name__):
                exists = False
            else:
                exists = True
            results.append([m().klass_group, m.__name__, exists])
        self.attr_test_output("model", "__doc__", results)

    def test_model_unique_key(self):
        """
        Verify that each model has a UNIQUE_KEY attribute set.
        """
        results = []
        # Loop through the models
        for m in get_model_list():

            # Verify the model has a UNIQUE_KEY attribute
            exists = m().UNIQUE_KEY is not None

            # Verify that the field names are not lowercase
            lowercases = sum([
                1 for k in m().get_unique_key_list()
                if re.search("[a-z]{1,}", k)
            ]) or 0
            if lowercases:
                exists = False

            # Verify that the fields actually exist
            missing = [
                f for f in m().get_unique_key_list()
                if not hasattr(m(), f.lower()) and not hasattr(m(), f.lower() + "_id")
            ]
            if missing:
                exists = False

            # Pass out results
            results.append([m().klass_group, m.__name__, exists])

        # Print results
        self.attr_test_output("model", "UNIQUE_KEY", results)

    def test_model_documentcloud_pages(self):
        """
        Verify that each model has DOCUMENTCLOUD_PAGES defined.
        """
        results = []
        for m in get_model_list():
            if m().DOCUMENTCLOUD_PAGES:
                exists = True
            else:
                exists = False
            results.append([m().klass_group, m.__name__, exists])
        self.attr_test_output("model", "DOCUMENTCLOUD_PAGES", results)

    def test_model_documentcloud_pages_for_both_links(self):
        """
        Verify that models linked to DocumentCloud reference.
        """
        results = []
        exceptions = [
            # campaign models
            'F501502Cd',
            # "common" models
            'FilernameCd',
            'FilerFilingsCd',
            'FilingsCd',
            'HeaderCd',
            'CvrE530Cd',
            # lobbying models
            'LobbyingChgLogCd',
            'LobbyistContributions1Cd',
            'LobbyistContributions2Cd',
            'LobbyistContributions3Cd',
            'LobbyistEmployer1Cd',
            'LobbyistEmployer2Cd',
            'LobbyistEmployer3Cd',
            'LobbyistEmployerHistoryCd',
            'LobbyistEmployerFirms1Cd',
            'LobbyistEmployerFirms2Cd',
            'LobbyistEmpLobbyist1Cd',
            'LobbyistEmpLobbyist2Cd',
            'LobbyistFirm1Cd',
            'LobbyistFirm2Cd',
            'LobbyistFirm3Cd',
            'LobbyistFirmEmployer1Cd',
            'LobbyistFirmEmployer2Cd',
            'LobbyistFirmLobbyist1Cd',
            'LobbyistFirmLobbyist2Cd',
            'LobbyistFirmHistoryCd',
            # "other" models (this is indeed all of them)
            'AcronymsCd',
            'AddressCd',
            'BallotMeasuresCd',
            'EfsFilingLogCd',
            'FilersCd',
            'FilerAcronymsCd',
            'FilerAddressCd',
            'FilerEthicsClassCd',
            'FilerInterestsCd',
            'FilerLinksCd',
            'FilerStatusTypesCd',
            'FilerToFilerTypeCd',
            'FilerTypesCd',
            'FilerXrefCd',
            'FilerTypePeriodsCd',
            'FilingPeriodCd',
            'GroupTypesCd',
            'ImageLinksCd',
            'LegislativeSessionsCd',
            'LookupCodesCd',
            'NamesCd',
            'ReceivedFilingsCd',
            'ReportsCd',
        ]
        model_list = [
            x for x in get_model_list() if x.__name__ not in exceptions
        ]

        for m in model_list:

            if m().DOCUMENTCLOUD_PAGES:
                cal_access_tables = False
                map_cal_format = False

                # cycle through objs, checking for IDs
                for doc_pages in m().DOCUMENTCLOUD_PAGES:

                    if doc_pages.id == '2711614-CalAccessTablesWeb':
                        cal_access_tables = True
                    elif doc_pages.id == '2711616-MapCalFormat2Fields':
                        map_cal_format = True

                # if both exist, return True, if both don't exist return false
                if cal_access_tables and map_cal_format:
                    complete = True
                else:
                    complete = False

            # if the object doesn't exist at all, will fail test
            else:
                complete = False

            results.append([m().klass_group, m.__name__, complete])
        self.attr_test_output("model", "DOCUMENTCLOUD_PAGES_COMPLETE", results)

    def test_filing_forms(self):
        """
        Verify that model's with a form field are linked to a FilingForm object.
        """
        results = []
        exceptions = ['HeaderCd']
        model_list = [
            x for x in get_model_list() if x.__name__ not in exceptions
        ]
        for m in model_list:
            field_names = m._meta.get_fields()
            if 'form_type' in field_names or 'form_id' in field_names:
                if m().FILING_FORMS:
                    exists = True
                else:
                    exists = False
                results.append([m().klass_group, m.__name__, exists])
        self.attr_test_output("model", "FILING_FORMS", results)

    def test_field_help_text(self):
        """
        Verify that all fields have help_text documentation.
        """
        results = []
        for m in get_model_list():
            for f in m().get_field_list():
                if f.name == 'id':
                    continue
                if len(f.help_text) > 0:
                    exists = True
                else:
                    exists = False
                results.append([m().klass_group, "%s.%s" % (m.__name__, f.name), exists])
        self.attr_test_output("field", "help_text", results)

    def test_choices(self):
        """
        Verify that valid choices are available for all expected fields on all models.
        """
        # substrings that appear in choice fields
        choice_field_strs = [
            '_cd',
            '_code',
            '_type',
            'status',
            '_lvl',
            'reportname',
            'form_id',
        ]
        exceptions = [
            'LookupCodesCd.code_type',
            'S497Cd.sup_off_cd',
            'FilerStatusTypesCd.status_type',
            'FilerStatusTypesCd.status_desc',
            'FilerTypesCd.filer_type',
        ]

        results = []
        model_list = sorted(
            get_model_list(),
            key=lambda x: (x().klass_group, x().klass_name)
        )

        for m in model_list:
            for f in m._meta.fields:
                if (
                    any(x in f.name for x in choice_field_strs)
                    and f.name != 'memo_code'
                    and f.__class__ is not ForeignKeyField
                    and '{}.{}'.format(m().klass_name, f.name) not in exceptions
                ):
                    if not f.choices:
                        results.append((
                            m().klass_group,
                            m.__name__,
                            f.name,
                            "Has no CHOICES defined"
                        ))

                    if not f.documentcloud_pages:
                        results.append((
                            m().klass_group,
                            m.__name__,
                            f.name,
                            "Has no `documentcloud_pages` defined"
                        ))

                    # Pull out all the choices in that field
                    for slug, name in f.flatchoices:
                        # Make sure that each has a definition
                        if not name or name == '':
                            results.append((
                                m().klass_group,
                                m.__name__,
                                f.name,
                                "Value '%s' undefined in CHOICES" % slug
                            ))

        table = agate.Table(results, ['group', 'model', 'field', 'message'])
        table.print_table(max_rows=None, max_column_width=50)
