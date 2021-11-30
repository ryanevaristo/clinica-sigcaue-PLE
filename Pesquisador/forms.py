
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models import fields
from django.forms import ModelForm
from .models import Protocolo, Bioterio,User
from django import forms

class PesquisadorForm(UserCreationForm):
    nome = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=100)
    idade = forms.CharField(max_length=3)
    cpf = forms.CharField(max_length=14 ,label='CPF')
    universidade = forms.CharField(max_length=100)
    is_avaliador = forms.BooleanField(label="Avaliador")
    is_presidente = forms.BooleanField(label="Presidente")
    
    class Meta:
        model = User
        fields = ['username','nome','email','idade','cpf','universidade',
        'is_avaliador','is_presidente','password1','password2']


class PesquisadorChangeForm(UserChangeForm):
    nome = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=100)
    idade = forms.CharField(max_length=3)
    cpf = forms.CharField(max_length=14 ,label='CPF')
    universidade = forms.CharField(max_length=100)
    is_avaliador = forms.BooleanField(label="Avaliador")
    is_presidente = forms.BooleanField(label="Presidente")
    class Meta:
        model = User
        fields = ['username','nome','email','idade','cpf','universidade',
        'is_avaliador','is_presidente']


class DateInput(forms.DateInput):
    input_type = 'date'



class ProtocoloForm(ModelForm):
 
    class Meta:
        model = Protocolo
        fields = ['titulo_protocolo','justificativa', 'especie','bioterio', 'quantidade',
        'resumo', 'resumo_en','status', 'data_inicio', 'data_termino'
        ]
        widgets = {
            'data_inicio': DateInput(),
            'data_termino': DateInput(),
        }

class BioterioForm(ModelForm):

    class Meta:
        model = Bioterio
        fields = ['nome_bioterio', 'cnpj', 'rua', 'numero', 'bairro', 'cidade', 'estado'
        ]
