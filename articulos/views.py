from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArticuloForm
from .models import Articulo


def listado(request):
    articulos = Articulo.objects.all()
    return render(request, "articulos/listado.html", {"articulos": articulos})


def detalle(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, "articulos/detalle.html", {"articulo": articulo})


def buscar(request):
    texto = request.GET.get("q", "").strip()
    resultados = []
    if texto:
        resultados = Articulo.objects.filter(
            Q(titulo__icontains=texto) | Q(cuerpo__icontains=texto)
        )
    return render(request, "articulos/buscar.html", {"texto": texto, "resultados": resultados})


@login_required
def crear(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            messages.success(request, "Artículo publicado.")
            return redirect("detalle", pk=articulo.pk)
    else:
        form = ArticuloForm()
    return render(request, "articulos/formulario.html", {"form": form, "accion": "Nuevo artículo"})


@login_required
def editar(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if articulo.autor != request.user:
        return HttpResponseForbidden("Solo el autor puede editar este artículo.")
    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            messages.success(request, "Artículo actualizado.")
            return redirect("detalle", pk=articulo.pk)
    else:
        form = ArticuloForm(instance=articulo)
    return render(
        request,
        "articulos/formulario.html",
        {"form": form, "accion": "Editar artículo", "articulo": articulo},
    )


@login_required
def eliminar(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if articulo.autor != request.user:
        return HttpResponseForbidden("Solo el autor puede eliminar este artículo.")
    if request.method == "POST":
        articulo.delete()
        messages.success(request, "Artículo eliminado.")
        return redirect("listado")
    return render(request, "articulos/confirmar_eliminar.html", {"articulo": articulo})
