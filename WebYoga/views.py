from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola mundo")

def probandoTemplate(request):
    diccionario={"yoga": "yoga"}
    plantilla=loader.get_template("inicio.html")

    documento=plantilla.render(diccionario)
    return HttpResponse(documento)