from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.

def inicio(request):
    return render(request, "AppYoga/inicio.html")

def formaciones(request):
    return render(request, "AppYoga/formaciones.html")

def alumnos(request):

    if request.method == "POST":
        nombre=request.POST['nombre']
        apellido=request.POST['apellido']
        dni=request.POST['dni']
        alumno=Alumnos(nombre=nombre, apellido=apellido, dni=dni)
        alumno.save()
        return render(request, "AppYoga/inicio.html")
    
    return render(request, "AppYoga/alumnos.html")

def clases(request):
    return render(request, "AppYoga/clases.html")

def asanas(request):
    return render(request, "AppYoga/asanas.html")
