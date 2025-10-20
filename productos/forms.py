from django import forms
from .models import Producto  
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto 
        fields = ['nombre', 'precio', 'detalle', 'id_categoria', 'id_proveedor']
        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'detalle': 'Detalle',
            'id_categoria': 'Id Categoria',
            'id_proveedor': 'Id Proveedor',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'detalle': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'id_categoria': forms.Select(attrs={'class': 'form-control'}),
            'id_proveedor': forms.Select(attrs={'class': 'form-control'}),
        }
