from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField("Sobre mí", max_length=200, blank=True)
    avatar = models.ImageField(upload_to="avatares/", null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"
