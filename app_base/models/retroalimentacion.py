from dataclasses import dataclass
from uuid import UUID
from datetime import date

@dataclass
class Retroalimentacion:
    folio_compra: UUID
    fecha_compra: date
    comprador: str
    comentarios: str
    cantidad_comprada: str
