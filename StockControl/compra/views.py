from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404 
from .models import Proveedor, Producto


# Create your views here.

# proveedor------------------------
def crear_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')

        proveedor = Proveedor.objects.create(
            nombre=nombre,
            apellido=apellido,
            dni=dni
        )
        return redirect('proveedores_list')
    else:
        return render(request, 'proveedores_list.html', {'proveedor':proveedor})

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores_list.html', {'proveedores': proveedores})



def modificar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.apellido = request.POST.get('apellido')
        proveedor.dni = request.POST.get('dni')
        proveedor.save()
        return redirect('proveedores_list')  
    
    return render(request, 'editar_proveedor.html', {'proveedor': proveedor})

""" def mostrar_datos_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedores_list.html', {'proveedor': proveedor})
 """
def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.delete()
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores_list.html', {'proveedores': proveedores})


#producto----------------------

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock_actual = request.POST.get('stock')
        proveedor_nombre = request.POST.get('proveedor')

        # Verificar si el proveedor existe en la base de datos
        proveedor = Proveedor.objects.filter(nombre=proveedor_nombre).first()
        if not proveedor:
           return render(request, 'productos_list.html', {'error_message': 'El proveedor no existe'})

        try:
            producto = Producto.objects.create(
                nombre=nombre,
                precio=float(precio),
                stock_actual=int(stock_actual),
                proveedor=proveedor
            )
            return redirect('productos_list')
        except Exception as e:
            print(e)
            return redirect('productos_list')
    else:
        return render(request, 'productos_list.html')
    

def listar_productos(request):
    productos = Producto.objects.all().order_by('pk')
    return render(request, 'productos_list.html', {'productos': productos})

def modificar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.stock_actual = request.POST.get('stock_actual')
        
        proveedor_nombre = request.POST.get('proveedor')
        proveedor = Proveedor.objects.filter(nombre=proveedor_nombre).first()

        if not proveedor:
            return render(request, 'editar_producto.html', {'producto': producto, 'error_message': 'El proveedor no existe'})
        else:
            producto.proveedor = proveedor

        producto.save()
        return redirect('productos_list')
    else:
        return render(request, 'editar_producto.html', {'producto': producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()

    productos = Producto.objects.all()
    return render(request, 'productos_list.html', {'productos': productos})
