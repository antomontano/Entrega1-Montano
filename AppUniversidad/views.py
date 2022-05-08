from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def datos(self):
    datos= Datos(Nombre="Camila", Apellido= "Serrano", DNI= 4155698)
    datos.save()
    texto= f"Nombre: {datos.Nombre}, Apellido: {datos.Apellido}, DNI: {datos.DNI}"
    return HttpResponse(texto)