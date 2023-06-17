from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from app.carrito import Carrito
from .models import Articulo

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def registro( request):
     data = {
         'form': CustomUserCreationForm()
     }

     if request.method == 'POST':
         formulario = CustomUserCreationForm(data=request.POST)
         if formulario.is_valid():
             formulario.save()
             user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
             login(request, user)
             messages.success(request, "Te has registrado correctamente")
             return redirect(to="home")
         data["form"] = formulario

     return render(request, 'registration/registro.html', data)

def vista_cliente(request):
    Articulos = Articulo.objects.all()
    return render(request, "app/vista_cliente.html", {'articulos':Articulos})

def agregar_articulo(request, articulo_id):
    carrito = Carrito(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carrito.agregar(articulo)
    return redirect("vista_cliente")

def eliminar_articulo(request, articulo_id):
    carrito = Carrito(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carrito.eliminar(articulo)
    return redirect("vista_cliente")

def restar_articulo(request, articulo_id):
    carrito = Carrito(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carrito.restar(articulo)
    return redirect("vista_cliente")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("vista_cliente")