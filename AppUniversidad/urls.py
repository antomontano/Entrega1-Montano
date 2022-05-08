from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('datos/', datos),
    path('carreras', carreras),
    path('cursos/', cursos),
    
]