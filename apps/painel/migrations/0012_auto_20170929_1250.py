# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-29 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0011_auto_20170929_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('1', 'Aquarismo'), ('2', 'Lago Ornamental'), ('3', 'Camping'), ('4', 'Arqueria e Tiro esportivo'), ('5', 'Mergulho'), ('6', 'Pesca esportiva')], max_length=25),
        ),
    ]
