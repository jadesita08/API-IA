from pydantic import BaseModel  # Base para modelos de datos con validación

class Producto(BaseModel):
    # Modelo de datos para productos.
    # FastAPI usará este esquema para validar requests/responses.
    nombre: str        # Nombre del producto
    marca_id: int      # ID de la marca asociada (relación con Marca)
    categoria: str     # Categoría del producto (ej. "labial", "base")
    precio: float      # Precio del producto
    stock: int         # Cantidad disponible en inventario
