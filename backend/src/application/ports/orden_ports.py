from typing import Protocol
from src.domain.entities.orden_reparacion import OrdenReparacion, EstadoOrden


class OrdenPort(Protocol):

    def obtener_uno(self, orden_id: int) -> OrdenReparacion | None:
        ...

    def obtener_todos(self, estado: EstadoOrden | None = None) -> list[OrdenReparacion]:
        ...

    def obtener_por_equipo(self, equipo_id: int) -> list[OrdenReparacion]:
        ...

    def guardar(self, orden: OrdenReparacion) -> OrdenReparacion:
        ...

    def actualizar(self, orden: OrdenReparacion) -> OrdenReparacion | None:
        ...
