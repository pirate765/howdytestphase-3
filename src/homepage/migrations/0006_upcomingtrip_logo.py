# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-04 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20180404_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingtrip',
            name='logo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
