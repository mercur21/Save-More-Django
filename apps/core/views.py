from django.shortcuts import render, get_list_or_404, redirect
import folium

# Create your views here.
def index(request):
    return render(request, 'core/index.html')