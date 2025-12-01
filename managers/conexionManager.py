import psycopg
import os
from dotenv import load_dotenv

load_dotenv() 

class ConexionManager:
    def __init__(self):
        # Obtiene la URL de conexión
        self.db_url = os.getenv('URLDATABASE')
        
    def get_connection(self):
        """Establece la conexión a PostgreSQL. Lanza error si falla."""
        try:
            conn = psycopg.connect(self.db_url)
            return conn
        except psycopg.Error:
            # En caso de error, retorna None para ser manejado en los Managers
            return None
