# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poi',
            name='priority',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='poi',
            name='progress',
            field=models.IntegerField(max_length=3),
        ),
    ]
