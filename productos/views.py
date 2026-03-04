from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from productos.models import Producto
from django.views.generic import CreateView, UpdateView, DeleteView
from productos.forms import ProductoForm
from django.urls import reverse_lazy

# Create your views here.
def lista_prod (request): 
    producto_list = Producto.objects.all()

    paginator = Paginator(producto_list, 5)
    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)
    context = {
        'productos' : productos
    }
    return render(request, 'listar_prod.html', context)

class ProductCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'crear_prod.html'
    success_url = reverse_lazy('lista_prod')

class ProductUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'crear_prod.html'
    success_url = reverse_lazy('lista_prod')

def eliminar_prod(request):
    return HttpResponse("elimnar producto")