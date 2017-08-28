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

	def __str__(self):
	    return str(self.titulo)

class Projeto(models.Model):
	id = models.AutoField(primary_key=True)
	usuario = models.ForeignKey(User)
	titulo = models.CharField('Título', max_length=50, unique=True)
	descricao = models.TextField('Descrição')
	data = models.DateTimeField('Data de Publicação', default=timezone.now)

	def __str__(self):
	    return str(self.titulo)

	def save(self, force_insert=False, force_update=False):
		super(Projeto, self).save(force_insert, force_update)
		try:
			pring_google()
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
			pring_google()
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
			pring_google()
		except Exception:
			pass

class Telefone(models.Model):
	numero = models.CharField('Número', max_length=50, unique=True)
	usuario = models.ForeignKey(User)
	data = models.DateTimeField('Data de Criação', default=timezone.now)

	def __str__(self):
	    return str(self.numero)

	def get_numero(self):
		return re.sub('[^0-9]', '', self.numero)