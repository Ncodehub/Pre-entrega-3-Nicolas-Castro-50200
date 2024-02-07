from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('repuestos/', repuestos, name="repuestos"),
    path('maquina/', maquina, name="maquina"),
    path('proveedor/', proveedores, name="proveedores"),

    #
    path('repuestos_form/', repuestosForm, name="repuestos_form"),
    path('maquina_form/', maquinaForm, name="maquina_form"),
    path('provee_form/', proveedoresForm, name="provee_form"),

    path('buscar/', buscar, name="buscar"),
    path('buscarRepuestos/', buscarRepuestos, name="buscarRepuestos"),
]