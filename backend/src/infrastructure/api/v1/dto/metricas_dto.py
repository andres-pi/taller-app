from pydantic import BaseModel


class MetricasRespuesta(BaseModel):
    ordenes_recibidas_hoy: int
    pendientes: int
    diagnostico: int
    en_reparacion: int
    reparadas: int
    entregadas: int
    canceladas: int
    actividades_hoy: int

    model_config = {"from_attributes": True}
