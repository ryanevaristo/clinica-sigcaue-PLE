from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SecretariaForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from Pesquisador.models import User


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


class SecretariaUpdate(UpdateView):
    model = User
    template_name = 'administrador/forms-secretaria.html'
    form_class = SecretariaForm
    success_url = reverse_lazy('index')



class SecretariaDelete(DeleteView):
    model = User
    form_class = SecretariaForm()
    template_name = 'administrador/form-excluir.html'
    success_url = reverse_lazy('index')

class PesquisadorList(ListView):
    model = User
    template_name = 'administrador/presidente/lista-pesquisador.html'

    def get_queryset(self):
        return User.objects.filter(groups=5)


class PesquisadorUpdate(UpdateView):
    template_name = 'administrador/presidente/forms-pesquisador.html'
    model = User
    fields = ['username','nome', 'email', 'idade', 'cpf','universidade', 
    'groups','is_presidente',]
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        presidente = form.cleaned_data.get('is_presidente')
        print(presidente)
        try:
            if presidente == False:
                
                grupo = get_object_or_404(Group, name="Pesquisador")
                url = super().form_valid(form)
                self.object.groups.add(grupo)
                self.object.save()
                return url
            elif presidente == True and User.objects.filter(groups=3) > 1:
                
                grupo = get_object_or_404(Group, name="Presidente")
                grupo1 = get_object_or_404(Group, name="Pesquisador")
                url = super().form_valid(form)
                self.object.groups.add(grupo)
                self.object.groups.add(grupo1)
                self.object.save()
                return url
            else:
                print("SO pode ter 1 presidente")
        except:
            print()
