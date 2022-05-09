from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def dato(self):
    dato= Datos(Nombre="Camila", Apellido= "Serrano", DNI= 4155698)
    dato.save()
    texto= f"Nombre: {dato.Nombre}, Apellido: {dato.Apellido}, DNI: {dato.DNI}"
    return HttpResponse(texto)

def inicio(request):
    return render(request,'AppUniversidad/inicio.html')

def datos(request):
    return render(request,'AppUniversidad/datos.html')

def carreras(request):

    if request.method == 'POST':
        carrera=Carrera(Facultad=request.post['facultad'], Carrera=request.post['carrera'] )
        carrera.save()
        return render(request,'AppUniversidad/cursos.html')

    return render(request,'AppUniversidad/carreras.html')

def cursos(request):
    return render(request,'AppUniversidad/cursos.html')

def noalumno(request):
    return render(request,'AppUniversidad/NoAlumno.html')
