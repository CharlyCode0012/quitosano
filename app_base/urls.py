from django.urls import path
from .views.envio_api import listar_envios, crear_envio, actualizar_envio, eliminar_envio
from .views.datos_ambi_api import listar_datos_ambientales, crear_ambiente, actualizar_ambiente, eliminar_ambiente
from .views.transporte_quitosano_api import listar_transportes, crear_transporte, actualizar_transporte, eliminar_transporte
from .views.usuario_api import listar_usuarios, crear_usuario, actualizar_usuario, eliminar_usuario

urlpatterns = [
    path('envios/', listar_envios),
    path('envios/crear/', crear_envio),
    path('envios/<uuid:envio_id>/actualizar/', actualizar_envio),
    path('envios/<uuid:envio_id>/eliminar/', eliminar_envio),

    path('ambiente/', listar_datos_ambientales),
    path('ambiente/crear/', crear_ambiente),
    path('ambiente/<str:transporte_id>/actualizar/', actualizar_ambiente),
    path('ambiente/<str:transporte_id>/eliminar/', eliminar_ambiente),

    path('transporte/', listar_transportes),
    path('transporte/crear/', crear_transporte),
    path('transporte/<str: id_transporte>/actualizar/', actualizar_transporte),
    path('transporte/<str: id_transporte>/eliminar/', eliminar_transporte),

    path('usuario/', listar_usuarios),
    path('usuario/crear/', crear_usuario),
    path('usuario/<str: nombre>/actualizar', actualizar_usuario),
    path('usuario/<str: nombre>/eliminar', eliminar_usuario),

    
]
