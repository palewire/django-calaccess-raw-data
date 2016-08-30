#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Models for tracking CAL-ACCESS updates over time.
"""
from __future__ import unicode_literals
from .. import managers
from django.db import models
from hurry.filesize import size as sizeformat
from calaccess_raw import archive_directory_path, get_model_list
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class RawDataVersion(models.Model):
    """
    A version of CAL-ACCESS raw source data, typically released every day.
    """
    release_datetime = models.DateTimeField(
        unique=True,
        null=False,
        verbose_name='date and time of release',
        help_text='Date and time the version of the CAL-ACCESS database was released '
                  '(value of last-modified field in HTTP response header)'
    )
    expected_size = models.BigIntegerField(
        null=False,
        verbose_name='expected downloaded zip size',
        help_text='The expected size of the downloaded CAL-ACCESS zip, as '
                  'specified in the content-length field in HTTP response header.'
    )
    update_start_datetime = models.DateTimeField(
        null=True,
        verbose_name='date and time update started',
        help_text='Date and time when the update to the CAL-ACCESS version started',
    )
    update_finish_datetime = models.DateTimeField(
        null=True,
        verbose_name='date and time update finished',
        help_text='Date and time when the update to the CAL-ACCESS version finished',
    )
    download_start_datetime = models.DateTimeField(
        null=True,
        verbose_name='date and time download started',
        help_text='Date and time when the download of the CAL-ACCESS database export started',
    )
    download_finish_datetime = models.DateTimeField(
        null=True,
        verbose_name='date and time download finished',
        help_text='Date and time when the download of the CAL-ACCESS database export finished',
    )
    extract_start_datetime = models.DateTimeField(
        null=True,
        verbose_name='date and time extraction started',
        help_text='Date and time when extraction of the CAL-ACCESS data files started',
    )
    extract_finish_datetime = models.DateTimeField(
        null=True,
        verbose_name='date and time extraction finished',
        help_text='Date and time when extraction of the CAL-ACCESS data files finished',
    )
    download_zip_archive = models.FileField(
        blank=True,
        max_length=255,
        upload_to=archive_directory_path,
        verbose_name='download files zip file',
        help_text='An archive of the original zipped file downloaded from CAL-ACCESS.'
    )
    clean_zip_archive = models.FileField(
        blank=True,
        max_length=255,
        upload_to=archive_directory_path,
        verbose_name='cleaned files zip archive',
        help_text='An archive zip of cleaned (and error log) files'
    )
    download_zip_size = models.BigIntegerField(
        null=True,
        verbose_name='downloaded zip size',
        help_text='The actual size of the downloaded CAL-ACCESS zip after the '
                  'downloaded completed.'
    )
    clean_zip_size = models.BigIntegerField(
        null=True,
        verbose_name='clean zip size',
        help_text='The size of the zip containing all cleaned raw data files '
                  'and error logs.'
    )
    objects = managers.RawDataVersionManager()

    class Meta:
        """
        Meta model options.
        """
        app_label = 'calaccess_raw'
        verbose_name = 'CAL-ACCESS raw data version'
        ordering = ('-release_datetime',)
        get_latest_by = 'release_datetime'

    def __str__(self):
        return str(self.release_datetime)

    @property
    def update_completed(self):
        """
        Check if the database update to the version completed.

        Return True or False.
        """
        if self.update_finish_datetime:
            is_completed = True
        else:
            is_completed = False

        return is_completed

    @property
    def update_stalled(self):
        """
        Check if the database update to the version started but did not complete.

        Return True or False.
        """
        if self.update_start_datetime and not self.update_finish_datetime:
            is_stalled = True
        else:
            is_stalled = False

        return is_stalled

    @property
    def download_completed(self):
        """
        Check if the download of the version's zip completed.

        Return True or False.
        """
        if self.download_finish_datetime:
            is_completed = True
        else:
            is_completed = False

        return is_completed

    @property
    def download_stalled(self):
        """
        Check if the download of the version's zip started but did not complete.

        Return True or False.
        """
        if self.download_start_datetime and not self.download_finish_datetime:
            is_stalled = True
        else:
            is_stalled = False

        return is_stalled

    @property
    def extract_completed(self):
        """
        Check if the extract of files from the downloaded zip completed.

        Return True or False.
        """
        if self.extract_finish_datetime:
            is_completed = True
        else:
            is_completed = False

        return is_completed

    @property
    def extract_stalled(self):
        """
        Check if the extract of files from the downloaded zip started but did not complete.

        Return True or False.
        """
        if self.extract_start_datetime and not self.extract_finish_datetime:
            is_stalled = True
        else:
            is_stalled = False

        return is_stalled

    def pretty_expected_size(self):
        """
        Returns a prettified version (e.g., "725M") of the expected size of the downloaded zip.
        """
        if not self.expected_size:
            return None
        return sizeformat(self.expected_size)
    pretty_expected_size.short_description = 'expected download zip size'
    pretty_expected_size.admin_order_field = 'expected download zip size'

    def pretty_download_size(self):
        """
        Returns a prettified version (e.g., "725M") of the actual size of the downloaded zip.
        """
        if not self.download_zip_size:
            return None
        return sizeformat(self.download_zip_size)
    pretty_download_size.short_description = 'download zip size'
    pretty_download_size.admin_order_field = 'download zip size'

    def pretty_clean_size(self):
        """
        Returns a prettified version (e.g., "725M") of the zip of clean data files and error logs.
        """
        if not self.clean_zip_size:
            return None
        return sizeformat(self.clean_zip_size)
    pretty_clean_size.short_description = 'clean zip size'
    pretty_clean_size.admin_order_field = 'clean zip size'

    @property
    def download_file_count(self):
        """
        Returns the count of files included in the version's downloaded zip.
        """
        return self.files.count()

    @property
    def download_record_count(self):
        """
        Returns the count of records in the version's downloaded files.
        """
        return self.files.aggregate(
            total=models.Sum('download_records_count')
        )['total']

    @property
    def clean_file_count(self):
        """
        Returns the count of files cleaned in the version.
        """
        return self.files.exclude(clean_file_archive='').count()

    @property
    def clean_record_count(self):
        """
        Returns the count of records in the version's cleaned files.
        """
        return self.files.aggregate(
            total=models.Sum('clean_records_count')
        )['total']

    @property
    def error_file_count(self):
        """
        Returns the count of cleaned files with errors in the version.
        """
        return self.files.exclude(error_log_archive='').count()

    @property
    def error_count(self):
        """
        Returns the count of cleaning errors in the version.
        """
        return self.files.aggregate(
            total=models.Sum('error_count')
        )['total']


@python_2_unicode_compatible
class RawDataFile(models.Model):
    """
    A data file included in a version of the CAL-ACCESS raw source data.
    """
    version = models.ForeignKey(
        'RawDataVersion',
        on_delete=models.CASCADE,
        related_name='files',
        verbose_name='raw data version',
        help_text='Foreign key referencing the version of the raw '
                  'source data in which the file was included'
    )
    file_name = models.CharField(
        max_length=100,
        verbose_name='raw data file name',
        help_text='Name of the raw source data file without extension',
    )
    download_records_count = models.IntegerField(
        null=False,
        default=0,
        verbose_name='download records count',
        help_text='Count of records in the original file downloaded from CAL-ACCESS'
    )
    clean_records_count = models.IntegerField(
        null=False,
        default=0,
        verbose_name='clean records count',
        help_text='Count of records in the cleaned file generated by calaccess_raw'
    )
    load_records_count = models.IntegerField(
        null=False,
        default=0,
        verbose_name='load records count',
        help_text="Count of records in the loaded from cleaned file into "
                  "calaccess_raw's data model"
    )
    download_columns_count = models.IntegerField(
        null=False,
        default=0,
        verbose_name='download columns count',
        help_text='Count of columns in the original file downloaded from CAL-ACCESS'
    )
    clean_columns_count = models.IntegerField(
        null=False,
        default=0,
        verbose_name='clean columns count',
        help_text='Count of columns in the cleaned file generated by calaccess_raw'
    )
    load_columns_count = models.IntegerField(
        null=False,
        default=0,
        verbose_name='load columns count',
        help_text='Count of columns on the loaded calaccess_raw data model'
    )
    download_file_archive = models.FileField(
        blank=True,
        max_length=255,
        upload_to=archive_directory_path,
        verbose_name='archive of download file',
        help_text='An archive of the original raw data file downloaded '
                     'from CAL-ACCESS.'
    )
    download_file_size = models.BigIntegerField(
        null=False,
        default=0,
        verbose_name='size of raw data file in bytes',
        help_text='Size of the .TSV file'
    )
    clean_file_archive = models.FileField(
        blank=True,
        max_length=255,
        upload_to=archive_directory_path,
        verbose_name='archive of clean file',
        help_text='An archive of the raw data file after being cleaned.'
    )
    clean_file_size = models.BigIntegerField(
        null=False,
        default=0,
        verbose_name='size of clean data file in bytes',
        help_text='Size of the .CSV file'
    )
    error_count = models.IntegerField(
        null=False,
        default=0,
        verbose_name='error count',
        help_text='Count of records in the original download that could not '
                  'be parsed and are excluded from the cleaned file.'
    )
    error_log_archive = models.FileField(
        blank=True,
        max_length=255,
        upload_to=archive_directory_path,
        verbose_name='archive of error log',
        help_text='An archive of the error log containing lines from the '
                  'original download file that could not be parsed and are '
                  'excluded from the cleaned file.'
    )
    clean_start_datetime = models.DateTimeField(
        null=True,
        verbose_name='date and time cleaning started',
        help_text='Date and time when the cleaning of the file started',
    )
    clean_finish_datetime = models.DateTimeField(
        null=True,
        verbose_name='date and time cleaning finished',
        help_text='Date and time when the cleaning of the file finished',
    )
    load_start_datetime = models.DateTimeField(
        null=True,
        verbose_name='date and time loading started',
        help_text='Date and time when the loading of the file started',
    )
    load_finish_datetime = models.DateTimeField(
        null=True,
        verbose_name='date and time extraction finished',
        help_text='Date and time when the loading of the file finished',
    )

    class Meta:
        """
        Meta model options.
        """
        app_label = 'calaccess_raw'
        unique_together = (('version', 'file_name'),)
        verbose_name = 'CAL-ACCESS raw data file'
        ordering = ('-version_id', 'file_name',)

    def __str__(self):
        return self.file_name

    def pretty_download_file_size(self):
        """
        Returns a prettified version (e.g., "725M") of the downloaded file's size.
        """
        return sizeformat(self.download_file_size)
    pretty_download_file_size.short_description = 'download file size'
    pretty_download_file_size.admin_order_field = 'download file size'

    def pretty_clean_file_size(self):
        """
        Returns a prettified version (e.g., "725M") of the cleaned file's size.
        """
        return sizeformat(self.clean_file_size)
    pretty_clean_file_size.short_description = 'clean file size'
    pretty_clean_file_size.admin_order_field = 'clean file size'

    @property
    def model(self):
        """
        Returns the RawDataFile's corresponding CalAccess database model object.
        """
        try:
            return [
                m for m in get_model_list() if m().db_table == self.file_name
            ][0]
        except IndexError:
            return None
