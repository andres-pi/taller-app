from fastapi import Depends

from src.application.ports.metricas_ports import MetricasPort
from src.application.use_cases.metricas import ObtenerMetricas
from src.core.dependencies import obtener_metricas_repository


def obtener_metricas_use_case(metricas_port: MetricasPort = Depends(obtener_metricas_repository)) -> ObtenerMetricas:
    return ObtenerMetricas(metricas_port)
