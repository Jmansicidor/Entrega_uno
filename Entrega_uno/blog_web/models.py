from ast import AugStore
from time import time
from unicodedata import category
from django.db import models

# Create your models here.

class Persona(models.Model):
    pass

class Posteo(models.Model):
    autor = models.TextField(max_length=100)
    titulo = models.TextField(max_length=100)
    categoria = models.TextField(max_length=100)
    post = models.TextField(max_length=1000)
    fecha_posteo = models.DateTimeField(auto_now_add=True)