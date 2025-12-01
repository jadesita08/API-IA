from pydantic import BaseModel

class MarcaModel(BaseModel):
    id: int | None = None
    nombre: str
