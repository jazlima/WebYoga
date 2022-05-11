from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def inicio(request):
    return render(request, "AppYoga/inicio.html")

def buscarAlumnos(request):
    return render(request,"AppYoga/buscarAlumnos.html")

def buscar(request):
    

    if request.GET['apellido']:
        apellido=request.GET['apellido']
        alumnos=Alumnos.objects.filter(apellido__icontains=apellido)
        return render(request, "AppYoga/resultados.html",{'apellido':apellido, 'alumnos':alumnos})
    else:
        respuesta="No se ingreso ningun apellido"
        return render(request, "AppYoga/buscarAlumnos.html", {'respuesta':respuesta})  

def clases(request):
    if request.method == "POST":
        nombre=request.POST["nombre"]
        dias=request.POST["dias"]
        horarios=request.POST["horarios"]
        clase=Clases(nombre=nombre, dias=dias, horarios=horarios)
        clase.save()
        return render(request, "AppYoga/inicio.html")
    else:
        return render(request, "AppYoga/clases.html")

def formaciones(request):
    if request.method == "POST":
        nombre=request.POST["nombre"]
        comision=request.POST["comision"]
        formacion=Formaciones(nombre=nombre, comision=comision)
        formacion.save()
        return render(request, "AppYoga/inicio.html")
    else:
        return render(request, "AppYoga/formaciones.html")

def alumnos(request):

    if request.method == "POST":
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        dni=request.POST["dni"]
        alumno=Alumnos(nombre=nombre, apellido=apellido, dni=dni)
        alumno.save()
        return render(request, "AppYoga/inicio.html")

    else:
        return render(request, "AppYoga/alumnos.html")

def asanas(request):
    if request.method == "POST":
        nombre=request.POST["nombre"]
        tipo=request.POST["tipo"]
        asana=Asanas(nombre=nombre, tipo=tipo)
        asana.save()
        return render(request, "AppYoga/inicio.html")
    else:
        return render(request, "AppYoga/asanas.html")
