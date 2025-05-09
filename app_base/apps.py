# Archivo apps.py dentro de la aplicación 'app_base'.
# Define la configuración de la aplicación para que Django la registre correctamente.
from django.apps import AppConfig

class AppBaseConfig(AppConfig):
    # Campo auto-incremental por defecto para modelos (recomendado desde Django 3.2).
    default_auto_field = 'django.db.models.BigAutoField'
    # Nombre de la aplicación. Debe coincidir con el nombre del paquete (carpeta) de la app.
    name = 'app_base'
    # Nombre legible (opcional) para la aplicación, por ejemplo para el panel de administración.
    # verbose_name = 'Base de Aplicación'
