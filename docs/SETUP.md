# Configuración y puesta en marcha de Taller API

Este documento explica cómo levantar el proyecto localmente, conectando Docker (PostgreSQL), el backend (FastAPI) y el frontend (React).

## 1. Requisitos

Debes contar con las siguientes herramientas instaladas: Git, Docker y Docker Compose, Python 3.12+, Node.js y npm.

## 2. Clonar el proyecto

```bash
git clone <URL_DEL_REPOSITORIO>
cd taller-app
```

## 3. Infraestructura (Base de datos)

Levanta PostgreSQL utilizando Docker Compose. Los scripts `schema.sql` y `seed.sql` ubicados en `database/` se ejecutarán automáticamente al crear el volumen por primera vez.

```bash
docker compose up -d
```
*Nota: Si modificas los scripts SQL iniciales, debes destruir el volumen para que se vuelvan a ejecutar: `docker compose down -v` y luego levantar nuevamente.*

## 4. Configurar el Backend

```bash
cd backend
python3 -m venv .venv

# En Linux/macOS:
source .venv/bin/activate

# En Windows (Símbolo del sistema - cmd):
.venv\Scripts\activate.bat

# En Windows (PowerShell):
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

Crea un archivo `.env` en `backend/` basado en el entorno de desarrollo (debe incluir credenciales de base de datos y URL del frontend).

**Levantar servidor:**
```bash
fastapi dev
```
La API estará en `http://127.0.0.1:8000` y Swagger en `/docs`.

**Ejecutar tests:**
```bash
pytest
```

## 5. Configurar el Frontend

Abre otra terminal:
```bash
cd frontend
npm install
```

Crea un archivo `.env` en `frontend/` configurando la variable `VITE_API_URL` apuntando a tu backend local.

**Levantar Vite:**
```bash
npm run dev
```
Estará disponible en `http://localhost:5173`. Las llamadas al backend se realizan de forma centralizada mediante una instancia de Axios previamente configurada.

## 6. Flujo completo de la petición

```text
React (Axios)
    │
    ▼
Infrastructure: API (Routers / DTOs)
    │
    ▼
Application (Casos de uso / Puertos)
    │
    ▼
Domain (Reglas / Entidades)
    │
    ▼
Infrastructure: Database (Repositorios / Modelos)
    │
    ▼
PostgreSQL (Docker)
```

## 7. Qué hacer al comenzar una nueva funcionalidad

Cuando agregues algo nuevo (ej. `CrearCliente`), respeta este orden en el backend antes de tocar el frontend:
1. **Domain:** Define entidades y reglas.
2. **Application:** Crea el caso de uso y actualiza los puertos si hace falta.
3. **Infrastructure (Database):** Implementa las operaciones en el repositorio (`ClienteRepository`).
4. **Infrastructure (API):** Crea los DTOs y añade la ruta en el router.
5. **Tests:** Prueba todo el flujo.

## 8. Comandos rápidos útiles

* **Iniciar BD:** `docker compose up -d`
* **Apagar BD:** `docker compose down`
* **Reiniciar BD limpia:** `docker compose down -v && docker compose up -d`
* **Iniciar backend:** `fastapi dev`
* **Tests backend:** `pytest -v`
* **Iniciar frontend:** `npm run dev`