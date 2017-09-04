# -*- coding: utf-8 -*-
from django import forms
from .models import Contato 

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'descricao']

    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['data-validation'] = '[NOTEMPTY]'
        self.fields['nome'].widget.attrs['placeholder'] = 'Nome'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'

        self.fields['telefone'].widget.attrs['class'] = 'form-control celular'
        self.fields['telefone'].widget.attrs['placeholder'] = 'Telefone'
        self.fields['telefone'].widget.attrs['data-validation'] = '[NOTEMPTY]'

        self.fields['descricao'].widget.attrs['class'] = 'form-control'
        self.fields['descricao'].widget.attrs['placeholder'] = 'Digite aqui sua mensagem'