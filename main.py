from fastapi import FastAPI
from dotenv import load_dotenv
from routes import clienteRouter, productoRouter, ventaRouter, marcaRouter

load_dotenv() 

app = FastAPI(
    title="API de Maquillaje",
    version="1.0.0"
)

app.include_router(clienteRouter.router, prefix="/clientes", tags=["Clientes"])
app.include_router(productoRouter.router, prefix="/productos", tags=["Productos"])
app.include_router(ventaRouter.router, prefix="/ventas", tags=["Ventas"])

@app.get("/", tags=["Root"])
def read_root():
    return {"mensaje": "Bienvenido a la API de Maquillaje"}
