from django.test import TestCase
from django.test.utils import override_settings
from django.db.models import get_app, get_models


class CalAccessTest(TestCase):

    @override_settings(BASE_DIR='example/')
    def test_csv_gettrs(self):
        model_list = get_models(get_app("calaccess_raw"))
        for m in model_list:
            self.assertEqual(m.objects.get_csv_name(), m().get_csv_name())
            self.assertEqual(m.objects.get_csv_path(), m().get_csv_path())
