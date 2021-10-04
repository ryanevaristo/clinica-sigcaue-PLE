from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SecretariaForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    cpf = forms.CharField(max_length=14 ,label='CPF')
    

    class Meta:
        model = User
        fields = ['username','email','cpf','password1','password2',]