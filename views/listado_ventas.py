import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ListadoVentas(tk.Frame):
    def __init__(self, master, sistema):
        super().__init__(master)
        self.sistema = sistema
        
        # Configuración del Treeview
        self.ventas_tree = ttk.Treeview(self, columns=("ID", "Auto", "Cliente", "Fecha de Venta", "Vendedor"), show="headings")
        self.ventas_tree.heading("ID", text="ID Venta")
        self.ventas_tree.heading("Auto", text="Auto")
        self.ventas_tree.heading("Cliente", text="Cliente")
        self.ventas_tree.heading("Fecha de Venta", text="Fecha de Venta")
        self.ventas_tree.heading("Vendedor", text="Vendedor")
        self.ventas_tree.grid(row=1, column=0, columnspan=3)

        # Filtro por Cliente ID
        self.label_cliente = tk.Label(self, text="Filtrar por Cliente ID:")
        self.label_cliente.grid(row=0, column=0, padx=10, pady=10)
        
        self.combo_cliente = ttk.Combobox(self, state="readonly")
        self.combo_cliente.grid(row=0, column=1, padx=10, pady=10)
        self.combo_cliente.bind("<<ComboboxSelected>>", self.filtrar_ventas)  # Llamar a filtrar cuando se seleccione un cliente

        self.boton_mostrar_todas = tk.Button(self, text="Mostrar Todas las Ventas", command=self.cargar_ventas)
        self.boton_mostrar_todas.grid(row=0, column=2, padx=10, pady=10)

        # Cargar clientes y ventas
        self.cargar_clientes()
        self.cargar_ventas()

    def cargar_ventas(self, id_cliente=None):
        # Limpiar el Treeview
        for item in self.ventas_tree.get_children():
            self.ventas_tree.delete(item)
        
        # Obtener y mostrar las ventas
        ventas = self.sistema.listar_ventas(id_cliente)  # Filtrar por cliente si se proporciona un ID
        for venta in ventas:
            self.ventas_tree.insert("", "end", values=venta)

    def filtrar_ventas(self, event=None):
        # Obtener el ID del cliente desde el ComboBox
        id_cliente = self.combo_cliente.get()
        
        if id_cliente:  # Si hay un ID de cliente seleccionado
            self.cargar_ventas(id_cliente)
        else:  # Si no se selecciona cliente, mostrar todas las ventas
            self.cargar_ventas()
            
    def cargar_clientes(self):
        # Obtiene la lista de clientes y la carga en el ComboBox de cliente_id
        clientes = self.sistema.listar_clientes()
        cliente_ids = [cliente[0] for cliente in clientes]  # Obtener solo los IDs de los clientes
        self.combo_cliente['values'] = cliente_ids
            
            
    def refrescar(self):
        self.cargar_ventas()