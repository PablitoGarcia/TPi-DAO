from database import Database
from models.cliente import Cliente
from models.cliente import Vendedor
from models.venta import Venta
from models.auto import Auto
from models.servicio import Servicio
from models.singleton import Singleton

class GestorSistema:
    def __init__(self):
        self.db = Database()
       
    
    #CLIENTES
    
    def registrar_cliente(self,cliente:Cliente):
        
        try:
            self.db.agregar_cliente(cliente.id_cliente,cliente.nombre,cliente.apellido,cliente.direccion,cliente.telefono)
            return f"Cliente registrado con éxito."
        except Exception as e:
            return f"Error: {e}"
            
        

    def listar_clientes(self):
        return self.db.get_clientes()
    

    #AUTOS
    def registrar_auto(self,auto:Auto):
        
        try:
            self.db.agregar_auto(auto.vin,auto.marca,auto.modelo,auto.anio,auto.precio,auto.estado,auto.idCliente)
            return f"Auto registrado con éxito."
        except Exception as e:
            return f"Error: {e}"
    
    def listar_autos(self):
        return self.db.get_autos()


    #VENDEDORES    
    def registrar_vendedor(self,vendedor:Vendedor):
        
        try:
            self.db.agregar_vendedor(vendedor.id_cliente,vendedor.nombre,vendedor.apellido,vendedor.comision)
            return f"Vendedor registrado con éxito."
        except Exception as e:
            return f"Error: {e}"
            
        

    def listar_vendedores(self):
        return self.db.get_vendedores()
    
    
    #VENTAS    
    def registrar_venta(self,venta:Venta):
        
        try:
            self.db.agregar_venta(venta.id_venta,venta.id_auto,venta.id_cliente,venta.fecha,venta.id_vendedor)
            return f"Venta registrada con éxito."
        except Exception as e:
            return f"Error: {e}"
            
        

    def listar_ventas(self, id_cliente=None):
        if id_cliente is None:
            return self.db.get_ventas()
        else:
            return self.db.get_ventas_cliente(id_cliente)
        
        
        
    def registrar_servicio(self, servicio:Servicio):
        
        try:
            self.db.agregar_servicio(servicio.id_servicio, servicio.id_auto, servicio.tipo_servicio, servicio.fecha, servicio.costo)
            return f"Servicio registrado con éxito."
        except Exception as e:
            return f"Error: {e}"
        
     
    def listar_servicios(self, id_auto=None):
        if id_auto is None:
            return self.db.get_servicios()
        else:
            return self.db.get_servicios_cliente(id_auto)
    
