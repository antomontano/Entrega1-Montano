from django import forms


class CarrerasFormulario(forms.Form):
    Facultad= forms.CharField(max_length=50)
    NombreCarrera= forms.CharField(max_length=50)