from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    idade = forms.CharField(max_length=3)
    cpf = forms.CharField(max_length=14 ,label='CPF')
    universidade = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username','email','idade','cpf','universidade','password1','password2']

