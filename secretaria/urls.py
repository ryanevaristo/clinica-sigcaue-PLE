from django.urls import path, include
from secretaria import views

urlpatterns = [
    path('listar/pesquisador/', views.PesquisadorList.as_view(), name="lista-pesq"),
    path('editar/pesquisador/<int:pk>', views.PesquisadorUpdate.as_view(), name="update-pesq"),
    path('listar/protocolo-pendente/', views.ProtocolPendList.as_view(), name="protocolo-pendente"),
    path('listar/protocolo-aprovado/', views.ProtocolAprovList.as_view(), name="protocolo-aprovado"),
    #ENCAMINHAR PENDENTE
    path('create/encaminhar/', views.EncaminharCreate.as_view(), name="encaminhar"),
    path('listar/encaminhar/',views.EncaminharList.as_view(), name="listar1"),
    #APROVADO
    path('create/encaminhar/aprovado', views.EncaminharAPCreate.as_view(), name="encaminharAP"),
]
