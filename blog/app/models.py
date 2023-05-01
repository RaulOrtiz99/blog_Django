from django.db import models

# Create your models here.

class Publicacion(models.Model):
    titulo  = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=250)
    email   = models.EmailField(blank=True, null=True)