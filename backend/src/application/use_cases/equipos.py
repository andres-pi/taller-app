from src.domain.entities.equipo import Equipo
from src.application.ports.equipo_ports import EquipoPort


class ObtenerEquipo:

    def __init__(self, equipo_port: EquipoPort):
        self.equipo_port = equipo_port

    def ejecutar(self, equipo_id: int) -> Equipo | None:
        return self.equipo_port.obtener_uno(equipo_id)


class ObtenerEquipos:

    def __init__(self, equipo_port: EquipoPort):
        self.equipo_port = equipo_port

    def ejecutar(self) -> list[Equipo]:
        return self.equipo_port.obtener_todos()


class ObtenerEquiposPorCliente:

    def __init__(self, equipo_port: EquipoPort):
        self.equipo_port = equipo_port

    def ejecutar(self, cliente_id: int) -> list[Equipo]:
        return self.equipo_port.obtener_por_cliente(cliente_id)
