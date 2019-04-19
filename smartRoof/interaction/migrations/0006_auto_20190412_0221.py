# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-12 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0005_auto_20190411_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='local', help_text='\u5e94\u7528\u540d\u79f0', max_length=32, verbose_name="App's name"),
        ),
        migrations.AlterField(
            model_name='project',
            name='position',
            field=models.CharField(default='local', help_text='\u5e94\u7528\u4f4d\u7f6e', max_length=32, verbose_name="App's position"),
        ),
    ]
