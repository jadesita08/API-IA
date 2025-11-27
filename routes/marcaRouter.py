from fastapi import APIRouter, HTTPException, status
# APIRouter: agrupa endpoints de marcas
# HTTPException/status: manejo de errores y códigos de estado

from managers.marcasManager import MarcasManager  # Acceso a datos/lógica de marcas
from models.marcaModel import Marca               # Modelo Pydantic para validar datos

router = APIRouter()       # Router dedicado a marcas
manager = MarcasManager()  # Manager que implementa CRUD contra la base

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_marca(marca: Marca):
    """Crea una nueva marca."""
    # Inserta una marca y devuelve su ID si se crea correctamente.
    try:
        marca_id = manager.crear_marca(marca)
        if marca_id is None:
             # Manejo de error interno si no se pudo crear
             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error de conexión o fallo al crear marca.")
        return {"id": marca_id, "mensaje": "Marca creada exitosamente"}
    except Exception as e:
        # Errores del lado del cliente (datos inválidos, etc.)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear marca: {e}")

@router.get("/")
def obtener_marcas():
    """Obtiene la lista completa de todas las marcas."""
    # Listado de marcas desde el manager.
    try:
        marcas = manager.obtener_marcas()
        return marcas
    except Exception as e:
        # Errores del servidor/DB
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al obtener marcas: {e}")

@router.put("/{marca_id}")
def actualizar_marca(marca_id: int, marca: Marca):
    """Actualiza una marca existente."""
    # Actualiza los datos de la marca indicada por ID.
    try:
        if not manager.actualizar_marca(marca_id, marca):
            # 404 si no se encuentra o no se realizaron cambios
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Marca no encontrada o datos no actualizados")
        return {"mensaje": f"Marca con ID {marca_id} actualizada exitosamente"}
    except Exception as e:
        # Errores de entrada/validación
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar marca: {e}")

@router.delete("/{marca_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_marca(marca_id: int):
    """Elimina una marca."""
    # Elimina por ID y retorna sin cuerpo (204).
    try:
        if not manager.eliminar_marca(marca_id):
            # No encontrado
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Marca no encontrada")
        return  # 204 No Content
    except Exception as e:
        # Error del servidor
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar marca: {e}")

