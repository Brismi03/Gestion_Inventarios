from django import forms
from productos.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'sku', 'descripcion', 'precio', 'unidad_medida', 'stock_minimo', 'activo','categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sku'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Precio','step': '0.01'}),
            'unidad_medida': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej. pieza, kg, litro'}),
            'stock_minimo': forms.NumberInput(attrs={'class': 'form-control','min': '0'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'activo': forms.RadioSelect(choices=[
                (True, 'Sí'),
                (False, 'No')
            ])
        }
        labels = {
            'nombre': 'Nombre del producto',
            'sku': 'Código SKU del producto',
            'descripcion': 'Descripción del producto',
            'precio': 'Precio $',
            'unidad_medida': 'Unidad de Medida',
            'stok_minimo': 'Stock minímo del producto',
            'categoria': 'Categoria del producto',
            'activo': '¿El producto esta activo?'
        }