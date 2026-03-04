from django.shortcuts import render, HttpResponse
from inventario.forms import MovimientoInventarioForm
from inventario.models import MovimientoInventario
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_movimientos (request):
    movimientos_list = MovimientoInventario.objects.all()
    paginator = Paginator(movimientos_list, 5)
    page_number = request.GET.get('page')
    movimientos = paginator.get_page(page_number)

    context = {
        'movimientos': movimientos
    }
    return render(request, 'inventario.html', context)

class EntradaInventarioCreateView(LoginRequiredMixin, CreateView):
    model = MovimientoInventario
    form_class = MovimientoInventarioForm
    template_name = 'inventario_form.html'
    success_url = reverse_lazy('listar_inventario')
    def get_initial(self):
        return {'tipo': 'entrada'}

    def form_valid(self, form):
        movimiento = form.save(commit=False)
        movimiento.usuario = self.request.user
        movimiento.tipo = 'entrada'

        producto = movimiento.producto

        with transaction.atomic():
            producto.stock_actual += movimiento.cantidad
            producto.save()
            movimiento.save()

        return super().form_valid(form)
    
class SalidaInventarioCreateView(LoginRequiredMixin, CreateView): 
    model = MovimientoInventario
    form_class = MovimientoInventarioForm
    template_name = 'inventario_form.html'
    success_url = reverse_lazy('listar_inventario')
    def get_initial(self):
        return {'tipo': 'ealida'}
    
    def form_valid(self, form):
        movimiento = form.save(commit=False)
        movimiento.usuario = self.request.user
        movimiento.tipo = 'salida'

        producto = movimiento.producto

        if movimiento.cantidad > producto.stock_actual:
            form.add_error('cantidad', 'Stock insuficiente.')
            return self.form_invalid(form)

        with transaction.atomic():
            producto.stock_actual -= movimiento.cantidad
            producto.save()
            movimiento.save()

        return super().form_valid(form)
