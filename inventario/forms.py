from django import forms 
from .models import MovimientoInventario, Producto

class MovimientoInventarioForm(forms.ModelForm): 
    class Meta: 
        model = MovimientoInventario
        fields = ['producto', 'cantidad', 'nota']

        widgets ={
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'nota': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }

        labels = {
            'producto': 'Selecciona un producto',
            'cantidad': 'Cantidad',
            'nota': 'Nota'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Solo productos activos
        self.fields['producto'].queryset = Producto.objects.filter(activo=True)