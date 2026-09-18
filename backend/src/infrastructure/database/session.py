from sqlmodel import Session, create_engine
from src.core.settings import settings

engine = create_engine(
    settings.database_url,
    echo=settings.app_debug
)

def obtener_session():
    with Session(engine) as session:
        yield session