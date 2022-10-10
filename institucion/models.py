from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    contrasenna=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)

class complejo_deportivo(models.Model):
    nombre_complejo=models.CharField(max_length=50)
    tipo_deporte=models.CharField(max_length=50)
    id_usuario=models.IntegerField()

class Escuela(models.Model):
    tipo_deporte=models.CharField(max_length=50)
    nombre_escuela=models.CharField(max_length=50)
    horario=models.DateField()
    id_profesores=models.IntegerField()
    logros=models.CharField(max_length=50)
    
class Profesores(models.Model):
    id_profesores=models.IntegerField()
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)