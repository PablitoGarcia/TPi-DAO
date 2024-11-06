
import tkinter as tk
from tkinter import ttk
from models.Observer.Suscriptor import Suscriptor

class ListadoVentas(tk.Frame, Suscriptor):
    def __init__(self, master, sistema):
        super().__init__(master)
        self.sistema = sistema
        #self.title("Listado de Ventas")
        
        # Configuración del Treeview
        self.ventas_tree = ttk.Treeview(self, columns=("ID", "Auto", "Cliente", "Fecha de Venta", "Vendedor"), show="headings")
        self.ventas_tree.heading("ID", text="ID Venta")
        self.ventas_tree.heading("Auto", text="Auto")
        self.ventas_tree.heading("Cliente", text="Cliente")
        self.ventas_tree.heading("Fecha de Venta", text="Fecha de Venta")
        self.ventas_tree.heading("Vendedor", text="Vendedor")
        self.ventas_tree.grid(row=0, column=0, columnspan=2)
        
        
        self.cargar_ventas()
    
    def cargar_ventas(self):
        # Limpiar el Treeview
        for item in self.ventas_tree.get_children():
            self.ventas_tree.delete(item)
        
        # Obtener y mostrar los ventas
        ventas = self.sistema.listar_ventas()
        for venta in ventas:
            self.ventas_tree.insert("", "end", values=venta)
    
    def refrescar(self):
        self.cargar_ventas()