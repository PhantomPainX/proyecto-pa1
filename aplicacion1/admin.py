from django.contrib import admin
from aplicacion1.models import *
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display=['id','user','nombre','apellido','email']

class VendedorAdmin(admin.ModelAdmin):
    list_display=['id','user','nombre','apellido','email']

class CategoriaAdmin(admin.ModelAdmin):
    list_display=['id','nombre']

class ArticuloAdmin(admin.ModelAdmin):
    list_display=['id','nombre','precio','stock','categorias']

class DetalleAdmin(admin.ModelAdmin):
    list_display=['id','boletas','pedidos']

class PedidoAdmin(admin.ModelAdmin):
    
    list_display=['id','clientes','articulos','completado','cantidad']

class BoletaAdmin(admin.ModelAdmin):
    
    list_display=['id','vendedors','clientes','fecha','total']


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Vendedor,VendedorAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Detalle,DetalleAdmin)
admin.site.register(Boleta, BoletaAdmin)
admin.site.register(Pedido,PedidoAdmin)
