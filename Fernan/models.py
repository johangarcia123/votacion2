from turtle import title
from django.db import models

# Create your models here.
class Fernan(models.Model): 
    title = models.CharField(max_length=100) 
    description = models.TextField(blank=True)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=7)
    
class Articulo(models.Model):
    descripcion = models.CharField(max_length=20)
    precio = models.IntegerField()
    nombre = models.CharField(max_length=20)

class Pedidos(models.Model):
    numero     = models.IntegerField()
    fecha      = models.DateField()
    entregado  = models.BooleanField()