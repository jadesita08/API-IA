from managers.conexionManager import ConexionManager
from models.marcaModel import MarcaModel

class MarcasManager:
    @staticmethod
    def listar_marcas():
        conn = ConexionManager.obtener_conexion()
        cur = conn.cursor()
        cur.execute("SELECT id, nombre FROM marcas")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [{"id": r[0], "nombre": r[1]} for r in rows]

    @staticmethod
    def crear_marca(marca: MarcaModel):
        conn = ConexionManager.obtener_conexion()
        cur = conn.cursor()
        cur.execute("INSERT INTO marcas (nombre) VALUES (%s) RETURNING id", (marca.nombre,))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return {"id": id, "nombre": marca.nombre}
