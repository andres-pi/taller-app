from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.settings import settings

from src.infrastructure.api.routers.clientes_router import router as clientes_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(clientes_router, prefix=settings.app_v1_str)

@app.get("/", tags=["System"], include_in_schema=False)
def root():
    return {
        "message": "Taller API",
        "docs": "/docs"
    }

@app.get("/health", tags=["System"])
def health():
    return {
        "status": "OK",
        "service": "taller-api"
    }