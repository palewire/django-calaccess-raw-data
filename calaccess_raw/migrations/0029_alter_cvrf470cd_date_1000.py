# Generated by Django 4.1.13 on 2024-07-12 14:35

import calaccess_raw.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("calaccess_raw", "0028_remove_cvrf470cd_cand_adr1"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cvrf470cd",
            name="date_1000",
            field=calaccess_raw.fields.DateField(
                blank=True,
                db_column="DATE_1000",
                help_text="Date contributions totaling $1,000 or more. (For the 470-S)",
                null=True,
            ),
        ),
    ]
