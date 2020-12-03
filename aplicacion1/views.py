from .models import Cliente
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):

    return render(request, "home.html")


@login_required
def cuenta(request):
    
    try:
        usuario = request.user

        cliente = request.user.cliente

        return render(request,"cuenta_cliente.html", {"usuario":usuario, "cliente":cliente})

    except:

        usuario = request.user

        return render(request,"cuenta_admin.html", {"usuario":usuario})
  
@login_required
def subido(request): 
    return HttpResponse('successfully uploaded') 

@login_required
def eliminar_cuenta(request):

    usuario = request.user
    username = usuario.username
    cliente= User.objects.get(username=username)

    cliente.delete()

    return redirect(to= "home")

@login_required
def editar_perfil(request):

    usuario = request.user
    username1 = usuario.username
    usercliente= User.objects.get(username=username1)

    cliente1 = request.user.cliente
    username2 = cliente1.user
    clienteuser = Cliente.objects.get(user=username2)

    data ={
        'form': EditarUsuarioForm(instance=usercliente),
        'form2': EditarClienteForm(instance=clienteuser)
    }
    if request.method =="POST":
        formulario1 = EditarUsuarioForm(data=request.POST, instance= usercliente)
        formulario2 = EditarClienteForm(request.POST, request.FILES,instance= clienteuser)
        if formulario1.is_valid() and formulario2.is_valid():
            formulario1.save()
            formulario2.save()
            data['mensaje']= "Modificado Correctamente"
            data['form']= formulario1
            data['form2']= formulario2

    return render(request, "editar_perfil.html", data)

@login_required
def hacerpedido(request):
    if request.method=="POST":
        form = PedidoForm(request.POST)

        if form.is_valid:

            instance = form.save(commit=False)
            instance.cliente = request.user.cliente
            instance.completado = False

            Articuloz = instance.articulo
            stockart = Articuloz.stock

            clientea = request.user.cliente

            instanceall = Pedido.objects.filter(cliente=clientea)
            articuloall = Articulo.objects.all()
            total=0

            diccionario = {
                "articulo":Articuloz,
                "current":instance,
                "Pedidoall":instanceall,
                "art":articuloall,
                "total":total
                
            }

            if instance.cantidad > stockart or instance.cantidad <= 0:
                return render(request, "pedido_erroneo.html", diccionario)
            else:
                instance.save()
                for x in instanceall:
                    for y in articuloall:   
                        if  x.articulo_id == y.id:
                            total= total+x.cantidad*y.precio
                diccionario = {
                "articulo":Articuloz,
                "current":instance,
                "Pedidoall":instanceall,
                "art":articuloall,
                "total":total
                
            }
                return render(request, "ver_pedidos.html",diccionario)             

    else:
        form=PedidoForm()
        return render(request, "hacer_pedido.html", {"form":form})

@login_required
def ver_pedidos(request):

    mensaje = " "
    if request.method=="POST":

        dato = request.POST['prd']
        iddato=Pedido.objects.filter(id__contains=dato)

        if iddato:

            mensaje = "El pedido con el ID '%s' ha sido eliminado" %dato
            iddato.delete()

        else:

            mensaje = "Usted ingreso la ID '%s', que no se encuentra en el carro"  %dato

    diccionario = {
        "mensaje":mensaje     
    }

    clientea = request.user.cliente

    instanceall = Pedido.objects.filter(cliente=clientea)
    articuloall = Articulo.objects.all()
    total=0

    for x in instanceall:
        for y in articuloall:   
            if  x.articulo_id == y.id:
                total= total+x.cantidad*y.precio

    diccionario = {
        "Pedidoall":instanceall,
        "art":articuloall,
        "total":total,
        "mensaje":mensaje
    }
    
    return render(request, "ver_pedidos.html",diccionario) 
    




























def registrar(request):
    data = {
        'form':registroForm()
    }
    if request.method =="POST":
        formulario=registroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado exitosamente"       

    return render(request, 'registrar.html', data)
