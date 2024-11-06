import tkinter as tk
from tkinter import ttk
from models.Observer.Suscriptor import Suscriptor

class ListadoVendedores(tk.Frame, Suscriptor):
    def __init__(self, master, sistema):
        super().__init__(master)
        self.sistema = sistema
        #self.title("Listado de Vendedores")
        
        # Configuración del Treeview
        self.vendedores_tree = ttk.Treeview(self, columns=("ID", "Nombre", "Apellido",  "Comision"), show="headings")
        self.vendedores_tree.heading("ID", text="ID Vendedor")
        self.vendedores_tree.heading("Nombre", text="Nombre")
        self.vendedores_tree.heading("Apellido", text="Apellido")
        self.vendedores_tree.heading("Comision", text="Comision")
        self.vendedores_tree.grid(row=0, column=0, columnspan=2)
        
        
        self.cargar_vendedores()
    
    def cargar_vendedores(self):
        # Limpiar el Treeview
        for item in self.vendedores_tree.get_children():
            self.vendedores_tree.delete(item)
        
        # Obtener y mostrar los vendedores
        vendedores = self.sistema.listar_vendedores()
        for cliente in vendedores:
            self.vendedores_tree.insert("", "end", values=cliente)
    
    def refrescar(self):
        self.cargar_vendedores()