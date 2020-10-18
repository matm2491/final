from django.shortcuts import render
from django.views.generic import ListView, DetailView 

#importamos los modelos
from .models import TinUsuarios
# Create your views here.

class listado(ListView):
    model = TinUsuarios

def inicio(request):

    return render(request, 'inicio.html')


