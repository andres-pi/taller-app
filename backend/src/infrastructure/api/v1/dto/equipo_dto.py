from pydantic import BaseModel


class EquipoRespuesta(BaseModel):
    id: int
    cliente_id: int
    tipo: str
    marca: str
    modelo: str
    numero_serie: str | None = None

    model_config = {"from_attributes": True}
