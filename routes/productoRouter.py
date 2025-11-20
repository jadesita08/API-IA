from fastapi import APIRouter, HTTPException, status
from managers.productosManager import ProductosManager
from models.productoModel import Producto 


router = APIRouter()
manager = ProductosManager()
ia_manager = RecomendacionManager()

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_producto(producto: Producto):
    """Crea un nuevo producto."""
    try:
        producto_id = manager.crear_producto(producto)
        if producto_id is None:
             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Fallo de conexión o error al crear producto.")
        return {"id": producto_id, "mensaje": "Producto creado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear producto: {e}")

@router.get("/")
def obtener_productos():
    """Obtiene la lista completa de productos."""
    try:
        productos = manager.obtener_productos()
        return productos
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al obtener productos: {e}")

@router.put("/{producto_id}")
def actualizar_producto(producto_id: int, producto: Producto):
    """Actualiza un producto existente."""
    try:
        if not manager.actualizar_producto(producto_id, producto):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado o datos no actualizados")
        return {"mensaje": f"Producto con ID {producto_id} actualizado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar producto: {e}")

@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(producto_id: int):
    """Elimina un producto."""
    try:
        if not manager.eliminar_producto(producto_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
        return
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar producto: {e}")

@router.get("/recomendacion/{cliente_id}", tags=["IA"])
def obtener_recomendacion_ia(cliente_id: int):
    """Obtiene recomendaciones de IA para un cliente."""
    try:
        recomendaciones = ia_manager.obtener_recomendacion(cliente_id)
        return recomendaciones
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al obtener recomendación de IA: {e}")
