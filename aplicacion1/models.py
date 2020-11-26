from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    direccion = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='cuenta/', default='cuenta/default.jpg', blank=True, null=True)

    def nombre(self):
        return self.user.first_name
    def apellido(self):
        return self.user.last_name
    def email(self):
        return self.user.email
    
    def __str__(self):
        return self.user.username

class Vendedor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    direccion=models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='cuenta/', default='cuenta/default.jpg',blank=True, null=True)

    def nombre(self):
        return self.user.first_name
    def apellido(self):
        return self.user.last_name
    def email(self):
        return self.user.email
    def __str__(self):
        return self.user.username


class Categoria(models.Model):

    nombre=models.CharField(max_length=32)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):

    nombre=models.CharField(max_length=32)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio=models.BigIntegerField()
    stock=models.IntegerField()

    def __str__(self):
        return self.nombre

    def categorias(self):
        return self.categoria.nombre

class Boleta(models.Model):

    vendedor=models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha=models.DateField()
    total=models.BigIntegerField()

    def __str__(self):
        return "%s | %s"%(self.cliente,self.fecha)
    def vendedors(self):
        return self.vendedor.nombre
    def clientes(self):
        return self.cliente.nombre

class Pedido(models.Model):

    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    completado = models.BooleanField(default=False)
    cantidad=models.IntegerField()
    
    def __str__(self):
        return "%s | %s | %d" %(self.cliente,self.articulo,self.cantidad)
    def clientes(self):
        return self.cliente.user.username
    def articulos(self):
        return self.articulo.nombre

class Detalle(models.Model):

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, default=0)
    boleta=models.ForeignKey(Boleta, on_delete=models.CASCADE)

    def pedidos(self):
        return self.pedido.id
    def boletas(self):
        return self.boleta.id

