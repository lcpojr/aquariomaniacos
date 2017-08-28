from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User as Usuario
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import *

class UsuarioForm(UserCreationForm):
	class Meta:
		model = Usuario
		fields = ['username', 'email', 'first_name', 'last_name', 'is_staff']

	def __init__(self, *args, **kwargs):
		super(UsuarioForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['is_staff'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

		self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['first_name'].widget.attrs['placeholder'] = 'Nome'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Sobrenome'
		self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmação de senha'

		self.fields['username'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		self.fields['password1'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		self.fields['password2'].widget.attrs['data-validation'] = '[NOTEMPTY]'


class PublicacaoForm(forms.ModelForm):
	class Meta:
		model = Publicacao
		fields = ['titulo', 'resumo', 'imagem', 'conteudo']

	def __init__(self, *args, **kwargs):
		super(PublicacaoForm, self).__init__(*args, **kwargs)
		self.fields['titulo'].widget.attrs['class'] = 'form-control'
		self.fields['resumo'].widget.attrs['class'] = 'form-control'
		self.fields['imagem'].widget.attrs['class'] = 'form-control'
		self.fields['conteudo'].widget.attrs['class'] = 'form-control summernote'

		self.fields['titulo'].widget.attrs['placeholder'] = 'Título da publicação'
		self.fields['resumo'].widget.attrs['placeholder'] = 'Breve resumo da publicação'
		self.fields['imagem'].widget.attrs['placeholder'] = 'Imagem de capa da publicação'
		self.fields['conteudo'].widget.attrs['placeholder'] = 'Conteúdo da publicação'

		self.fields['titulo'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		self.fields['resumo'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		self.fields['conteudo'].widget.attrs['data-validation'] = '[NOTEMPTY]'



class LoginForm(forms.Form):
	usuario = forms.CharField(label='Usuário',required=True,max_length=50)
	password = forms.CharField(label='Senha',required=True, widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		if cleaned_data.get("usuario") and cleaned_data.get("password"):
			user = authenticate(username=cleaned_data.get("usuario"), password=cleaned_data.get("password"))
			if not user:
				self.add_error('password', 'Usuário e/ou senha inválido(s)')



class ChangePasswordForm(PasswordChangeForm):
	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)
		self.fields['old_password'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['class'] = 'form-control'

		self.fields['old_password'].widget.attrs['placeholder'] = 'Senha antiga'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Nova senha'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirmação de senha'

		self.fields['old_password'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		self.fields['new_password1'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		self.fields['new_password2'].widget.attrs['data-validation'] = '[NOTEMPTY]'



class ProjetoForm(forms.ModelForm):
	class Meta:
		model = Projeto
		fields = ['titulo', 'descricao']

	def __init__(self, *args, **kwargs):
		super(ProjetoForm, self).__init__(*args, **kwargs)
		self.fields['titulo'].widget.attrs['class'] = 'form-control'
		self.fields['descricao'].widget.attrs['class'] = 'form-control'

		self.fields['titulo'].widget.attrs['placeholder'] = 'Título do projeto'
		self.fields['descricao'].widget.attrs['placeholder'] = 'Descrição do projeto'

		self.fields['titulo'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		self.fields['descricao'].widget.attrs['data-validation'] = '[NOTEMPTY]'



class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ['titulo', 'data_album', 'categoria']

	def __init__(self, *args, **kwargs):
		super(AlbumForm, self).__init__(*args, **kwargs)
		self.fields['titulo'].widget.attrs['class'] = 'form-control'
		self.fields['data_album'].widget.attrs['class'] = 'form-control data'
		self.fields['categoria'].widget.attrs['class'] = 'form-control'

		self.fields['titulo'].widget.attrs['placeholder'] = 'Título da publicação'
		self.fields['data_album'].widget.attrs['placeholder'] = '__/__/____'
		self.fields['categoria'].widget.attrs['placeholder'] = 'Categoria da publicação'

		self.fields['titulo'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		self.fields['data_album'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		self.fields['categoria'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		

class TelefoneForm(forms.ModelForm):
	class Meta:
		model = Telefone
		fields = ['numero']

	def __init__(self, *args, **kwargs):
		super(TelefoneForm, self).__init__(*args, **kwargs)
		self.fields['numero'].widget.attrs['class'] = 'form-control celular'

		self.fields['numero'].widget.attrs['placeholder'] = 'Numero do telefone com DDD.'

		self.fields['numero'].widget.attrs['data-validation'] = '[NOTEMPTY]'