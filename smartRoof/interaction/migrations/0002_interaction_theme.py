# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-05 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='theme',
            field=models.CharField(default='pink', max_length=32),
        ),
    ]
