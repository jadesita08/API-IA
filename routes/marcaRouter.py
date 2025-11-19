from fastapi import APIRouter, HTTPException, status
from managers.marcasManager import MarcasManager
from models.marcaModel import Marca 

router = APIRouter()
manager = MarcasManager()

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_marca(marca: Marca):
    """Crea una nueva marca."""
    try:
        marca_id = manager.crear_marca(marca)
        if marca_id is None:
             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error de conexión o fallo al crear marca.")
        return {"id": marca_id, "mensaje": "Marca creada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear marca: {e}")

@router.get("/")
def obtener_marcas():
    """Obtiene la lista completa de todas las marcas."""
    try:
        marcas = manager.obtener_marcas()
        return marcas
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al obtener marcas: {e}")

@router.put("/{marca_id}")
def actualizar_marca(marca_id: int, marca: Marca):
    """Actualiza una marca existente."""
    try:
        if not manager.actualizar_marca(marca_id, marca):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Marca no encontrada o datos no actualizados")
        return {"mensaje": f"Marca con ID {marca_id} actualizada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar marca: {e}")

@router.delete("/{marca_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_marca(marca_id: int):
    """Elimina una marca."""
    try:
        if not manager.eliminar_marca(marca_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Marca no encontrada")
        return
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar marca: {e}")