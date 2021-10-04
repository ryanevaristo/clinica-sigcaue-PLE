from django.urls import path, include
from administrador import views

urlpatterns = [

    path('dashboard-adm/',views.index, name="index-adm"),
    path('cadastro/secretaria', views.SecretariaCreate.as_view(), name="cadastro-sec"),
    
]
