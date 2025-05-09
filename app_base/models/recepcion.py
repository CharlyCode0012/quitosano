
from dataclasses import dataclass

@dataclass
class Recepcion:
    id_recepcion: str         # UUID como string
    id_envio: str             # UUID de envío relacionado
    fecha_llegada: str        # YYYY-MM-DD
    hora_llegada: str         # HH:MM
    temperatura_llegada: float
    unidad_temperatura: str
    nombre_producto: str
    cantidad: float
    unidad: str
    observaciones: str
    condiciones: str
    recibido_por: str