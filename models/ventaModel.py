from pydantic import BaseModel

class Venta(BaseModel):
    cliente_id: int
    producto_id: int
    cantidad: int
    total: float