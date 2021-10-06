from django.contrib import admin
from .models import Protocolo

@admin.register(Protocolo)
class ProtocoloAdmin(admin.ModelAdmin):
    list_display = ['justificativa', 'bioterio','quantidade','data_inicio','data_termino']
    list_filter = ['bioterio']

        
