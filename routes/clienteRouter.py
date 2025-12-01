from fastapi import APIRouter
from managers.clientesManager import ClientesManager
from models.clienteModel import ClienteModel

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
def listar_clientes():
    return ClientesManager.listar_clientes()

@router.post("/")
def crear_cliente(cliente: ClienteModel):
    return ClientesManager.crear_cliente(cliente)
