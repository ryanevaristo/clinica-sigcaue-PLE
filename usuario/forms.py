
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Protocolo
from django import forms

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    idade = forms.CharField(max_length=3)
    cpf = forms.CharField(max_length=14 ,label='CPF')
    universidade = forms.CharField(max_length=100)
    

    class Meta:
        model = User
        fields = ['username','email','idade','cpf','universidade','password1','password2']



class DateInput(forms.DateInput):
    input_type = 'date'



class ProtocoloForm(ModelForm):
 
    class Meta:
        model = Protocolo
        fields = ['justificativa', 'bioterio', 'especie', 'quantidade',
        'resumo', 'resumo_en','status', 'data_inicio', 'data_termino'
        ]
        widgets = {
            'data_inicio': DateInput(),
            'data_termino': DateInput(),
        }
  