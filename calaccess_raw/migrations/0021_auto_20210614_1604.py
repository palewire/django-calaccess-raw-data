# Generated by Django 3.2.4 on 2021-06-14 16:04

from django.db import migrations
import ia_storage.fields
import ia_storage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_raw', '0020_auto_20210614_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rawdatafile',
            name='InternetArchiveFileField',
        ),
        migrations.AddField(
            model_name='rawdatafile',
            name='download_file_archive',
            field=ia_storage.fields.InternetArchiveFileField(blank=True, help_text='An archive of the original raw data file downloaded from CAL-ACCESS.', max_length=255, storage=ia_storage.storage.InternetArchiveStorage, upload_to='', verbose_name='archive of download file'),
        ),
    ]
