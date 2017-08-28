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

    # URLS DOACAO
    url(r'^doacoes/$', views.DoacaoList.as_view(), name='doacao-listar'),
    url(r'^doacoes/visualizar/(?P<pk>\d+)/$', login_required(views.DoacaoDetail.as_view()), name='doacao-detalhes'),
    url(r'^doacoes/deletar/(?P<pk>\d+)/$', login_required(views.DoacaoDelete.as_view()), name='doacao-deletar'),

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

    # URLS ALBUM
    url(r'^telefone/$', login_required(views.TelefoneList.as_view()), name='telefone-listar'),
    url(r'^telefone/cadastrar/$', login_required(views.TelefoneRegister.as_view()), name='telefone-cadastrar'),
    url(r'^telefone/editar/(?P<pk>\d+)/$', login_required(views.TelefoneEdit.as_view()), name='telefone-editar'),
    url(r'^telefone/delete/(?P<pk>\d+)/$', login_required(views.TelefoneDelete.as_view()), name='telefone-deletar'),
]