# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-11 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0002_auto_20170624_0707'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensorId',
            field=models.CharField(default='sds-af4a', max_length=32),
            preserve_default=False,
        ),
    ]