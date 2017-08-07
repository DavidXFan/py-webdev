# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Online',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'online',
            },
        ),
        migrations.AlterModelTable(
            name='dreamreal',
            table='dreamreal',
        ),
    ]