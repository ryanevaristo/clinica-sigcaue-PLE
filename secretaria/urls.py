from django.urls import path, include
from secretaria import views

urlpatterns = [
    path('listar/pesquisador/', views.PesquisadorList.as_view(), name="lista-pesq"),
    path('editar/pesquisador/<int:pk>', views.PesquisadorUpdate.as_view(), name="update-pesq"),
    
]
