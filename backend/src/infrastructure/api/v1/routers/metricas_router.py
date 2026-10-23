from fastapi import APIRouter, Depends, HTTPException, status

from src.application.use_cases.metricas import ObtenerMetricas
from src.infrastructure.api.v1.dto.metricas_dto import MetricasRespuesta
from src.core.deps.metricas_deps import obtener_metricas_use_case
from datetime import date

router = APIRouter(prefix="/metricas", tags=["Métricas"])


@router.get("", response_model=MetricasRespuesta, status_code=status.HTTP_200_OK)
def obtener_metricas(
    fecha: date | None = None,
    use_case: ObtenerMetricas = Depends(obtener_metricas_use_case)
):
    metricas = use_case.ejecutar(fecha)

    return MetricasRespuesta.model_validate(metricas.__dict__)
