from fastapi import APIRouter, Depends, HTTPException, status

from src.application.use_cases.clientes import (
    ObtenerCliente,
    ObtenerClientes,
    CrearCliente,
    ActualizarCliente,
    EditarCliente
)
from src.infrastructure.api.v1.dto.cliente_dto import (
    ClienteNuevo,
    ClienteRespuesta,
    ClienteActualizar,
    ClienteEditar
)
from src.core.deps.clientes_deps import (
    obtener_cliente_use_case,
    obtener_clientes_use_case,
    crear_cliente_use_case,
    actualizar_cliente_use_case,
    editar_cliente_use_case
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


@router.post("", response_model=ClienteRespuesta, status_code=status.HTTP_201_CREATED)
def crear(
    payload: ClienteNuevo,
    use_case: CrearCliente = Depends(crear_cliente_use_case)
):
    try:
        cliente = use_case.ejecutar(
            nombre=payload.nombre,
            apellido=payload.apellido,
            telefono=payload.telefono,
            email=payload.email
        )
    except ValueError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(err)
        )
    except HTTPException as http_exc:
        raise http_exc

    return ClienteRespuesta.model_validate(cliente)


@router.put("/{id}/actualizar", response_model=ClienteRespuesta, status_code=status.HTTP_200_OK)
def actualizar(
    id: int,
    datos: ClienteActualizar,
    use_case: ActualizarCliente = Depends(actualizar_cliente_use_case)
):
    try:
        cliente = use_case.ejecutar(
            cliente_id=id,
            nombre=datos.nombre,
            apellido=datos.apellido,
            telefono=datos.telefono,
            email=datos.email
        )
    except ValueError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(err)
        )
    except HTTPException as http_exc: raise http_exc

    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con {id} no encontrado"
        )

    return ClienteRespuesta.model_validate(cliente)


@router.patch("/{id}/editar", response_model=ClienteRespuesta, status_code=status.HTTP_200_OK)
def editar(
    id: int,
    datos: ClienteEditar,
    use_case: EditarCliente = Depends(editar_cliente_use_case)
):
    cambios = datos.model_dump(exclude_unset=True)

    try:
        cliente = use_case.ejecutar(cliente_id=id, cambios=cambios)
    except ValueError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(err)
        )
    except HTTPException as http_exc: raise http_exc

    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con {id} no encontrado"
        )
    return ClienteRespuesta.model_validate(cliente)
