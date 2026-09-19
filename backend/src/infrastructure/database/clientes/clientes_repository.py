from sqlmodel import Session, select

from src.domain.entities.cliente import Cliente
from src.infrastructure.database.clientes.clientes_models import ClienteModel

class ClienteRepository:

    def __init__(self, session: Session):
        self.session = session

    def obtener_uno(self, cliente_id: int) -> Cliente | None:

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

    def obtener_todos(self) -> list[Cliente]:

        statement = select(ClienteModel)

        modelos = self.session.exec(statement).all()

        return [
            Cliente(
                id=modelo.id,
                nombre=modelo.nombre,
                apellido=modelo.apellido,
                telefono=modelo.telefono,
                email=modelo.email
            )
            for modelo in modelos
        ]

    def guardar(self, cliente: Cliente) -> Cliente:

        modelo = ClienteModel(
            nombre=cliente.nombre,
            apellido=cliente.apellido,
            telefono=cliente.telefono,
            email=cliente.email
        )

        self.session.add(modelo)
        self.session.commit()
        self.session.refresh(modelo)

        return Cliente(
            id=modelo.id,
            nombre=modelo.nombre,
            apellido=modelo.apellido,
            telefono=modelo.telefono,
            email=modelo.email
        )