from typing import Protocol
from datetime import date
from src.domain.entities.metricas import Metricas


class MetricasPort(Protocol):

    def obtener(self, fecha: date | None = None) -> Metricas:
        ...
