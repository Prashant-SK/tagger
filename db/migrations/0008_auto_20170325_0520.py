# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_merge_20170325_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='symbol',
            field=models.CharField(max_length=30),
        ),
    ]
