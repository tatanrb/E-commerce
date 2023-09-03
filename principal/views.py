from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    # Obtener ropa
    categoria_ropa = Categoria.objects.get(nombre="Prendas de vestir")

    # Obtenemos los primeros 3
    portada_ropa = Producto.objects.filter(categoria=categoria_ropa.id)[0:3]
    print(portada_ropa)

    return render(request, 'index.html', {
        "portada_ropa": portada_ropa
    })


def fashion(request):
    return render(request, 'fashion.html')
