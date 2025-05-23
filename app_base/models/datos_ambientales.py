from dataclasses import dataclass


@dataclass
class DatosAmbientales:
    id_transporte: str
    producto: str
    temperatura_actual: float
    temperatura_min: float
    temperatura_max: float
    humedad_actual: float
    humedad_min: float
    humedad_max: float