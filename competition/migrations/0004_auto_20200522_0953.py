# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-22 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0003_auto_20200521_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='match1',
        ),
        migrations.AddField(
            model_name='competition',
            name='lionsscore2',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='lionsscore3',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='lionsscore4',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='lionsscore5',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='lionsscore6',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='lionsscore7',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='lionsscore8',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='points_accrued',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='sascore2',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='sascore3',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='sascore4',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='sascore5',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='sascore6',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='sascore7',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='competition',
            name='sascore8',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='competition',
            name='lionsscore1',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='competition',
            name='sascore1',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]