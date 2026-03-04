from django.urls import path
from productos.views import lista_prod, ProductCreateView, ProductUpdateView, eliminar_producto

urlpatterns = [
    path('listar', lista_prod, name='lista_prod'), 
    path('crear', ProductCreateView.as_view(), name='crear_prod'),
    path('editar/<int:pk>/', ProductUpdateView.as_view(), name='editar_prod'),
    path('eliminar/<int:id>/', eliminar_producto, name='eliminar_prod')
]
