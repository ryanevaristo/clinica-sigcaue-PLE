from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from Pesquisador.forms import PesquisadorForm
from Pesquisador.models import User, Protocolo
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_protect
from .forms import EncaminharForm, EncaminharFormAP
from .models import Encaminhar, EncaminharAP



# Create your views here.
class EncaminharCreate(CreateView):
    form_class = EncaminharForm
    template_name = 'secretaria/encaminhar/forms-encaminhar.html'
    success_url = reverse_lazy('index')
    
class EncaminharAPCreate(CreateView):
    form_class = EncaminharFormAP
    template_name = 'secretaria/encaminhar/forms-encaminhar.html'
    success_url = reverse_lazy('index')

class EncaminharList(ListView):
    model = Encaminhar
    template_name = 'pesquisador/avaliador/lista-protocolo-pe.html'

    def get_queryset(self):
        self.object_list = Encaminhar.objects.filter(UserProtocolo=self.request.user)
        return self.object_list


class EncaminharAPList(ListView):
    model = EncaminharAP
    template_name = 'pesquisador/avaliador/lista-protocolo-pe.html'

    def get_queryset(self):
        self.object_list = Encaminhar.objects.filter(UserProtocolo=self.request.user)
        return self.object_list
        
    


class ProtocolPendList(ListView):
    model = Protocolo
    template_name = 'secretaria/pendentes/lista-protocolo-pe.html'

    def get_queryset(self):
        return Protocolo.objects.filter(status="PENDENTE")



class ProtocolAprovList(ListView):
    model = Protocolo
    template_name = 'secretaria/pendentes/lista-protocolo-pe.html'


    def get_queryset(self):
        return Protocolo.objects.filter(status="APROVADO")


class PesquisadorList(ListView):
    model = User
    template_name = 'secretaria/lista-pesquisador.html'

    def get_queryset(self):
        return User.objects.filter(groups=5)
    



class PesquisadorUpdate(UpdateView):
    template_name = 'secretaria/forms-pesquisador.html'
    model = User
    fields = ['username', 'email', 'idade', 'cpf','universidade', 
    'groups','is_avaliador',]
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        avaliador = form.cleaned_data.get('is_avaliador')
        print(avaliador)
        try:
            if avaliador == True:
                grupo = get_object_or_404(Group, name="Avaliador")
                grupo1 = get_object_or_404(Group, name="Pesquisador")
                url = super().form_valid(form)
                self.object.groups.add(grupo)
                self.object.groups.add(grupo1)
                self.object.save()
                return url
            else:
                grupo = get_object_or_404(Group, name="Pesquisador")
                url = super().form_valid(form)
                self.object.groups.add(grupo)
                self.object.save()
                return url
        except:
            print()


    
