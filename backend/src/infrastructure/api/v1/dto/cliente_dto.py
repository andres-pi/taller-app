from pydantic import BaseModel, EmailStr

class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    telefono: str
    email: EmailStr | None = None

class ClienteNuevo(ClienteBase):
    pass

class ClienteActualizar(ClienteBase):
    pass

class ClienteEditar(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    telefono: str | None = None
    email: EmailStr | None = None

class ClienteRespuesta(ClienteBase):
    id: int
    model_config = { "from_attributes": True }