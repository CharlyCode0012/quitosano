from django.urls import path
from .views.envio_api import listar_envios, crear_envio, actualizar_envio, eliminar_envio
from .views.datos_ambi_api import listar_datos_ambientales, crear_ambiente, actualizar_ambiente, eliminar_ambiente

urlpatterns = [
    path('envios/', listar_envios),
    path('envios/crear/', crear_envio),
    path('envios/<uuid:envio_id>/actualizar/', actualizar_envio),
    path('envios/<uuid:envio_id>/eliminar/', eliminar_envio),

    path('ambiente/', listar_datos_ambientales),
    path('ambiente/crear/', crear_ambiente),
    path('ambiente/<str:transporte_id>/actualizar/', actualizar_ambiente),
    path('ambiente/<str:transporte_id>/elminar/', eliminar_ambiente)


]
