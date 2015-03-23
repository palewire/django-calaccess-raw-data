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

    def test_form_type_choices(self):
        """
        Verify that proper choices appear for all form_type fields.
        """
        # Loop through the models
        for m in get_model_list():

            # And then through the fields
            for f in m._meta.fields:

                # Only test against the ones called form_type
                if not f.name == 'form_type':
                    continue

                # Pull out all the choices in that field
                slug_list = []
                for slug, name in f.choices:
                    # Make sure that each has a definition
                    # self.assertIsNot(name, '')
                    if not name:
                        warnings.warn("%s form_type '%s' undefined" % (
                            m.__name__,
                            slug,
                        ))
                    slug_list.append(slug)

                # The query the database and make sure everything in
                # there has a matching definition in the choices
                for v in m.objects.values("form_type").distinct():
                    self.assertIn(v, slug_list)
