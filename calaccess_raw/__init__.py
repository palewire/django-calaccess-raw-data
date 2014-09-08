import os
from django.conf import settings
from django.db.models.loading import get_models, get_app
default_app_config = 'calaccess_raw.apps.CalAccessRawConfig'


def get_download_directory():
    """
    Returns the download directory where we will store downloaded data.
    """
    if hasattr(settings, 'CALACCESS_DOWNLOAD_DIR'):
        return getattr(settings, 'CALACCESS_DOWNLOAD_DIR')
    elif hasattr(settings, 'BASE_DIR'):
        return os.path.join(getattr(settings, 'BASE_DIR'), 'data')
    raise ValueError("CalAccess download directory not configured. Set either \
CALACCESS_DOWNLOAD_DIR or BASE_DIR in settings.py")


def get_model_list():
    """
    Returns a model list with all the data tables in this application
    """
    return get_models(get_app("calaccess_raw"))
