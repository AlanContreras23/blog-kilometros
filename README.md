# Bitácora de Kilómetros — Proyecto final

Blog web hecho con Django sobre running y entrenamiento. Los usuarios se registran, publican artículos con imagen de portada y tienen un perfil con avatar.

## Tecnologías

- Python 3.10+
- Django 5.2
- Pillow (imágenes)
- SQLite (base de datos de desarrollo)
- HTML / CSS

## Funcionalidades

- CRUD completo de artículos (listar, ver, crear, editar, eliminar) desde la web.
- Imagen de portada opcional en cada artículo; si no tiene, la página se ve bien igual.
- Registro, login y logout de usuarios.
- Perfil con bio y avatar, editable.
- La barra de navegación cambia según haya o no sesión iniciada.
- Rutas protegidas con `@login_required`: crear, editar y eliminar artículos, y el perfil.
- Solo el autor puede editar o eliminar sus artículos.
- Buscador por título o contenido.

## Cómo correrlo

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # opcional, para entrar a /admin
python manage.py runserver
```

Abrí http://127.0.0.1:8000/

### Variables de entorno (opcional)

El proyecto funciona sin configurar nada. Para cambiar la clave secreta o desactivar el modo debug, definí las variables de `.env.example` (`DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`).

## Estructura

```
config/      configuración del proyecto (settings, urls)
articulos/   app del blog: modelo Articulo, vistas, formularios, templates
cuentas/     app de usuarios: registro, login, perfil
templates/   base.html (plantilla común a todas las páginas)
static/css/  estilos
```

## Autor

Proyecto final de la diplomatura Python — Coderhouse.
Autor: Alan Contreras
