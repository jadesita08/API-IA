from pydantic import BaseModel

class ClienteModel(BaseModel):
    id: int | None = None
    nombre: str
    correo: str
