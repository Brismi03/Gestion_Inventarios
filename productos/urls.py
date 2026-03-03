from django.urls import path
from productos.views import lista_prod, crear_prod, editar_prod, eliminar_prod

urlpatterns = [
    path('listar', lista_prod, name='lista_prod'), 
    path('crear', crear_prod, name='crear_prod'),
    path('editar', editar_prod, name='editar_prod'),
    path('eliminar', eliminar_prod, name='eliminar_prod')
]
