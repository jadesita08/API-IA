import psycopg2
from managers.conexionManager import ConexionManager
from models.ventaModel import Venta 

class VentasManager:
    def __init__(self):
        self.conn_manager = ConexionManager()
    
    def crear_venta(self, venta: Venta):
        try:
            conn = self.conn_manager.get_connection()
            if conn is None:
                return None
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO ventas (cliente_id, producto_id, cantidad, total) VALUES (%s, %s, %s, %s) RETURNING id",
                    (venta.cliente_id, venta.producto_id, venta.cantidad, venta.total)
                )
                venta_id = cursor.fetchone()[0]
                conn.commit()
            conn.close()
            return venta_id
        except psycopg2.Error as e:
            print("Error en crear_venta:", e)
            return None
    
    def obtener_ventas(self):
        try:
            conn = self.conn_manager.get_connection()
            if conn is None:
                return []
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, cliente_id, producto_id, cantidad, total, fecha_venta FROM ventas")
                column_names = [desc[0] for desc in cursor.description]
                ventas = []
                for row in cursor.fetchall():
                    venta_dict = dict(zip(column_names, row))
                    if 'fecha_venta' in venta_dict and venta_dict['fecha
