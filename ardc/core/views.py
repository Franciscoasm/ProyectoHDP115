from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
Filtrar Datos/
Agregar Informacion/
Iniciar Sesion/
"""
def filtrar(request):
    return HttpResponse("Filtrar Datos")

def agregar(request):
    return HttpResponse("Agregar Informacion")

def iniciar(request):
    return HttpResponse("Iniciar Sesion")