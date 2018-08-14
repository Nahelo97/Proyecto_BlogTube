# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-31 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200, null=True, verbose_name='Usuario')),
                ('mail', models.EmailField(max_length=200, null=True, verbose_name='Correo')),
                ('fecha', models.DateTimeField(null=True, verbose_name='Fecha')),
                ('comentario', models.TextField(null=True, verbose_name='Comentario')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
                ('fecha', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='video.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='video.Video'),
        ),
    ]