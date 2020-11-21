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
def operaciones(request):

    return render(request, "crud.html")

@login_required
def crear(request):

    return HttpResponse('bien hecho')

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

def eliminar_cuenta(request):

    return render(request, "eliminar_cuenta.html")


def editar_perfil(request):

    return render(request, "editar_perfil.html")