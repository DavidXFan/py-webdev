# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import wines.models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0005_auto_20170905_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='abv',
            field=models.CharField(max_length=4, validators=[wines.models.valid_pct]),
        ),
    ]
