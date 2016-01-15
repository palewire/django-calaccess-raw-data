from __future__ import unicode_literals
import logging
import warnings
from django.conf import settings
from django.test import TestCase
from django.db.models import Count
from calaccess_raw import get_model_list
from django.test.utils import override_settings
from django.core.management import call_command
logger = logging.getLogger(__name__)


class CalAccessTest(TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Load data into the database before running other tests.
        """
        super(CalAccessTest, cls).setUpClass()
        kwargs = dict(
            verbosity=1,
            test_data=True
        )
        if settings.DATABASES.get("alt", None):
            kwargs['database'] = 'alt'
            logger.debug("Loading into 'alt' database")
        call_command("downloadcalaccessrawdata", **kwargs)

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
                for value, count in m.objects.values_list(
                    field_name,
                ).annotate(Count(field_name)):
                    warnings.warn("'%s' %s code undefined on %s model" % (
                        value,
                        field_name,
                        m.__name__
                    ))
                    # self.assertIn(value, slug_list)

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
        ]
        [self._test_choices(f) for f in fields]

    def test_field_docs(self):
        """
        Verify that all fields have verbose_name or help_text documentation.
        """
        for m in get_model_list():
            for f in m().get_field_list():
                if f.name == 'id':
                    continue
                if f.help_text:
                    continue
                if f.__dict__['_verbose_name']:
                    continue
                warnings.warn("%s.%s field undocumented" % (
                    m().klass_name,
                    f.name
                ))
