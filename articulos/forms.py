from django import forms

from .models import Articulo


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ["titulo", "cuerpo", "portada"]
        labels = {"cuerpo": "Contenido", "portada": "Imagen de portada"}

    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"].strip()
        if len(titulo) < 5:
            raise forms.ValidationError("El título debe tener al menos 5 caracteres.")
        return titulo
