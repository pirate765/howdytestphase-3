# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-23 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0052_auto_20181022_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventure',
            name='logo',
            field=models.CharField(blank=True, max_length=200),
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
