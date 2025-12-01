  from pydantic import BaseModel  # Importa BaseModel para crear modelos de datos

class Marca(BaseModel):
    # Esquema de la entidad Marca.
    # Útil para validar y documentar la API en FastAPI.
    nombre: str  # Nombre de la marca
    pais: str    # País de origen de la marca
