from managers.conexionManager import ConexionManager
from models.clienteModel import ClienteModel

class ClientesManager:
    @staticmethod
    def listar_clientes():
        conn = ConexionManager.obtener_conexion()
        cur = conn.cursor()
        cur.execute("SELECT id, nombre, correo FROM clientes")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [{"id": r[0], "nombre": r[1], "correo": r[2]} for r in rows]

    @staticmethod
    def crear_cliente(cliente: ClienteModel):
        conn = ConexionManager.obtener_conexion()
        cur = conn.cursor()
        cur.execute("INSERT INTO clientes (nombre, correo) VALUES (%s, %s) RETURNING id",
                    (cliente.nombre, cliente.correo))
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return {"id": id, "nombre": cliente.nombre, "correo": cliente.correo}
