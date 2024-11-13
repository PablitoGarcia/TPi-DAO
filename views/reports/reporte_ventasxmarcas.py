import tkinter as tk
from tkinter import ttk , messagebox
from models.reporte import ReportePDF
from datetime import datetime


class ReporteVentasxMarcas(tk.Frame):
    def __init__(self, master, sistema):
        super().__init__(master)
        self.sistema = sistema
        self.master = master

        self.grid_columnconfigure(0, weight=1)  # Centrar la columna
        self.grid_rowconfigure(0, weight=1)  # Centrar la fila

        tk.Label(self, text="Reporte de Autos mas vendidos por Marca").grid(row=0, column=0, pady=10, sticky="n")
        # Botón para generar el reporte
        tk.Button(self, text="Generar Reporte de Autos", command=self.generar_reporte_autosxmarca).grid(row=1, column=0, pady=10, sticky="n")
        

    def generar_reporte_autosxmarca(self):
        # Obtener los datos de ingresos
        datos_ventasxmarca = self.sistema.reporte_autos_vendidos_marca()


        encabezados = ["Marca","Cantidad"]

        reporte = ReportePDF("Reporte de Autos mas vendidos por Marca ", encabezados, datos_ventasxmarca)
        nombreReportefile = "Reporte-VentasxMarcas-" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".pdf"
        reporte.generar_reporte(nombreReportefile)

        messagebox.showinfo("Éxito", f"Reporte generado exitosamente:{nombreReportefile}")
