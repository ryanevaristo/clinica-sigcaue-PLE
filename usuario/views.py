from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
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
    return HttpResponseRedirect('/login')



class UserCreate(CreateView):
    template_name = 'login/forms.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')




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