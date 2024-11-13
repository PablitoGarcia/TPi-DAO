# views/registro_venta.py
import tkinter as tk
from tkinter import ttk
from models.venta import Venta
from models.Observer.Sujeto import Sujeto
from tkcalendar import DateEntry

class RegistroVenta(tk.Frame,Sujeto):
    def __init__(self, master, sistema):
        super().__init__(master)
        Sujeto.__init__(self)
        self.sistema = sistema
        self.master = master
        
        # Campos de entrada
        tk.Label(self, text="ID Venta:").grid(row=0, column=0)
        self.id_venta_entry = tk.Entry(self)
        self.id_venta_entry.grid(row=0, column=1)
        
        tk.Label(self, text="Auto:").grid(row=1, column=0)
        self.id_auto_venta_combobox = ttk.Combobox(self, state="readonly")
        self.id_auto_venta_combobox.grid(row=1, column=1)
        self.cargar_autos() 
        
        tk.Label(self, text="Cliente:").grid(row=2, column=0)
        self.id_cliente_venta_combobox = ttk.Combobox(self, state="readonly")
        self.id_cliente_venta_combobox.grid(row=2, column=1)
        self.cargar_clientes() 
        
        tk.Label(self, text="Fecha de venta:").grid(row=3, column=0)
        self.fecha_venta_entry = DateEntry(self, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.fecha_venta_entry.grid(row=3, column=1)
        
        tk.Label(self, text="Vendedor:").grid(row=4, column=0)
        self.id_vendedor_venta_combobox = ttk.Combobox(self, state="readonly")
        self.id_vendedor_venta_combobox.grid(row=4, column=1)
        self.cargar_vendedores() 
        
        # Botón de registrar
        tk.Button(self, text="Registrar Venta", command=self.registrar_venta).grid(row=5, column=0, columnspan=2)
        
     
        # Mensaje de confirmación
        self.message_label = tk.Label(self, text="", fg="green")
        self.message_label.grid(row=6, column=0, columnspan=2)

        
    
    def registrar_venta(self):
        id_venta = self.id_venta_entry.get()
        auto = self.id_auto_venta_combobox.get()
        cliente = self.id_cliente_venta_combobox.get()
        fecha = self.fecha_venta_entry.get_date()
        vendedor = self.id_vendedor_venta_combobox.get()
        
        #extraigo id
        auto_id = auto.split(" - ")[0]
        cliente_id = cliente.split(" - ")[0]
        vendedor_id = vendedor.split(" - ")[0]

        nuevo_venta = Venta(id_venta,auto_id , cliente_id, fecha, vendedor_id)
        self.sistema.vender_auto(cliente_id, auto_id)
        
        mensaje = self.sistema.registrar_venta(nuevo_venta)
        self.message_label.config(text=mensaje)

        self.notificar()
        
        # Limpiar entradas
        self.id_venta_entry.delete(0, tk.END)
        self.id_auto_venta_combobox.set("")
        self.id_cliente_venta_combobox.set("")
        #self.fecha_venta_entry.set_date("")
        self.id_vendedor_venta_combobox.set("")
       
        self.cargar_autos()

        
    #cargar autos en combobox
    def cargar_autos(self):
        autos = self.sistema.listar_autos_no_vendidos()
        auto_descriptions = [f"{auto[0]} - {auto[1]} ({auto[2]})" for auto in autos]  # ID - Modelo (Año)
        self.id_auto_venta_combobox['values'] = auto_descriptions


    #cargar clientes en combobox
    def cargar_clientes(self):
        # Obtiene la lista de clientes y la carga en el ComboBox de cliente_id
        clientes = self.sistema.listar_clientes()
        cliente_descriptions = [f"{cliente[0]} - {cliente[1]} {cliente[2]}" for cliente in clientes]  # ID - Nombre Apellido
        self.id_cliente_venta_combobox['values'] = cliente_descriptions
     #cargar clientes en combobox
    def cargar_vendedores(self):
        # Obtiene la lista de vendedores y la carga en el ComboBox de id_vendedor
        vendedores = self.sistema.listar_vendedores()
        vendedor_descriptions = [f"{vendedor[0]} - {vendedor[1]} {vendedor[2]}" for vendedor in vendedores]  # ID - Nombre Apellido
        self.id_vendedor_venta_combobox['values'] = vendedor_descriptions