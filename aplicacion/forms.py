from django import forms
from .models import *

class RecetaForm(forms.Form):
    titulo = forms.CharField(max_length=100, required=True)
    ingredientes = forms.CharField(widget=forms.Textarea, required=True)
    instrucciones = forms.CharField(widget=forms.Textarea, required=True)
    tiempo_preparacion = forms.IntegerField(required=True)
           
class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, required=True)
    email = forms.EmailField(required=True)
    telefono = forms.IntegerField(label="Telefono", required=True)
    direccion = forms.CharField(label="Domicilio", max_length=500, required=True)
        
