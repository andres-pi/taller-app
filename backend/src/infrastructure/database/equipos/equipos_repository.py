from sqlmodel import Session, select

from src.domain.entities.equipo import Equipo
from src.infrastructure.database.equipos.equipos_models import EquipoModel


class EquipoRepository:

    def __init__(self, session: Session):
        self.session = session

    def obtener_uno(self, equipo_id: int) -> Equipo | None:

        modelo = self.session.get(EquipoModel, equipo_id)

        if modelo is None:
            return None

        return self._mapear(modelo)

    def obtener_todos(self) -> list[Equipo]:

        statement = select(EquipoModel)
        modelos = self.session.exec(statement).all()

        return [self._mapear(m) for m in modelos]

    def obtener_por_cliente(self, cliente_id: int) -> list[Equipo]:

        statement = select(EquipoModel).where(EquipoModel.cliente_id == cliente_id)
        modelos = self.session.exec(statement).all()

        return [self._mapear(m) for m in modelos]

    def guardar(self, equipo: Equipo) -> Equipo:

        modelo = EquipoModel(
            cliente_id=equipo.cliente_id,
            tipo=equipo.tipo,
            marca=equipo.marca,
            modelo=equipo.modelo,
            numero_serie=equipo.numero_serie
        )

        self.session.add(modelo)
        self.session.commit()
        self.session.refresh(modelo)

        return self._mapear(modelo)

    def _mapear(self, modelo: EquipoModel) -> Equipo:
        return Equipo(
            id=modelo.id,
            cliente_id=modelo.cliente_id,
            tipo=modelo.tipo,
            marca=modelo.marca,
            modelo=modelo.modelo,
            numero_serie=modelo.numero_serie
        )
