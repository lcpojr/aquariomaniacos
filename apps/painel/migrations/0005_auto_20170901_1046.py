# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-01 13:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('painel', '0004_auto_20170829_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
                ('cargo', models.CharField(blank=True, max_length=50, verbose_name='Cargo')),
                ('descricao', models.TextField(blank=True, max_length=50, verbose_name='Descrição')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='Email')),
                ('endereco', models.CharField(blank=True, max_length=50, verbose_name='Endereço')),
                ('data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de Criação')),
            ],
        ),
        migrations.RemoveField(
            model_name='telefone',
            name='data',
        ),
        migrations.RemoveField(
            model_name='telefone',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='telefone',
            name='numero',
            field=models.CharField(max_length=50, verbose_name='Número'),
        ),
        migrations.AddField(
            model_name='informacao',
            name='telefones',
            field=models.ManyToManyField(to='painel.Telefone'),
        ),
        migrations.AddField(
            model_name='informacao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]