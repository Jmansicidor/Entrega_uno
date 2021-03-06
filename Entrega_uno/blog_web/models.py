from ast import AugStore
from time import time
from unicodedata import category
from django.db import models


# Create your models here.

class Usuario(models.Model):
    pais = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    sexo = models.CharField(max_length=255)

    def __str__(self):
        return f'Pais {self.pais}: {self.domicilio} {self.sexo}'


class Persona(models.Model):
    nombre_completo = models.CharField(max_length=255)
    edad = models.IntegerField()
    email = models.CharField(max_length=255)
    otros_datos = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)


class Posteo(models.Model):
    autor = models.TextField(max_length=100)
    titulo = models.TextField(max_length=100)
    categoria = models.TextField(max_length=100)
    post = models.TextField(max_length=1000)
    fecha_posteo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Posteo {self.id}: {self.titulo} {self.categoria} {self.post} {self.fecha_posteo}'
