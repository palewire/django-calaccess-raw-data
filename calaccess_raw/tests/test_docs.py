#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import agate
import logging
from django.test import TestCase
from django.db.models import Count
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
        table = agate.Table(results, ['group', 'model', attr_name])

        # Count the number with no __str__
        fails = table.where(lambda row: row[attr_name] is False)
        if fails.rows:
            print("Fail: %s %ss are missing %s" % (
                len(fails.rows),
                obj_type,
                attr_name
            ))
            fails.select(["group", "model"]).print_table(max_column_width=50)

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

    def test_model_unique_key(self):
        """
        Verify that each model has a UNIQUE_KEY attribute set.
        """
        results = []
        for m in get_model_list():
            exists = m().UNIQUE_KEY is not None
            results.append([m.__name__, exists])
        self.attr_test_output("model", "UNIQUE_KEY", results)

    def test_model_documentcloud_pages(self):
        """
        Verify that each model has DOCUMENTCLOUD_PAGES defined
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
        Verify that each model has both DOCUMENTCLOUD_PAGES
        """
        results = []
        for m in get_model_list():
            # check if exists -- not sure if this is actually neccessary?
            if m().DOCUMENTCLOUD_PAGES:

                cal_access_tables = False
                map_cal_format = False

                # cycle through objs, checking for IDs
                for doc_pages in m().DOCUMENTCLOUD_PAGES:
                    # is this how you reference id?
                    if doc_pages.id is '2711614-CalAccessTablesWeb':
                        cal_access_tables = True
                    elif doc_pages.id is '2711616-MapCalFormat2Fields':
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

    def _test_choices(self, field_name):
        """
        Verify that proper choices appear for the provided field.
        """
        message_list = []
        # Loop through the models
        for m in get_model_list():

            # And then through the fields
            for f in m._meta.fields:

                # Only test against the provided field name
                if not f.name == field_name:
                    continue

                if not f.choices:
                    message_list.append((
                        m().klass_group,
                        m.__name__,
                        field_name,
                        "Has no CHOICES defined"
                    ))

                if not f.documentcloud_pages:
                    message_list.append((
                        m().klass_group,
                        m.__name__,
                        field_name,
                        "Has no `documentcloud_pages` defined"
                    ))

                # Pull out all the choices in that field
                slug_list = []
                for slug, name in f.choices:
                    # Make sure that each has a definition
                    if not name:
                        message_list.append((
                            m().klass_group,
                            m.__name__,
                            field_name,
                            "Value '%s' undefined in CHOICES" % slug
                        ))
                    if name.lower() == 'unknown':
                        message_list.append((
                            m().klass_group,
                            m.__name__,
                            field_name,
                            "Value '%s' defined as 'Unknown'" % slug
                        ))
                    slug_list.append(slug)

                # The query the database and make sure everything in
                # there has a matching definition in the choices
                for value, count in m.objects.values_list(
                    field_name,
                ).annotate(Count(field_name)):
                    message_list.append((
                        m().klass_group,
                        m.__name__,
                        field_name,
                        "Value '%s' in database but not in CHOICES" % value
                    ))
        return message_list

    def test_choices(self):
        """
        Verify that valid choices are available for all expected fields
        on all models.
        """
        # List of fields that we expect there to be valid choices defined
        fields = [
            'form_type',
            'form_id',
            'entity_code',
            'filer_type',
            'filing_type',
            'activity_type',
            'status',
            'off_s_h_cd',
            'pform_type',
            'stmnt_type',
            'stmnt_status',
            'rec_type',
            'party_cd',
            'sup_opp_cd',
            'elec_type',
            'reportname',
            'expn_code',
            'status_type',
        ]
        results = []
        for f in fields:
            results.extend(self._test_choices(f))
        table = agate.Table(results, ['group', 'model', 'field', 'message'])
        table.print_table(max_column_width=50)
