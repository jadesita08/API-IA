from pydantic import BaseModel  # Base para definir modelos con validación

class Venta(BaseModel):
    # Esquema de la entidad Venta.
    # Representa una transacción entre cliente y producto.
    cliente_id: int  # ID del cliente que realiza la compra
    producto_id: int # ID del producto vendido
    cantidad: int    # Unidades vendidas del producto
    total: float     # Total de la venta (precio * cantidad)
