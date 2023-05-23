from datetime import datetime
import json
import requests
from Persona import Persona
from Usuario import Usuario
from Venta import Venta
from DAOPersona import DAOPersona
from DAOUsuario import DAOUsuario
from DAOVenta import DAOVenta


archivo = open('ventas.json')
data1 = json.load(archivo)
archivo.close()

r1 = requests.get('https://csarivan.000webhostapp.com/repositorios/personas.json')
data2 = r1.json()

r2 = requests.get('https://csarivan.000webhostapp.com/repositorios/usuarios.json')
data3 = r2.json()

daoPersonas = DAOPersona()
for fila in data2:
    pers = Persona(fila['rut'], fila['nombre'], fila['direccion'], fila['fechaNacimiento'], fila['comuna'], fila['correoElectronico'])
    daoPersonas.insertarPersona(pers)

listarPers = daoPersonas.listaPersonas()

for pers in listarPers:
    print(pers)

daoUsuarios = DAOUsuario()
for fila in data3:
    user = Usuario(fila ['id'], fila['rut'], fila['pass'])
    daoUsuarios.insertarUsuario(user)

listarUsers = daoUsuarios.listaUsuarios()
for user in listarUsers:
    print(user)

daoVentas = DAOVenta()
for fila in data1:
    fecha = fila['fechaVenta'].split('-')
    fecha = datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]))
    ven = Venta(fila['idVenta'], fecha, fila['valorNeto'], fila['rutVendedor'])
    daoVentas.insertarVenta(ven)

listarVentas = daoVentas.listaVentas()
for venta in listarVentas:
    print(venta)    