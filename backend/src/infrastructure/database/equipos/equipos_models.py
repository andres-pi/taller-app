from sqlmodel import SQLModel, Field
from datetime import datetime

class EquipoModel(SQLModel, table=True):
    __tablename__ = "equipos"

    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="clientes.id")
    tipo: str = Field(max_length=50)
    marca: str = Field(max_length=100)
    modelo: str = Field(max_length=100)
    numero_serie: str | None = Field(default=None, max_length=100)
    fecha_creacion: datetime = Field(default_factory=datetime.now)
    fecha_actualizacion: datetime = Field(default_factory=datetime.now)
