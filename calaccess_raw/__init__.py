import os
import warnings
warnings.simplefilter('ignore', DeprecationWarning)  # noqa
from django.conf import settings
default_app_config = 'calaccess_raw.apps.CalAccessRawConfig'


def get_download_directory():
    """
    Returns the download directory where we will store downloaded data.
    """
    if hasattr(settings, 'CALACCESS_DOWNLOAD_DIR'):
        return getattr(settings, 'CALACCESS_DOWNLOAD_DIR')
    elif hasattr(settings, 'BASE_DIR'):
        return os.path.join(getattr(settings, 'BASE_DIR'), 'data')
    raise ValueError("CAL-ACCESS download directory not configured. Set either \
CALACCESS_DOWNLOAD_DIR or BASE_DIR in settings.py")


def get_test_download_directory():
    """
    Returns the download directory where we will store test data.
    """
    if hasattr(settings, 'CALACCESS_TEST_DOWNLOAD_DIR'):
        return getattr(settings, 'CALACCESS_TEST_DOWNLOAD_DIR')
    elif hasattr(settings, 'BASE_DIR'):
        return os.path.join(getattr(settings, 'BASE_DIR'), 'test-data')
    raise ValueError("CAL-ACCESS test download directory not configured. \
Set either CALACCESS_TEST_DOWNLOAD_DIR or BASE_DIR in settings.py")


def get_model_list():
    """
    Returns a model list with all the data tables in this application
    """
    from django.apps import apps
    return apps.get_app_config("calaccess_raw").models.values()
