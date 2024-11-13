from datetime import datetime
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
import matplotlib.pyplot as plt
from io import BytesIO
import tkinter as tk
from tkinter import ttk
import pandas as pd
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

class ReporteExtra(tk.Frame):
    def __init__(self, master, sistema):
        super().__init__(master)
        self.sistema = sistema
        self.master = master
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        tk.Label(self, text="Reporte de Ventas por marca e ingresos mensuales").grid(row=0, column=0, pady=10, sticky="n")
        tk.Button(self, text="Generar", command=self.generar_reporte_ventas_marca_ventas_mensuales).grid(row=1, column=0, pady=10, sticky="n")

    def generar_reporte_ventas_marca_ventas_mensuales(self):
        doc = SimpleDocTemplate("reporte_extra.pdf", pagesize=A4)
        elements = []

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Heading1'],
            fontName='Helvetica-Bold',
            fontSize=18,
            spaceAfter=12,
            alignment=0
        )

        elements.append(Paragraph("Reporte ventas por marca e ingresos mensuales", title_style))
        elements.append(Spacer(1, 12))
        
        elements.append(Paragraph(f"Fecha de generación: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", styles['Normal']))
        elements.append(Spacer(1, 12))
        
        datos = self.sistema.reporte_ventas_por_marca()
        marcas = [row[0] for row in datos]
        cant_ventas = [row[1] for row in datos]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 20))
        ax1.pie(cant_ventas, labels=marcas, autopct='%1.1f%%', startangle=140)
        ax1.axis('equal')
        
        ingresos_mensuales = self.sistema.reporte_ingresos_mensuales()
        mes = [row[0] for row in ingresos_mensuales]
        ingresos = [row[1] for row in ingresos_mensuales]
        
        df = pd.DataFrame({'Mes': mes, 'Ingresos': ingresos})
        
        ax2.bar(df['Mes'], df['Ingresos'], color='skyblue')
        ax2.set_title('Ingresos Mensuales')
        ax2.set_xlabel('Mes')
        ax2.set_ylabel('Ingresos ($)')
        ax2.set_xticks(range(len(df['Mes'])))
        ax2.set_xticklabels(df['Mes'], rotation=45)

        for i, v in enumerate(df['Ingresos']):
            ax2.text(i, v + 500, f"${v:,}", ha='center', fontsize=10)

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        elements.append(Image(buffer, width=300, height=600))
        elements.append(Spacer(1, 12))

        doc.build(elements)

        nombreReportefile = "Reporte-Ventas-Por-Marca-E-Ingresos-Mensuales-" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".pdf"
        messagebox.showinfo("Éxito", f"Reporte de ingresos generado exitosamente: {nombreReportefile}")
