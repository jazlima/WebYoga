from django.urls import path 
from .views import formaciones, alumnos, clases, asanas, inicio

urlpatterns = [

    path('', inicio, name='inicio'),
    path('formaciones/', formaciones, name='formaciones'),
    path('alumnos/', alumnos, name='alumnos'),
    path('clases/', clases, name='clases'),
    path('asanas/', asanas, name='asanas'),
    
]