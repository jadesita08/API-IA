from fastapi import APIRouter, HTTPException, status
# APIRouter: agrupa endpoints para productos
# HTTPException/status: manejo de errores y respuestas

from managers.productosManager import ProductosManager  # Lógica y acceso a datos de productos
from models.productoModel import Producto               # Esquema de validación de producto

router = APIRouter()          # Router dedicado a productos
manager = ProductosManager()  # Manager que implementa el CRUD

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_producto(producto: Producto):
    """Crea un nuevo producto."""
    # Inserta un producto en la base y retorna su ID si fue creado.
    try:
        producto_id = manager.crear_producto(producto)
        if producto_id is None:
             # Error interno si la creación falla
             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Fallo de conexión o error al crear producto.")
        return {"id": producto_id, "mensaje": "Producto creado exitosamente"}
    except Exception as e:
        # Errores de entrada/validación
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear producto: {e}")

@router.get("/")
def obtener_productos():
    """Obtiene la lista completa de producttos."""
    # Retorna el listado de productos desde el manager.
    try:
        productos = manager.obtener_productos()
        return productos
    except Exception as e:
        # Error del servidor/DB
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al obtener productos: {e}")

@router.put("/{producto_id}")
def actualizar_producto(producto_id: int, producto: Producto):
    """Actualiza un producto existente."""
    # Actualiza los datos del producto indicado por ID.
    try:
        if not manager.actualizar_producto(producto_id, producto):
            # 404 si no existe o no hubo cambios
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado o datos no actualizados")
        return {"mensaje": f"Producto con ID {producto_id} actualizado exitosamente"}
    except Exception as e:
        # Errores de entrada/validación
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar producto: {e}")

@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(producto_id: int):
    """Elimina un producto."""
    # Elimina por ID y responde 204 si se logró.
    try:
        if not manager.eliminar_producto(producto_id):
            # 404 si no se encuentra
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
        return  # 204 No Content
    except Exception as e:
        # Error del servidor
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar producto: {e}")

