from django.urls import path
from .views.envio_api import listar_envios, crear_envio, actualizar_envio, eliminar_envio

urlpatterns = [
    path('envios/', listar_envios),
    path('envios/crear/', crear_envio),
    path('envios/<uuid:envio_id>/actualizar/', actualizar_envio),
    path('envios/<uuid:envio_id>/eliminar/', eliminar_envio),
]
