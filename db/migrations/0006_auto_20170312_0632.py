# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_auto_20170226_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='areamap',
            name='ll_lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='areamap',
            name='ll_lon',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='areamap',
            name='ur_lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='areamap',
            name='ur_lon',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
