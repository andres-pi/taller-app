from dataclasses import dataclass

@dataclass
class Metricas:
    ordenes_recibidas_hoy: int
    pendientes: int
    diagnostico: int
    en_reparacion: int
    reparadas: int
    entregadas: int
    canceladas: int
    actividades_hoy: int
