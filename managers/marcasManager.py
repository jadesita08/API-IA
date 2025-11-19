import psycopg
from managers.conexionManager import ConexionManager
from models.marcaModel import Marca 

class MarcasManager:
    def __init__(self):
        self.conn_manager = ConexionManager()
    
    def crear_marca(self, marca: Marca):
        """Crea una nueva marca."""
        try:
            conn = self.conn_manager.get_connection()
            if conn is None: return None
            
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO marcas (nombre, pais) VALUES (%s, %s) RETURNING id",
                (marca.nombre, marca.pais)
            )
            marca_id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            conn.close()
            return marca_id
        except psycopg.Error:
            return None
    
    def obtener_marcas(self):
        """Obtiene todas las marcas."""
        try:
            conn = self.conn_manager.get_connection()
            if conn is None: return []

            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, pais FROM marcas")
            
            column_names = [desc[0] for desc in cursor.description]
            marcas = [dict(zip(column_names, row)) for row in cursor.fetchall()]
                
            cursor.close()
            conn.close()
            return marcas
        except psycopg.Error:
            return []
    
    def actualizar_marca(self, marca_id: int, marca: Marca):
        """Actualiza una marca existente."""
        try:
            conn = self.conn_manager.get_connection()
            if conn is None: return False
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE marcas SET nombre = %s, pais = %s WHERE id = %s",
                (marca.nombre, marca.pais, marca_id)
            )
            updated_rows = cursor.rowcount
            conn.commit()
            cursor.close()
            conn.close()
            return updated_rows > 0
        except psycopg.Error:
            return False

    def eliminar_marca(self, marca_id: int):
        """Elimina una marca."""
        try:
            conn = self.conn_manager.get_connection()
            if conn is None: return False
            cursor = conn.cursor()
            cursor.execute("DELETE FROM marcas WHERE id = %s", (marca_id,))
            deleted_rows = cursor.rowcount
            conn.commit()
            cursor.close()
            conn.close()
            return deleted_rows > 0
        except psycopg.Error:
            return False