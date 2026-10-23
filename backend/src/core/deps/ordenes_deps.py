from fastapi import Depends

from src.application.ports.orden_ports import OrdenPort
from src.application.use_cases.ordenes import (
    ObtenerOrden,
    ObtenerOrdenes,
    ObtenerOrdenesPorEquipo
)
from src.core.dependencies import obtener_orden_repository


def obtener_orden_use_case(orden_port: OrdenPort = Depends(obtener_orden_repository)) -> ObtenerOrden:
    return ObtenerOrden(orden_port)

def obtener_ordenes_use_case(orden_port: OrdenPort = Depends(obtener_orden_repository)) -> ObtenerOrdenes:
    return ObtenerOrdenes(orden_port)

def obtener_ordenes_por_equipo_use_case(orden_port: OrdenPort = Depends(obtener_orden_repository)) -> ObtenerOrdenesPorEquipo:
    return ObtenerOrdenesPorEquipo(orden_port)
