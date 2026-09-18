from fastapi import Depends
from sqlmodel import Session

from src.application.use_cases.clientes import ObtenerCliente
from src.infrastructure.database.clientes.clientes_repository import ClienteRepository
from src.infrastructure.database.session import obtener_session

def obtener_cliente_use_case( session: Session = Depends(obtener_session), ) -> ObtenerCliente:

    persistencia = ClienteRepository(session)
    return ObtenerCliente(persistencia)