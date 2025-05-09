from django.urls import path
from .views.envio_api import listar_envios, crear_envio, actualizar_envio, eliminar_envio

urlpatterns = [
    path('api/envios/', listar_envios),
    path('api/envios/crear/', crear_envio),
    path('api/envios/<uuid:envio_id>/actualizar/', actualizar_envio),
    path('api/envios/<uuid:envio_id>/eliminar/', eliminar_envio),
]
