from django.shortcuts import render
from django.http import HttpResponse
from .models import Departamento
from .models import Municipio
from core.forms import UbicacionForm

# Create your views here.
"""
Filtrar Datos/
Iniciar Sesion/
Agregar Informacion/
"""
departamentos = Departamento.objects.all()
municipios = Municipio.objects.all()
def filtrar(request):
    form = UbicacionForm()
    if request.method == 'POST':
        form = UbicacionForm(request.POST)
        if form.is_valid():
            # Guardar los datos
            #url = reverse('home')
            return HttpResponseRedirect(url)
    return render(request, "core/filtrar.html",{'form':form})


def iniciar(request):
    return render(request, "core/iniciar.html")


def agregar(request):
    return render(request, "core/agregar.html")