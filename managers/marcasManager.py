import psycopg2
from managers.conexionManager import ConexionManager
from models.marcaModel import Marca 

class MarcasManager:
    def __init__(self):
        self.conn_manager = ConexionManager()
    
    def crear_marca(self, marca: Marca):
        try:
            conn = self.conn_manager.get_connection()
            if conn is None:
                return None
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO marcas (nombre, pais) VALUES (%s, %s) RETURNING id",
                    (marca.nombre, marca.pais)
                )
                marca_id = cursor.fetchone()[0]
                conn.commit()
            conn.close()
            return marca_id
        except psycopg2.Error as e:
            print("Error en crear_marca:", e)
            return None
    
    def obtener_marcas(self):
        try:
            conn = self.conn_manager.get_connection()
            if conn is None:
                return []
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nombre, pais FROM marcas")
                column_names = [desc[0] for desc in cursor.description]
                marcas = [dict(zip(column_names, row)) for row in cursor.fetchall()]
            conn.close()
            return marcas
        except psycopg2.Error as e:
            print("Error en obtener_marcas:", e)
            return []
    
    def actualizar_marca(self, marca_id: int, marca: Marca):
        try:
            conn = self.conn_manager.get_connection()
            if conn is None:
                return False
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE marcas SET nombre = %s, pais = %s WHERE id = %s",
                    (marca.nombre, marca.pais, marca_id)
                )
                updated_rows = cursor.rowcount
                conn.commit()
            conn.close()
            return updated_rows > 0
        except psycopg2.Error as e:
            print("Error en actualizar_marca:", e)
            return False
    
    def eliminar_marca(self, marca_id: int):
        try:
            conn = self.conn_manager.get_connection()
            if conn is None:
                return False
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM marcas WHERE id = %s", (marca_id,))
                deleted_rows = cursor.rowcount
                conn.commit()
            conn.close()
            return deleted_rows > 0
        except psycopg2.Error as e:
            print("Error en eliminar_marca:", e)
            return False
