from django import forms
from .models import *

class RecetaForm(forms.Form):
    titulo = forms.CharField(max_length=100, required=True)
    ingredientes = forms.CharField(widget=forms.Textarea, required=True)
    instrucciones = forms.CharField(widget=forms.Textarea, required=True)
    tiempo_preparacion = forms.IntegerField(required=True)
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion']
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'puesto', 'salario', 'fecha_contratacion']