from sqlmodel import Session, select
from datetime import date, datetime

from src.domain.entities.orden_reparacion import OrdenReparacion, EstadoOrden
from src.infrastructure.database.ordenes.ordenes_models import OrdenReparacionModel


class OrdenRepository:

    def __init__(self, session: Session):
        self.session = session

    def obtener_uno(self, orden_id: int) -> OrdenReparacion | None:

        modelo = self.session.get(OrdenReparacionModel, orden_id)

        if modelo is None:
            return None

        return self._mapear(modelo)

    def obtener_todos(self, estado: EstadoOrden | None = None) -> list[OrdenReparacion]:

        statement = select(OrdenReparacionModel)

        if estado is not None:
            statement = statement.where(OrdenReparacionModel.estado == estado)

        modelos = self.session.exec(statement).all()

        return [self._mapear(m) for m in modelos]

    def obtener_por_equipo(self, equipo_id: int) -> list[OrdenReparacion]:

        statement = select(OrdenReparacionModel).where(
            OrdenReparacionModel.equipo_id == equipo_id
        )
        modelos = self.session.exec(statement).all()

        return [self._mapear(m) for m in modelos]

    def guardar(self, orden: OrdenReparacion) -> OrdenReparacion:

        modelo = OrdenReparacionModel(
            equipo_id=orden.equipo_id,
            problema_reportado=orden.problema_reportado,
            diagnostico=orden.diagnostico,
            estado=orden.estado,
            fecha_ingreso=orden.fecha_ingreso,
            fecha_finalizacion=orden.fecha_finalizacion,
            observaciones=orden.observaciones
        )

        self.session.add(modelo)
        self.session.commit()
        self.session.refresh(modelo)

        return self._mapear(modelo)

    def actualizar(self, orden: OrdenReparacion) -> OrdenReparacion | None:

        modelo = self.session.get(OrdenReparacionModel, orden.id)

        if modelo is None:
            return None

        modelo.problema_reportado = orden.problema_reportado
        modelo.diagnostico = orden.diagnostico
        modelo.estado = orden.estado
        modelo.fecha_finalizacion = orden.fecha_finalizacion
        modelo.observaciones = orden.observaciones

        self.session.add(modelo)
        self.session.commit()
        self.session.refresh(modelo)

        return self._mapear(modelo)

    def _mapear(self, modelo: OrdenReparacionModel) -> OrdenReparacion:
        return OrdenReparacion(
            id=modelo.id,
            equipo_id=modelo.equipo_id,
            problema_reportado=modelo.problema_reportado,
            diagnostico=modelo.diagnostico,
            estado=modelo.estado,
            fecha_ingreso=modelo.fecha_ingreso,
            fecha_finalizacion=modelo.fecha_finalizacion,
            observaciones=modelo.observaciones
        )
