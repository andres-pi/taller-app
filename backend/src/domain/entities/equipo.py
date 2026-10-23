from dataclasses import dataclass

@dataclass
class Equipo:
    id: int | None
    cliente_id: int
    tipo: str
    marca: str
    modelo: str
    numero_serie: str | None
