from django.contrib import admin
from .models import Encaminhar


# Register your models here.

@admin.register(Encaminhar)
class EncaminharAdmin(admin.ModelAdmin):
    list_display = ['UserProtocolo']
    list_filter = ['UserProtocolo']


    