# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-04 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_auto_20161223_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='coin',
            field=models.IntegerField(default=0, verbose_name='\u91d1\u5e01'),
        ),
        migrations.AddField(
            model_name='information',
            name='experience',
            field=models.IntegerField(default=0, verbose_name='\u7ecf\u9a8c'),
        ),
        migrations.AddField(
            model_name='information',
            name='level',
            field=models.IntegerField(default=0, verbose_name='\u7b49\u7ea7'),
        ),
        migrations.AlterField(
            model_name='information',
            name='birthday',
            field=models.DateField(verbose_name='\u751f\u65e5'),
        ),
        migrations.AlterField(
            model_name='information',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='information',
            name='head',
            field=models.ImageField(upload_to='img', verbose_name='\u5934\u50cf'),
        ),
    ]
