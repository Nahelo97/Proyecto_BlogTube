# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-07 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_auto_20180807_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='video.Categoria'),
        ),
    ]
