class Auto:
    def __init__(self, vin, marca, modelo, anio, precio,estado):
        self.vin = vin
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        self.estado = estado
        self.idCliente = None
    def __str__(self):
        return f"{self.vin} - {self.marca} {self.modelo} ({self.anio}) - ${self.precio} - Cliente: {self.idCliente} - {self.estadoVenta}"
    
    