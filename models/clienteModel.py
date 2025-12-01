from pydantic import BaseModel  # Importa BaseModel de Pydantic para validar datos

class Cliente(BaseModel):
    # Esquema de la entidad Cliente.
    # FastAPI usará este modelo para validar requests/responses.
    nombre: str    # Nombre del cliente
    email: str     # Email del cliente
    telefono: str  # Teléfono de contacto del cliente
