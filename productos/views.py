from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from productos.models import Producto
from django.views.generic import CreateView, UpdateView, DeleteView
from productos.forms import ProductoForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def lista_prod (request): 
    producto_list = Producto.objects.all()

    paginator = Paginator(producto_list, 5)
    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)
    context = {
        'productos' : productos
    }
    return render(request, 'listar_prod.html', context)

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'crear_prod.html'
    success_url = reverse_lazy('lista_prod')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'crear_prod.html'
    success_url = reverse_lazy('lista_prod')

def eliminar_prod(request):
    return HttpResponse("elimnar producto")