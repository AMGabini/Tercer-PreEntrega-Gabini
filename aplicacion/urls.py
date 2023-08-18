
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = "menu"),
    path('recetas/', recetas, name = "recetas"),
    path('clientes/', clientes, name = "clientes"),
    path('empleados/', empleados, name = "empleados"),
    
    path('receta_form/', recetaForm, name = "receta_form"),
    path('receta_form2/', recetaForm2, name = "receta_form2"),
    
    path('empleado_form/', empleadoForm, name = "empleado_form"),
    
    path('cliente_form/', clienteForm, name = "cliente_form"),
       
    path('buscar_cliente/', buscarCliente, name = "buscar_cliente"),
    path('buscar2/', buscar2, name = "buscar2"),
]
