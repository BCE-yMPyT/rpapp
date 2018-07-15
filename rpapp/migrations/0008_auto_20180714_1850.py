# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-14 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpapp', '0007_auto_20180714_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rental_condition',
            field=models.CharField(choices=[(None, 'unknown'), ('free', 'free'), ('leased', 'leased')], default='free', max_length=6),
        ),
    ]
