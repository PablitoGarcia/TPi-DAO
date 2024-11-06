
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from datetime import datetime

class ReportePDF:
    def __init__(self, titulo, encabezados, datos):
        self.titulo = titulo
        self.encabezados = encabezados
        self.datos = datos

    def generar_reporte(self, filename="reporte.pdf"):
        # Crear el canvas para el PDF
        pdf = canvas.Canvas(filename, pagesize=A4)
        pdf.setTitle(self.titulo)

        # Agregar el título y fecha de generación
        self._agregar_encabezado(pdf)
        
        # Agregar tabla de datos
        self._agregar_tabla(pdf)
        
        # Guardar el PDF
        pdf.save()
        print(f"Reporte generado: {filename}")

    def _agregar_encabezado(self, pdf):
        pdf.setFont("Helvetica-Bold", 20)
        pdf.drawString(72, 750, self.titulo)

        pdf.setFont("Helvetica", 12)
        pdf.drawString(72, 730, f"Fecha de generación: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    def _agregar_tabla(self, pdf):
        # Agregar encabezados de la tabla
        data = [self.encabezados] + self.datos

        # Crear tabla con estilo
        table = Table(data, colWidths=[1.5*inch] * len(self.encabezados))
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Posicionar la tabla en el PDF
        width, height = A4
        table.wrapOn(pdf, width, height)
        table.drawOn(pdf, 72, 600 - len(self.datos) * 20)