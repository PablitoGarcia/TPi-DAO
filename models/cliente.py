from abc import ABC, abstractmethod

class Persona:
    def __init__(self, id_cliente, nombre, apellido):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.id_cliente} - {self.nombre} {self.apellido}"

class Cliente(Persona):
    def __init__(self, id_cliente, nombre, apellido, direccion, telefono):
        super().__init__(id_cliente, nombre, apellido)
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"{self.id_cliente} - {self.nombre} {self.apellido} - {self.direccion} - {self.telefono}"
    

class Vendedor(Persona):
    def __init__(self, id_vendedor, nombre, apellido, comision):
        super().__init__(id_vendedor, nombre, apellido)
        self.comision = comision

    def __str__(self):
        return f"{self.id_cliente} - {self.nombre} {self.apellido} - {self.comision} "