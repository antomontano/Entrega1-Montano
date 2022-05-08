from django.db import models

# Create your models here.

class Datos(models.Model):
    Nombre= models.CharField(max_length=50)
    Apellido= models.CharField(max_length=50)
    DNI= models.IntegerField()

class Carrera(models.Model):
    Facultad= models.CharField(max_length=50)
    Carrera= models.CharField(max_length=50)

class Curso(models.Model):
    Año= models.IntegerField()
    Turno= models.CharField(max_length=50)