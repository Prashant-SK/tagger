# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_truncate_tags_and_markers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='date',
            field=models.DateField(),
        ),
    ]
