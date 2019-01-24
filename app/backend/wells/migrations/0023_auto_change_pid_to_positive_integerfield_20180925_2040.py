# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-25 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):
    engine = settings.DATABASES.get('default').get('engine')
    atomic = engine == 'django.db.backends.postgresql' or engine == 'django.contrib.gis.db.backends.postgis'

    dependencies = [
        ('wells', '0022_update_casing_material_code'),
    ]

    operations = [
        # If this alteration fails, it means you have bad data in your database that you have to resolve 1st!
        migrations.AlterField(
            model_name='well',
            name='legal_pid',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Property Identification Description (PID)'),
        ),
        migrations.RenameField(
            model_name='lithologydescription',
            old_name='well_tag_number',
            new_name='well',
        ),
        migrations.AlterField(
            model_name='lithologydescription',
            name='activity_submission',
            field=models.ForeignKey(blank=True, db_column='filing_number', null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='lithologydescription_set', to='wells.ActivitySubmission'),
        ),
        migrations.AlterField(
            model_name='lithologydescription',
            name='well',
            field=models.ForeignKey(blank=True, db_column='well_tag_number', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lithologydescription_set', to='wells.Well'),
        )
    ]
