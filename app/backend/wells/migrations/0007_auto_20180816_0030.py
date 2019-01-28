# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-16 00:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

from django.conf import settings


class Migration(migrations.Migration):
    atomic = settings.DATABASES.get('default').get('engine') == 'django.contrib.gis.db.backends.postgis'

    dependencies = [
        ('wells', '0006_load_casing_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casing',
            old_name='well_tag_number',
            new_name='well',
        ),
        migrations.AlterField(
            model_name='casing',
            name='well',
            field=models.ForeignKey(blank=True, db_column='well_tag_number', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='casing_set', to='wells.Well'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='owner_city',
            field=models.CharField(blank=True, max_length=100, verbose_name='Town/City'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='owner_mailing_address',
            field=models.CharField(blank=True, max_length=100, verbose_name='Mailing Address'),
        ),
        migrations.AlterField(
            model_name='casing',
            name='activity_submission',
            field=models.ForeignKey(blank=True, db_column='filing_number', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='casing_set', to='wells.ActivitySubmission'),
        ),
        migrations.AlterField(
            model_name='casing',
            name='casing_code',
            field=models.ForeignKey(db_column='casing_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='wells.CasingCode', verbose_name='Casing Type Code'),
        ),
        migrations.AlterField(
            model_name='well',
            name='alteration_end_date',
            field=models.DateField(null=True, verbose_name='Alteration Date'),
        ),
        migrations.AlterField(
            model_name='well',
            name='alteration_start_date',
            field=models.DateField(null=True, verbose_name='Alteration Start Date'),
        ),
        migrations.AlterField(
            model_name='well',
            name='construction_end_date',
            field=models.DateField(null=True, verbose_name='Construction Date'),
        ),
        migrations.AlterField(
            model_name='well',
            name='construction_start_date',
            field=models.DateField(null=True, verbose_name='Construction Start Date'),
        ),
        migrations.AlterField(
            model_name='well',
            name='decommission_end_date',
            field=models.DateField(null=True, verbose_name='Decommission Date'),
        ),
        migrations.AlterField(
            model_name='well',
            name='decommission_start_date',
            field=models.DateField(null=True, verbose_name='Decommission Start Date'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='owner_province_state',
            field=models.ForeignKey(db_column='province_state_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ProvinceStateCode', verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='owner_full_name',
            field=models.CharField(max_length=200, null=True, verbose_name='Owner Name'),
        ),
    ]
