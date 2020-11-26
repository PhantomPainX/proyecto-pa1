from django import forms
from aplicacion1.models import *

class ClienteForm(forms.ModelForm): 
  
    class Meta: 
        model = Cliente
        fields = ['avatar']


class PedidoForm(forms.ModelForm): 
  
    class Meta: 
        model = Pedido
        exclude = ('cliente','estado',)
        fields = ['articulo','cantidad'] 


class BoletaForm(forms.ModelForm):

    class Meta:
        model = Boleta
        exclude = ('vendedor',)
        fields = ['cliente',] 

    
        



