from django.db import models
import uuid
from .envio import Envio

class Recepcion(models.Model):
    id_recepcion = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_envio = models.ForeignKey(Envio, on_delete=models.CASCADE)
    fecha_llegada = models.DateField()
    hora_llegada = models.TimeField()
    temperatura_llegada = models.FloatField()
    unidad_temperatura = models.TextField()
    nombre_producto = models.TextField()
    cantidad = models.FloatField()
    unidad = models.TextField()
    observaciones = models.TextField(blank=True)
    condiciones = models.TextField(blank=True)
    recibido_por = models.TextField()
