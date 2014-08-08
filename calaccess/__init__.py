import os
from django.conf import settings


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
