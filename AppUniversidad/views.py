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
    return HttpResponse("Datos")

def carreras(request):
    return HttpResponse("Carreras")

def cursos(request):
    return HttpResponse("Cursos")

def noalumno(request):
    return render(request,'AppUniversidad/NoAlumno.html')