from pydantic import BaseModel, EmailStr

class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    telefono: str
    email: EmailStr | None = None

class CrearCliente(ClienteBase):
    pass

class ClienteRespuesta(ClienteBase):
    id: int
    model_config = { "from_attributes": True }