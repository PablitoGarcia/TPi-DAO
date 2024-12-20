# views/registro_autos.py
import tkinter as tk
from tkinter import ttk
from models.auto import Auto
from models.Observer.Sujeto import Sujeto

class RegistroAuto(tk.Frame,Sujeto):
    def __init__(self, master, sistema):
        super().__init__(master)
        Sujeto.__init__(self)
        self.sistema = sistema
        
        
        # Campos de entrada vin,marca,modelo,anio,precio,estado,cliente_id
        tk.Label(self, text="VIN:").grid(row=0, column=0)
        self.vin_auto_entry = tk.Entry(self)
        self.vin_auto_entry.grid(row=0, column=1)
        
        tk.Label(self, text="Marca:").grid(row=1, column=0)
        self.marca_auto_entry = tk.Entry(self)
        self.marca_auto_entry.grid(row=1, column=1)
        
        tk.Label(self, text="Modelo:").grid(row=2, column=0)
        self.modelo_auto_entry = tk.Entry(self)
        self.modelo_auto_entry.grid(row=2, column=1)
        
        tk.Label(self, text="Anio:").grid(row=3, column=0)
        self.anio_auto_entry = tk.Entry(self)
        self.anio_auto_entry.grid(row=3, column=1)
        
        tk.Label(self, text="Precio:").grid(row=4, column=0)
        self.precio_auto_entry = tk.Entry(self)
        self.precio_auto_entry.grid(row=4, column=1)

        tk.Label(self, text="Estado:").grid(row=5, column=0)
        self.estado_combobox = ttk.Combobox(self,values=["Nuevo", "Usado"], state="readonly")
        self.estado_combobox.grid(row=5, column=1)
        self.estado_combobox.set("Nuevo")  # Valor por defecto

        
        
        # Botón de registrar
        tk.Button(self, text="Registrar auto", command=self.registrar_auto).grid(row=7, column=0, columnspan=2)
        
        # Mensaje de confirmación
        self.message_label = tk.Label(self, text="", fg="green")
        self.message_label.grid(row=8, column=0, columnspan=2)
    
    def registrar_auto(self):
        vin = self.vin_auto_entry.get()
        marca = self.marca_auto_entry.get()
        modelo = self.modelo_auto_entry.get()
        anio = self.anio_auto_entry.get()
        precio = self.precio_auto_entry.get()
        estado = self.estado_combobox.get()
        
        nuevo_auto = Auto(vin,marca,modelo,int(anio),float(precio),estado)
        mensaje = self.sistema.registrar_auto(nuevo_auto)
        self.message_label.config(text=mensaje)
        

        self.notificar()
        # Limpiar entradas
        self.vin_auto_entry.delete(0, tk.END)
        self.marca_auto_entry.delete(0, tk.END)
        self.modelo_auto_entry.delete(0, tk.END)
        self.anio_auto_entry.delete(0, tk.END)
        self.precio_auto_entry.delete(0, tk.END)
        self.estado_combobox.set("nuevo")

    #cargar clientes en combobox
    def cargar_clientes(self):
        # Obtiene la lista de clientes y la carga en el ComboBox de cliente_id
        clientes = self.sistema.listar_clientes()
        cliente_ids = [cliente[0] for cliente in clientes]  # Obtener solo los IDs de los clientes
        self.cliente_id_combobox['values'] = cliente_ids