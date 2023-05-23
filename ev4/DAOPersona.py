from Persona import Persona;
import mysql.connector
from dataclasses import dataclass

@dataclass
class DAOPersona:
    def insertarPersona(self, Persona:Persona):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = "insert into personas values (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(Persona.rut, Persona.nombre, Persona.direccion, Persona.fecha_nacimiento, Persona.comuna, Persona.correo_electronico))
        conector.commit()
        conector.close()
    
    def actualizarPersona(self, Persona:Persona):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = "update personas set nombre = %s, direccion = %s, fecha_nacimiento = %s, comuna = %s, correo_electronico %s where rut = %s"
        cursor.execute(sql,(Persona.rut, Persona.nombre, Persona.direccion, Persona.fecha_nacimiento, Persona.comuna, Persona.correo_electronico))
        conector.commit()
        conector.close()

    def eliminarPersona(self, Persona:Persona):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = f"delete from personas where rut = '{Persona.rut}'"
        cursor.execute(sql)
        conector.commit()
        conector.close()
    

    def buscarPersona(self, rut:str):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = f"select * from personas where rut like '{rut}'"
        cursor.execute(sql)
        fila = cursor.fetchone()
        prod = Persona(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
        conector.close()
        return prod

    def listaPersonas(self):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = "select * from personas"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        listaProd = list()
        conector.close()
        for fila in resultados: 
            prod = Persona(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            listaProd.append(prod)
        return listaProd