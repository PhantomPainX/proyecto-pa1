from django import forms
from aplicacion1.models import Cliente

class ClienteForm(forms.ModelForm): 
  
    class Meta: 
        model = Cliente
        fields = ['avatar'] 