from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from apps.painel import views 

urlpatterns = [
	url(r'^$', login_required(views.Home.as_view()), name='home'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),

    # URLS USUARIO
    url(r'^usuario/$', login_required(views.UsuarioList.as_view()), name='usuario-listar'),
    url(r'^usuario/cadastrar/$', login_required(views.UsuarioRegister.as_view()), name='usuario-cadastrar'),
    url(r'^usuario/deletar/(?P<pk>\d+)/$', login_required(views.UsuarioDelete.as_view()), name='usuario-deletar'),
    url(r'^usuario/senha/$', login_required(views.UsuarioChangePassword.as_view()), name='usuario-senha'),

	# URLS PUBLICAÇÃO
	url(r'^publicacao/$', login_required(views.PublicacaoList.as_view()), name='publicacao-listar'),
    url(r'^publicacao/cadastrar/$', login_required(views.PublicacaoRegister.as_view()), name='publicacao-cadastrar'),
    url(r'^publicacao/editar/(?P<pk>\d+)/$', login_required(views.PublicacaoEdit.as_view()), name='publicacao-editar'),
    url(r'^publicacao/deletar/(?P<pk>\d+)/$', login_required(views.PublicacaoDelete.as_view()), name='publicacao-deletar'),

    # URLS CONTATO
    url(r'^mensagem/$', views.ContatoList.as_view(), name='contato-listar'),
    url(r'^mensagem/visualizar/(?P<pk>\d+)/$', login_required(views.ContatoDetail.as_view()), name='contato-detalhes'),
    url(r'^mensagem/deletar/(?P<pk>\d+)/$', login_required(views.ContatoDelete.as_view()), name='contato-deletar'),

    # URLS PROJETO
    url(r'^projeto/$', login_required(views.ProjetoList.as_view()), name='projeto-listar'),
    url(r'^projeto/cadastrar/$', login_required(views.ProjetoRegister.as_view()), name='projeto-cadastrar'),
    url(r'^projeto/editar/(?P<pk>\d+)/$', login_required(views.ProjetoEdit.as_view()), name='projeto-editar'),
    url(r'^projeto/deletar/(?P<pk>\d+)/$', login_required(views.ProjetoDelete.as_view()), name='projeto-deletar'),

    # URLS ALBUM
    url(r'^album/$', login_required(views.AlbumList.as_view()), name='album-listar'),
    url(r'^album/cadastrar/$', login_required(views.AlbumRegister.as_view()), name='album-cadastrar'),
    url(r'^album/editar/(?P<pk>\d+)/$', login_required(views.AlbumEdit.as_view()), name='album-editar'),
    url(r'^album/delete/(?P<pk>\d+)/$', login_required(views.AlbumDelete.as_view()), name='album-deletar'),
    url(r'^foto/delete/(?P<pk>\d+)/$', login_required(views.FotoDelete.as_view()), name='foto-deletar'),

    # URLS CLIENTE
    url(r'^informacao/$', login_required(views.InformacaoList.as_view()), name='informacao-listar'),
    url(r'^informacao/cadastrar/$', login_required(views.InformacaoRegister.as_view()), name='informacao-cadastrar'),
    url(r'^informacao/editar/(?P<pk>\d+)/$', login_required(views.InformacaoEdit.as_view()), name='informacao-editar'),
    url(r'^informacao/delete/(?P<pk>\d+)/$', login_required(views.InformacaoDelete.as_view()), name='informacao-deletar'),

    # URLS CLIENTE
    url(r'^cliente/$', login_required(views.ClienteList.as_view()), name='cliente-listar'),
    url(r'^cliente/cadastrar/$', login_required(views.ClienteRegister.as_view()), name='cliente-cadastrar'),
    url(r'^cliente/editar/(?P<pk>\d+)/$', login_required(views.ClienteEdit.as_view()), name='cliente-editar'),
    url(r'^cliente/delete/(?P<pk>\d+)/$', login_required(views.ClienteDelete.as_view()), name='cliente-deletar'),

]