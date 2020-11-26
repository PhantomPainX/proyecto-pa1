from .models import Cliente
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):

    return render(request, "home.html")


@login_required
def cuenta(request):
    
    usuario = request.user

    cliente = request.user.cliente

    return render(request,"cuenta.html", {"usuario":usuario, "cliente":cliente})


@login_required
def subir_imagen(request): 
  
    if request.method == 'POST': 
        form = ClienteForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('subido') 
    else: 
        form = ClienteForm() 
    return render(request, 'subirimg.html', {'form' : form}) 
  
@login_required
def subido(request): 
    return HttpResponse('successfully uploaded') 

@login_required
def display_cliente_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Image = Cliente.objects.all()
        return render(request, 'display_cliente_images.html', {'cliente_img' : Image}) 

@login_required
def eliminar_cuenta(request):

    return render(request, "eliminar_cuenta.html")

@login_required
def editar_perfil(request):

    return render(request, "editar_perfil.html")

def hacerpedido(request):
    if request.method=="POST":
        form = PedidoForm(request.POST)

        if form.is_valid:

            instance = form.save(commit=False)
            instance.cliente = request.user.cliente
            instance.completado = False

            Articulo = instance.articulo
            stockart = Articulo.stock

            diccionario = {
                "articulo":Articulo,
                "current":instance
            }

            if instance.cantidad > stockart or instance.cantidad <= 0:
                return render(request, "pedido_erroneo.html", diccionario)
            else:
                instance.save()
                return render(request, "pedido_completo.html",diccionario)
    else:
        form=PedidoForm()
        return render(request, "hacer_pedido.html", {"form":form})


def crearboleta(request):
    if request.method=="POST":  
        form = BoletaForm(request.POST)

        
        if form.is_valid:

            Cliente = Cliente.nombre

            instance = form.save(commit=False)
            instance.cliente = request.user.cliente

            diccionario = {
                "Nombre":Cliente,
            }
            
    return render(request, "boleta.html", {"form":form})