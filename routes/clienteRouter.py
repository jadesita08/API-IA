from fastapi import APIRouter, HTTPException, status
# APIRouter: crea un grupo de endpoints para clientes
# HTTPException: permite manejar y devolver errores HTTP controlados
# status: enum con códigos de estado HTTP

from managers.clientesManager import ClientesManager  # Lógica de negocio y acceso a datos para clientes
from models.clienteModel import Cliente               # Modelo Pydantic para validar la entrada/salida

router = APIRouter()          # Instancia del router específico para clientes
manager = ClientesManager()   # Instancia del manager que realiza las operaciones (CRUD)

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_cliente(cliente: Cliente):
    """Crea un nuevo cliente."""
    # Recibe un objeto Cliente validado por Pydantic.
    # Llama al manager para crear el cliente en la base de datos.
    try:
        cliente_id = manager.crear_cliente(cliente)  # Intenta insertar en DB y devuelve el ID creado
        if cliente_id is None:
             # Si no hay ID, se asume un fallo de conexión o error al crear
             raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Fallo de conexión o error al crear cliente.")
        # Respuesta estándar con el ID y un mensaje
        return {"id": cliente_id, "mensaje": "Cliente creado exitosamente"}
    except Exception as e:
        # Errores de validación/entrada se devuelven como 400
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al crear cliente: {e}")

@router.get("/")
def obtener_clientes():
    """Obtiene la lista completa de clientes."""
    # Llama al manager para traer todos los clientes y los retorna tal cual.
    try:
        clientes = manager.obtener_clientes()
        return clientes
    except Exception as e:
        # Errores del servidor (DB, conexión, etc.)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al obtener clientes: {e}")

@router.put("/{cliente_id}")
def actualizar_cliente(cliente_id: int, cliente: Cliente):
    """Actualiza un cliente existente."""
    # Recibe el ID del cliente y los nuevos datos validados.
    try:
        if not manager.actualizar_cliente(cliente_id, cliente):
            # Si no se actualiza, se devuelve 404 (no encontrado o sin cambios)
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado o datos no actualizados")
        return {"mensaje": f"Cliente con ID {cliente_id} actualizado exitosamente"}
    except Exception as e:
        # Errores de entrada/validación se devuelven como 400
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error al actualizar cliente: {e}")

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_cliente(cliente_id: int):
    """Elimina un cliente."""
    # Elimina por ID y retorna 204 (sin contenido) si todo va bien.
    try:
        if not manager.eliminar_cliente(cliente_id):
            # Si no se encuentra el cliente, 404
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
        return  # 204 implica respuesta vacía
    except Exception as e:
        # Errores del servidor
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar cliente: {e}")

