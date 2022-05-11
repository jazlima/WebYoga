from django.urls import path 
from .views import formaciones, alumnos, clases, asanas, inicio, buscarAlumnos, buscar

urlpatterns = [

    path('', inicio, name='inicio'),
    path('formaciones/', formaciones, name='formaciones'),
    path('alumnos/', alumnos, name='alumnos'),
    path('clases/', clases, name='clases'),
    path('asanas/', asanas, name='asanas'),
    path('buscarAlumnos/', buscarAlumnos, name='buscarAlumnos'),
    path('buscar/', buscar, name='buscar'),
    
    
]