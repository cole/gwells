# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-01 14:51
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema):
    if schema.connection.vendor == 'postgresql':
        schema.execute("alter sequence aquifer_aquifer_id_seq restart with 2000")


def backwards(apps, schema):
    # It's no big deal if we don't go back
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('aquifers', '0007_auto_20181031_2320'),
    ]

    operations = [
        migrations.RunPython(forwards, reverse_code=backwards)
    ]
