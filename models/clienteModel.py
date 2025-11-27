from pydantic import BaseModel  # Importa BaseModel de Pydantic para validar datos

class Cliente(BaseModel):
    # Define el esquema de datos de un cliente.
    # Pydantic valida tipos y estructura automáticamente al recibir/retornar datos en FastAPI.
    nombre: str     # Nombre del cliente
    email: str      # Email del cliente (se puede validar formato si se usa EmailStr)
    telefono: str   # Teléfono de contacto del cliente
