# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-19 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0049_auto_20181019_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='logo',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='addon',
            name='destination_package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addons', to='homepage.Destinationpackage'),
        ),
        migrations.AlterField(
            model_name='destinationimage',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinationimages', to='homepage.Destinationpackage'),
        ),
    ]
