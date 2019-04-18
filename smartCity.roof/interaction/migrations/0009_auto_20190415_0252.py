# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-15 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0008_auto_20190415_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(help_text='\u5386\u53f2\u65f6\u95f4', verbose_name='Time')),
                ('temperature', models.FloatField(help_text='\u6e29\u5ea6\u5386\u53f2\u6570\u636e', verbose_name="Temperature's trend")),
                ('humidity', models.FloatField(help_text='\u6e7f\u5ea6\u5386\u53f2\u6570\u636e', verbose_name="Humidity's trend")),
                ('light', models.FloatField(help_text='\u5149\u7167\u5386\u53f2\u6570\u636e', verbose_name="Light's trend")),
                ('noise', models.FloatField(help_text='\u566a\u58f0\u5386\u53f2\u6570\u636e', verbose_name="Noise's trend")),
                ('gas', models.FloatField(help_text='\u566a\u58f0\u5386\u53f2\u6570\u636e', verbose_name='Gas trend')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='refresh',
            field=models.IntegerField(help_text='\u6570\u636e\u5237\u65b0\u65f6\u95f4(ms)', verbose_name="Data's refresh"),
        ),
    ]