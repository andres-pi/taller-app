from sqlmodel import SQLModel, Field
from datetime import datetime
from src.domain.entities.orden_reparacion import EstadoOrden

class OrdenReparacionModel(SQLModel, table=True):
    __tablename__ = "ordenes_reparacion"

    id: int | None = Field(default=None, primary_key=True)
    equipo_id: int = Field(foreign_key="equipos.id")
    problema_reportado: str
    diagnostico: str | None = None
    estado: EstadoOrden = Field(default=EstadoOrden.PENDIENTE)
    fecha_ingreso: datetime = Field(default_factory=datetime.now)
    fecha_finalizacion: datetime | None = None
    observaciones: str | None = None
    fecha_creacion: datetime = Field(default_factory=datetime.now)
    fecha_actualizacion: datetime = Field(default_factory=datetime.now)
