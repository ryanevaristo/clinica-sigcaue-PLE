from django.contrib import admin
from .models import Protocolo
from .models import Bioterio

@admin.register(Protocolo)
class ProtocoloAdmin(admin.ModelAdmin):
    list_display = ['titulo_protocolo', 'justificativa','quantidade','data_inicio','data_termino']
    list_filter = ['titulo_protocolo']

@admin.register(Bioterio)
class BioterioAdmin(admin.ModelAdmin):
    list_display = ['nome_bioterio', 'cnpj', 'rua', 'numero', 'bairro', 'cidade', 'estado']
    list_filter = ['nome_bioterio']
