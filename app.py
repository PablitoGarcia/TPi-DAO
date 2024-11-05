import tkinter as tk
from tkinter import ttk
from models.gestorSistema import GestorSistema
from views.listado_clientes import ListadoClientes
from views.registro_clientes import RegistroCliente

from views.registro_autos import RegistroAuto
from views.listado_autos import ListadoAutos

class App:
    def __init__(self,root):
        self.root = root 
        self.sistema = GestorSistema()
        root.title("Sistema de Gestion de Venta de Autos")

        
        # Crear el menú principal
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Menú Archivo
        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        archivo_menu.add_command(label="Salir", command=root.destroy)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

        # Menú Clientes
        clientes_menu = tk.Menu(menu_bar, tearoff=0)
        clientes_menu.add_command(label="Registrar Cliente", command=self.abrir_registro_cliente)
        clientes_menu.add_command(label="Listar Clientes", command=self.abrir_listado_clientes)
        menu_bar.add_cascade(label="Clientes", menu=clientes_menu)

        # Menú Autos
        clientes_menu = tk.Menu(menu_bar, tearoff=0)
        clientes_menu.add_command(label="Registrar Auto", command=self.abrir_registro_auto)
        clientes_menu.add_command(label="Listar Autos", command=self.abrir_listado_autos)
        menu_bar.add_cascade(label="Autos", menu=clientes_menu)

    def abrir_registro_cliente(self):
        self.registro_frame = RegistroCliente(self.root, self.sistema)
        self.registro_frame.grid(row=0, column=0, sticky="nsew")

         
        self.listado_frame = ListadoClientes(self.root, self.sistema)
        self.listado_frame.grid(row=10, column=0, sticky="nsew")

        self.mostrar_frame(self.registro_frame)
        self.mostrar_frame(self.listado_frame)

    def mostrar_frame(self, frame):
        frame.tkraise()
        
    def abrir_listado_clientes(self):
        ListadoClientes(self.root, self.sistema)

    def abrir_registro_auto(self):
        RegistroAuto(self.root,self.sistema)
    
    def abrir_listado_autos(self):
        ListadoAutos(self.root, self.sistema)


