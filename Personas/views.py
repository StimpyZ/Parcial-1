import re
from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.
def home(request):
    empleadosListados = Empleado.objects.all()
    return render(request, "gestionEmpleado.html", {"empleados": empleadosListados} )

def registrarEmpleados(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    edad = request.POST['txtEdad']
    peso = request.POST['txtPeso']
    Fcardiaca = request.POST['txtFCardiaca']
    stress = request.POST['txtStress']
    SOsangre = request.POST['txtSOSangre']
    
    empleado = Empleado.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, edad=edad, peso=peso, Fcardiaca=Fcardiaca,stress=stress,SOsangre=SOsangre)
    return redirect('/')

def eliminarEmpleado(request, codigo):
    empleado = Empleado.objects.get(codigo=codigo)
    empleado.delete()
    return redirect('/')
    
def edicionEmpleados(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    edad = request.POST['txtEdad']
    peso = request.POST['txtPeso']
    Fcardiaca = request.POST['txtFCardiaca']
    stress = request.POST['txtStress']
    SOsangre = request.POST['txtSOSangre']
    
    empleado = Empleado.objects.get(codigo=codigo)
    empleado.nombre = nombre
    empleado.apellido = apellido
    empleado.edad = edad
    empleado.peso = peso
    empleado.Fcardiaca = Fcardiaca
    empleado.stress = stress
    empleado.SOsangre = SOsangre
    
    empleado.save()
    return redirect('/')

def editarEmpleado(request, codigo):
    empleado = Empleado.objects.get(codigo=codigo)
    return render(request, "editarEmpleado.html", {"empleado": empleado})