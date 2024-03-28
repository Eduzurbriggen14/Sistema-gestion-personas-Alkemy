from django.urls import path
from .  import views

urlpatterns = [
    #producto urls
    path('', views.listar_productos, name= 'productos_list'),
    path('registrarProducto/', views.crear_producto, name='registrar_producto'),
    #path('modificarProducto/<int:pk>', views.modificar_producto, name='modificar_producto'),
    path('eliminarProducto/<int:pk>', views.eliminar_producto, name='eliminar_producto'),
    #provedor urls
    path('proveedores/', views.listar_proveedores, name='proveedores_list'),
    path('registrarProveedor/', views.crear_proveedor, name='registrar_proveedor'),
    path('modificarProveedor/<int:pk>', views.modificar_proveedor, name = 'modificar_proveedor'),
    path('eliminarProveedor/<int:pk>', views.eliminar_proveedor, name='eliminar_proveedor'),

    
    ]