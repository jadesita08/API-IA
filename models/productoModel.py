from pydantic import BaseModel

class Producto(BaseModel):
    nombre: str
    marca_id: int 
    categoria: str
    precio: float
    stock: int