from django.urls import path, include
from administrador import views

urlpatterns = [
    path('cadastro/secretaria', views.SecretariaCreate.as_view(), name="cadastro-sec"),
    path('editar/secretaria/<int:pk>', views.SecretariaUpdate.as_view(), name="editar-sec"),
    path('excluir/secretaria/<int:pk>', views.SecretariaDelete.as_view(), name="excluir-sec"),
    path('listar/presidente/', views.PesquisadorList.as_view(),name="pesqList"),
    path('editar/presidente/<int:pk>', views.PesquisadorUpdate.as_view(),name="pesqUpdate"),
    
]
