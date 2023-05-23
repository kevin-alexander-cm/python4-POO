from dataclasses import dataclass
from datetime import datetime


class Usuario:

    user_id: int
    rut: str
    contrasenia: str

    def __init__(self, user_id: int, rut: str, contrasenia: str):
        self.user_id = user_id
        self.rut = rut
        self.contrasenia = contrasenia

    def __repr__(self):
        imprimir = "==============================================\n"
        imprimir = imprimir + f"User ID = {self.user_id}\n" 
        imprimir = imprimir + f"Rut = {self.rut}\n"
        return imprimir