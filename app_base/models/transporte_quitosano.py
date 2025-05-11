from dataclasses import dataclass
from datetime import datetime

@dataclass
class TransporteQuitosano:
    id_transporte: str
    origen: str
    destino: str
    producto: str
    cantidad_kg: float
    fecha: datetime