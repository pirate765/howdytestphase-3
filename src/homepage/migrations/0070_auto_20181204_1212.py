# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-04 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0069_auto_20181130_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='howdystays',
            name='ap_per_person',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='howdystays',
            name='cp_per_person',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='howdystays',
            name='ep_per_person',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='howdystays',
            name='mapai_per_person',
            field=models.IntegerField(blank=True, null=True),
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
