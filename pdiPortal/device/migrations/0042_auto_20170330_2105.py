# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 04:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0041_auto_20170330_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicefacilitylist',
            name='device',
        ),
        migrations.RemoveField(
            model_name='devicefacilitylist',
            name='facility',
        ),
        migrations.AlterField(
            model_name='device',
            name='facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.Facility'),
        ),
        migrations.DeleteModel(
            name='DeviceFacilityList',
        ),
    ]
