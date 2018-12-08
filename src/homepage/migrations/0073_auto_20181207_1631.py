# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-07 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0072_auto_20181207_1553'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='grouppackageitenerary',
            name='destination_package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinationitinerary', to='homepage.Destinationpackage'),
        ),
    ]