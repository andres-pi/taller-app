from src.domain.entities.orden_reparacion import OrdenReparacion, EstadoOrden
from src.application.ports.orden_ports import OrdenPort


class ObtenerOrden:

    def __init__(self, orden_port: OrdenPort):
        self.orden_port = orden_port

    def ejecutar(self, orden_id: int) -> OrdenReparacion | None:
        return self.orden_port.obtener_uno(orden_id)


class ObtenerOrdenes:

    def __init__(self, orden_port: OrdenPort):
        self.orden_port = orden_port

    def ejecutar(self, estado: EstadoOrden | None = None) -> list[OrdenReparacion]:
        return self.orden_port.obtener_todos(estado)


class ObtenerOrdenesPorEquipo:

    def __init__(self, orden_port: OrdenPort):
        self.orden_port = orden_port

    def ejecutar(self, equipo_id: int) -> list[OrdenReparacion]:
        return self.orden_port.obtener_por_equipo(equipo_id)
