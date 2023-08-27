#_____IMPORTACIONES_____#

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

#_____Funcion_Home_____#

def home(request):
    return render(request, "aplicacion/home.html")

#_____Funciones_de_Recetas_____#

def recetas(request):
    contexto = {'Receta': Receta.objects.all(),'titulo': 'Recetas'}
    return render(request, "aplicacion/recetas.html", contexto)

def recetaForm(request):
    if request.method == "POST":
        receta = Receta(titulo=request.POST['titulo'],
                        ingredientes=request.POST['ingredientes'],
                        instrucciones=request.POST['instrucciones'],
                        tiempo_preparacion=request.POST['tiempo_preparacion'])
        receta.save()
        return HttpResponse("Se grabo con exito la receta!")
    
    return render(request, "aplicacion/recetaForm.html")

def recetaForm2(request):
    if request.method == "POST":
        miForm = RecetaForm(request.POST)
        if miForm.is_valid():
            receta_titulo= miForm.cleaned_data.get('titulo')
            receta_ingredientes = miForm.cleaned_data.get('ingredientes')
            receta_instrucciones = miForm.cleaned_data.get('instrucciones')
            receta_tiempo_preparacion = miForm.cleaned_data.get('tiempo_preparacion')
            receta = Receta(titulo=receta_titulo,
                            ingredientes=receta_ingredientes,
                            instrucciones=receta_instrucciones,
                            tiempo_preparacion=receta_tiempo_preparacion)
            receta.save()
            return render(request, "aplicacion/base.html")
    else: 
        miForm = RecetaForm() 
    
    return render(request, "aplicacion/recetaForm2.html", {"form": miForm})

#_____Funciones_de_Clientes:_Implementacion_CRUD_____#

def clientes(request):
    contexto = {'Cliente': Cliente.objects.all(), 'titulo': 'Listado de Clientes'}
    return render(request, "aplicacion/clientes.html", contexto)

def updateCliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.nombre = miForm.cleaned_data.get('nombre') 
            cliente.email = miForm.cleaned_data.get('email')
            cliente.telefono = miForm.cleaned_data.get('telefono')
            cliente.direccion = miForm.cleaned_data.get('direccion') 
            cliente.save()
            return redirect(reverse_lazy('clientes'))   
    else:
        miForm = ClienteForm(initial={
            'nombre': cliente.nombre,
            'email': cliente.email,
            'telefono': cliente.telefono,
            'direccion': cliente.direccion,
        })
    return render(request, "aplicacion/clienteForm.html", {'form': miForm})

def deleteCliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect(reverse_lazy('clientes'))

def createCliente(request):    
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            c_nombre = miForm.cleaned_data.get('nombre')
            c_email = miForm.cleaned_data.get('email')
            c_telefono = miForm.cleaned_data.get('telefono')
            c_direccion = miForm.cleaned_data.get('direccion')
            cliente = Cliente(nombre=c_nombre, 
                             email=c_email,
                             telefono=c_telefono,
                             direccion=c_direccion,
                             )
            cliente.save()
            return redirect(reverse_lazy('clientes'))
    else:
        miForm = ClienteForm()

    return render(request, "aplicacion/clienteForm.html", {"form":miForm})



#_____Funciones_de_eMPLEADOS:_Implementación_CBV_____#

class EmpleadoList(ListView):
    model = Empleado

class EmpleadoCreate(CreateView):
    model = Empleado
    fields = ['nombre', 'puesto', 'salario', 'fecha_contratacion']
    success_url = reverse_lazy('empleados')

class EmpleadoUpdate(UpdateView):
    model = Empleado
    fields = ['nombre', 'puesto', 'salario', 'fecha_contratacion']
    success_url = reverse_lazy('empleados')

class EmpleadoDelete(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')
    
#_____FIN_____#





