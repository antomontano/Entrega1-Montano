from django.db import models

# Create your models here.

class Datos(models.Model):
    Nombre= models.CharField(max_length=50)
    Apellido= models.CharField(max_length=50)
    DNI= models.IntegerField()
    
    def __str__(self):
        return self.Apellido+" "+self.Nombre+" "+str(self.DNI)

class Carrera(models.Model):
    Facultad= models.CharField(max_length=50)
    NombreCarrera= models.CharField(max_length=50)

    def __str__(self):
        return self.Facultad+" - "+self.NombreCarrera

class Curso(models.Model):
    Año= models.IntegerField()
    Turno= models.CharField(max_length=50)

    def __str__(self):
        return str(self.Año)+" "+self.Turno