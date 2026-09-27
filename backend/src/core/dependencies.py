from fastapi import Depends
from sqlmodel import Session

from src.application.ports.cliente_ports import ClientePort
from src.infrastructure.database.clientes.clientes_repository import ClienteRepository
from src.infrastructure.database.session import obtener_session


# Dependencia única para construir el repositorio del módulo
def obtener_cliente_repository(session: Session = Depends(obtener_session),) -> ClientePort:
    return ClienteRepository(session)

