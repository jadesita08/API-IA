from fastapi import APIRouter
from managers.ventasManager import VentasManager
from models.ventaModel import VentaModel

router = APIRouter(prefix="/ventas", tags=["Ventas"])

@router.get("/")
def listar_ventas():
    return VentasManager.listar_ventas()

@router.post("/")
def crear_venta(venta: VentaModel):
    return VentasManager.crear_venta(venta)
