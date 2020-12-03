from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name= 'home'),
    path('hacerpedido/', hacerpedido, name = 'hacerpedido'),
    path('cuenta/', cuenta, name = 'cuenta'),
    path('cuenta/editarperfil/', editar_perfil, name = 'editarperfil'),
    path('cuenta/eliminarcuenta/', eliminar_cuenta, name = 'eliminarcuenta'),
    path('registro/', registrar, name="registrar"),
    path('ver_pedidos/',ver_pedidos, name="verpedidos")
]

