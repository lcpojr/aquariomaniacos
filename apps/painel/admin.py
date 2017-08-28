# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Publicacao, Projeto, Album

admin.site.register(Publicacao)
admin.site.register(Projeto)
admin.site.register(Album)