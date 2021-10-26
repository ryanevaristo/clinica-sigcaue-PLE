from django.urls import path, include
from usuario import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('login/submit', views.login_submit, name='submit'),
    path('',views.index, name="index"),
    path('registrar/', views.UserCreate.as_view(), name='registrar'),
    path('logout/', views.logout_user,name="logout"),
    path('cadastrar/protocolo/', views.ProtocoloCreate.as_view(), name="cadastrar-protocolo"),
    path('editar/protocolo/<int:pk>/', views.ProtocoloUpdate.as_view(), name="editar-protocolo"),
    path('excluir/protocolo/<int:pk>/', views.ProtocoloDelete.as_view(), name="excluir-protocolo"),
    path('lista/protocolo/', views.ProtocoloList.as_view(), name="lista-protocolo"),
    
]
