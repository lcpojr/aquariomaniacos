# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-29 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0002_auto_20170829_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='descricao',
        ),
        migrations.AddField(
            model_name='projeto',
            name='conteudo',
            field=models.TextField(default=1, verbose_name='Conteúdo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(default=1, upload_to='', verbose_name='Imagem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projeto',
            name='resumo',
            field=models.TextField(default=1, verbose_name='Resumo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projeto',
            name='tipo',
            field=models.CharField(default=1, max_length=50, verbose_name='Tipo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projeto',
            name='data',
            field=models.DateField(blank=True, null=True, verbose_name='Data do projeto'),
        ),
    ]
