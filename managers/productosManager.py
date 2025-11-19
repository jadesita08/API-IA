import psycopg
from managers.conexionManager import ConexionManager
from models.productoModel import Producto 

class ProductosManager:
    def __init__(self):
        self.conn_manager = ConexionManager()
    
    def crear_producto(self, producto: Producto):
        """Crea un nuevo producto, referenciando marca_id."""
        try:
            conn = self.conn_manager.get_connection()
            if conn is None: return None
            
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO productos (nombre, marca_id, categoria, precio, stock) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                (producto.nombre, producto.marca_id, producto.categoria, producto.precio, producto.stock)
            )
            producto_id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            conn.close()
            return producto_id
        except psycopg.Error:
            return None
    
    def obtener_productos(self):
        """Obtiene la lista de productos."""
        try:
            conn = self.conn_manager.get_connection()
            if conn is None: return []

            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, marca_id, categoria, precio, stock FROM productos")
            
            column_names = [desc[0] for desc in cursor.description]
            productos = [dict(zip(column_names, row)) for row in cursor.fetchall()]
                
            cursor.close()
            conn.close()
            return productos
        except psycopg.Error:
            return []
    
    def actualizar_producto(self, producto_id: int, producto: Producto):
        """Actualiza un producto existente."""
        try:
            conn = self.conn_manager.get_connection()
            if conn is None: return False
            
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE productos SET nombre = %s, marca_id = %s, categoria = %s, precio = %s, stock = %s WHERE id = %s",
                (producto.nombre, producto.marca_id, producto.categoria, producto.precio, producto.stock, producto_id)
            )
            updated_rows = cursor.rowcount
            conn.commit()
            cursor.close()
            conn.close()
            return updated_rows > 0
        except psycopg.Error:
            return False
    
    def eliminar_producto(self, producto_id: int):
        """Elimina un producto."""
        try:
            conn = self.conn_manager.get_connection()
            if conn is None: return False
            
            cursor = conn.cursor()
            cursor.execute("DELETE FROM productos WHERE id = %s", (producto_id,))
            deleted_rows = cursor.rowcount
            conn.commit()
            cursor.close()
            conn.close()
            return deleted_rows > 0
        except psycopg.Error:
            return False