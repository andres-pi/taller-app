from fastapi import APIRouter, Depends, HTTPException, status

from src.application.use_cases.ordenes import (
    ObtenerOrden,
    ObtenerOrdenes,
    ObtenerOrdenesPorEquipo
)
from src.infrastructure.api.v1.dto.orden_dto import OrdenRespuesta
from src.core.deps.ordenes_deps import (
    obtener_orden_use_case,
    obtener_ordenes_use_case,
    obtener_ordenes_por_equipo_use_case
)
from src.domain.entities.orden_reparacion import EstadoOrden

router = APIRouter(prefix="/ordenes", tags=["Órdenes"])


@router.get("", response_model=list[OrdenRespuesta], status_code=status.HTTP_200_OK)
def obtener_todos(
    estado: EstadoOrden | None = None,
    use_case: ObtenerOrdenes = Depends(obtener_ordenes_use_case)
):
    ordenes = use_case.ejecutar(estado)

    return [
        OrdenRespuesta.model_validate(orden.__dict__)
        for orden in ordenes
    ]


@router.get("/{id}", response_model=OrdenRespuesta, status_code=status.HTTP_200_OK)
def obtener_por_id(
    id: int,
    use_case: ObtenerOrden = Depends(obtener_orden_use_case)
):
    orden = use_case.ejecutar(id)

    if orden is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Orden con id {id} no encontrada"
        )

    return OrdenRespuesta.model_validate(orden.__dict__)
