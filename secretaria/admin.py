from django.contrib import admin
from .forms import SecretariaForm
from .models import Protocolo
# Register your models here.

@admin.register(Protocolo)
class ProtocoloAdmin(admin.ModelAdmin):
    list_display = ['justificativa', 'bioterio','quantidade','data_inicio','data_termino']
    list_filter = ['bioterio']
    