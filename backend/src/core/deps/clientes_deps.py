from fastapi import Depends

from src.application.ports.cliente_ports import ClientePort
from src.application.use_cases.clientes import (
    ObtenerCliente,
    ObtenerClientes,
    CrearCliente,
    ActualizarCliente,
    EditarCliente
)
from src.core.dependencies import obtener_cliente_repository


def obtener_cliente_use_case(cliente_port: ClientePort = Depends(obtener_cliente_repository),) -> ObtenerCliente:
    return ObtenerCliente(cliente_port)

def obtener_clientes_use_case(cliente_port: ClientePort = Depends(obtener_cliente_repository),) -> ObtenerClientes:
    return ObtenerClientes(cliente_port) 

def crear_cliente_use_case(cliente_port: ClientePort = Depends(obtener_cliente_repository),) -> CrearCliente:
    return CrearCliente(cliente_port)

def actualizar_cliente_use_case(cliente_port: ClientePort = Depends(obtener_cliente_repository),) -> ActualizarCliente:
    return ActualizarCliente(cliente_port)

def editar_cliente_use_case(cliente_port: ClientePort = Depends(obtener_cliente_repository),) -> EditarCliente:
    return EditarCliente(cliente_port)