from pydantic import BaseModel

class VentaModel(BaseModel):
    id: int | None = None
    cliente_id: int
    producto_id: int
    cantidad: int
