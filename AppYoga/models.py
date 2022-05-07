from django.db import models

# Create your models here.

class Formaciones(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.comision)

class Alumnos(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()

    def __str__(self):
        return self.nombre+self.apellido+" "+str(self.dni)

class Clases(models.Model):
    nombre=models.CharField(max_length=50)
    dias=models.CharField(max_length=50)
    horarios=models.IntegerField()

    def __str__(self):
        return self.nombre+self.dias+" "+str(self.horarios)

class Asanas(models.Model):
    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.tipo
    
