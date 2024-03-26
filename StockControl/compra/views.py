from django.shortcuts import render, redirect, get_object_or_404, request 
from .models import Proveedor


# Create your views here.

def crear_proveedor(render):
    if request.method == 'POST':
        pass

def listar_proveedores(render):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores.html', {'proveedores': proveedores})

def modificar_proveedor(render, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        pass

def datos_proveedor(render, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedor.html', {'proveedor': proveedor})

def elimar_proveedor(render, pk):
    proveedor = get_object_or_404(Proveedor, pk)


