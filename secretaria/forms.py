from django import forms
from Pesquisador.models import User
from .models import Encaminhar, EncaminharAP
from django.forms import ModelForm

class EncaminharForm(ModelForm):
    class Meta:
        model = Encaminhar
        fields = ['UserProtocolo', 'protocoloEN']


class EncaminharFormAP(ModelForm):
    class Meta:
        model = EncaminharAP
        fields = ['UserProtocolo', 'protocoloEN']

