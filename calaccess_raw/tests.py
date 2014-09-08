from django.test import TestCase
from calaccess_raw import get_model_list
from django.test.utils import override_settings


class CalAccessTest(TestCase):

    @override_settings(BASE_DIR='example/')
    def test_csv_gettrs(self):
        for m in get_model_list():
            self.assertEqual(m.objects.get_csv_name(), m().get_csv_name())
            self.assertEqual(m.objects.get_csv_path(), m().get_csv_path())
