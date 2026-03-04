from django.urls import path
from inventario.views import list_movimientos, EntradaInventarioCreateView, SalidaInventarioCreateView

urlpatterns = [
    path('listar', list_movimientos, name='listar_inventario'),
    path('entrada', EntradaInventarioCreateView.as_view(), name='entrada_inventario'),
    path('salida', SalidaInventarioCreateView.as_view(), name='salida_inventario' )
]