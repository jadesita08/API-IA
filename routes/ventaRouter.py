from fastapi import APIRouter, HTTPException, status
# APIRouter: agrupa endpoints de ventas
# HTTPException/status: manejo de errores y códigos de respuesta

from managers.ventasManager import VentasManager  # Lógica y acceso a datos de ventas
from models.ventaModel import Venta               # Esquema de validación de ventas

router = APIRouter()       # Router dedicado a ventas
manager = VentasManager()  # Manager que implementa operaciones sobre ventas

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_venta(venta: Venta):
    """Crea una nueva venta."""
    # Inserta una venta y devuelve el ID de la transacción.
    try:
        venta_id = manager.crear_venta(venta)
        if venta_id is None:
            # Error interno en caso de fallo al crear
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Fallo de conexión o error al crear venta.")
        return {"id": venta_id, "mensaje": "Venta creada exitosamente"}
    except Exception as e:
        # Errores de entrada/validación
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear venta: {e}")

@router.get("/")
def obtener_ventas():
    """Obtiene la lista completa de ventas."""
    # Trae todas las ventas desde el manager.
    try:
        ventas = manager.obtener_ventas()
        return ventas
    except Exception as e:
        # Error del servidor/DB
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al obtener ventas: {e}")

@router.put("/{venta_id}")
def actualizar_venta(venta_id: int, venta: Venta):
    """Actualiza una venta existente."""
    # Actualiza la venta indicada por ID.
    try:
        if not manager.actualizar_venta(venta_id, venta):
            # 404 si no se encuentra o no hay cambios
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrada o datos no actualizados")
        return {"mensaje": f"Venta con ID {venta_id} actualizado exitosamente"}
    except Exception as e:
        # Errores de entrada/validación
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar venta: {e}")

@router.delete("/{venta_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_venta(venta_id: int):
    """Elimina una venta."""
    # Elimina por ID y retorna sin contenido si se logró.
    try:
        if not manager.eliminar_venta(venta_id):
            # 404 si no existe
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrada")
        return  # 204 No Content
    except Exception as e:
        # Error del servidor
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar venta: {e}")
