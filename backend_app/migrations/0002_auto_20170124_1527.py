# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=32),
        ),
    ]
