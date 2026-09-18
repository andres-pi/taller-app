from typing import Protocol
from src.domain.entities.cliente import Cliente

class ClientePort(Protocol):

    def obtener(self, cliente_id: int) -> Cliente | None:
        ...