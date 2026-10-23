from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class EstadoOrden(str, Enum):
    PENDIENTE = "PENDIENTE"
    DIAGNOSTICO = "DIAGNOSTICO"
    EN_REPARACION = "EN_REPARACION"
    REPARADA = "REPARADA"
    ENTREGADA = "ENTREGADA"
    CANCELADA = "CANCELADA"

@dataclass
class OrdenReparacion:
    id: int | None
    equipo_id: int
    problema_reportado: str
    diagnostico: str | None
    estado: EstadoOrden
    fecha_ingreso: datetime
    fecha_finalizacion: datetime | None
    observaciones: str | None
