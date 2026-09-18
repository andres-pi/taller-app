from sqlmodel import SQLModel, Field

class ClienteModel(SQLModel, table=True):
    __tablename__ = "clientes"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100)
    apellido: str = Field(max_length=100)
    telefono: str = Field(max_length=14)
    email: str | None = None