class Venta:
    def __init__(self, id_venta, id_auto, id_cliente, fecha, id_vendedor):
        self.id_venta = id_venta
        self.id_auto = id_auto
        self.id_cliente = id_cliente
        self.fecha = fecha
        self.id_vendedor = id_vendedor

    def __str__(self):
        return f"{self.id_venta} - Auto: {self.id_auto} - Cliente: {self.id_cliente}  - {self.fecha} - Vendedor: {self.id_vendedor}"