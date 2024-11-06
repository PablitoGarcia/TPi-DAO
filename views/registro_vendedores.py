# views/registro_vendedor.py
import tkinter as tk
from models.cliente import Vendedor
from models.Observer.Sujeto import Sujeto

class RegistroVendedor(tk.Frame,Sujeto):
    def __init__(self, master, sistema):
        super().__init__(master)
        Sujeto.__init__(self)
        self.sistema = sistema
        self.master = master
        #self.title("Registrar Vendedor")
        
        # Campos de entrada
        tk.Label(self, text="ID Vendedor:").grid(row=0, column=0)
        self.id_vendedor_entry = tk.Entry(self)
        self.id_vendedor_entry.grid(row=0, column=1)
        
        tk.Label(self, text="Nombre:").grid(row=1, column=0)
        self.nombre_vendedor_entry = tk.Entry(self)
        self.nombre_vendedor_entry.grid(row=1, column=1)
        
        tk.Label(self, text="Apellido:").grid(row=2, column=0)
        self.apellido_vendedor_entry = tk.Entry(self)
        self.apellido_vendedor_entry.grid(row=2, column=1)
        
        tk.Label(self, text="Comision:").grid(row=3, column=0)
        self.comision_vendedor_entry = tk.Entry(self)
        self.comision_vendedor_entry.grid(row=3, column=1)
        
        # Botón de registrar
        tk.Button(self, text="Registrar Vendedor", command=self.registrar_vendedor).grid(row=5, column=0, columnspan=2)
        
     
        # Mensaje de confirmación
        self.message_label = tk.Label(self, text="", fg="green")
        self.message_label.grid(row=6, column=0, columnspan=2)

        
    
    def registrar_vendedor(self):
        id_vendedor = self.id_vendedor_entry.get()
        nombre = self.nombre_vendedor_entry.get()
        apellido = self.apellido_vendedor_entry.get()
        comision = self.comision_vendedor_entry.get()
        
        nuevo_vendedor = Vendedor(id_vendedor, nombre, apellido, comision)
        mensaje = self.sistema.registrar_vendedor(nuevo_vendedor)
        self.message_label.config(text=mensaje)

        self.notificar()
        
        # Limpiar entradas
        self.id_vendedor_entry.delete(0, tk.END)
        self.nombre_vendedor_entry.delete(0, tk.END)
        self.apellido_vendedor_entry.delete(0, tk.END)
        self.comision_vendedor_entry.delete(0, tk.END)

        