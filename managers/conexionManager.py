import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class ConexionManager:
    @staticmethod
    def obtener_conexion():
        url = os.getenv("URLDATABASE")
        if not url:
            raise Exception("No se encontró la variable de entorno URLDATABASE")
        return psycopg2.connect(url)
