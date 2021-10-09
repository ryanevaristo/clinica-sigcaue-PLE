from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SecretariaForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group, User

# Create your views here.


class SecretariaCreate(CreateView):
    login_required = True
    template_name = 'administrador/forms-secretaria.html'
    form_class = SecretariaForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="Secretária")

        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()

        return url
