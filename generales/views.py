from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
import json
from  productos.models import Producto 
from inventario.models import MovimientoInventario
from categorias.models import Categoria
from django.db.models import Sum
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.
def home (request):

    hoy = timezone.now().date()
     # Filtro por categoría
    categoria_id = request.GET.get("categoria")
    productos = Producto.objects.all()

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    # Totales de hoy
    total_entradas = MovimientoInventario.objects.filter(
        tipo='entrada',
        fecha__date=hoy
    ).aggregate(total=Sum('cantidad'))['total'] or 0

    total_salidas = MovimientoInventario.objects.filter(
        tipo='salida',
        fecha__date=hoy
    ).aggregate(total=Sum('cantidad'))['total'] or 0

    # Paginación
    paginator = Paginator(productos, 5)
    page = request.GET.get("page")
    productos = paginator.get_page(page)

    categorias = Categoria.objects.all()

    context = {
        "productos": productos,
        "categorias": categorias,
        "total_entradas": total_entradas,
        "total_salidas": total_salidas,
        "fecha_actual": hoy
    }

    return render(request, "home.html", context)



def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 🔐 Crear sesión clásica
            login(request, user)

            # 🔑 Generar JWT
            refresh = RefreshToken.for_user(user)

            return JsonResponse({
                "success": True,
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })

        return JsonResponse({"success": False}, status=400)

    return render(request, "login.html")
