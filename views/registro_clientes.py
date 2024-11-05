# views/registro_cliente.py
import tkinter as tk
from models.cliente import Cliente

class RegistroCliente(tk.Frame):
    def __init__(self, master, sistema):
        super().__init__(master)
        self.sistema = sistema
        self.master = master
        #self.title("Registrar Cliente")
        
        # Campos de entrada
        tk.Label(self, text="ID Cliente:").grid(row=0, column=0)
        self.id_cliente_entry = tk.Entry(self)
        self.id_cliente_entry.grid(row=0, column=1)
        
        tk.Label(self, text="Nombre:").grid(row=1, column=0)
        self.nombre_cliente_entry = tk.Entry(self)
        self.nombre_cliente_entry.grid(row=1, column=1)
        
        tk.Label(self, text="Apellido:").grid(row=2, column=0)
        self.apellido_cliente_entry = tk.Entry(self)
        self.apellido_cliente_entry.grid(row=2, column=1)
        
        tk.Label(self, text="Dirección:").grid(row=3, column=0)
        self.direccion_cliente_entry = tk.Entry(self)
        self.direccion_cliente_entry.grid(row=3, column=1)
        
        tk.Label(self, text="Teléfono:").grid(row=4, column=0)
        self.telefono_cliente_entry = tk.Entry(self)
        self.telefono_cliente_entry.grid(row=4, column=1)
        
        # Botón de registrar
        tk.Button(self, text="Registrar Cliente", command=self.registrar_cliente).grid(row=5, column=0, columnspan=2)
        
     
        # Mensaje de confirmación
        self.message_label = tk.Label(self, text="", fg="green")
        self.message_label.grid(row=6, column=0, columnspan=2)

        
    
    def registrar_cliente(self):
        id_cliente = self.id_cliente_entry.get()
        nombre = self.nombre_cliente_entry.get()
        apellido = self.apellido_cliente_entry.get()
        direccion = self.direccion_cliente_entry.get()
        telefono = self.telefono_cliente_entry.get()
        
        nuevo_cliente = Cliente(id_cliente, nombre, apellido, direccion, telefono)
        mensaje = self.sistema.registrar_cliente(nuevo_cliente)
        self.message_label.config(text=mensaje)

        
        # Limpiar entradas
        self.id_cliente_entry.delete(0, tk.END)
        self.nombre_cliente_entry.delete(0, tk.END)
        self.apellido_cliente_entry.delete(0, tk.END)
        self.direccion_cliente_entry.delete(0, tk.END)
        self.telefono_cliente_entry.delete(0, tk.END)

        self.master.listar_clientes()
        