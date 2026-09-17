# Taller APP

Sistema de gestión para un taller de reparaciones, desarrollado como proyecto de práctica para profundizar conceptos de backend, frontend, bases de datos, arquitectura y despliegue.

El proyecto busca resolver un problema cotidiano de los talleres que gestionan sus reparaciones de manera manual: la dificultad para mantener un registro organizado de los trabajos recibidos, conocer el estado de cada reparación y llevar un control de las actividades realizadas durante una jornada.

> **Proyecto educativo:** Taller APP no está pensado inicialmente como un producto comercial. Su objetivo principal es servir como entorno de práctica para aplicar y consolidar buenas prácticas de desarrollo de software.

---

# 1. Descripción

Un taller de reparaciones recibe diariamente diferentes equipos que necesitan diagnóstico, mantenimiento o reparación.

Cuando esta información se registra de manera manual, pueden aparecer problemas como:

* Dificultad para conocer el estado actual de una reparación.
* Pérdida o dispersión de información.
* Dificultad para consultar qué trabajos se realizaron durante un día determinado.
* Falta de historial sobre las tareas realizadas sobre un equipo.
* Dificultad para obtener estadísticas básicas sobre el trabajo realizado.
* Mayor posibilidad de cometer errores al registrar información.

**Taller APP** propone una solución tecnológica sencilla para centralizar esta información.

El sistema permitirá registrar clientes, equipos, órdenes de reparación y las actividades realizadas sobre cada orden.

El flujo principal será:

```text
Cliente
   │
   ▼
Equipo
   │
   ▼
Orden de reparación
   │
   ▼
Actividades realizadas
   │
   ▼
Historial de la reparación
```

El sistema también contará con un dashboard que permitirá consultar información resumida sobre el trabajo realizado.

---

# 2. Objetivos

## 2.1 Objetivo general

Desarrollar un sistema web sencillo para gestionar reparaciones de un taller, utilizando una arquitectura organizada y aplicando buenas prácticas de desarrollo tanto en backend como en frontend.

## 2.2 Objetivos técnicos

El proyecto busca practicar y consolidar:

* Desarrollo de APIs REST con **FastAPI**.
* Validación de datos mediante **Pydantic**.
* Persistencia de datos utilizando **PostgreSQL**.
* Uso de **SQLModel** como ORM.
* Diseño y manejo de relaciones entre entidades.
* Creación y evolución de la estructura de la base de datos sin utilizar un sistema de migraciones externo.
* Implementación de reglas de negocio.
* Arquitectura hexagonal.
* Separación de responsabilidades.
* Manejo de errores.
* Testing de lógica de negocio y API.
* Uso de **Redis** como sistema de caché.
* Desarrollo de interfaces con **React y JavaScript**.
* Comunicación entre frontend y backend mediante HTTP/JSON.
* Containerización mediante **Docker y Docker Compose**.
* Manejo de variables de entorno y configuración por ambientes.

---

# 3. Alcance

La primera versión del sistema incluirá:

### Clientes

* Registrar clientes.
* Consultar clientes.
* Modificar información.
* Eliminar clientes cuando sea posible.
* Consultar los equipos asociados a un cliente.

### Equipos

* Registrar equipos pertenecientes a un cliente.
* Consultar información del equipo.
* Modificar información.
* Consultar el historial de reparaciones.

### Órdenes de reparación

* Crear órdenes de reparación.
* Registrar el problema informado por el cliente.
* Registrar diagnóstico.
* Gestionar el estado de la reparación.
* Registrar fechas relevantes.
* Consultar órdenes.
* Filtrar órdenes por estado.
* Consultar el detalle de una orden.

### Actividades

* Registrar trabajos realizados sobre una orden.
* Consultar las actividades de una orden.
* Consultar actividades realizadas durante una fecha determinada.
* Mantener un historial de trabajo.

### Dashboard

Mostrar información resumida, por ejemplo:

* Órdenes recibidas durante el día.
* Órdenes pendientes.
* Órdenes en reparación.
* Órdenes reparadas.
* Órdenes entregadas.
* Cantidad de actividades realizadas.

### Infraestructura

* PostgreSQL como base de datos.
* Redis para caché.
* Docker para ejecutar los servicios.
* Variables de entorno para configuración.

---

# 4. No alcance

Para mantener el proyecto acotado y evitar convertirlo en un ERP, inicialmente **no se implementarán**:

* Facturación.
* Contabilidad.
* Gestión financiera.
* Pagos.
* Gestión de proveedores.
* Gestión avanzada de stock.
* Compras.
* Integración con sistemas externos.
* WhatsApp.
* Notificaciones por correo.
* Integración con servicios de mensajería.
* Gestión avanzada de usuarios y permisos.
* Multiempresa.
* Aplicación móvil.
* Sistema de turnos.
* Gestión de garantías.
* Inteligencia artificial.
* Reportes empresariales avanzados.

Estas funcionalidades podrían utilizarse posteriormente como ejercicios de extensión, pero no forman parte del objetivo inicial.

---

# 5. Casos de uso

## CU-01 — Registrar cliente

El usuario registra los datos básicos de un nuevo cliente.

### Datos principales

```text
Nombre
Apellido
Teléfono
Email
```

---

## CU-02 — Registrar equipo

El usuario registra un equipo perteneciente a un cliente.

Ejemplo:

```text
Cliente: Juan Pérez
Tipo: Notebook
Marca: Lenovo
Modelo: ThinkPad E14
Número de serie: ABC123
```

---

## CU-03 — Crear orden de reparación

El usuario recibe un equipo y crea una nueva orden.

Debe registrar:

```text
Cliente
Equipo
Problema reportado
Fecha de ingreso
Estado inicial
Observaciones
```

Una orden nueva comienza en estado:

```text
PENDIENTE
```

---

## CU-04 — Diagnosticar equipo

El técnico analiza el equipo y registra el diagnóstico.

Ejemplo:

```text
Problema reportado:
"No enciende"

Diagnóstico:
"Falla en la fuente de alimentación."
```

La orden puede pasar a:

```text
DIAGNOSTICO
```

---

## CU-05 — Registrar actividad

El usuario registra una tarea realizada sobre una orden.

Ejemplo:

```text
"Se realizó limpieza interna."
```

Cada actividad debe quedar asociada a:

* Una orden.
* Una fecha y hora.
* Una descripción.

---

## CU-06 — Cambiar estado de una orden

El usuario actualiza el estado de la reparación.

Ejemplo:

```text
PENDIENTE
    ↓
DIAGNOSTICO
    ↓
EN_REPARACION
    ↓
REPARADA
    ↓
ENTREGADA
```

---

## CU-07 — Consultar historial

El usuario consulta todas las actividades realizadas sobre una orden.

Ejemplo:

```text
ORDEN #154

16/09 09:15
Se realizó diagnóstico.

16/09 11:30
Se detectó falla en la fuente.

16/09 15:20
Se reemplazó componente.

16/09 17:00
Se realizó prueba de funcionamiento.
```

---

## CU-08 — Consultar trabajos realizados durante un día

El usuario selecciona una fecha y obtiene las actividades realizadas durante esa jornada.

Ejemplo:

```http
GET /api/v1/actividades?fecha=2026-09-16
```

Resultado:

```text
17 actividades realizadas
```

---

## CU-09 — Consultar dashboard

El usuario consulta un resumen de la actividad del taller.

Ejemplo:

```text
Órdenes recibidas:      8
Pendientes:             4
En reparación:          7
Reparadas:              5
Entregadas:             4
Actividades realizadas: 17
```

---

# 6. Entidades

El modelo inicial estará compuesto por cuatro entidades principales.

## Cliente

Representa a una persona que solicita una reparación.

```text
Cliente
├── id
├── nombre
├── apellido
├── telefono
├── email
├── fecha_creacion
└── fecha_actualizacion
```

Relaciones:

```text
Cliente 1 ───── N Equipo
```

---

## Equipo

Representa un equipo perteneciente a un cliente.

```text
Equipo
├── id
├── cliente_id
├── tipo
├── marca
├── modelo
├── numero_serie
├── fecha_creacion
└── fecha_actualizacion
```

Relaciones:

```text
Equipo 1 ───── N OrdenReparacion
```

---

## Orden de reparación

Representa una solicitud de reparación.

```text
OrdenReparacion
├── id
├── equipo_id
├── problema_reportado
├── diagnostico
├── estado
├── fecha_ingreso
├── fecha_finalizacion
├── observaciones
├── fecha_creacion
└── fecha_actualizacion
```

Relaciones:

```text
OrdenReparacion 1 ───── N Actividad
```

---

## Actividad

Representa una tarea realizada sobre una orden.

```text
Actividad
├── id
├── orden_id
├── descripcion
└── fecha
```

---

# 7. Relaciones

El modelo general será:

```text
┌────────────┐
│  Cliente   │
└─────┬──────┘
      │
      │ 1:N
      ▼
┌────────────┐
│   Equipo   │
└─────┬──────┘
      │
      │ 1:N
      ▼
┌────────────────────┐
│ OrdenReparacion    │
└─────────┬──────────┘
          │
          │ 1:N
          ▼
┌────────────────────┐
│     Actividad      │
└────────────────────┘
```

La base de datos utilizará claves primarias y foráneas para garantizar la integridad referencial.

---

# 8. Estados de una orden

Una orden podrá encontrarse en uno de los siguientes estados:

```text
PENDIENTE
DIAGNOSTICO
EN_REPARACION
REPARADA
ENTREGADA
CANCELADA
```

El estado representa la situación actual de la reparación.

Las actividades, en cambio, representan los eventos que ocurrieron durante su procesamiento.

Esta distinción es importante:

```text
Estado
→ ¿En qué situación está la orden?

Actividad
→ ¿Qué se hizo sobre la orden?
```

---

# 9. Reglas de negocio

Las reglas de negocio serán responsabilidad de la aplicación y no únicamente de los endpoints HTTP.

## Clientes

* El nombre y apellido son obligatorios.
* El teléfono debe cumplir un formato válido.
* El email, cuando sea proporcionado, debe tener un formato válido.
* No se podrá eliminar un cliente que tenga información dependiente sin resolver previamente dicha relación.

## Equipos

* Un equipo debe pertenecer a un cliente existente.
* Un equipo no puede existir sin cliente.
* El número de serie, si se proporciona, debe respetar las restricciones definidas para el sistema.
* No se podrá eliminar un equipo que tenga órdenes asociadas sin resolver previamente dicha relación.

## Órdenes

* Una orden debe pertenecer a un equipo existente.
* Una orden comienza en estado `PENDIENTE`.
* La fecha de finalización no puede ser anterior a la fecha de ingreso.
* Una orden `ENTREGADA` no puede volver automáticamente a `EN_REPARACION`.
* Una orden `CANCELADA` no puede continuar avanzando en el flujo normal.
* Solo se permitirán determinadas transiciones de estado.

### Transiciones iniciales

```text
PENDIENTE
   │
   ├──> DIAGNOSTICO
   │
   └──> CANCELADA


DIAGNOSTICO
   │
   ├──> EN_REPARACION
   └──> CANCELADA


EN_REPARACION
   │
   ├──> REPARADA
   └──> CANCELADA


REPARADA
   │
   └──> ENTREGADA
```

Las transiciones inválidas deberán ser rechazadas por la lógica de negocio.

## Actividades

* Una actividad debe pertenecer a una orden existente.
* La descripción es obligatoria.
* Una actividad debe registrar fecha y hora.
* No se podrán registrar nuevas actividades sobre una orden `ENTREGADA` o `CANCELADA`.

## Dashboard

* Los datos del dashboard deben representar información existente en PostgreSQL.
* Redis se utilizará únicamente como mecanismo de caché.
* La pérdida del caché no debe impedir el funcionamiento del sistema.
* Cuando una operación modifique información utilizada por el dashboard, deberá invalidarse el caché correspondiente.

---

# 10. Endpoints previstos

Los endpoints podrán modificarse durante el desarrollo. Esta es la propuesta inicial.

## Clientes

```http
GET    /api/v1/clientes
GET    /api/v1/clientes/{id}
POST   /api/v1/clientes
PUT    /api/v1/clientes/{id}
DELETE /api/v1/clientes/{id}
```

---

## Equipos

```http
GET    /api/v1/equipos
GET    /api/v1/equipos/{id}
POST   /api/v1/equipos
PUT    /api/v1/equipos/{id}
DELETE /api/v1/equipos/{id}
```

Consultar equipos de un cliente:

```http
GET /api/v1/clientes/{id}/equipos
```

---

## Órdenes

```http
GET    /api/v1/ordenes
GET    /api/v1/ordenes/{id}
POST   /api/v1/ordenes
PUT    /api/v1/ordenes/{id}
DELETE /api/v1/ordenes/{id}
```

Filtrar por estado:

```http
GET /api/v1/ordenes?estado=EN_REPARACION
```

Consultar órdenes de un equipo:

```http
GET /api/v1/equipos/{id}/ordenes
```

Cambiar estado:

```http
PATCH /api/v1/ordenes/{id}/estado
```

---

## Actividades

```http
GET  /api/v1/ordenes/{id}/actividades
POST /api/v1/ordenes/{id}/actividades
```

Consultar actividades por fecha:

```http
GET /api/v1/actividades?fecha=2026-09-16
```

---

## Dashboard

```http
GET /api/v1/dashboard
```

Opcionalmente:

```http
GET /api/v1/dashboard?fecha=2026-09-16
```

---

# 11. Stack tecnológico

## Backend

* **Python 3.12+**
* **FastAPI**
* **Pydantic**
* **SQLModel**
* **PostgreSQL**
* **Redis**
* **pytest**

SQLModel será utilizado como ORM para trabajar con PostgreSQL y modelar las entidades y relaciones de la aplicación.

## Frontend

* **JavaScript**
* **React**
* React Router
* Fetch API

## Infraestructura

* **Docker**
* **Docker Compose**
* PostgreSQL container
* Redis container

## Herramientas

* Git
* GitHub
* VS Code / IntelliJ
* HTTP client para pruebas
* Swagger/OpenAPI mediante FastAPI

---

# 12. Arquitectura

El backend utilizará una arquitectura basada en **Hexagonal Architecture**, buscando separar el dominio y la lógica de negocio de los detalles externos.

La estructura conceptual será:

```text
                 ┌──────────────────────┐
                 │       FastAPI        │
                 │    Presentation      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     Application      │
                 │   Casos de uso       │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │       Domain         │
                 │ Entidades y reglas   │
                 │    de negocio        │
                 └──────────┬───────────┘
                            │
                 ┌──────────┴───────────┐
                 ▼                      ▼
        ┌─────────────────┐    ┌─────────────────┐
        │   PostgreSQL    │    │      Redis      │
        │    SQLModel     │    │      Cache      │
        └─────────────────┘    └─────────────────┘
```

## Capas

### Presentation

Responsable de:

* HTTP.
* Routing.
* Request/Response.
* Schemas Pydantic.
* Códigos de estado HTTP.

No debería contener reglas de negocio complejas.

### Application

Responsable de:

* Casos de uso.
* Orquestación.
* Coordinación entre dominio e infraestructura.
* Aplicación de operaciones del sistema.

Ejemplos:

```text
CrearCliente
CrearOrden
CambiarEstadoOrden
RegistrarActividad
ObtenerDashboard
```

### Domain

Contendrá:

* Entidades.
* Reglas de negocio.
* Excepciones de dominio.
* Lógica relacionada directamente con el funcionamiento del sistema.

El dominio no debería depender directamente de FastAPI, PostgreSQL o Redis.

### Infrastructure

Contendrá los detalles técnicos externos:

```text
SQLModel
PostgreSQL
Redis
Configuración externa
```

La infraestructura será responsable de implementar la persistencia y las conexiones con servicios externos.

> **Nota:** No se implementará inicialmente Repository Pattern. Para el alcance de este proyecto se considera suficiente trabajar directamente con SQLModel desde la capa de infraestructura. Si durante el desarrollo aparece una necesidad real de desacoplar la persistencia, se evaluará incorporarlo como una evolución del proyecto.

---

# 13. ORM con SQLModel

El proyecto utilizará **SQLModel** como ORM.

El objetivo es practicar el uso de un ORM después de haber trabajado previamente con SQL directo en otros proyectos.

Se buscará practicar:

* Definición de modelos.
* Relaciones entre modelos.
* Primary Keys.
* Foreign Keys.
* Consultas.
* Filtros.
* Ordenamiento.
* Relaciones entre entidades.
* Manejo de sesiones.
* Transactions.
* Persistencia de objetos.

La separación conceptual será:

```text
Pydantic / SQLModel
→ Validación y representación de datos.

SQLModel
→ Modelado y persistencia de datos.

PostgreSQL
→ Almacenamiento definitivo.
```

Uno de los objetivos del proyecto será comprender qué problemas simplifica un ORM y cuáles son sus limitaciones, manteniendo los conocimientos de SQL adquiridos previamente.

---

# 14. Redis

Redis se utilizará inicialmente para implementar **caché del dashboard**.

Flujo:

```text
GET /dashboard
       │
       ▼
     Redis
       │
       ├── Cache HIT ──────► Respuesta
       │
       └── Cache MISS
               │
               ▼
          PostgreSQL
               │
               ▼
             Redis
               │
               ▼
            Respuesta
```

El caché tendrá un tiempo de expiración definido mediante TTL.

Cuando una operación modifique información relevante para el dashboard:

```text
Crear orden
Cambiar estado
Registrar actividad
```

se invalidará el caché correspondiente.

Redis no será considerado una fuente principal de datos.

---

# 15. Docker

El proyecto se ejecutará mediante Docker Compose.

Servicios iniciales:

```text
┌──────────────────────────────┐
│         Docker Compose       │
│                              │
│  ┌─────────┐                 │
│  │ Backend │                 │
│  └────┬────┘                 │
│       │                      │
│  ┌────▼──────┐  ┌─────────┐  │
│  │PostgreSQL │  │  Redis  │  │
│  └───────────┘  └─────────┘  │
│                              │
│  ┌──────────┐                │
│  │ Frontend │                │
│  └──────────┘                │
│                              │
└──────────────────────────────┘
```

Se practicarán:

* Dockerfiles.
* Docker Compose.
* Networks.
* Volúmenes.
* Variables de entorno.
* Healthchecks.
* Persistencia de PostgreSQL.
* Comunicación entre contenedores.

---

# 16. Estructura general del proyecto

```text
taller-app/
│
├── backend/
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
├── .gitignore
├── README.md
└── docs/
    ├── arquitectura.md
    └── modelo-datos.md
```

---

# 17. Roadmap

El desarrollo se realizará incrementalmente.

## Fase 1 — Análisis

* [ ] Definir problema.
* [ ] Definir alcance.
* [ ] Definir entidades.
* [ ] Definir relaciones.
* [ ] Definir casos de uso.
* [ ] Definir reglas de negocio.
* [ ] Definir estados y transiciones.
* [ ] Definir endpoints iniciales.

---

## Fase 2 — Inicialización

* [ ] Crear repositorio.
* [ ] Configurar Python.
* [ ] Configurar FastAPI.
* [ ] Configurar Pydantic.
* [ ] Configurar SQLModel.
* [ ] Crear estructura Hexagonal.
* [ ] Configurar variables de entorno.
* [ ] Crear endpoint de health check.

---

## Fase 3 — Base de datos

* [ ] Configurar PostgreSQL.
* [ ] Configurar SQLModel.
* [ ] Crear modelos.
* [ ] Definir relaciones.
* [ ] Crear tablas.
* [ ] Implementar sesiones.
* [ ] Probar operaciones CRUD.

---

## Fase 4 — Dominio

* [ ] Implementar entidad Cliente.
* [ ] Implementar entidad Equipo.
* [ ] Implementar entidad OrdenReparacion.
* [ ] Implementar entidad Actividad.
* [ ] Implementar reglas de negocio.
* [ ] Implementar transiciones de estado.
* [ ] Implementar excepciones de dominio.

---

## Fase 5 — API

* [ ] CRUD de clientes.
* [ ] CRUD de equipos.
* [ ] CRUD de órdenes.
* [ ] Gestión de estados.
* [ ] Registro de actividades.
* [ ] Consulta de historial.
* [ ] Consulta de actividades por fecha.
* [ ] Dashboard.

---

## Fase 6 — Testing

* [ ] Tests de entidades.
* [ ] Tests de reglas de negocio.
* [ ] Tests de transiciones de estado.
* [ ] Tests de operaciones de persistencia.
* [ ] Tests de endpoints.
* [ ] Tests de casos inválidos.

El foco principal estará en probar las reglas de negocio y no únicamente los endpoints.

---

## Fase 7 — Redis

* [ ] Configurar Redis.
* [ ] Implementar conexión.
* [ ] Implementar cache-aside.
* [ ] Implementar TTL.
* [ ] Implementar serialización.
* [ ] Implementar invalidación.
* [ ] Manejar caída de Redis sin comprometer la aplicación.

---

## Fase 8 — Frontend

* [ ] Crear proyecto React.
* [ ] Configurar routing.
* [ ] Crear layout.
* [ ] Crear dashboard.
* [ ] Crear gestión de clientes.
* [ ] Crear gestión de equipos.
* [ ] Crear gestión de órdenes.
* [ ] Crear detalle de reparación.
* [ ] Crear historial de actividades.
* [ ] Implementar formularios y validaciones.

La lógica de acceso a la API deberá mantenerse separada de los componentes visuales.

---

## Fase 9 — Docker

* [ ] Crear Dockerfile backend.
* [ ] Crear Dockerfile frontend.
* [ ] Configurar Docker Compose.
* [ ] Configurar PostgreSQL.
* [ ] Configurar Redis.
* [ ] Configurar networks.
* [ ] Configurar volúmenes.
* [ ] Configurar healthchecks.
* [ ] Probar ejecución completa desde cero.

---

## Fase 10 — Documentación y revisión

* [ ] Documentar arquitectura.
* [ ] Documentar modelo de datos.
* [ ] Revisar reglas de negocio.
* [ ] Revisar separación de responsabilidades.
* [ ] Revisar manejo de errores.
* [ ] Revisar tests.
* [ ] Revisar Docker.
* [ ] Revisar código.
* [ ] Actualizar README.

---

# 18. Objetivo final del ejercicio

Al finalizar el proyecto deberíamos poder levantar todo el sistema mediante:

```bash
docker compose up
```

y disponer de:

```text
                    Taller APP
                        │
        ┌───────────────┴───────────────┐
        │                               │
     Frontend                         Backend
       React                          FastAPI
        │                               │
        │                         ┌─────┴─────┐
        │                         │           │
        │                    PostgreSQL     Redis
        │
        └──────────── HTTP / JSON ────────────┘
```

El resultado no busca ser un sistema completo de gestión empresarial.

El objetivo es que, al terminarlo, el equipo haya practicado un flujo de desarrollo más cercano a un proyecto profesional:

```text
Problema
   ↓
Análisis
   ↓
Modelo de dominio
   ↓
Reglas de negocio
   ↓
Arquitectura
   ↓
Persistencia
   ↓
API
   ↓
Testing
   ↓
Cache
   ↓
Frontend
   ↓
Docker
   ↓
Documentación
```

El principal criterio de éxito será que el código no solamente funcione, sino que exista una **separación clara entre presentación, aplicación, dominio e infraestructura**, y que las reglas importantes del sistema estén correctamente modeladas y testeadas.
