# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0005_auto_20170622_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
