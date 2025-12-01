from fastapi import FastAPI  # Framework para crear la API
from dotenv import load_dotenv  # Carga variables de entorno desde .env

from routes.clienteRouter import router as clienteRouter  # Router de clientes
from routes.productoRouter import router as productoRouter  # Router de productos
from routes.ventaRouter import router as ventaRouter  # Router de ventas
from routes.marcaRouter import router as marcaRouter  # Router de marcas

# Inicializa la carga de variables de entorno (ej. credenciales DB, etc.)
load_dotenv()

# Instancia de la aplicación FastAPI
app = FastAPI(
    title="API de Maquillaje",  # Título mostrado en la documentación automática (Swagger)
    version="1.0.0"  # Versión de la API
)

# Registro de routers: organiza endpoints por entidad con prefijos y etiquetas
app.include_router(clienteRouter, prefix="/clientes", tags=["Clientes"])
app.include_router(productoRouter, prefix="/productos", tags=["Productos"])
app.include_router(ventaRouter, prefix="/ventas", tags=["Ventas"])
app.include_router(marcaRouter, prefix="/marcas", tags=["Marcas"])

@app.get("/", tags=["Root"])
def read_root():
    # Endpoint raíz para verificar que el servicio está corriendo
    return {"mensaje": "Bienvenido a la API de Maquillaje"}
