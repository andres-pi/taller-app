from sqlmodel import Session, select, func
from datetime import date, datetime

from src.domain.entities.metricas import Metricas
from src.domain.entities.orden_reparacion import EstadoOrden
from src.infrastructure.database.ordenes.ordenes_models import OrdenReparacionModel


class MetricasRepository:

    def __init__(self, session: Session):
        self.session = session

    def obtener(self, fecha: date | None = None) -> Metricas:

        fecha_consulta = fecha or date.today()

        inicio_dia = datetime(fecha_consulta.year, fecha_consulta.month, fecha_consulta.day, 0, 0, 0)
        fin_dia = datetime(fecha_consulta.year, fecha_consulta.month, fecha_consulta.day, 23, 59, 59)

        # Ordenes recibidas en el dia consultado
        ordenes_hoy = self.session.exec(
            select(func.count(OrdenReparacionModel.id)).where(
                OrdenReparacionModel.fecha_ingreso >= inicio_dia,
                OrdenReparacionModel.fecha_ingreso <= fin_dia
            )
        ).one()

        # Conteo por estado (total general)
        def contar_estado(estado: EstadoOrden) -> int:
            return self.session.exec(
                select(func.count(OrdenReparacionModel.id)).where(
                    OrdenReparacionModel.estado == estado
                )
            ).one()

        return Metricas(
            ordenes_recibidas_hoy=ordenes_hoy,
            pendientes=contar_estado(EstadoOrden.PENDIENTE),
            diagnostico=contar_estado(EstadoOrden.DIAGNOSTICO),
            en_reparacion=contar_estado(EstadoOrden.EN_REPARACION),
            reparadas=contar_estado(EstadoOrden.REPARADA),
            entregadas=contar_estado(EstadoOrden.ENTREGADA),
            canceladas=contar_estado(EstadoOrden.CANCELADA),
            actividades_hoy=0  # Se completará cuando se implemente el módulo de actividades
        )
