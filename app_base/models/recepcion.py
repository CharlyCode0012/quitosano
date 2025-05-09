from dataclasses import dataclass
from uuid import UUID
from datetime import date, time

@dataclass
class Recepcion:
    id_recepcion: UUID
    id_envio: UUID
    fecha_llegada: date
    hora_llegada: time
    temperatura_llegada: float
    unidad_temperatura: str
    nombre_producto: str
    cantidad: float
    unidad: str
    observaciones: str
    condiciones: str
    recibido_por: str
