from django import forms
from django.contrib.auth.forms import UserCreationForm,  UserChangeForm
from Pesquisador.models import User


class SecretariaForm(UserCreationForm):
    nome = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=100)
    cpf = forms.CharField(max_length=14 ,label='CPF')
    

    class Meta:
        model = User
        fields = ['nome','username','cpf', 'email','password1','password2']


class SecretariaChangeForm(UserChangeForm):
    nome = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=100)
    cpf = forms.CharField(max_length=14 ,label='CPF')
    class Meta:
        model = User
        fields = ['nome','username','email','idade','cpf','universidade']
