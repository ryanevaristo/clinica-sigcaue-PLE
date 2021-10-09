from django.urls import path, include
from administrador import views

urlpatterns = [
    path('cadastro/secretaria', views.SecretariaCreate.as_view(), name="cadastro-sec"),
    
]
