from src.domain.entities.cliente import Cliente
from src.application.ports.cliente_ports import ClientePort

class ObtenerCliente:

    def __init__(self, cliente_port: ClientePort):
        self.cliente_port = cliente_port

    def ejecutar(self, cliente_id: int) -> Cliente | None:
        return self.cliente_port.obtener_uno(cliente_id)


class ObtenerClientes:

    def __init__(self, cliente_port: ClientePort):
        self.cliente_port = cliente_port

    def ejecutar(self) -> list[Cliente]:
        return self.cliente_port.obtener_todos()