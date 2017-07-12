#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


def archive_directory_path(instance, filename):
    """
    Returns a path to an archived raw data file or ZIP.

    (e.g., MEDIA_ROOT/YYYY-MM-DD_HH-MM-SS/filename.ext)
    """
    from calaccess_raw.models.tracking import RawDataVersion, RawDataFile

    if isinstance(instance, RawDataVersion):
        release_datetime = instance.release_datetime
        f_name, f_ext = filename.split('.')
        path = '{fn}_{dt:%Y-%m-%d_%H-%M-%S}.{fx}'.format(
            fn=f_name,
            dt=release_datetime,
            fx=f_ext,
        )
    elif isinstance(instance, RawDataFile):
        release_datetime = instance.version.release_datetime
        path = '{dt:%Y-%m-%d_%H-%M-%S}/{f}'.format(dt=release_datetime, f=filename)
    else:
        raise TypeError("Must be called on RawDataVersion or RawDataFile instance.")
    return path


def get_model_list():
    """
    Returns a model list with all the data tables in this application.
    """
    from django.apps import apps
    model_list = apps.get_app_config("calaccess_raw").models.values()
    return [m for m in model_list if "CalAccessBaseModel" in str(m.__base__)]
