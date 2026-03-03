from django import forms 
from categorias.models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta: 
        model = Categoria
        fields = ['nombre', 'descripcion', 'activa']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Descripción', 'rows':3}),
            'activa': forms.RadioSelect(choices=[
                (True, 'Sí'),
                (False, 'No')
            ])
        }
        labels = {
            'nombre': 'Nombre de la categoria',
            'descripcion': 'Descripción',
            'activa': '¿La categoría se encuentra activa?'

        }