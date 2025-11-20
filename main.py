from fastapi import FastAPI
from dotenv import load_dotenv


from routes.clienteRouter import router as clienteRouter
from routes.productoRouter import router as productoRouter
from routes.ventaRouter import router as ventaRouter
from routes.marcaRouter import router as marcaRouter

load_dotenv() 

app = FastAPI(
    title="API de Maquillaje",
    version="1.0.0"
)

app.include_router(clienteRouter, prefix="/clientes", tags=["Clientes"])
app.include_router(productoRouter, prefix="/productos", tags=["Productos"])
app.include_router(ventaRouter, prefix="/ventas", tags=["Ventas"])
app.include_router(marcaRouter, prefix="/marcas", tags=["Marcas"])

@app.get("/", tags=["Root"])
def read_root():
    return {"mensaje": "Bienvenido a la API de Maquillaje"}
