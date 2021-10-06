from django.urls import path, include
from usuario import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('login/submit', views.login_submit, name='submit'),
    path('',views.index, name="index"),
    path('registrar/', views.UserCreate.as_view(), name='registrar'),
    path('logout/', views.logout,name="logout"),
    path('cadastrar/protocolo/', views.ProtocoloCreate.as_view(), name="Protocolo-create")
    
]
