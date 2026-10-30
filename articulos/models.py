from django.contrib.auth.models import User
from django.db import models


class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    cuerpo = models.TextField()
    portada = models.ImageField(upload_to="portadas/", null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo
