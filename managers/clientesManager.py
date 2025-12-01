import psycopg2
from managers.conexionManager import ConexionManager
from models.clienteModel import Cliente 

class ClientesManager:
    def __init__(self):
        self.conn_manager = ConexionManager()
    
    def crear_cliente(self, cliente: Cliente):
        try:
            conn = self.conn_manager.get_connection()
            if conn is None:
                return None
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s) RETURNING id",
                    (cliente.nombre, cliente.email, cliente.telefono)
                )
                cliente_id = cursor.fetchone()[0]
                conn.commit()
            conn.close()
            return cliente_id
        except psycopg2.Error as e:
            print("Error en crear_cliente:", e)
            return None
    
    def obtener_clientes(self):
        try:
            conn = self.conn_manager.get_connection()
            if conn is None:
                return []
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nombre, email, telefono FROM clientes")
                column_names = [desc[0] for desc in cursor.description]
                clientes = [dict(zip(column_names, row)) for row in cursor.fetchall()]
            conn.close()
            return clientes
        except psycopg2.Error as e:
            print("Error en obtener_clientes:", e)
            return []
    
    def actualizar_cliente(self, cliente_id: int, cliente: Cliente):
        try:
            conn = self.conn_manager.get_connection()
            if conn is None:
                return False
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE clientes SET nombre = %s, email = %s, telefono = %s WHERE id = %s",
                    (cliente.nombre, cliente.email, cliente.telefono, cliente_id)
                )
                updated_rows = cursor.rowcount
                conn.commit()
            conn.close()
            return updated_rows > 0
        except psycopg2.Error as e:
            print("Error en actualizar_cliente:", e)
            return False
    
    def eliminar_cliente(self, cliente_id: int):
        try:
            conn = self.conn_manager.get_connection()
            if conn is None:
                return False
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
                deleted_rows = cursor.rowcount
                conn.commit()
            conn.close()
            return deleted_rows > 0
        except psycopg2.Error as e:
            print("Error en eliminar_cliente:", e)
            return False
