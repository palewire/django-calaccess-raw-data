# Generated by Django 3.2.6 on 2021-08-22 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("calaccess_raw", "0023_alter_rawdataversion_clean_zip_archive"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rawdatafile",
            name="download_columns_count",
        ),
        migrations.RemoveField(
            model_name="rawdatafile",
            name="download_records_count",
        ),
        migrations.RemoveField(
            model_name="rawdatafile",
            name="error_count",
        ),
        migrations.RemoveField(
            model_name="rawdatafile",
            name="error_log_archive",
        ),
    ]
