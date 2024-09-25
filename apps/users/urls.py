from django.urls import path, include
from apps.users.views import registro, login, perfil

urlpatterns = [
    path("login", login, name='login'),
    path("registro", registro, name='registro'),
    path("perfil", perfil, name='perfil'),
]