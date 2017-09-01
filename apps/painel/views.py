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
from django.forms import modelformset_factory
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


class InformacaoRegister(View):
    def get(self, request):
        form = InformacaoForm(prefix='form')
        formset = modelformset_factory(Telefone, form=TelefoneForm, can_delete=False, extra=1)
        formset = formset(queryset=Telefone.objects.none(), prefix='formset')

        context = {'form':form, 'formset':formset}
        return render (request, 'informacao/register.html', context)

    def post(self, request):
        form = InformacaoForm(request.POST, prefix='form')
        formset = modelformset_factory(Telefone, form=TelefoneForm, can_delete=False, extra=1)
        formset = formset(request.POST, prefix='formset')

        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()

            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
                obj.telefones.add(instance)

            return redirect(reverse_lazy("painel:informacao-listar"))
        else:
            return render (request, 'informacao/register.html', context)


class InformacaoEdit(View):
    def get(self, request, pk):
        informacao = Informacao.objects.get(pk=pk)

        form = InformacaoForm(instance=informacao, prefix='form')
        formset = modelformset_factory(Telefone, form=TelefoneForm, can_delete=True, extra=0)
        formset = formset(queryset=informacao.telefones.all(), prefix='formset')

        context = {'form':form, 'formset':formset, 'informacao':informacao}
        return render (request, 'informacao/edit.html', context)

    def post(self, request, pk):
        informacao = Informacao.objects.get(pk=pk)

        form = InformacaoForm(request.POST, instance=informacao, prefix='form')
        formset = modelformset_factory(Telefone, form=TelefoneForm, can_delete=True, extra=0)
        formset = formset(request.POST, prefix='formset')

        context = {'form':form, 'formset':formset, 'informacao':informacao}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()

            instances = formset.save(commit=False)
            for fields in formset.deleted_objects:
                fields.delete()

            for instance in instances:
                instance.save()
                obj.telefones.add(instance)

            return redirect(reverse_lazy("painel:informacao-listar"))
        else:
            return render (request, 'informacao/edit.html', context)


class InformacaoList(View):
    def get(self, request):
        obj_list = Informacao.objects.all().order_by('-data')

        paginator = Paginator(obj_list, 25)
        page = request.GET.get('page')
        try:
            informacoes = paginator.page(page)
        except PageNotAnInteger:
            informacoes = paginator.page(1)
        except EmptyPage:
            informacoes = paginator.page(paginator.num_pages)
        context = {'informacoes': informacoes}
        return render(request, 'informacao/list.html', context)


class InformacaoDelete(View):
    def get(self, request, pk):
        informacoes = Informacoes.objects.get(pk=pk).delete()
        return redirect(reverse_lazy("painel:informacao-listar"))


class ClienteRegister(View):
    def get(self, request):
        form = ClienteForm()
        context = {'form':form}
        return render (request, 'cliente/register.html', context)

    def post(self, request):
        form = ClienteForm(request.POST, request.FILES)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            return redirect(reverse_lazy("painel:cliente-listar"))
        else:
            return render (request, 'cliente/register.html', context)


class ClienteEdit(View):
    def get(self, request, pk):
        cliente = Cliente.objects.get(pk=pk)
        form = ClienteForm(instance=cliente)
        context = {'form':form, 'cliente':cliente}
        return render (request, 'cliente/edit.html', context)

    def post(self, request, pk):
        cliente = Cliente.objects.get(pk=pk)
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            return redirect(reverse_lazy("painel:cliente-listar"))
        else:
            return render (request, 'cliente/edit.html', context)


class ClienteList(View):
    def get(self, request):
        obj_list = Cliente.objects.all().order_by('-data')

        paginator = Paginator(obj_list, 25)
        page = request.GET.get('page')
        try:
            clientes = paginator.page(page)
        except PageNotAnInteger:
            clientes = paginator.page(1)
        except EmptyPage:
            clientes = paginator.page(paginator.num_pages)
        context = {'clientes': clientes}
        return render(request, 'cliente/list.html', context)


class ClienteDelete(View):
    def get(self, request, pk):
        clientes = Cliente.objects.get(pk=pk).delete()
        return redirect(reverse_lazy("painel:cliente-listar"))