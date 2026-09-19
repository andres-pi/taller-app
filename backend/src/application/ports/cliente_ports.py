from typing import Protocol
from src.domain.entities.cliente import Cliente

class ClientePort(Protocol):

    def obtener_uno(self, cliente_id: int) -> Cliente | None:
        ...

    def obtener_todos(self) -> list[Cliente]:
        ...

    def guardar(self, cliente: Cliente) -> Cliente:
        ...