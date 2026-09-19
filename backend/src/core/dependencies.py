from fastapi import Depends
from sqlmodel import Session

from src.application.ports.cliente_ports import ClientePort
from src.application.use_cases.clientes import (
    ObtenerCliente,
    ObtenerClientes,
    CrearCliente
)
from src.infrastructure.database.clientes.clientes_repository import ClienteRepository
from src.infrastructure.database.session import obtener_session


# Dependencia única para construir el repositorio del módulo
def obtener_cliente_repository(session: Session = Depends(obtener_session),) -> ClientePort:
    return ClienteRepository(session)


# Dependencias Módulo Clientes
def obtener_cliente_use_case(cliente_port: ClientePort = Depends(obtener_cliente_repository),) -> ObtenerCliente:
    return ObtenerCliente(cliente_port)

def obtener_clientes_use_case(cliente_port: ClientePort = Depends(obtener_cliente_repository),) -> ObtenerClientes:
    return ObtenerClientes(cliente_port) 

def crear_cliente_use_case(cliente_port: ClientePort = Depends(obtener_cliente_repository),) -> CrearCliente:
    return CrearCliente(cliente_port)