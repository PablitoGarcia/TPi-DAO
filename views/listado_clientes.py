# views/listado_clientes.py
import tkinter as tk
from tkinter import ttk
from models.Observer.Suscriptor import Suscriptor

class ListadoClientes(tk.Frame, Suscriptor):
    def __init__(self, master, sistema):
        super().__init__(master)
        self.sistema = sistema
        #self.title("Listado de Clientes")
        
        # Configuración del Treeview
        self.clientes_tree = ttk.Treeview(self, columns=("ID", "Nombre", "Apellido", "Dirección", "Teléfono"), show="headings")
        self.clientes_tree.heading("ID", text="ID Cliente")
        self.clientes_tree.heading("Nombre", text="Nombre")
        self.clientes_tree.heading("Apellido", text="Apellido")
        self.clientes_tree.heading("Dirección", text="Dirección")
        self.clientes_tree.heading("Teléfono", text="Teléfono")
        self.clientes_tree.grid(row=0, column=0, columnspan=2)
        
        
        self.cargar_clientes()
    
    def cargar_clientes(self):
        # Limpiar el Treeview
        for item in self.clientes_tree.get_children():
            self.clientes_tree.delete(item)
        
        # Obtener y mostrar los clientes
        clientes = self.sistema.listar_clientes()
        for cliente in clientes:
            self.clientes_tree.insert("", "end", values=cliente)
    
    def refrescar(self):
        self.cargar_clientes()