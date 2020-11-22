from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('hacerpedido/', hacerpedido, name = 'hacerpedido'),
    path('cuenta/', cuenta, name = 'cuenta'),
    path('cuenta/editarperfil/', editar_perfil, name = 'editarperfil'),
    path('cuenta/eliminarcuenta/', eliminar_cuenta, name = 'eliminarcuenta'),
    path('subirimagen/', subir_imagen),
    path('subido/', subido, name = 'subido'),
    path('cliente_images', display_cliente_images, name = 'cliente_images'),
]

