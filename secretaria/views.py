from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from Pesquisador.forms import PesquisadorForm
from Pesquisador.models import User
from django.contrib.auth.models import Group


# Create your views here.


class PesquisadorList(ListView):
    model = User
    template_name = 'secretaria/lista-pesquisador.html'

    def get_queryset(self):
        return User.objects.all()


class PesquisadorUpdate(UpdateView):
    template_name = 'secretaria/forms-pesquisador.html'
    model = User
    fields = ['username', 'email', 'idade', 'cpf','universidade', 
    'groups',]
    success_url = reverse_lazy('index')



class PesquisadorDelete(DeleteView):
    template_name = 'administrador/form-excluir.html'
    sucess_url = reverse_lazy("index")