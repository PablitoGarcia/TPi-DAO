import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from models.gestorSistema import GestorSistema
from views.listado_clientes import ListadoClientes
from views.registro_clientes import RegistroCliente

from views.registro_autos import RegistroAuto
from views.listado_autos import ListadoAutos


from views.listado_vendedores import ListadoVendedores
from views.registro_vendedores import RegistroVendedor

from views.listado_ventas import ListadoVentas
from views.registro_ventas import RegistroVenta

from views.listado_servicios import ListadoServicios
from views.registro_servicios import RegistroServicio

from views.Reports.reporte_ingresos_totales import ReporteIngresosTotales
from views.Reports.reporte_ventasxmarcas import ReporteVentasxMarcas
from views.Reports.reporte_ventasxperiodo import ReporteVentasxPeriodo
from views.Reports.reporte_extra import ReporteExtra

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
        menu_bar.add_cascade(label="Clientes", menu=clientes_menu)

        # Menú Autos
        clientes_menu = tk.Menu(menu_bar, tearoff=0)
        clientes_menu.add_command(label="Registrar Auto", command=self.abrir_registro_auto)
        menu_bar.add_cascade(label="Autos", menu=clientes_menu)

        # Menú Vendedores
        vendedores_menu = tk.Menu(menu_bar, tearoff=0)
        vendedores_menu.add_command(label="Registrar Vendedor", command=self.abrir_registro_vendedor)
        menu_bar.add_cascade(label="Vendedores", menu=vendedores_menu)

        # Menú Ventas
        venta_menu = tk.Menu(menu_bar, tearoff=0)
        venta_menu.add_command(label="Registrar Venta", command=self.abrir_registro_venta)
        menu_bar.add_cascade(label="Ventas", menu=venta_menu)
        
        # Menú Servicios
        servicios_menu = tk.Menu(menu_bar, tearoff=0)
        servicios_menu.add_command(label="Registrar Servicio", command=self.abrir_registro_servicios)
        menu_bar.add_cascade(label="Servicios", menu=servicios_menu)

        # Reportes 
        servicios_menu = tk.Menu(menu_bar, tearoff=0)
        servicios_menu.add_command(label="Autos vendidos por Periodo", command=self.abrir_reporte_ventasxperiodo)
        servicios_menu.add_command(label="Ingresos Totales", command=self.abrir_reporte_ingresosTotales)
        servicios_menu.add_command(label="Autos Mas vendidos por Marca", command=self.abrir_reporte_ventasxmarca)
        servicios_menu.add_command(label="Ventas por marca e ingresos mensuales", command=self.abrir_reporte_extra)

        menu_bar.add_cascade(label="Reportes", menu=servicios_menu)

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)


    def mostrar_frame(self, frame):
        frame.tkraise()

    def abrir_registro_cliente(self):
        self.limpiar_frame()
    
        self.registro_cliente_frame = RegistroCliente(self.root, self.sistema)
        self.registro_cliente_frame.grid(row=0, column=0, sticky="nsew")

         
        self.listado_clientes_frame = ListadoClientes(self.root, self.sistema)
        self.listado_clientes_frame.grid(row=10, column=0, sticky="nsew")
        
        self.registro_cliente_frame.suscribir(self.listado_clientes_frame)


        self.mostrar_frame(self.registro_cliente_frame)
        self.mostrar_frame(self.listado_clientes_frame)

    

    def abrir_registro_auto(self):
        self.limpiar_frame()
        self.registro_auto_frame = RegistroAuto(self.root,self.sistema)
        self.registro_auto_frame.grid(row=0, column=0, sticky="nsew")

         
        self.listado_auto_frame = ListadoAutos(self.root, self.sistema)
        self.listado_auto_frame.grid(row=10, column=0, sticky="nsew")
        
        self.registro_auto_frame.suscribir(self.listado_auto_frame)


        self.mostrar_frame(self.registro_auto_frame)
        self.mostrar_frame(self.listado_auto_frame)


    def abrir_registro_vendedor(self):
        self.limpiar_frame()
        self.registro_vendedor_frame = RegistroVendedor(self.root, self.sistema)
        self.registro_vendedor_frame.grid(row=0, column=0, sticky="nsew")

         
        self.listado_vendedores_frame = ListadoVendedores(self.root, self.sistema)
        self.listado_vendedores_frame.grid(row=10, column=0, sticky="nsew")
        
        self.registro_vendedor_frame.suscribir(self.listado_vendedores_frame)


        self.mostrar_frame(self.registro_vendedor_frame)
        self.mostrar_frame(self.listado_vendedores_frame)


    def abrir_registro_venta(self):
        self.limpiar_frame()
        self.registro_venta_frame = RegistroVenta(self.root, self.sistema)
        self.registro_venta_frame.grid(row=0, column=0, sticky="nsew")

         
        self.listado_ventas_frame = ListadoVentas(self.root, self.sistema)
        self.listado_ventas_frame.grid(row=10, column=0, sticky="nsew")
        
        self.registro_venta_frame.suscribir(self.listado_ventas_frame)


        self.mostrar_frame(self.registro_venta_frame)
        self.mostrar_frame(self.listado_ventas_frame)
        
        
    def abrir_registro_servicios(self):
        self.limpiar_frame()
        self.registro_servicios_frame = RegistroServicio(self.root, self.sistema)
        self.registro_servicios_frame.grid(row=0, column=0, sticky="nsew")

         
        self.listado_servicios_frame = ListadoServicios(self.root, self.sistema)
        self.listado_servicios_frame.grid(row=10, column=0, sticky="nsew")
        
        self.registro_servicios_frame.suscribir(self.listado_servicios_frame)


        self.mostrar_frame(self.registro_servicios_frame)
        self.mostrar_frame(self.listado_servicios_frame)
    
    def abrir_reporte_ingresosTotales(self):
        
        self.limpiar_frame()
            
        self.reporte_ingresosTotales_frame = ReporteIngresosTotales(self.root, self.sistema)
        self.reporte_ingresosTotales_frame.grid(row=0, column=0, sticky="nsew")
        

        self.mostrar_frame(self.reporte_ingresosTotales_frame)
    
    def abrir_reporte_ventasxmarca(self):
        
        self.limpiar_frame()
            
        
        self.reporte_ventasxmarca_frame = ReporteVentasxMarcas(self.root, self.sistema)
        self.reporte_ventasxmarca_frame.grid(row=5, column=0, sticky="nsew")

        self.mostrar_frame(self.reporte_ventasxmarca_frame)

    def abrir_reporte_ventasxperiodo(self):
        
        self.limpiar_frame()
            
        
        self.reporte_ventasxperiodo_frame = ReporteVentasxPeriodo(self.root, self.sistema)
        self.reporte_ventasxperiodo_frame.grid(row=5, column=0, sticky="nsew")

        self.mostrar_frame(self.reporte_ventasxperiodo_frame)
        
    def abrir_reporte_extra(self):
        
        self.limpiar_frame()
        
        self.reporte_extra_frame = ReporteExtra(self.root, self.sistema)
        self.reporte_extra_frame.grid(row=5, column=0, sticky="nsew")

        self.mostrar_frame(self.reporte_extra_frame)
        
    
        
    def limpiar_frame(self):
        for child in self.root.winfo_children():
            if not isinstance(child, tk.Menu):
                child.destroy()
                
    def cerrar_aplicacion(self):
        respuesta = messagebox.askyesno("Confirmar", "¿Realmente deseas cerrar la aplicación?")
        if respuesta:
            self.sistema.cerrar_bd()
            self.root.quit()  # Detiene el ciclo de eventos de Tkinter
            self.root.destroy()  # Destruye la ventana principal
        else:
            pass 

