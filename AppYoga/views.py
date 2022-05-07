from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def formaciones(request):
    formacion=Formaciones(nombre="Yoga para niños", comision=1234)
    formacion.save()
    return HttpResponse(f"Formacion creada = {formacion.nombre}")
