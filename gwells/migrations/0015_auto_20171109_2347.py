# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 23:47
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0014_auto_20171109_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casing',
            name='internal_diameter',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.5'))], verbose_name='Diameter'),
        ),
    ]