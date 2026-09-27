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


class ActualizarCliente:

    def __init__(self, cliente_port: ClientePort):
        self.cliente_port = cliente_port

    def ejecutar(
        self,
        cliente_id: int,
        nombre: str,
        apellido: str,
        telefono: str,
        email: str | None
    ) -> Cliente:

        if not validar_telefono(telefono): raise ValueError("El teléfono no es válido")

        cliente = self.cliente_port.obtener_uno(cliente_id)

        if cliente is None: return None

        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.telefono = telefono
        cliente.email = email

        return self.cliente_port.actualizar(cliente)


class EditarCliente:
    def __init__(self, cliente_port: ClientePort):
        self.cliente_port = cliente_port

    def ejecutar(
        self,
        cliente_id: int,
        cambios: dict
    ) -> Cliente | None:

        cliente = self.cliente_port.obtener_uno(cliente_id)

        if cliente is None: return None

        if "nombre" in cambios: cliente.nombre = cambios["nombre"]
        if "apellido" in cambios: cliente.apellido = cambios["apellido"]
        if "telefono" in cambios:
            if not validar_telefono(cambios["telefono"]): raise ValueError("El teléfono no es válido")
            cliente.telefono = cambios["telefono"]
        if "email" in cambios: cliente.email = cambios["email"]

        return self.cliente_port.actualizar(cliente)