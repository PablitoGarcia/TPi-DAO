import tkinter as tk
from tkinter import ttk , messagebox
from models.reporte import ReportePDF
from datetime import datetime
from tkcalendar import DateEntry


class ReporteVentasxPeriodo(tk.Frame):
    def __init__(self, master, sistema):
        super().__init__(master)
        self.sistema = sistema
        self.master = master

        self.grid_columnconfigure(0, weight=1)  # Centrar la columna
        self.grid_rowconfigure(0, weight=1)  # Centrar la fila
        
        self.label_venta = tk.Label(self, text="Reporte Ventas Realizadas en el periodo:")
        self.label_venta.grid(row=5, column=0, padx=10, pady=10)
        # Fecha de inicio
        self.label_ventaFechaInicio = tk.Label(self, text="Fecha de inicio:").grid(row=6, column=0, padx=5, pady=5)
        self.fecha_inicio = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_inicio.grid(row=6, column=1, padx=5, pady=5)

        # Fecha de fin
        self.label_ventaFechaInicio = tk.Label(self, text="Fecha de fin:").grid(row=7, column=0, padx=5, pady=5)
        self.fecha_fin = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_fin.grid(row=7, column=1, padx=5, pady=5)
        self.boton_generar_reporte = tk.Button(self, text="Generar Reporte", command=self.generar_reporte_ventasxperiodo)
        self.boton_generar_reporte.grid(row=8, column=1, padx=10, pady=10)
        

    def generar_reporte_ventasxperiodo(self):
        fecha_inicio = self.fecha_inicio.get_date()
        fecha_fin = self.fecha_fin.get_date()

        if fecha_inicio > fecha_fin:
            messagebox.showerror("Error", "La fecha de inicio no puede ser posterior a la fecha de fin.")
            return
        
        # Obtener los datos de ingresos
        datos_ventasxperiodo = self.sistema.reporte_ventas_xperiodo(fecha_inicio,fecha_fin)

        encabezados = ["ID Venta", "Auto", "Cliente", "Fecha", "Vendedor"]
        reporte = ReportePDF(f"Reporte de Ventas {fecha_inicio} a {fecha_fin}", encabezados, datos_ventasxperiodo)
        nombreReportefile = "Reporte-ventasxperiodo-" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".pdf"
        reporte.generar_reporte(nombreReportefile)

        messagebox.showinfo("Éxito", f"Reporte de ingresos generado exitosamente:{nombreReportefile}")
