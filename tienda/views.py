from django.shortcuts import render, get_object_or_404

# Create your views here.
from tienda.models import Producto, Categoria
from tienda.carrito import Cart


def index(request):
    product_list = Producto.objects.order_by('nombre')[:9]
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'product_list': product_list,
                                          'categorias': categorias})


def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias = Categoria.objects.all()
    return render(request, 'producto.html', {'categorias': categorias, 'producto': producto})


def categoria(request, categoria_id):
    categorias = Categoria.objects.all()
    cate = get_object_or_404(Categoria, pk=categoria_id)
    productos = Producto.objects.filter(categoria_id=categoria_id)
    return render(request, 'categoria.html', {'categorias': categorias, 'productos': productos, 'categoria': cate})


def agregarCarrito(request, producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto, 1)
    print(request.session.get("cart"))
    return render(request, 'carrito.html')


def eliminarProductoCarrito(request, producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request, 'carrito.html')


def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request, 'carrito.html')


def carrito(request):
    print(request.session.get("cart"))
    return render(request, 'carrito.html')
