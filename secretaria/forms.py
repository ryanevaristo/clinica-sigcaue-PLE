from django import forms
from django.contrib.auth.models import User
from .models import Encaminhar
from django.forms import ModelForm

class EncaminharForm(ModelForm):
    class Meta:
        model = Encaminhar
        fields = ['UserProtocolo', 'protocoloEN']