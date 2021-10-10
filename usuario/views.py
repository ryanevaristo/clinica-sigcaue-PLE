from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from braces.views import GroupRequiredMixin
from .models import Protocolo

from .forms import UsuarioForm, ProtocoloForm

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    dashboard_pesquisador = render(request, 'index.html')

    return dashboard_pesquisador


@login_required
def sair(request):
    logout(request)
    return redirect('/login')



class UserCreate(CreateView):
    template_name = 'login/forms.html'
    form_class = UsuarioForm
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
    template_name = 'administrador/forms-secretaria.html'
    form_class = ProtocoloForm
    success_url = reverse_lazy('index')