# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-05 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_auto_20170105_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='money',
            new_name='price',
        ),
        migrations.AddField(
            model_name='goods',
            name='picture',
            field=models.ImageField(default=22, upload_to='img', verbose_name='\u56fe\u7247'),
            preserve_default=False,
        ),
    ]
