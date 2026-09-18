# Insertar reglas aplicadas a la entidad cliente

def validar_telefono(telefono: str) -> bool:
    telefono_limpio = telefono.replace(" ", "").replace("-", "")
    return telefono_limpio.isdigit() and 10 <= len(telefono_limpio) <= 14