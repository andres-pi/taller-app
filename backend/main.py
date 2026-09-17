from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.settings import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5178"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["System"])
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