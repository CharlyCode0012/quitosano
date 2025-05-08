from django.contrib import admin
from .models import Envio, Recepcion, Retroalimentacion

admin.site.register(Envio)
admin.site.register(Recepcion)
admin.site.register(Retroalimentacion)