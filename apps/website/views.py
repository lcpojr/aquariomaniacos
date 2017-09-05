# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView, CreateView
from django.template import RequestContext
from django.http import (JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseRedirect)
from datetime import datetime, timedelta, date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import sitemaps
import json

from .forms import *
from apps.painel.models import *


class Home(View):
    def get(self, request):
        form = ContatoForm
        publicacoes = Publicacao.objects.filter(status=True, slideshow=True)
        projetos = Projeto.objects.filter(status=True).order_by('-data')[:6]
        clientes = Cliente.objects.filter(status=True).order_by('-data')[:10]
        informacoes = Informacao.objects.filter(status=True).order_by('-data')[:3]
        albuns = Album.objects.all().order_by('-data')[:6]
        imagens = Imagem.objects.all().order_by('-album__data')

        galeria = []
        for album in albuns:
            for imagem in imagens:
                if album.pk == imagem.album.pk:
                    galeria.append(imagem)

        context = {
    		'form':form, 
    		'message':False, 
    		'publicacoes':publicacoes, 
    		'projetos':projetos, 
    		'clientes':clientes, 
    		'informacoes':informacoes, 
    		'galeria':galeria
    	}

        return render (request, 'home.html', context)

    def post(self, request, *args, **kwargs):
        form = ContatoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            subject = "Você recebeu um contato atrávez de seu website aquariomaniacos.com.br"
            message = obj.descricao
            email = obj.email
            contacts = settings.CONTACT_EMAILS
            template = render_to_string('email.html', {
                'message':obj.descricao, 
                'email':obj.email, 
                'name':obj.nome, 
                'phone':obj.telefone,
                'date':obj.data
            })

            send_mail(subject, message, email, contacts, html_message=template)


        form = ContatoForm()
        publicacoes = Publicacao.objects.filter(status=True, slideshow=True)
        projetos = Projeto.objects.filter(status=True).order_by('-data')[:6]
        clientes = Cliente.objects.filter(status=True).order_by('-data')
        informacoes = Informacao.objects.filter(status=True)
        albuns = Album.objects.all().order_by('-data')[:5]
        imagens = Imagem.objects.all().order_by('-album__data')

        galeria = []
        for album in albuns:
            for imagem in imagens:
                if album.pk == imagem.album.pk:
                    galeria.append(imagem)

        context = {
            'form':form, 
            'message':True, 
            'publicacoes':publicacoes, 
            'projetos':projetos, 
            'clientes':clientes, 
            'informacoes':informacoes,
            'galeria':galeria
        }
        return render (request, 'home.html', context)


class Sobre(View):
    def get(self, request):
        slideshow = Publicacao.objects.filter(status=True, slideshow=True)
        context = {'slideshow':slideshow}
        return render (request, 'sobre.html', context) 


class Galeria(View):
	def get(self, request, pk):
		imagens = Imagem.objects.filter(album=pk)
		context = {'imagens':imagens}
		return render(request, 'galeria/galeria.html', context)


class ListaGaleria(View):
	def get(self, request):
		albuns = Album.objects.all().order_by('-data')[:4]
		imagens = Imagem.objects.all().order_by('-album__data')

		galeria = []
		for album in albuns:
			for imagem in imagens:
				if album.pk == imagem.album.pk:
					galeria.append(imagem)
					break
				pass
			pass
			
		context = {'galeria':galeria}
		return render(request, 'galeria/list.html', context)


class Noticia(View):
	def get(self, request, pk):
		publicacao = Publicacao.objects.get(pk=pk)
		context = {'publicacao':publicacao}
		return render(request, 'noticia/noticia.html', context)


class ListaNoticias(View):
	def get(self, request):
		publicacoes = Publicacao.objects.filter(status=True)
		slideshow = publicacoes.filter(slideshow=True)
		context = {'publicacoes':publicacoes, 'slideshow':slideshow}
		return render(request, 'noticia/list.html', context)


class ProjetoRecente(View):
	def get(self, request, pk):
		projeto = Projeto.objects.get(pk=pk)
		slideshow = Publicacao.objects.filter(status=True, slideshow=True)
		context = {'projeto':projeto, 'slideshow':slideshow}
		return render(request, 'projetorecente/projeto.html', context)


class ListaProjetosRecente(View):
	def get(self, request):
		projetos = Projeto.objects.filter(status=True).order_by('-data')
		slideshow = Publicacao.objects.filter(status=True, slideshow=True)
		context = {'projetos':projetos, 'slideshow':slideshow}
		return render(request, 'projetorecente/list.html', context)