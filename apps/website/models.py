# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Contato(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(max_length=100,  blank=True, null=True, verbose_name='E-mail')
    telefone = models.CharField(max_length=20,  blank=True, null=True, verbose_name='Telefone')
    descricao = models.TextField(max_length=255,  blank=True, null=True, verbose_name='Descrição')
    is_visualizada = models.BooleanField(default=False, verbose_name='Visualizada ?')
    data = models.DateTimeField(default=timezone.now, verbose_name='Data')

    class Meta:
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.nome