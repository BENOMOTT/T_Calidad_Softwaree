from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from .bde import clp_to_usd_conversion, usd_to_clp_conversion
from .bde import get_clp_to_usd
from .bde import clp_to_usd_conversion
from decimal import Decimal
from .forms import ( SignUpForm, UsuarioForm)
from .models import (Address, Producto, Record,
                     Tutorial, Usuario_direccion)
from django.shortcuts import render
import requests

# Create your views here.

def clp_to_usd_view(request):
    try:
        clp_to_usd = get_clp_to_usd()
        if clp_to_usd:
            return JsonResponse({'clp_to_usd': str(clp_to_usd)})
        else:
            return JsonResponse({'error': 'No se pudo obtener el tipo de cambio.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
        

def calcular(request):
    result = None
    if request.method == 'POST':
        if 'clp_amount' in request.POST:
            clp_amount = request.POST.get('clp_amount', '').strip()
            if not clp_amount:
                return render(request, 'calculadora.html', {'error': 'Por favor ingrese un valor válido.'})
            clp_amount = Decimal(clp_amount)
            result = round(clp_to_usd_conversion(clp_amount), 2)
        elif 'usd_amount' in request.POST:
            usd_amount = request.POST.get('usd_amount', '').strip()
            if not usd_amount:
                return render(request, 'calculadora.html', {'error': 'Por favor ingrese un valor válido.'})
            usd_amount = Decimal(usd_amount)
            result = round(usd_to_clp_conversion(usd_amount), 2)
    return render(request, 'calculadora.html', {'result': result})


class AddressView (CreateView):
    model = Address
    fields = ['address']
    template_name = 'core/puntos.html'
    success_url = '/'


def index(request):
        return render (request, 'core/index.html', {})

def tienda(request):
    productos = Producto.objects.all()    
    return render(request, 'core/tienda.html', {"productos": productos})

def inicio_sesion(request):
   
    return render(request, 'Registro/inicio_sesion.html', {})

def vendedor(request):
    # Aquí puedes realizar cualquier lógica adicional que necesites para el vendedor
    return render(request, 'vendedor/vendedor.html', {})

def crear_cuenta(request):
    # Aquí puedes realizar cualquier lógica adicional que necesites para el vendedor
    return render(request, 'Registro/crear_cuenta.html', {})

def recuperar_cuenta(request):
    # Aquí puedes realizar cualquier lógica adicional que necesites para el vendedor
    return render(request, 'Registro/recuperar_cuenta.html', {})

def bodegero(request):
    # Aquí puedes realizar cualquier lógica adicional que necesites para el vendedor
    return render(request, 'bodegero/bodegero.html', {})

def admin(request):
    # Aquí puedes realizar cualquier lógica adicional que necesites para el vendedor
    return render(request, 'admin/admin.html', {})

def contador(request):
    # Aquí puedes realizar cualquier lógica adicional que necesites para el vendedor
    return render(request, 'contador/contador.html', {})

def detalle_pedido(request, order_id):
    # Aquí obtienes el order_id como parámetro y realizas las operaciones necesarias
    # Por ejemplo, puedes consultar la orden específica usando order_id
    # y luego pasar esa información al template de detalle_pedido.html
    return render(request, 'vendedor/detalle_pedido.html', {'order_id': order_id})


def detalle_bodega(request, order_id):
    # Aquí obtienes el order_id como parámetro y realizas las operaciones necesarias
    # Por ejemplo, puedes consultar la orden específica usando order_id
    # y luego pasar esa información al template de detalle_pedido.html
    return render(request, 'bodegero/detalle_bodega.html', {'order_id': order_id})

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio_sesion')  # Asegúrate de que 'inicio_sesion' sea el nombre correcto de la URL de inicio de sesión


def agregar_direccion(request):
    data = {'form': UsuarioForm()}

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            
            return redirect(to= "direccion")
        else:
            data['form']= formulario

    return render(request, 'core/Direccion/agregar.html',data)

def contacto(request):   

    return render(request, 'core/contacto.html')

def direccion(request):  
    if request.user.is_authenticated:
        direcciones = Usuario_direccion.objects.all()
        data = {'direcciones' : direcciones}
        return render (request, 'core/direccion.html',data) 

 




def datos(request):   

    return render(request, 'core/datos.html')

def ingresar(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success (request, "Bienvenido" )
            return redirect('index')
        else:
            messages.success(request, "error al ingresar por favor intenta de nuevo. . .")
            return redirect('ingresar')
    else:
        return render(request, 'core/ingresar.html')

def cuenta(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Te has registrado correctamente. Bienvenido")
			return redirect('index')
	else:
		form = SignUpForm()
		return render(request, 'core/cuenta.html', {'form':form})

	return render(request, 'core/cuenta.html', {'form':form})


def tutoriales(request):
    tutoriales = Tutorial.objects.all()
    data = {"tutoriales": tutoriales}

    return render(request, 'core/tutoriales.html',data)

