from database import Database
from models.cliente import Cliente
from models.auto import Auto
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
