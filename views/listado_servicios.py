import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ListadoServicios(tk.Frame):
    def __init__(self, master, sistema):
        super().__init__(master)
        self.sistema = sistema
        
        # Configuración del Treeview
        self.servicios_tree = ttk.Treeview(self, columns=("ID", "Auto", "Tipo de servicio", "Fecha", "Costo"), show="headings")
        self.servicios_tree.heading("ID", text="ID Servicio")
        self.servicios_tree.heading("Auto", text="Auto")
        self.servicios_tree.heading("Tipo de servicio", text="Tipo de servicio")
        self.servicios_tree.heading("Fecha", text="Fecha")
        self.servicios_tree.heading("Costo", text="Costo")
        self.servicios_tree.grid(row=1, column=0, columnspan=3)

        # Filtro por Cliente ID
        self.label_auto = tk.Label(self, text="Filtrar por id de Auto:")
        self.label_auto.grid(row=0, column=0, padx=10, pady=10)
        
        self.combo_auto = ttk.Combobox(self, state="readonly")
        self.combo_auto.grid(row=0, column=1, padx=10, pady=10)
        self.combo_auto.bind("<<ComboboxSelected>>", self.filtrar_servicios)  # Llamar a filtrar cuando se seleccione un cliente

        self.boton_mostrar_todos = tk.Button(self, text="Mostrar todos los servicios", command=self.cargar_servicios)
        self.boton_mostrar_todos.grid(row=0, column=2, padx=10, pady=10)

        # Cargar clientes y ventas
        self.cargar_autos()
        self.cargar_servicios()

    def cargar_servicios(self, id_auto=None):
        # Limpiar el Treeview
        for item in self.servicios_tree.get_children():
            self.servicios_tree.delete(item)
        
        # Obtener y mostrar los servicios
        servicios = self.sistema.listar_servicios(id_auto)  # Filtrar por auto si se proporciona un ID
        for servicio in servicios:
            self.servicios_tree.insert("", "end", values=servicio)

    def filtrar_servicios(self, event=None):
        # Obtener el ID del cliente desde el ComboBox
        auto = self.combo_auto.get()
        id_auto = auto.split(" - ")[0]
        
        if id_auto:  # Si hay un ID de cliente seleccionado
            self.cargar_servicios(id_auto)
        else:  # Si no se selecciona cliente, mostrar todas las ventas
            self.cargar_servicios()
            
    def cargar_autos(self):
        # Obtiene la lista de autos y la carga en el ComboBox de id_autos
        autos = self.sistema.listar_autos()
        auto_descriptions = [f"{auto[0]} - {auto[1]} ({auto[2]})" for auto in autos]  # ID - Modelo (Año)
        self.combo_auto['values'] = auto_descriptions
            
            
    def refrescar(self):
        self.cargar_servicios()