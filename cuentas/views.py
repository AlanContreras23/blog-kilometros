from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from articulos.models import Articulo

from .forms import PerfilForm, RegistroForm
from .models import Perfil


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(usuario=usuario)
            messages.success(request, "Cuenta creada. Ya podés iniciar sesión.")
            return redirect("login")
    else:
        form = RegistroForm()
    return render(request, "cuentas/registro.html", {"form": form})


@login_required
def perfil(request):
    perfil_usuario, creado = Perfil.objects.get_or_create(usuario=request.user)
    mis_articulos = Articulo.objects.filter(autor=request.user)
    return render(
        request, "cuentas/perfil.html", {"perfil": perfil_usuario, "mis_articulos": mis_articulos}
    )


@login_required
def editar_perfil(request):
    perfil_usuario, creado = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil_usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado.")
            return redirect("perfil")
    else:
        form = PerfilForm(instance=perfil_usuario)
    return render(request, "cuentas/editar_perfil.html", {"form": form})
