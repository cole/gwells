# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 23:04
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    atomic = settings.DATABASES.get('default').get('engine') == 'django.contrib.gis.db.backends.postgis'

    dependencies = [
        ('registries', '0007_auto_20180611_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proofofagecode',
            name='registries_proof_of_age_code',
            field=models.CharField(db_column='registries_proof_of_age_code', editable=False, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='applicationstatuscode',
            name='registries_application_status_code',
            field=models.CharField(db_column='registries_application_status_code', editable=False, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registriesremovalreason',
            name='registries_removal_reason_code',
            field=models.CharField(db_column='registries_removal_reason_code', editable=False, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.RenameField(
            model_name='proofofagecode',
            old_name='registries_proof_of_age_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='applicationstatuscode',
            old_name='registries_application_status_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='registriesremovalreason',
            old_name='registries_removal_reason_code',
            new_name='code',
        ),
    ]
