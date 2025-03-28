from django.contrib import admin
from django.urls import path,include
from . import views 
from .views import AddressView

urlpatterns = [
    path('', views.inicio_sesion, name='inicio_sesion'), 
    path('inicio', views.inicio_sesion, name='inicio_sesion'), 
    path('index', views.index, name='index'),   
    path('datos', views.datos, name='datos'), 
    path('tienda', views.tienda, name='tienda'),
    path('clp_to_usd/', views.clp_to_usd_view, name='clp_to_usd_view'),   
    path('calculadora', views.calcular, name='calculadora'), 
    path('contacto', views.contacto, name='contacto'), 
    path('direccion', views.direccion, name='direccion'), 
    path('cuenta', views.cuenta, name='cuenta'), 
    path('ingresar', views.ingresar, name='ingresar'),
    path('puntos', AddressView.as_view(), name='puntos'), 
    path('tutoriales', views.tutoriales, name='tutoriales'),    
    path('detalle/<int:order_id>', views.detalle_pedido, name='detalle_pedido'), 
    path('vendedor', views.vendedor, name='vendedor'), 
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('bodegero', views.bodegero, name='bodegero'),  # Agrega esta línea
    path('detalleb/<int:order_id>', views.detalle_bodega, name='detalle_bodega'),
    path('admin', views.admin, name='admin'),
    path('contador', views.contador, name='contador'),
    path('crear_cuenta', views.crear_cuenta, name='crear_cuenta'),
    path('recuperar_cuenta', views.recuperar_cuenta, name='recuperar_cuenta'),
]
