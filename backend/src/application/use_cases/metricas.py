from datetime import date
from src.domain.entities.metricas import Metricas
from src.application.ports.metricas_ports import MetricasPort


class ObtenerMetricas:

    def __init__(self, metricas_port: MetricasPort):
        self.metricas_port = metricas_port

    def ejecutar(self, fecha: date | None = None) -> Metricas:
        return self.metricas_port.obtener(fecha)
