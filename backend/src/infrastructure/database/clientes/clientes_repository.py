from sqlmodel import Session

from src.domain.entities.cliente import Cliente
from src.infrastructure.database.clientes.clientes_models import ClienteModel

class ClienteRepository:

    def __init__(self, session: Session):
        self.session = session

    def obtener(self, cliente_id: int) -> Cliente | None:

        modelo = self.session.get(ClienteModel, cliente_id)

        if modelo is None:
            return None

        return Cliente(
            id=modelo.id,
            nombre=modelo.nombre,
            apellido=modelo.apellido,
            telefono=modelo.telefono,
            email=modelo.email,
        )