from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.painel.models import Publicacao, Album, Projeto

class StaticViewSitemap(Sitemap):
	priority = 1.0
	changefreq = 'daily'

	def items(self):
		return ['website:home','website:sobre', 'website:galeria-lista', 'website:noticia-lista', 'website:projetorecente-lista']

	def location(self, url):
		return reverse(url)


class NoticiaSitemap(Sitemap):
	priority = 1.0
	changefreq = 'daily'

	def items(self):
		urls = []
		publicacoes = Publicacao.objects.all()
		for publicacao in publicacoes:
			urls.append({'name':'website:noticia', 'pk':publicacao.pk, 'data': publicacao.data})
		return urls

	def location(self, url):
		return reverse(url['name'], kwargs={'pk':url['pk']})

	def lastmod(self, url):
		return url['data']


class GaleriaSitemap(Sitemap):
	priority = 1.0
	changefreq = 'daily'

	def items(self):
		urls = []
		albuns = Album.objects.all()
		for album in albuns:
			urls.append({'name':'website:galeria', 'pk':album.pk, 'data': album.data})
		return urls

	def location(self, url):
		return reverse(url['name'], kwargs={'pk':url['pk']})

	def lastmod(self, url):
		return url['data']


class ProjetoSitemap(Sitemap):
	priority = 1.0
	changefreq = 'daily'

	def items(self):
		urls = []
		projetos = Projeto.objects.all()
		for projeto in projetos:
			urls.append({'name':'website:projetorecente', 'pk':projeto.pk, 'data': projeto.data})
		return urls

	def location(self, url):
		return reverse(url['name'], kwargs={'pk':url['pk']})

	def lastmod(self, url):
		return url['data']