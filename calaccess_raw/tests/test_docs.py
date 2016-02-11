#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import agate
import logging
from django.test import TestCase
from calaccess_raw import get_model_list
logger = logging.getLogger(__name__)


class DocumentationTestCase(TestCase):
    """
    Tests related to the documentation of models, fields and values
    """
    # @classmethod
    # def setUpClass(cls):
    #     """
    #     Load data into the database before running other tests.
    #     """
    #     super(DocumentationTestCase, cls).setUpClass()
    #     kwargs = dict(verbosity=3, test_data=True)
    #     if settings.DATABASES.get("alt", None):
    #         kwargs['database'] = 'alt'
    #         logger.debug("Loading into 'alt' database")
    #     call_command("updatecalaccessrawdata", **kwargs)

    def attr_test_output(self, obj_type, attr_name, results):
        # Load the data
        table = agate.Table(results, ['model', attr_name])

        # Count the number with no __str__
        fails = table.where(lambda row: row[attr_name] is False)
        if fails.rows:
            print("Fail: %s %ss are missing %s" % (
                len(fails.rows),
                obj_type,
                attr_name
            ))
            fails.select(["model"]).print_table()
        else:
            print("Win: All %s %ss have %s" % (
                len(table.rows),
                obj_type,
                attr_name
            ))

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
            results.append([m.__name__, is_custom])
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
            results.append([m.__name__, exists])
        self.attr_test_output("model", "__doc__", results)

    def test_field_verbose_name(self):
        """
        Verify that all fields have verbose_name documentation.
        """
        results = []
        for m in get_model_list():
            for f in m().get_field_list():
                if f.name == 'id':
                    continue
                if f.__dict__['_verbose_name']:
                    exists = True
                else:
                    exists = False
                results.append(("%s.%s" % (m.__name__, f.name), exists))
        self.attr_test_output("field", "verbose_name", results)

    def test_field_help_text(self):
        """
        Verify that all fields have help_text documentation.
        """
        results = []
        for m in get_model_list():
            for f in m().get_field_list():
                if f.name == 'id':
                    continue
                if f.help_text:
                    exists = True
                else:
                    exists = False
                results.append(("%s.%s" % (m.__name__, f.name), exists))
        self.attr_test_output("field", "help_text", results)

    #
    # def _test_choices(self, field_name):
    #     """
    #     Verify that proper choices appear for the provided field.
    #     """
    #     # Loop through the models
    #     for m in get_model_list():
    #
    #         # And then through the fields
    #         for f in m._meta.fields:
    #
    #             # Only test against the provided field name
    #             if not f.name == field_name:
    #                 continue
    #
    #             # Pull out all the choices in that field
    #             slug_list = []
    #             if not f.choices:
    #                 warnings.warn("%s %s has no choices defined" % (
    #                     m.__name__,
    #                     field_name
    #                 ))
    #             for slug, name in f.choices:
    #                 # Make sure that each has a definition
    #                 # self.assertIsNot(name, '')
    #                 if not name:
    #                     warnings.warn("%s %s '%s' undefined" % (
    #                         m.__name__,
    #                         field_name,
    #                         slug,
    #                     ))
    #                 slug_list.append(slug)
    #
    #             # The query the database and make sure everything in
    #             # there has a matching definition in the choices
    #             for value, count in m.objects.values_list(
    #                 field_name,
    #             ).annotate(Count(field_name)):
    #                 warnings.warn("'%s' %s code undefined on %s model" % (
    #                     value,
    #                     field_name,
    #                     m.__name__
    #                 ))
    #                 # self.assertIn(value, slug_list)
    #
    # def test_choices(self):
    #     """
    #     Verify that valid choices are available for all expected fields
    #     on all models.
    #     """
    #     # List of fields that we expect there to be valid choices defined
    #     fields = [
    #         'form_type',
    #         'form_id',
    #         'entity_code',
    #         'filer_type',
    #         'filing_type',
    #         'activity_type',
    #         'status',
    #         'off_s_h_cd',
    #         'pform_type',
    #         'stmnt_type',
    #         'stmnt_status',
    #         'rec_type',
    #         'party_cd',
    #         'sup_opp_cd',
    #         'elec_type',
    #         'reportname',
    #         'expn_code',
    #         'status_type',
    #     ]
    #     [self._test_choices(f) for f in fields]
