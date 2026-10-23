from fastapi import Depends
from sqlmodel import Session

from src.application.ports.equipo_ports import EquipoPort
from src.application.ports.orden_ports import OrdenPort
from src.application.ports.metricas_ports import MetricasPort
from src.infrastructure.database.equipos.equipos_repository import EquipoRepository
from src.infrastructure.database.ordenes.ordenes_repository import OrdenRepository
from src.infrastructure.database.metricas.metricas_repository import MetricasRepository
from src.infrastructure.database.session import obtener_session


def obtener_equipo_repository(session: Session = Depends(obtener_session)) -> EquipoPort:
    return EquipoRepository(session)


def obtener_orden_repository(session: Session = Depends(obtener_session)) -> OrdenPort:
    return OrdenRepository(session)


def obtener_metricas_repository(session: Session = Depends(obtener_session)) -> MetricasPort:
    return MetricasRepository(session)
