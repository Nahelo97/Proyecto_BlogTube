# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-07 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0008_auto_20180807_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='video.Categoria'),
        ),
        migrations.AlterField(
            model_name='video',
            name='fecha',
            field=models.DateTimeField(null=True, verbose_name='Fecha'),
        ),
    ]
