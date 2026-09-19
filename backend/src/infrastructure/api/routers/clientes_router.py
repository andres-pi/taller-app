from fastapi import APIRouter, Depends, HTTPException, status

from src.application.use_cases.clientes import (
    ObtenerCliente,
    ObtenerClientes
)
from src.infrastructure.api.dto.cliente_dto import ClienteRespuesta
from src.core.dependencies import (
    obtener_cliente_use_case,
    obtener_clientes_use_case
)

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.get("", response_model=list[ClienteRespuesta], status_code=status.HTTP_200_OK)
def obtener_todos(
    use_case: ObtenerClientes = Depends(obtener_clientes_use_case)
):
    clientes = use_case.ejecutar()

    return [
        ClienteRespuesta.model_validate(cliente)
        for cliente in clientes
    ]


@router.get("/{id}", response_model=ClienteRespuesta, status_code=status.HTTP_200_OK)
def obtener_por_id(
    id: int,
    use_case: ObtenerCliente = Depends(obtener_cliente_use_case)
):
    cliente = use_case.ejecutar(id)

    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con {id} no encontrado"
        )

    return ClienteRespuesta.model_validate(cliente)