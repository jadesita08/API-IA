from managers.conexionManager import ConexionManager
from models.productoModel import ProductoModel

class ProductosManager:
    @staticmethod
    def listar_productos():
        conn = ConexionManager.obtener_conexion()
        cur = conn.cursor()
        cur.execute("SELECT id, nombre, precio, marca_id FROM productos")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [{"id": r[0], "nombre": r[1], "precio": r[2], "marca_id": r[3]} for r in rows]

    @staticmethod
    def crear_producto(producto: ProductoModel):
        conn = ConexionManager.obtener_conexion()
        cur = conn.cursor()
        cur.execute("INSERT INTO productos (nombre, precio, marca_id) VALUES (%s, %s, %s) RETURNING id",
                    (producto.nombre, producto.precio, producto.marca_id))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return {"id": id, "nombre": producto.nombre, "precio": producto.precio, "marca_id": producto.marca_id}
