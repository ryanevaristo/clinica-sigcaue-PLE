from django.urls import path, include
from Pesquisador import views

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


    path('cadastrar/bioterio/', views.BioterioCreate.as_view(), name="cadastrar-bioterio"),
    path('editar/bioterio/<int:pk>/', views.BioterioUpdate.as_view(), name="editar-bioterio"),   
    path('excluir/bioterio/<int:pk>/', views.BioterioDelete.as_view(), name="excluir-bioterio"),
    path('lista/bioterio/', views.BioterioList.as_view(), name="lista-bioterio"),

    path('listar/encaminhar/aprovado',views.EncaminharAPList.as_view(), name="listarAP"),

    path('criar/parecer/', views.ParecerCreate.as_view(), name='parecer'),
    path('edita/parecer/<int:pk>/', views.ParecerUpdate.as_view(), name='EditarParecer'),    
    path('lista/parecer/', views.ParecerList.as_view(), name='ListaParecer'),
]
