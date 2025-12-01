from managers.conexionManager import ConexionManager
from models.ventaModel import VentaModel

class VentasManager:
    @staticmethod
    def listar_ventas():
        conn = ConexionManager.obtener_conexion()
        cur = conn.cursor()
        cur.execute("SELECT id, cliente_id, producto_id, cantidad FROM ventas")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [{"id": r[0], "cliente_id": r[1], "producto_id": r[2], "cantidad": r[3]} for r in rows]

    @staticmethod
    def crear_venta(venta: VentaModel):
        conn = ConexionManager.obtener_conexion()
        cur = conn.cursor()
        cur.execute("INSERT INTO ventas (cliente_id, producto_id, cantidad) VALUES (%s, %s, %s) RETURNING id",
                    (venta.cliente_id, venta.producto_id, venta.cantidad))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return {"id": id, "cliente_id": venta.cliente_id, "producto_id": venta.producto_id, "cantidad": venta.cantidad}

