# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0034_auto_20170327_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portaluser',
            name='facility',
            field=models.ManyToManyField(to='facility.Facility'),
        ),
    ]
