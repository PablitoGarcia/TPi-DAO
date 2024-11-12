# views/registro_venta.py
import tkinter as tk
from tkinter import ttk
from models.servicio import Servicio
from models.Observer.Sujeto import Sujeto
from tkcalendar import DateEntry

class RegistroServicio(tk.Frame,Sujeto):
    def __init__(self, master, sistema):
        super().__init__(master)
        Sujeto.__init__(self)
        self.sistema = sistema
        self.master = master
        
        # Campos de entrada
        tk.Label(self, text="ID Servicio:").grid(row=0, column=0)
        self.id_servicio_entry = tk.Entry(self)
        self.id_servicio_entry.grid(row=0, column=1)
        
        tk.Label(self, text="Auto:").grid(row=1, column=0)
        self.id_auto_servicio_combobox = ttk.Combobox(self, state="readonly")
        self.id_auto_servicio_combobox.grid(row=1, column=1)
        self.cargar_autos_vendidos() 
        
        tk.Label(self, text="Tipo de servicio:").grid(row=2, column=0)
        self.tipo_combobox = ttk.Combobox(self,values=["Mantenimiento", "Reparacion"], state="readonly")
        self.tipo_combobox.grid(row=2, column=1)
        self.tipo_combobox.set("Mantenimiento")  # Valor por defecto
        
        
        tk.Label(self, text="Fecha de servicio:").grid(row=3, column=0)
        self.fecha_servicio_entry = DateEntry(self, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.fecha_servicio_entry.grid(row=3, column=1)
        
        tk.Label(self, text="Costo:").grid(row=4, column=0)
        self.costo_servicio_entry = tk.Entry(self)
        self.costo_servicio_entry.grid(row=4, column=1)
        
        # Botón de registrar
        tk.Button(self, text="Registrar Servicio", command=self.registrar_servicio).grid(row=5, column=0, columnspan=2)
        
     
        # Mensaje de confirmación
        self.message_label = tk.Label(self, text="", fg="green")
        self.message_label.grid(row=6, column=0, columnspan=2)

        
    
    def registrar_servicio(self):
        id_servicio = self.id_servicio_entry.get()
        auto = self.id_auto_servicio_combobox.get()
        tipo_servicio = self.tipo_combobox.get()
        fecha = self.fecha_servicio_entry.get_date()
        costo = self.costo_servicio_entry.get()
        
        nuevo_servicio = Servicio(id_servicio, auto, tipo_servicio, fecha, costo)
        mensaje = self.sistema.registrar_servicio(nuevo_servicio)
        self.message_label.config(text=mensaje)

        self.notificar()
        
        # Limpiar entradas
        self.id_servicio_entry.delete(0, tk.END)
        self.id_auto_servicio_combobox.set("")
        self.tipo_combobox.set("mantenimiento")
        self.fecha_servicio_entry.set_date("")
        self.costo_servicio_entry.delete(0, tk.END)

        
    #cargar autos en combobox
    def cargar_autos_vendidos(self):
        # Obtiene la lista de autos y la carga en el ComboBox de id_autos
        autos = self.sistema.listar_autos_vendidos()
        auto_ids = [auto[0] for auto in autos]  # Obtener solo los IDs de los autos
        self.id_auto_servicio_combobox['values'] = auto_ids

