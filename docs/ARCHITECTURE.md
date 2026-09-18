# Arquitectura de Taller API

Este documento explica la arquitectura utilizada en Taller API, enfocada en separar responsabilidades y controlar dependencias sin añadir complejidad innecesaria.

## 1. Objetivo de la arquitectura

Taller API se organiza en tres capas principales para separar:
1. Las reglas y conceptos del negocio (Domain).
2. Los casos de uso de la aplicación (Application).
3. La comunicación HTTP, persistencia y detalles tecnológicos (Infrastructure).

**Regla de oro:** Una capa no debe conocer detalles que pertenecen a una capa más externa.
* `domain` y `application` no conocen FastAPI, SQLModel ni PostgreSQL.
* `infrastructure` conoce y maneja todas las tecnologías concretas (HTTP, FastAPI, bases de datos).

## 2. Estructura base

```text
backend/
├── main.py
├── src/
│   ├── application/
│   │   ├── ports/
│   │   └── use_cases/
│   │
│   ├── core/
│   │   ├── dependencies.py
│   │   └── settings.py
│   │
│   ├── domain/
│   │   ├── entities/
│   │   └── exceptions/
│   │
│   └── infrastructure/
│       ├── api/
│       │   ├── dto/
│       │   └── routers/
│       └── database/
│           ├── clientes/
│           └── models/
```

## 3. Las responsabilidades principales

**Domain**
Representa el núcleo del negocio. Contiene entidades (ej. `Cliente`), reglas y excepciones propias. No contiene lógica de bases de datos, APIs ni librerías externas.

**Application**
Representa lo que el sistema puede hacer mediante casos de uso (ej. `ObtenerCliente`). Define "puertos" (interfaces/protocolos) cuando necesita interactuar con el exterior, sin saber cómo se implementan.

**Infrastructure**
Contiene todas las implementaciones tecnológicas, divididas principalmente en dos áreas:
* **api**: La frontera HTTP. Contiene los routers de FastAPI y los DTOs de entrada/salida.
* **database**: La persistencia de datos. Contiene los modelos de SQLModel y los repositorios (ej. `ClienteRepository`) que interactúan con PostgreSQL.

## 4. DTOs y Modelos

Es fundamental separar cómo se transfiere la información (DTO), cómo se procesa (Entidad) y cómo se guarda (Modelo).
* **Cliente**: Entidad pura de negocio (`domain/`).
* **ClienteModel**: Representación para la base de datos (`infrastructure/database/models/`).
* **ClienteRespuesta**: DTO para enviar/recibir por HTTP (`infrastructure/api/dto/`).

La infraestructura se encarga de transformar (mapear) los datos entre estas representaciones.

## 5. Puertos y Repositorios

Un puerto es un contrato definido en `application` que establece qué necesita hacer el sistema (ej. `ClientePort` definiendo un método `obtener()`). 

La implementación concreta reside en `infrastructure`. Por ejemplo, `ClienteRepository` implementa `ClientePort` usando SQLModel. Esto permite que la lógica de aplicación dependa de la abstracción y no de la base de datos directamente, facilitando los tests mediante implementaciones falsas (fakes).

## 6. El flujo completo

Ejemplo de flujo para `GET /clientes/1`:

1. **HTTP/Router** (`infrastructure/api`) recibe la petición.
2. **Caso de uso** (`application`) es invocado por el router.
3. **Puerto** (`application/ports`) es llamado por el caso de uso.
4. **Repositorio** (`infrastructure/database/clientes`) ejecuta la implementación concreta.
5. **PostgreSQL** devuelve los datos.
6. El flujo regresa mapeando el modelo a Entidad y luego a DTO para la respuesta HTTP 200.

## 7. Dependencias (`core/dependencies.py`)

Se encarga de conectar las implementaciones concretas con los casos de uso para que FastAPI las inyecte. Aquí es donde `ClienteRepository` se instancia con una sesión de base de datos y se le inyecta al caso de uso `ObtenerCliente`.

## 8. Reglas para mantener la arquitectura

* **Regla 1:** Domain y Application no importan librerías tecnológicas (ni SQLModel, ni FastAPI).
* **Regla 2:** Infrastructure coordina tanto la entrada HTTP (routers) como la salida (base de datos).
* **Regla 3:** No crear abstracciones innecesarias si una responsabilidad es simple.
* **Regla 4:** Nombra los archivos por su función explícita (`cliente_dto.py`, `cliente_repository.py`) en lugar de nombres genéricos (`utils.py`, `helpers.py`).

## 9. Regla mental para ubicar código

* ¿Es una regla del negocio? → `domain`
* ¿Es una acción del sistema? → `application/use_cases`
* ¿Es un contrato que requiere la App? → `application/ports`
* ¿Habla con una base de datos o expone rutas HTTP (FastAPI)? → `infrastructure`
* ¿Es configuración general? → `core`