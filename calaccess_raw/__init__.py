"""
A hodgepodge of utilities related to the app's settings and configuration.
"""
import os
from django.conf import settings
default_app_config = 'calaccess_raw.apps.CalAccessRawConfig'


def get_data_directory():
    """
    Returns download directory for data storage downloaded data.
    """
    if getattr(settings, 'CALACCESS_DATA_DIR', None):
        return getattr(settings, 'CALACCESS_DATA_DIR')
    elif getattr(settings, 'BASE_DIR', None):
        return os.path.join(getattr(settings, 'BASE_DIR'), 'data')
    raise ValueError("CAL-ACCESS download directory not configured. Set either \
CALACCESS_DATA_DIR or BASE_DIR in settings.py")


def get_model_list():
    """
    Returns a model list with all the data tables in this application.
    """
    from django.apps import apps
    model_list = apps.get_app_config("calaccess_raw").models.values()
    return [m for m in model_list if "CalAccessBaseModel" in str(m.__base__)]
