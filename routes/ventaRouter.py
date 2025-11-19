from fastapi import APIRouter, HTTPException, status
from managers.ventasManager import VentasManager
from models.ventaModel import Venta 

router = APIRouter()
manager = VentasManager()

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_venta(venta: Venta):
    """Crea una nueva venta."""
    try:
        venta_id = manager.crear_venta(venta)
        if venta_id is None:
             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Fallo de conexión o error al crear venta.")
        return {"id": venta_id, "mensaje": "Venta creada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear venta: {e}")

@router.get("/")
def obtener_ventas():
    """Obtiene la lista completa de ventas."""
    try:
        ventas = manager.obtener_ventas()
        return ventas
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al obtener ventas: {e}")

@router.put("/{venta_id}")
def actualizar_venta(venta_id: int, venta: Venta):
    """Actualiza una venta existente."""
    try:
        if not manager.actualizar_venta(venta_id, venta):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrada o datos no actualizados")
        return {"mensaje": f"Venta con ID {venta_id} actualizada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar venta: {e}")

@router.delete("/{venta_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_venta(venta_id: int):
    """Elimina una venta."""
    try:
        if not manager.eliminar_venta(venta_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrada")
        return
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar venta: {e}")