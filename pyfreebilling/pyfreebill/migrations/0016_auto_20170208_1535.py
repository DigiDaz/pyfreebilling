# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-08 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pyfreebill', '0015_auto_20170208_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratecard',
            name='date_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
