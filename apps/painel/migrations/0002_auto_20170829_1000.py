# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-29 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacao',
            name='slideshow',
            field=models.BooleanField(default=False, verbose_name='Utilizar no Slideshow'),
        ),
        migrations.AddField(
            model_name='publicacao',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Ativar Publicação'),
        ),
    ]
