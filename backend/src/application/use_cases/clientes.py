from src.domain.entities.cliente import Cliente
from src.domain.rules.clientes_rules import validar_telefono
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


class CrearCliente:

    def __init__(self, cliente_port: ClientePort) :
        self.cliente_port = cliente_port

    def ejecutar(
        self,
        nombre: str,
        apellido: str,
        telefono: str,
        email: str | None = None
    ) -> Cliente:

        if not validar_telefono(telefono):
            raise ValueError("El teléfono no es válido")

        cliente = Cliente(
            id=None,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email
        )

        return self.cliente_port.guardar(cliente)