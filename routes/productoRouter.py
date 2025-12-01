from fastapi import APIRouter
from managers.productosManager import ProductosManager
from models.productoModel import ProductoModel

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/")
def listar_productos():
    return ProductosManager.listar_productos()

@router.post("/")
def crear_producto(producto: ProductoModel):
    return ProductosManager.crear_producto(producto)
