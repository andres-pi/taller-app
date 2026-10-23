from typing import Protocol
from src.domain.entities.equipo import Equipo


class EquipoPort(Protocol):

    def obtener_uno(self, equipo_id: int) -> Equipo | None:
        ...

    def obtener_todos(self) -> list[Equipo]:
        ...

    def obtener_por_cliente(self, cliente_id: int) -> list[Equipo]:
        ...

    def guardar(self, equipo: Equipo) -> Equipo:
        ...
