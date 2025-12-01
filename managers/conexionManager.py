import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class ConexionManager:
    def __init__(self):
        # Obtiene la URL de conexión desde .env
        self.db_url = os.getenv('URLDATABASE')
        
    def get_connection(self):
        """Establece la conexión a PostgreSQL. Lanza error si falla."""
        try:
            conn = psycopg2.connect(self.db_url)
            return conn
        except psycopg2.Error as e:
            print("Error de conexión a la base de datos:", e)
            return None
