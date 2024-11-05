class Cliente:
    def __init__(self, id_cliente, nombre, apellido, direccion, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"{self.id_cliente} - {self.nombre} {self.apellido} - {self.direccion} - {self.telefono}"