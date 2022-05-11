from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppUniversidad.forms import *
# Create your views here.

def dato(self):
    dato= Datos(Nombre="Camila", Apellido= "Serrano", DNI= 4155698)
    dato.save()
    texto= f"Nombre: {dato.Nombre}, Apellido: {dato.Apellido}, DNI: {dato.DNI}"
    return HttpResponse(texto)

def inicio(request):
    return render(request,'AppUniversidad/inicio.html')

def carreras(request):

    if request.method == 'POST':
        miformulario=CarrerasFormulario(request.POST)

        if miformulario.is_valid():
            informacion=miformulario.cleaned_data
            carrera=Carrera(Facultad=informacion['Facultad'], NombreCarrera=informacion['NombreCarrera'] )
            carrera.save()
            return render(request,'AppUniversidad/cursos.html')
        
    else:
        miformulario=CarrerasFormulario()
    return render(request, 'AppUniversidad/carreras.html', {'formulario':miformulario})


def cursos(request):
    if request.method == 'POST':
        miformulario2=CursosFormulario(request.POST)

        if miformulario2.is_valid():
            informacion2=miformulario2.cleaned_data
            curso=Curso(Año=informacion2['Año'], Turno=informacion2['Turno'])
            curso.save()
            return render(request, 'AppUniversidad/datos.html')

    else:
        miformulario2=CursosFormulario()
    return render(request, 'AppUniversidad/cursos.html', {'formulario2': miformulario2})


def datos(request):
    if request.method == 'POST':
        miformulario3=DatosFormulario(request.POST)

        if miformulario3.is_valid():
            informacion3=miformulario3.cleaned_data
            dato=Datos(Nombre=informacion3['Nombre'], Apellido=informacion3['Apellido'], DNI=informacion3['DNI'])
            dato.save()
            return render(request, 'AppUniversidad/inscripcioncompleta.html')

    else:
        miformulario3=DatosFormulario()
    return render(request, 'AppUniversidad/datos.html', {'formulario3': miformulario3})

def noalumno(request):
    return render(request,'AppUniversidad/NoAlumno.html')

def inscripcioncompleta(request):
    return render(request,'AppUniversidad/inscripcioncompleta.html')

def busquedaApellidos(request):
    return render(request, 'AppUniversidad/busquedaApellidos.html')

def buscar(request):
    if request.GET['Apellido']:
        Apellido=request.GET['Apellido']
        datos=Datos.objects.filter(Apellido=Apellido)
        return render(request, 'AppUniversidad/resultados.html', {'datos':datos, 'Apellido':Apellido})
    
    else:
        respuesta="No se ingresó apellido"
        return HttpResponse(respuesta)

