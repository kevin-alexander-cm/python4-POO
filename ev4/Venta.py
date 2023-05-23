from dataclasses import dataclass
from datetime import datetime

class Venta:

    id_venta: int
    fecha_venta: datetime
    valor_neto: int
    rut_vendedor: str

    def __init__(self, id_venta: int, fecha_venta: datetime, valor_neto: int, rut_vendedor: str):
        self.id_venta = id_venta
        self.fecha_venta = fecha_venta
        self.valor_neto = valor_neto
        self.rut_vendedor = rut_vendedor

    def __repr__(self):
        imprimir = "==============================================\n"
        imprimir = imprimir + f"Venta ID = {self.id_venta}\n" 
        imprimir = imprimir + f"Fecha Venta = {self.fecha_venta}\n"
        imprimir = imprimir + f"Valor Neto = {self.valor_neto}\n"
        imprimir = imprimir + f"Rut del Vendedor= {self.rut_vendedor}\n"
        return imprimir