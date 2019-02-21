from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings
from .forms import *


class Home(View):
    form = ContatoForm

    def get(self, request):
        return render(request, "home.html", {"form": self.form()})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            contact = form.cleaned_data

            """
            send_mail(
                "Novo cliente entrou em contato pelo seu WEBSITE",
                "Cliente: {} \n Telefone: {} \n Email: {} \n {}".format(
                    contact["nome"],
                    contact["telefone"],
                    contact["email"],
                    contact["descricao"],
                ),
                settings.DEFAULT_FROM_EMAIL,
                settings.CONTACT_EMAILS,
            )
            """

        render(request, "home.html", {"form": self.form()})
