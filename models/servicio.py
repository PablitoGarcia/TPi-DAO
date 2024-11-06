class Servicio:
    def __init__(self, id_servicio, id_auto, tipo_servicio, fecha, costo):
        self.id_servicio = id_servicio
        self.id_auto = id_auto
        self.tipo_servicio = tipo_servicio
        self.fecha = fecha
        self.costo = costo
        
    def __str__(self):
        return f"{self.id_servicio} - auto: {self.id_auto} - {self.tipo_servicio} - {self.fecha} - ${self.costo}"
        