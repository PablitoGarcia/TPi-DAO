import tkinter as tk
from tkinter import ttk
from models.reporte import ReportePDF


class ListadoIngresos(tk.Frame):
    def __init__(self, master, sistema):
        super().__init__(master)
        self.sistema = sistema
        self.master = master

        # Botón para generar el reporte
        tk.Button(self, text="Generar Reporte de Ingresos", command=self.generar_reporte_ingresos).grid(row=5, column=0, columnspan=2)
        

    def generar_reporte_ingresos(self):
        # Obtener los datos de ingresos
        print()
        datos_autos = self.sistema.reporte_ingreso_ventas()
        datos_servicios = self.sistema.reporte_ingreso_servicios()
        
        

        # Crear una lista unificada con etiquetas para diferenciar
        datos_unificados = []

        # Agregar los datos de autos a la lista unificada
        for modelo, cantidad, total in datos_autos:
            datos_unificados.append([f"Venta de Auto: {modelo}", cantidad, f"${total:.2f}"])

        # Agregar los datos de servicios a la lista unificada
        for servicio, cantidad, total in datos_servicios:
            datos_unificados.append([f"Servicio: {servicio}", cantidad, f"${total:.2f}"])

        # Encabezados de la tabla
        encabezados = ["Concepto", "Cantidad", "Total Ingresos"]

        # Generar el reporte
        reporte = ReportePDF("Reporte de Ingresos Totales", encabezados, datos_unificados)
        reporte.generar_reporte("reporte_ingresos.pdf")

        #messagebox.showinfo("Éxito", "Reporte de ingresos generado exitosamente: reporte_ingresos.pdf")
