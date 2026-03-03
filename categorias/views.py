from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.core.paginator import Paginator
from categorias.models import Categoria
from categorias.forms import CategoriaForm
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def lista_categorias(request):
    #Inicializar consulta de clientes
    categorias_list = Categoria.objects.all().order_by('nombre')

    paginator = Paginator(categorias_list, 5)
    page_number = request.GET.get('page')
    categorias = paginator.get_page(page_number)

    context = {
        'categorias': categorias
    }
    return render(request, 'listar_cat.html', context)

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'crear_cat.html'
    success_url = reverse_lazy('lista_categorias')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'crear_cat.html' 
    success_url = reverse_lazy('lista_categorias')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('lista_categorias')

