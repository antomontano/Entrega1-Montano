from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('datos/', datos, name= 'datos'),
    path('carreras', carreras, name= 'carreras'),
    path('cursos/', cursos, name= 'cursos'),
    path('noalumno/', noalumno, name= 'noalumno'),
    
]