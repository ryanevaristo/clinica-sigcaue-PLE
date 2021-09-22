from django.urls import path, include
from usuario import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('login/submit', views.login_submit, name='submit'),
    path('',views.index, name="index"),
    path('registrar/', views.UserCreate.as_view(), name='cadastro'),
    
]
