from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import templatize
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from braces.views import GroupRequiredMixin
from .models import Bioterio, Protocolo

<<<<<<< HEAD:Pesquisador/views.py
from .forms import PesquisadorForm, ProtocoloForm
=======
from .forms import BioterioForm, UsuarioForm, ProtocoloForm
>>>>>>> 72af12e09b58591d66388e176adbfac57633e635:usuario/views.py




# Create your views here.
@login_required(login_url='/login/')
def index(request):
    dashboard_pesquisador = render(request, 'index.html')

    return dashboard_pesquisador

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')



class UserCreate(CreateView):
    template_name = 'login/forms.html'
    form_class = PesquisadorForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
    
        grupo = get_object_or_404(Group, name="Pesquisador")

        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()

        return url



def login_user(request):
    return render(request, 'login/login.html')


@csrf_protect
def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect('/')
    else:
        messages.error(request, 'Usuário/Senha inválidos. Favor tentar novamente.')
    return redirect('/login/')







class ProtocoloCreate(CreateView):
    template_name = 'pesquisador/forms-protocolo.html'
    form_class = ProtocoloForm
    success_url = reverse_lazy('index')


class ProtocoloUpdate(UpdateView):
    template_name = 'pesquisador/forms-protocolo.html'
    model = Protocolo
    fields = ['titulo_protocolo', 'justificativa', 'especie', 'quantidade','resumo', 
    'resumo_en', 'status', 'data_inicio', 'data_termino']
    success_url = reverse_lazy('index')


class ProtocoloDelete(DeleteView):
   model = Protocolo
   template_name = 'administrador/form-excluir.html'
   success_url = reverse_lazy('index')

class ProtocoloList(ListView):
    model = Protocolo
    template_name = 'pesquisador/lista-protocolo.html'




class BioterioCreate(CreateView):
    template_name = 'pesquisador/forms-bioterio.html'
    form_class = BioterioForm
    def get_success_url(self):
        return reverse_lazy('index')

class BioterioUpdate(UpdateView):
    template_name = 'pesquisador/forms-bioterio.html'
    model = Bioterio
    fields = ['nome_bioterio', 'cnpj', 'rua','numero', 'bairro', 'cidade', 'estado']
    success_url = reverse_lazy('index')

class BioterioDelete(DeleteView):
    model = Bioterio
    template_name = 'administrador/form-excluir.html'
    success_url = reverse_lazy('index')

class BioterioList(ListView):
    model = Bioterio
    template_name = 'pesquisador/lista-bioterio.html'
