# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView, CreateView
from django.template import RequestContext
from django.http import (JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseRedirect)
from datetime import datetime, timedelta, date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as Usuario
from django.contrib.auth import update_session_auth_hash
from django.utils import timezone
import json

from apps.website.models import *
from apps.website.forms import *
from .models import *
from .forms import *


class Home(View):
    def get(self, request):
        return render (request, 'core/index.html')



class Login(View):
    def get(self, request):
        form = LoginForm()
        context = {'form':form}
        return render (request, 'registration/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get("usuario"), password=form.cleaned_data.get("password"))
            login(request, user)
            next = request.GET.get('next')
            if next:
                return redirect(next)
        return render (request, 'registration/login.html', context)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy("painel:login")+ '?next=/painel/')



class UsuarioRegister(View):
    def get(self, request):
        if not request.user.is_staff:
            return redirect(reverse_lazy("painel:home"))
        form = UsuarioForm()
        context = {'form':form}
        return render (request, 'usuario/register.html', context)

    def post(self, request, *args, **kwargs):
        form = UsuarioForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(reverse_lazy("painel:usuario-listar"))
        else:
            return render (request, 'usuario/register.html', context)

class UsuarioList(View):
    def get(self, request):
        obj_list = Usuario.objects.all().exclude(pk=request.user.pk).order_by('-date_joined')

        paginator = Paginator(obj_list, 25)
        page = request.GET.get('page')
        try:
            usuarios = paginator.page(page)
        except PageNotAnInteger:
            usuarios = paginator.page(1)
        except EmptyPage:
            usuarios = paginator.page(paginator.num_pages)
        context = {'usuarios': usuarios}
        return render(request, 'usuario/list.html', context)

class UsuarioDelete(View):
    def get(self, request, pk):
        usuario = Usuario.objects.get(pk=pk).delete()
        return redirect(reverse_lazy("painel:usuario-listar"))

class UsuarioChangePassword(View):
    def get(self, request):
        form = ChangePasswordForm(request.user)
        context = {'form':form}
        return render (request, 'usuario/changepassword.html', context)
    def post(self, request, *args, **kwargs):
        form = ChangePasswordForm(request.user, data=request.POST)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse_lazy("painel:home"))
        else:
            return render (request, 'usuario/changepassword.html', context)        


class PublicacaoRegister(View):
    def get(self, request):
        form = PublicacaoForm()
        context = {'form':form}
        return render (request, 'publicacao/register.html', context)

    def post(self, request, *args, **kwargs):
        form = PublicacaoForm(request.POST, request.FILES)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            return redirect(reverse_lazy("painel:publicacao-listar"))
        else:
            return render (request, 'publicacao/register.html', context)

class PublicacaoEdit(View):
    def get(self, request, pk):
        publicacao = Publicacao.objects.get(pk=pk)
        form = PublicacaoForm(instance=publicacao)
        context = {'form':form, 'publicacao':publicacao}
        return render (request, 'publicacao/edit.html', context)

    def post(self, request, pk, *args, **kwargs):
        publicacao = Publicacao.objects.get(pk=pk)
        form = PublicacaoForm(request.POST, request.FILES, instance=publicacao)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            return redirect(reverse_lazy("painel:publicacao-listar"))
        else:
            return render (request, 'publicacao/edit.html', context)

class PublicacaoList(View):
    def get(self, request):
        publicacoes = Publicacao.objects.all()
        context = {'publicacoes': publicacoes}
        return render(request, 'publicacao/list.html', context)

class PublicacaoDelete(View):
    def get(self, request, pk):
        publicacao = Publicacao.objects.get(pk=pk).delete()
        return redirect(reverse_lazy("painel:publicacao-listar"))



class ContatoList(View):
    def get(self, request):
        obj_list = Contato.objects.all().order_by('data')

        paginator = Paginator(obj_list, 25)
        page = request.GET.get('page')
        try:
            contatos = paginator.page(page)
        except PageNotAnInteger:
            contatos = paginator.page(1)
        except EmptyPage:
            contatos = paginator.page(paginator.num_pages)
        context = {'contatos': contatos}
        return render(request, 'contato/list.html', context)

class ContatoDetail(View):
    def get(self, request, pk):
        contato = Contato.objects.get(pk=pk)
        contato.is_visualizada = True
        contato.save()
        form = ContatoForm(instance=contato)
        form.fields['nome'].widget.attrs['disabled'] = True
        form.fields['telefone'].widget.attrs['disabled'] = True
        form.fields['email'].widget.attrs['disabled'] = True
        form.fields['descricao'].widget.attrs['disabled'] = True

        context = {'form':form, 'contato':pk}
        return render (request, 'contato/detail.html', context)

class ContatoDelete(View):
    def get(self, request, pk):
        contato = Contato.objects.get(pk=pk).delete()
        return redirect(reverse_lazy("painel:contato-listar"))



class DoacaoList(View):
    def get(self, request):
        obj_list = Doacao.objects.all().order_by('-data')

        paginator = Paginator(obj_list, 25)
        page = request.GET.get('page')
        try:
            doacoes = paginator.page(page)
        except PageNotAnInteger:
            doacoes = paginator.page(1)
        except EmptyPage:
            doacoes = paginator.page(paginator.num_pages)
        context = {'doacoes': doacoes}
        return render(request, 'doacao/list.html', context)

class DoacaoDetail(View):
    def get(self, request, pk):
        doacao = Doacao.objects.get(pk=pk)
        doacao.is_visualizada = True
        doacao.save()
        form = DoacaoForm(instance=doacao)
        form.fields['nome'].widget.attrs['disabled'] = True
        form.fields['rg'].widget.attrs['disabled'] = True
        form.fields['cpf'].widget.attrs['disabled'] = True
        form.fields['email'].widget.attrs['disabled'] = True
        form.fields['nome'].widget.attrs['disabled'] = True
        form.fields['telefone'].widget.attrs['disabled'] = True
        form.fields['celular'].widget.attrs['disabled'] = True
        form.fields['cep'].widget.attrs['disabled'] = True
        form.fields['rua'].widget.attrs['disabled'] = True
        form.fields['bairro'].widget.attrs['disabled'] = True
        form.fields['cidade'].widget.attrs['disabled'] = True
        form.fields['estado'].widget.attrs['disabled'] = True
        form.fields['valor'].widget.attrs['disabled'] = True
        form.fields['modalidade'].widget.attrs['disabled'] = True
        form.fields['banco'].widget.attrs['disabled'] = True
        form.fields['conta'].widget.attrs['disabled'] = True
        form.fields['agencia'].widget.attrs['disabled'] = True
        form.fields['titular'].widget.attrs['disabled'] = True
        form.fields['cpf_cnpj'].widget.attrs['disabled'] = True

        context = {'form':form, 'doacao':pk}
        return render (request, 'doacao/detail.html', context)

class DoacaoDelete(View):
    def get(self, request, pk):
        doacao = Doacao.objects.get(pk=pk).delete()
        return redirect(reverse_lazy("painel:doacao-listar"))
    


class ProjetoRegister(View):
    def get(self, request):
        form = ProjetoForm()
        context = {'form':form}
        return render (request, 'projeto/register.html', context)

    def post(self, request):
        form = ProjetoForm(request.POST, request.FILES)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            return redirect(reverse_lazy("painel:projeto-listar"))
        else:
            return render (request, 'projeto/register.html', context)

class ProjetoEdit(View):
    def get(self, request, pk):
        projeto = Projeto.objects.get(pk=pk)
        form = ProjetoForm(instance=projeto)
        context = {'form':form, 'projeto':projeto}
        return render (request, 'projeto/edit.html', context)

    def post(self, request, pk):
        projeto = Projeto.objects.get(pk=pk)
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            return redirect(reverse_lazy("painel:projeto-listar"))
        else:
            return render (request, 'projeto/edit.html', context)

class ProjetoList(View):
    def get(self, request):
        obj_list = Projeto.objects.all().order_by('-data')

        paginator = Paginator(obj_list, 25)
        page = request.GET.get('page')
        try:
            projetos = paginator.page(page)
        except PageNotAnInteger:
            projetos = paginator.page(1)
        except EmptyPage:
            projetos = paginator.page(paginator.num_pages)
        context = {'projetos': projetos}
        return render(request, 'projeto/list.html', context)

class ProjetoDelete(View):
    def get(self, request, pk):
        projeto = Projeto.objects.get(pk=pk).delete()
        return redirect(reverse_lazy("painel:projeto-listar"))


class AlbumRegister(View):
    def get(self, request):
        form = AlbumForm()
        context = {'form':form}
        return render(request, 'album/register.html', context)

    def post(self, request,*args, **kwargs):
        form = AlbumForm(request.POST, request.FILES)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            for value in request.FILES.getlist('imagem'):
                img = Imagem()
                img.album = obj
                img.imagem = value
                img.save()
            return redirect(reverse_lazy("painel:album-listar"))
        else:
            return render (request, 'album/register.html', context)


class AlbumEdit(View):
    def get(self, request, pk):
        album = Album.objects.get(pk=pk)
        form = AlbumForm(instance=album)
        context = {'form':form}
        return render(request, 'album/edit.html', context)

    def post(self, request, pk, *args, **kwargs):
        album = Album.objects.get(pk=pk)
        form = AlbumForm(request.POST, request.FILES, instance=album)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            for value in request.FILES.getlist('imagem'):
                img = Imagem()
                img.album = obj
                img.imagem = value
                img.save()
            return redirect(reverse_lazy("painel:album-listar"))
        else:
            return render (request, 'album/edit.html', context)


class AlbumList(View):
    def get(self, request):
        imagens = Imagem.objects.all()
        hoje = timezone.now
        context = {'imagens': imagens, 'hoje':hoje}
        return render(request, 'album/list.html', context)


class AlbumDelete(View):
    def get(self, request, pk):
        Album.objects.get(pk=pk).delete()
        return redirect(reverse_lazy("painel:album-listar"))


class FotoDelete(View):
    def get(self, request, pk):
        Imagem.objects.get(pk=pk).delete()
        return redirect(reverse_lazy("painel:album-listar"))



class TelefoneRegister(View):
    def get(self, request):
        form = TelefoneForm()
        context = {'form':form}
        return render (request, 'telefone/register.html', context)

    def post(self, request):
        form = TelefoneForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            return redirect(reverse_lazy("painel:telefone-listar"))
        else:
            return render (request, 'telefone/register.html', context)

class TelefoneEdit(View):
    def get(self, request, pk):
        telefone = Telefone.objects.get(pk=pk)
        form = TelefoneForm(instance=telefone)
        context = {'form':form, 'telefone':telefone}
        return render (request, 'telefone/edit.html', context)

    def post(self, request, pk):
        telefone = Telefone.objects.get(pk=pk)
        form = TelefoneForm(request.POST, instance=telefone)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            return redirect(reverse_lazy("painel:telefone-listar"))
        else:
            return render (request, 'telefone/edit.html', context)

class TelefoneList(View):
    def get(self, request):
        obj_list = Telefone.objects.all().order_by('-data')

        paginator = Paginator(obj_list, 25)
        page = request.GET.get('page')
        try:
            telefones = paginator.page(page)
        except PageNotAnInteger:
            telefones = paginator.page(1)
        except EmptyPage:
            telefones = paginator.page(paginator.num_pages)
        context = {'telefones': telefones}
        return render(request, 'telefone/list.html', context)

class TelefoneDelete(View):
    def get(self, request, pk):
        telefones = Telefone.objects.get(pk=pk).delete()
        return redirect(reverse_lazy("painel:telefone-listar"))