from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import*

# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html") # le digo que busque en aplicacion un home.html

def repuestos(request): # Cambiar a repuestos 
    contexto = {'repuestos': Repuestos.objects.all()}
    return render(request, "aplicacion/repuestos.html", contexto) # le digo que busque en aplicacion un cursos.html

def maquina(request): # Cambiar a maquinas 
   contexto = {'maquina': Maquina.objects.all()}
   return render(request, "aplicacion/maquina.html", contexto)

def proveedores(request):
    contexto = {'proveedor': Proveedores.objects.all()}
    return render(request, "aplicacion/proveedores.html", contexto)

def buscar(request):
    return render(request, "aplicacion/buscar.html")


def repuestosForm(request):
    if request.method == "POST":
        miForm= RepuestosForm(request.POST)
        if miForm.is_valid(): #pregunto si el formulario es valido 
            rep_nombre= miForm.cleaned_data.get("nombre")
            rep_marca= miForm.cleaned_data.get("marca")
            rep_precio= miForm.cleaned_data.get("precio")
            rep_cantidad= miForm.cleaned_data.get("cantidad")
            repuesto = Repuestos(nombre = rep_nombre, marca= rep_marca, precio= rep_precio, cantidad= rep_cantidad)
            repuesto.save()
            return render(request, "aplicacion/home.html")
    else:
        miForm = RepuestosForm()
    return render(request, "aplicacion/repuestosForm.html", {"form": miForm})

def maquinaForm(request):
    if request.method == "POST":
        miForm= MaquinaForm(request.POST)
        if miForm.is_valid(): #pregunto si el formulario es valido 
            maq_nombre= miForm.cleaned_data.get("nombre")
            maq_marca= miForm.cleaned_data.get("marca")
            maq_area= miForm.cleaned_data.get("area")
            maquina = Maquina(nombre = maq_nombre, marca= maq_marca, area= maq_area)
            maquina.save()
            return render(request, "aplicacion/home.html")
    else:
        miForm = MaquinaForm()
    return render(request, "aplicacion/maquinaForm.html", {"form": miForm})
    
def proveedoresForm(request):
    if request.method == "POST":
        miForm= ProveedoresForm(request.POST)
        if miForm.is_valid(): #pregunto si el formulario es valido 
            pro_nombre= miForm.cleaned_data.get("nombre")
            pro_direccion= miForm.cleaned_data.get("direccion")
            pro_fono= miForm.cleaned_data.get("fono")
            pro_email= miForm.cleaned_data.get("email")
            proveedores = Proveedores(nombre = pro_nombre, direccion= pro_direccion, fono = pro_fono,
                              email = pro_email)
            proveedores.save()
            return render(request, "aplicacion/home.html")
    else:
        miForm = ProveedoresForm()
    return render(request, "aplicacion/proveedoresForm.html", {"form": miForm})

def buscarRepuestos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        repuestos = Repuestos.objects.filter(nombre__icontains=patron)
        contexto = {"repuestos": repuestos }
        return render(request, "aplicacion/repuestos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")