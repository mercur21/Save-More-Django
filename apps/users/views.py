from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
# from .models import User
import folium

# Create your views here.
def registro(request):
    return render(request, 'apps/users/registro.html')

def login(request):
    return render(request, 'apps/users/login.html')

def perfil(request):
    return render(request, 'apps/users/perfil.html')