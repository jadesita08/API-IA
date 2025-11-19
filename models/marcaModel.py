from pydantic import BaseModel

class Marca(BaseModel):
    nombre: str
    pais: str