from fastapi import APIRouter, HTTPException, status
from ..managers.clientesManager import ClientesManager
from models.clienteModel import Cliente 

router = APIRouter()
manager = ClientesManager()

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_cliente(cliente: Cliente):
    """Crea un nuevo cliente."""
    try:
        cliente_id = manager.crear_cliente(cliente)
        if cliente_id is None:
             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Fallo de conexión o error al crear cliente.")
        return {"id": cliente_id, "mensaje": "Cliente creado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear cliente: {e}")

@router.get("/")
def obtener_clientes():
    """Obtiene la lista completa de clientes."""
    try:
        clientes = manager.obtener_clientes()
        return clientes
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al obtener clientes: {e}")

@router.put("/{cliente_id}")
def actualizar_cliente(cliente_id: int, cliente: Cliente):
    """Actualiza un cliente existente."""
    try:
        if not manager.actualizar_cliente(cliente_id, cliente):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado o datos no actualizados")
        return {"mensaje": f"Cliente con ID {cliente_id} actualizado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar cliente: {e}")

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_cliente(cliente_id: int):
    """Elimina un cliente."""
    try:
        if not manager.eliminar_cliente(cliente_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
        return
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar cliente: {e}")
