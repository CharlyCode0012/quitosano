from dataclasses import dataclass
from uuid import UUID
from datetime import date

@dataclass
class Retroalimentacion:
    id_feedback: UUID
    id_envio: UUID
    evaluador: str
    comentario: str
    fecha: date
    calificacion: int
