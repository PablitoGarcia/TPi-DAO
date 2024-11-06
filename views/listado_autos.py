# views/listado_autos.py
import tkinter as tk
from tkinter import ttk
from models.Observer.Suscriptor import Suscriptor

class ListadoAutos(tk.Frame, Suscriptor):
    def __init__(self, master, sistema):
        super().__init__(master)
        self.sistema = sistema
        #self.title("Listado de Autos")
        
        
        
        # Configuración del Treeview
        self.autos_tree = ttk.Treeview(self, columns=("Vin", "Marca", "Modelo", "Anio", "Precio","Estado","ID Cliente"), show="headings")
        self.autos_tree.heading("Vin", text="Vin")
        self.autos_tree.heading("Marca", text="Marca")
        self.autos_tree.heading("Modelo", text="Modelo")
        self.autos_tree.heading("Anio", text="Anio")
        self.autos_tree.heading("Precio", text="Precio")
        self.autos_tree.heading("Estado", text="Estado")
        self.autos_tree.heading("ID Cliente", text="ID Cliente")
        self.autos_tree.grid(row=0, column=0, columnspan=2)
        
        self.cargar_autos()
    
    def cargar_autos(self):
        # Limpiar el Treeview
        for item in self.autos_tree.get_children():
            self.autos_tree.delete(item)
        
        # Obtener y mostrar los autos
        autos = self.sistema.listar_autos()
        for cliente in autos:
            self.autos_tree.insert("", "end", values=cliente)
    
    def refrescar(self):
        self.cargar_autos()
