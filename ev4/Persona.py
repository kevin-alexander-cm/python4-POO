from dataclasses import dataclass
from datetime import datetime

@dataclass
class Persona:
    rut: str
    nombre: str
    direccion: str
    fecha_nacimiento: datetime
    comuna: str
    correo_electronico: str

    def __init__(self, rut: str, nombre: str, direccion: str, fecha_nacimiento: datetime, comuna: str, correo_electronico: str):
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.comuna = comuna
        self.correo_electronico = correo_electronico

    def __repr__(self):
        imprimir = "==============================================\n"
        imprimir = imprimir + f"Rut = {self.rut}\n" 
        imprimir = imprimir + f"Nombre = {self.nombre}\n"
        imprimir = imprimir + f"Dirección = {self.direccion}\n"
        imprimir = imprimir + f"Fecha Nacimiento= {self.fecha_nacimiento}\n"
        imprimir = imprimir + f"Comuna = {self.comuna}\n"
        imprimir = imprimir + f"Correo Eléctronico= {self.correo_electronico}\n"
        return imprimir 
