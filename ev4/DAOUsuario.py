from Usuario import Usuario;
import mysql.connector
from dataclasses import dataclass

@dataclass
class DAOUsuario:
    def insertarUsuario(self, usuario: Usuario):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = "insert into usuarios values (%s, %s, %s)"
        cursor.execute(sql, (usuario.user_id, usuario.rut, usuario.contrasenia))
        conector.commit()
        conector.close()
    
    def actualizarUsuario(self, usuario: Usuario):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = "update usuarios set rut = %s, contrasenia = %s where user_id = %s"
        cursor.execute(sql, (usuario.user_id, usuario.rut, usuario.contrasenia))
        conector.commit()
        conector.close()

    def eliminarUsuario(self, usuario: Usuario):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = f"delete from usuarios where user_id = '{usuario.user_id}'"
        cursor.execute(sql)
        conector.commit()
        conector.close()
    

    def buscarUsuario(self, user_id: int):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = f"select * from usuarios where user_id like '{user_id}'"
        cursor.execute(sql)
        fila = cursor.fetchone()
        user = Usuario(fila[0], fila[1], fila[2])
        conector.close()
        return user

    def listaUsuarios(self):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = "select * from usuarios"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        listaUsers = list()
        conector.close()
        for fila in resultados: 
            prod = Usuario(fila[0], fila[1], fila[2])
            listaUsers.append(prod)
        return listaUsers