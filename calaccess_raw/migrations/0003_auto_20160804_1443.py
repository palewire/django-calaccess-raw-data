# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_raw', '0002_auto_20160802_2101'),
    ]

    operations = [
        migrations.RenameField('RawDataVersion', 'size', 'expected_size'),
    ]
