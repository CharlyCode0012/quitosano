from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

@dataclass
class Envio:
    id_envio: UUID
    fechaHora_salida: datetime
    origen: str
    destino: str
    temperatura_objetivo: float
    unidad_temperatura: str
    nombre_producto: str
    cantidad: float
    unidad: str
    medio_transporte: str
    notas: str = ""
