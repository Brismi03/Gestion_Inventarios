from django.urls import path
from categorias.views import lista_categorias, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView
urlpatterns = [
    path('listar', lista_categorias, name='lista_categorias'),
    path('crear', CategoriaCreateView.as_view(), name="crear_categoria"),
    path('editar/<int:pk>/', CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='eliminar_categoria')
]