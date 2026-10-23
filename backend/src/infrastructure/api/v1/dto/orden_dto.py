from pydantic import BaseModel
from datetime import datetime
from src.domain.entities.orden_reparacion import EstadoOrden


class OrdenRespuesta(BaseModel):
    id: int
    equipo_id: int
    problema_reportado: str
    diagnostico: str | None = None
    estado: EstadoOrden
    fecha_ingreso: datetime
    fecha_finalizacion: datetime | None = None
    observaciones: str | None = None

    model_config = {"from_attributes": True}
