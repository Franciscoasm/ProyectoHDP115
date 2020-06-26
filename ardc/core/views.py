from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
Filtrar Datos/
Agregar Informacion/
Iniciar Sesion/
"""
def filtrar(request):
    return render(request, "core/filtrar.html")

def iniciar(request):
    return render(request, "core/iniciar.html")