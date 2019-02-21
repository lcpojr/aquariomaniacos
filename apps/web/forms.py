# -*- coding: utf-8 -*-
from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=50)
    email = forms.CharField(label="Email", max_length=50)
    telefone = forms.CharField(label="Telefone", max_length=20, required=False)
    descricao = forms.CharField(label="Descrição", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)

        self.fields["nome"].widget.attrs["class"] = "form-control"
        self.fields["nome"].widget.attrs["data-validation"] = "[NOTEMPTY]"
        self.fields["nome"].widget.attrs["placeholder"] = "Nome"

        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["placeholder"] = "E-mail"

        self.fields["telefone"].widget.attrs["class"] = "form-control celular"
        self.fields["telefone"].widget.attrs["placeholder"] = "Telefone"
        self.fields["telefone"].widget.attrs["data-validation"] = "[NOTEMPTY]"

        self.fields["descricao"].widget.attrs["class"] = "form-control"
        self.fields["descricao"].widget.attrs[
            "placeholder"
        ] = "Digite aqui sua mensagem"
