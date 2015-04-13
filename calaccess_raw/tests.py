from __future__ import unicode_literals
import warnings
from django.test import TestCase
from calaccess_raw import get_model_list
from django.test.utils import override_settings


class CalAccessTest(TestCase):

    @override_settings(BASE_DIR='example/')
    def test_csv_gettrs(self):
        """
        Verify that get_csv_name methods work for all models.
        """
        for m in get_model_list():
            self.assertEqual(m.objects.get_csv_name(), m().get_csv_name())
            self.assertEqual(m.objects.get_csv_path(), m().get_csv_path())

    def test_model_str(self):
        """
        Verify that __str__ methods exist and work for all models.
        """
        for m in get_model_list():
            m().__str__()
            self.assertNotEqual(m().__str__(), '%s object' % m.__name__)

    def test_model_doc(self):
        """
        Verify that __doc__ methods exist and work for all models.
        """
        for m in get_model_list():
            if m().__doc__.startswith(m.__name__):
                warnings.warn("%s __doc__ undefined" % (m.__name__))
            # self.assertNotEqual(m().__doc__, '')

    def _test_choices(self, field_name):
        """
        Verify that proper choices appear for the provided field.
        """
        # Loop through the models
        for m in get_model_list():

            # And then through the fields
            for f in m._meta.fields:

                # Only test against the provided field name
                if not f.name == field_name:
                    continue

                # Pull out all the choices in that field
                slug_list = []
                if not f.choices:
                    warnings.warn("%s %s has no choices defined" % (
                        m.__name__,
                        field_name
                    ))
                for slug, name in f.choices:
                    # Make sure that each has a definition
                    # self.assertIsNot(name, '')
                    if not name:
                        warnings.warn("%s %s '%s' undefined" % (
                            m.__name__,
                            field_name,
                            slug,
                        ))
                    slug_list.append(slug)

                # The query the database and make sure everything in
                # there has a matching definition in the choices
                for v in m.objects.values(field_name).distinct():
                    self.assertIn(v, slug_list)

    def test_form_type_choices(self):
        self._test_choices('form_type')

    def test_form_id_choices(self):
        self._test_choices('form_id')

    def test_entity_code_choices(self):
        self._test_choices('entity_code')

    def test_filer_type_choices(self):
        self._test_choices('filer_type')

    def test_filing_type_choices(self):
        self._test_choices('filing_type')

    def test_activity_type_choices(self):
        self._test_choices('activity_type')

    def test_status_choices(self):
        self._test_choices('status')

    def test_off_s_h_cd_choices(self):
        self._test_choices('off_s_h_cd')

    def test_pform_type_choices(self):
        self._test_choices('pform_type')

    def test_statement_type_choices(self):
        self._test_choices('stmnt_type')

    def test_statement_status_choices(self):
        self._test_choices('stmnt_status')

    def test_record_type_choices(self):
        self._test_choices('rec_type')
