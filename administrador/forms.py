from django import forms
from django.contrib.auth.forms import UserCreationForm,  UserChangeForm
from Pesquisador.models import User


class SecretariaForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    cpf = forms.CharField(max_length=14 ,label='CPF')
    

    class Meta:
        model = User
        fields = ['username','cpf', 'email','password1','password2']


class SecretariaChangeForm(UserChangeForm):
    email = forms.EmailField(max_length=100)
    cpf = forms.CharField(max_length=14 ,label='CPF')
    class Meta:
        model = User
        fields = ['username','email','idade','cpf','universidade']
