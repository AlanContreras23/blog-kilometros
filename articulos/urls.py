from django.urls import path

from . import views

urlpatterns = [
    path("", views.listado, name="listado"),
    path("buscar/", views.buscar, name="buscar"),
    path("nuevo/", views.crear, name="crear"),
    path("articulo/<int:pk>/", views.detalle, name="detalle"),
    path("articulo/<int:pk>/editar/", views.editar, name="editar"),
    path("articulo/<int:pk>/eliminar/", views.eliminar, name="eliminar"),
]
