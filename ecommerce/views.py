from django.shortcuts import redirect, render,get_object_or_404
from ecommerce.models import Producto, Blog
from django.db.models import Q
from django.views.generic import ListView
from ecommerce.carrito import Carrito
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.

class ProductoListView (ListView):
    template_name = 'ecommerce/index.html'
    model = Producto

def index(request):
    filtro = request.GET.get('filtro')
    if filtro == 'vendido':
        productos = Producto.objects.filter(valoracion=5)[:8]
    elif filtro == 'rebaja':
        productos = Producto.objects.filter(descuento__gte=1)[:8]
    elif filtro == 'ultimo':
        productos = Producto.objects.all().order_by('-id')[:8]
    else:
        productos= Producto.objects.all()[:8]
    
    seleccion = Producto.objects.filter(valoracion=5)[:4]
    blogs = Blog.objects.all()[:3]
    return render(request, 'ecommerce/index.html', {'productos' : productos, 'seleccion': seleccion, 'blogs' : blogs, 'filtro' : filtro})

def colection(request):
    orden = request.GET.get('orden')
    filtro = request.GET.get('filtro')
    
    
    if filtro == 'vendido':
        productos = Producto.objects.filter(valoracion=5)
    elif filtro == 'rebaja':
        productos = Producto.objects.filter(descuento__gte=1)
    elif filtro == 'ultimo':
        productos = Producto.objects.all().order_by('-id')
    
    elif filtro =='Componentes':
        productos = Producto.objects.filter(categoria='Componentes')
        
    elif filtro == "Perifericos":
        productos = Producto.objects.filter(categoria='Perifericos')    
        
    elif filtro == "Consolas":
        productos = Producto.objects.filter(categoria='Consolas')
    
    elif filtro == "precio1":
        productos = Producto.objects.filter(precio__range=(0,50000))
    
    elif filtro == "precio2":
        productos = Producto.objects.filter(precio__range=(50001,100000))
    
    elif filtro == "precio3":
        productos = Producto.objects.filter(precio__range=(100001,300000))
    
    elif filtro == "precio4":
        productos = Producto.objects.filter(precio__range=(300001,500000))
    
    elif filtro == "precio5":
        productos = Producto.objects.filter(precio__range=(500001,1000000))
        
    else:
        if orden == 'Relevancia':
            productos = Producto.objects.all().order_by('-valoracion')
        elif orden == 'Precio_menor':
            productos = Producto.objects.all().order_by('-precio')
        elif orden == 'Precio_mayor':
            productos = Producto.objects.all().order_by('precio')
        else:
            productos = Producto.objects.all()    
    return render(request, 'ecommerce/colection.html', {'productos': productos, 'filtro': filtro, 'orden': orden})


def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'ecommerce/blogs.html',{'blogs' : blogs})

def pago(request):
    return render(request, 'ecommerce/pago.html')

def about(request):
    return render(request, 'ecommerce/about.html')


@login_required
def carro_compras(request):
   return render(request, 'ecommerce/carro_compras.html')

def login_valida(request):
    return render(request, 'registration/login.html')


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            user = authenticate(username=user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('login')
    return render(request, 'registration/register.html',data)



def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'ecommerce/detalle_producto.html', {'producto' : producto})


def mostrarPublicacion(request):
    prod = Producto.objects.all().values()
    datos = {'prod' : prod}
    return render(request, 'index.html', datos)

    
def exit (request):
    logout(request)
    return redirect('index')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carro_compras")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carro_compras")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carro_compras")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carro_compras")
