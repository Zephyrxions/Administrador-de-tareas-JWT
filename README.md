z# Administrador de Tareas con Django y JWT

Este es un proyecto de administración de tareas desarrollado con Django que implementa autenticación JWT (JSON Web Tokens).

## Características

- Registro de usuarios
- Inicio de sesión con JWT
- Creación, edición y eliminación de tareas
- Visualización de tareas por usuario
- Perfil de usuario personalizado

## Requisitos Previos

- Python 3.13 o superior
- pip (gestor de paquetes de Python)
- Entorno virtual (recomendado)

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Zephyrxions/Administrador-de-tareas-JWT.git
cd Administrador-de-tareas-JWT
```

2. Crea y activa un entorno virtual:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
```

4. Realiza las migraciones de la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crea un superusuario (opcional):
```bash
python manage.py createsuperuser
```

## Ejecutar el Proyecto

1. Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

2. Abre tu navegador y visita:
- http://127.0.0.1:8000/ - Página principal
- http://127.0.0.1:8000/admin/ - Panel de administración (requiere superusuario)

## Uso

1. Regístrate como nuevo usuario en la página de registro
2. Inicia sesión con tus credenciales
3. Comienza a crear y administrar tus tareas
4. Puedes editar tu perfil desde la sección correspondiente

## Estructura del Proyecto

```
Django_Web/
├── db.sqlite3
├── manage.py
├── Django_Web/          # Configuración principal del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tareas/             # Aplicación de tareas
    ├── models.py       # Modelos de datos
    ├── views.py        # Vistas y lógica
    ├── forms.py        # Formularios
    ├── urls.py         # URLs de la aplicación
    └── templates/      # Plantillas HTML
```

## Contribuir

Si deseas contribuir al proyecto:

1. Haz un Fork del repositorio
2. Crea una nueva rama para tus cambios
3. Envía un Pull Request con tus mejoras

## Notas Adicionales

- La aplicación utiliza SQLite como base de datos por defecto
- Las contraseñas se almacenan de forma segura utilizando el hash por defecto de Django
- La autenticación se maneja mediante tokens JWT para mayor seguridad
