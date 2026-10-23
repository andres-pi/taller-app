from fastapi import Depends

from src.application.ports.equipo_ports import EquipoPort
from src.application.use_cases.equipos import (
    ObtenerEquipo,
    ObtenerEquipos,
    ObtenerEquiposPorCliente
)
from src.core.dependencies import obtener_equipo_repository


def obtener_equipo_use_case(equipo_port: EquipoPort = Depends(obtener_equipo_repository)) -> ObtenerEquipo:
    return ObtenerEquipo(equipo_port)

def obtener_equipos_use_case(equipo_port: EquipoPort = Depends(obtener_equipo_repository)) -> ObtenerEquipos:
    return ObtenerEquipos(equipo_port)

def obtener_equipos_por_cliente_use_case(equipo_port: EquipoPort = Depends(obtener_equipo_repository)) -> ObtenerEquiposPorCliente:
    return ObtenerEquiposPorCliente(equipo_port)
