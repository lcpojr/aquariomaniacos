from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from apps.website import views 

urlpatterns = [
    url(r'^$', cache_page(60 * 15)(views.Home.as_view()), name='home'),
    url(r'^sobre/$', cache_page(60 * 15)(views.Sobre.as_view()), name='sobre'),
    url(r'^galeria/(?P<pk>\d+)/$', cache_page(60 * 15)(views.Galeria.as_view()), name='galeria'),
    url(r'^galeria/lista/$', cache_page(60 * 15)(views.ListaGaleria.as_view()), name='galeria-lista'),
    url(r'^noticia/(?P<pk>\d+)/$', views.Noticia.as_view(), name='noticia'),
    url(r'^noticia/lista/$', views.ListaNoticias.as_view(), name='noticia-lista'),
    url(r'^projeto/(?P<pk>\d+)/$', views.ProjetoRecente.as_view(), name='projetorecente'),
    url(r'^projeto/lista/$', views.ListaProjetosRecente.as_view(), name='projetorecente-lista'),
]
