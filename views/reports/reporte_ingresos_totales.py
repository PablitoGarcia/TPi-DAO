import tkinter as tk
from tkinter import ttk , messagebox
from models.reporte import ReportePDF
from datetime import datetime


class ReporteIngresosTotales(tk.Frame):
    def __init__(self, master, sistema):
        super().__init__(master)
        self.sistema = sistema
        self.master = master

        self.grid_columnconfigure(0, weight=1)  # Centrar la columna
        self.grid_rowconfigure(0, weight=1)  # Centrar la fila

        tk.Label(self, text="Reporte de Ingresos Totales por ventas de autos y servicios").grid(row=0, column=0, pady=10, sticky="n")
        # Botón para generar el reporte
        tk.Button(self, text="Generar Reporte de Ingresos", command=self.generar_reporte_ingresos).grid(row=1, column=0, pady=10, sticky="n")
        

    def generar_reporte_ingresos(self):
        # Obtener los datos de ingresos
        datos_autos = self.sistema.reporte_ingreso_ventas()
        datos_servicios = self.sistema.reporte_ingreso_servicios()
        
        datos_unificados = []


        for vin,modelo,marca, cantidad, total in datos_autos:
            datos_unificados.append([f"{vin}-{modelo}-{marca}",f"Venta de Auto", cantidad, f"${total:.2f}"])
        for id_auto,modelo,marca,servicio, cantidad, total in datos_servicios:
            datos_unificados.append([f"{id_auto}-{modelo}-{marca}",f"Servicio: {servicio}", cantidad, f"${total:.2f}"])


        encabezados = ["Auto" ,"Concepto", "Cantidad", "Total Ingresos"]

        reporte = ReportePDF("Reporte de Ingresos Totales", encabezados, datos_unificados)
        nombreReportefile = "Reporte-IngresosTotales-" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".pdf"
        reporte.generar_reporte(nombreReportefile)

        messagebox.showinfo("Éxito", f"Reporte de ingresos generado exitosamente:{nombreReportefile}")
