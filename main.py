from fastapi import FastAPI
from routes import clienteRouter, marcaRouter, productoRouter, ventaRouter

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}

app.include_router(clienteRouter.router)
app.include_router(marcaRouter.router)
app.include_router(productoRouter.router)
app.include_router(ventaRouter.router)
