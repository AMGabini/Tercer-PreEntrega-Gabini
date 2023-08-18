from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def recetas(request):
    contexto = {'Receta': Receta.objects.all(),'titulo': 'Recetas'}
    return render(request, "aplicacion/recetas.html", contexto)

def clientes(request):
    contexto = {'Cliente': Cliente.objects.all(), 'titulo': 'Listado de Clientes'}
    return render(request, "aplicacion/clientes.html", contexto)

def empleados(request):
    contexto = {'Empleado': Empleado.objects.all(), 'titulo': 'Listado de Empleados'}
    return render(request, "aplicacion/empleados.html", contexto)






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

def clienteForm(request):
    if request.method == "POST":
        cliente = Cliente(nombre=request.POST['nombre'],
                          email=request.POST['email'],
                          telefono=request.POST['telefono'],
                          direccion=request.POST['direccion'])
        cliente.save()
        return HttpResponse("Se grabo con exito el cliente!")
    
    return render(request, "aplicacion/clienteForm.html")

def empleadoForm(request):
    if request.method == "POST":
        empleado = Empleado(nombre=request.POST['nombre'],
                            puesto=request.POST['puesto'],
                            salario=request.POST['salario'],
                            fecha_contratacion=request.POST['fecha_contratacion'])
        empleado.save()
        return HttpResponse("Se grabo con exito el empleado!")
    
    return render(request, "aplicacion/empleadoForm.html")




def buscarCliente(request):
    return render(request, "aplicacion/buscarCliente.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        clientes = Cliente.objects.filter(nombre__icontains=patron)
        contexto = {'clientes': clientes} 
        return render(request, "aplicacion/clientes.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")