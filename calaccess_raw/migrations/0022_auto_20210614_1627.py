# Generated by Django 3.2.4 on 2021-06-14 16:27

from django.db import migrations
import ia_storage.fields
import ia_storage.storage


class Migration(migrations.Migration):

    dependencies = [
        ("calaccess_raw", "0021_auto_20210614_1604"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rawdatafile",
            name="clean_file_archive",
            field=ia_storage.fields.InternetArchiveFileField(
                blank=True,
                help_text="An archive of the raw data file after being cleaned.",
                max_length=255,
                storage=ia_storage.storage.InternetArchiveStorage,
                upload_to="",
                verbose_name="archive of clean file",
            ),
        ),
        migrations.AlterField(
            model_name="rawdatafile",
            name="error_log_archive",
            field=ia_storage.fields.InternetArchiveFileField(
                blank=True,
                help_text="An archive of the error log containing lines from the original download file that could not be parsed and are excluded from the cleaned file.",
                max_length=255,
                storage=ia_storage.storage.InternetArchiveStorage,
                upload_to="",
                verbose_name="archive of error log",
            ),
        ),
    ]
