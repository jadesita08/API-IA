from fastapi import APIRouter
from managers.marcasManager import MarcasManager
from models.marcaModel import MarcaModel

router = APIRouter(prefix="/marcas", tags=["Marcas"])

@router.get("/")
def listar_marcas():
    return MarcasManager.listar_marcas()

@router.post("/")
def crear_marca(marca: MarcaModel):
    return MarcasManager.crear_marca(marca)
