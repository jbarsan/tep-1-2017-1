# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170726_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
