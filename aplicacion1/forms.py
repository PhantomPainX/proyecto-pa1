from django import forms
from aplicacion1.models import *
from django.forms import ModelForm

class ClienteForm(forms.ModelForm): 
  
    class Meta: 
        model = Cliente
        fields = ['avatar']


class PedidoForm(forms.ModelForm): 
  
    class Meta: 
        model = Pedido
        exclude = ('cliente','estado',)
        fields = ['articulo','cantidad']
      

class registroForm(forms.ModelForm):

    class Meta:
        model= User
        fields= ['username', 'first_name','last_name', 'email','password']

class EditarUsuarioForm(forms.ModelForm):

    class Meta:
        model= User
        fields= ['username', 'first_name','last_name', 'email']

class EditarClienteForm(forms.ModelForm):

    class Meta:
        model= Cliente
        fields= ['direccion', 'avatar']
    
        



