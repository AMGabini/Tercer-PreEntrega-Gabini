
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = "menu"),
    
    path('recetas/', recetas, name = "recetas"),
    path('receta_form/', recetaForm, name = "receta_form"),
    path('receta_form2/', recetaForm2, name = "receta_form2"),
    
    path('clientes/', clientes, name = "clientes"),
    path('update_cliente/<id_cliente>/', updateCliente, name="update_cliente" ), 
    path('delete_cliente/<id_cliente>/', deleteCliente, name="delete_cliente" ),
    path('create_cliente/', createCliente, name="create_cliente" ),
    path('buscar_cliente/', buscarCliente, name = "buscar_cliente"),
    path('buscar2/', buscar2, name = "buscar2"),
    
    path('empleados/', EmpleadoList.as_view(), name="empleados" ),
    path('create_empleado/', EmpleadoCreate.as_view(), name="create_empleado" ),    
    path('update_empleado/<int:pk>/', EmpleadoUpdate.as_view(), name="update_empleado" ),
    path('delete_empleado/<int:pk>/', EmpleadoDelete.as_view(), name="delete_empleado" ),
]
