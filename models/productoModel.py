from pydantic import BaseModel

class ProductoModel(BaseModel):
    id: int | None = None
    nombre: str
    precio: float
    marca_id: int
