from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from productos.models import Producto

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

def crear_prod(request): 
    return HttpResponse("crear producto")

def editar_prod(request): 
    return HttpResponse("editar producto")

def eliminar_prod(request):
    return HttpResponse("elimnar producto")