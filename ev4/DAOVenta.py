from Venta import Venta;
import mysql.connector
from dataclasses import dataclass

@dataclass
class DAOVenta:
    def insertarVenta(self, venta: Venta):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = "insert into ventas values (%s, %s, %s, %s)"
        cursor.execute(sql, (venta.id_venta, venta.fecha_venta, venta.valor_neto, venta.rut_vendedor))
        conector.commit()
        conector.close()
    
    def actualizarVenta(self, venta: Venta):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = "update ventas set fecha_venta = %s, valor_neto = %s, rut_vendedor = %s where venta_id = %s"
        cursor.execute(sql, (venta.id_venta, venta.fecha_venta, venta.valor_neto, venta.rut_vendedor))
        conector.commit()
        conector.close()

    def eliminarVenta(self, venta: Venta):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = f"delete from ventas where venta_id = '{venta.venta_id}'"
        cursor.execute(sql)
        conector.commit()
        conector.close()
    

    def buscarVenta(self, venta_id: int):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = f"select * from ventas where venta_id like '{venta_id}'"
        cursor.execute(sql)
        fila = cursor.fetchone()
        user = Venta(fila[0], fila[1], fila[2], fila[3])
        conector.close()
        return user

    def listaVentas(self):
        conector = mysql.connector.connect(user="root", database="ventas_db", host="localhost",password="")
        cursor = conector.cursor()
        sql = "select * from ventas"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        listaVentas = list()
        conector.close()
        for fila in resultados: 
            prod = Venta(fila[0], fila[1], fila[2], fila[3])
            listaVentas.append(prod)
        return listaVentas