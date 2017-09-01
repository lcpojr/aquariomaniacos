from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.sitemaps import ping_google
import re

class Publicacao(models.Model):
	id = models.AutoField(primary_key=True)
	usuario = models.ForeignKey(User)
	titulo = models.CharField('Título', max_length=50, unique=True)
	resumo = models.TextField('Breve Resumo')
	imagem = models.ImageField('Imagem')
	conteudo = models.TextField('Conteúdo')
	data = models.DateTimeField('Data de Publicação', default=timezone.now)
	status = models.BooleanField('Ativar Publicação', default=True)
	slideshow = models.BooleanField('Utilizar no Slideshow', default=False)

	def __str__(self):
	    return str(self.titulo)


class Projeto(models.Model):
	id = models.AutoField(primary_key=True)
	usuario = models.ForeignKey(User)
	titulo = models.CharField('Título', max_length=50, unique=True)
	tipo = models.CharField('Tipo', max_length=50)
	imagem = models.ImageField('Imagem')
	resumo = models.TextField('Resumo')
	data = models.DateField('Data do projeto', blank=True, null=True)
	conteudo = models.TextField('Conteúdo')
	status = models.BooleanField('Ativar Projeto', default=True)

	def __str__(self):
	    return str(self.titulo)

	def save(self, force_insert=False, force_update=False):
		super(Projeto, self).save(force_insert, force_update)
		try:
			ping_google()
		except Exception:
			pass


class Album(models.Model):
	usuario = models.ForeignKey(User)
	titulo = models.CharField('Título', max_length=50, unique=True)
	categoria = models.CharField('Categoria', max_length=50, blank=True)
	data_album = models.DateField('Data do Evento')
	data = models.DateTimeField('Data de Criação', default=timezone.now)

	def __str__(self):
	    return str(self.titulo)

	def save(self, force_insert=False, force_update=False):
		super(Album, self).save(force_insert, force_update)
		try:
			ping_google()
		except Exception:
			pass


class Imagem(models.Model):
	album = models.ForeignKey(Album)
	imagem = models.ImageField('Foto')

	def __str__(self):
	    return str(self.imagem)

	def save(self, force_insert=False, force_update=False):
		super(Imagem, self).save(force_insert, force_update)
		try:
			ping_google()
		except Exception:
			pass


class Telefone(models.Model):
	numero = models.CharField('Número', max_length=50)

	def __str__(self):
	    return str(self.numero)

	def get_numero(self):
		return re.sub('[^0-9]', '', self.numero)


class Informacao(models.Model):
	usuario = models.ForeignKey(User)
	nome = models.CharField('Nome', max_length=50, unique=True)
	cargo = models.CharField('Cargo', max_length=50, blank=True)
	descricao = models.TextField('Descrição', max_length=50, blank=True)
	email = models.EmailField('Email', max_length=50, blank=True)
	telefones = models.ManyToManyField(Telefone)
	endereco = models.CharField('Endereço', max_length=200, blank=True)
	lat = models.CharField('Latitude', max_length=200, blank=True)
	lng = models.CharField('Longitude', max_length=200, blank=True)
	data = models.DateTimeField('Data de Criação', default=timezone.now)
	status = models.BooleanField('Ativar Informação', default=True)

	def __str__(self):
	    return str(self.numero)

	    
class Cliente(models.Model):
	id = models.AutoField(primary_key=True)
	usuario = models.ForeignKey(User)
	nome = models.CharField('Nome', max_length=50, unique=True)
	imagem = models.ImageField('Imagem')
	data = models.DateTimeField('Data de Registro', default=timezone.now)
	status = models.BooleanField('Ativar Cliente', default=True)

	def __str__(self):
	    return str(self.titulo)