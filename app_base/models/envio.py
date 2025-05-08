from django.db import models
import uuid

class Envio(models.Model):
    id_envio = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()
    origen = models.TextField()
    destino = models.TextField()
    temperatura_objetivo = models.FloatField()
    unidad_temperatura = models.TextField()
    nombre_producto = models.TextField()
    cantidad = models.FloatField()
    unidad = models.TextField()
    medio_transporte = models.TextField()
    notas = models.TextField(blank=True)
