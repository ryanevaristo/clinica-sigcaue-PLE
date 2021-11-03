from django.contrib import admin
from .models import Protocolo, User

from django.contrib.auth import admin as auth_admin

from Pesquisador.forms import PesquisadorForm, PesquisadorChangeForm

@admin.register(Protocolo)
class ProtocoloAdmin(admin.ModelAdmin):
    list_display = ['justificativa', 'bioterio','quantidade','data_inicio','data_termino']
    list_filter = ['bioterio']

        


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = PesquisadorChangeForm
    add_form = PesquisadorForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields": ("idade","cpf","universidade",)}),
    )