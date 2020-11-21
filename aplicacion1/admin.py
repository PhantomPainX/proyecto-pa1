from django.contrib import admin
from aplicacion1.models import *
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display=['user','nombre','apellido','email']

class VendedorAdmin(admin.ModelAdmin):
    list_display=['user','nombre','apellido','email']

class CategoriaAdmin(admin.ModelAdmin):
    list_display=['id','nombre']

class ArticuloAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','stock','categorias']

class DetalleAdmin(admin.ModelAdmin):
    list_display=['articulos','cantidad','boletas']


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Vendedor,VendedorAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Detalle,DetalleAdmin)
admin.site.register(Boleta)
