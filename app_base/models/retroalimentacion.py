from django.db import models
import uuid

class Retroalimentacion(models.Model):
    folio_compra = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha_compra = models.DateField()
    cantidad_comprada = models.TextField()
    comentarios = models.TextField(blank=True)
    comprador = models.TextField()
