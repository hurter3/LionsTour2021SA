# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-10 08:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200610_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.AddField(
            model_name='order',
            name='date_ordered',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
