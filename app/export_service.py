import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

class ExportService:

    @staticmethod
    def export_csv(df, path="exports/report.csv"):
        df.to_csv(path, index=False)

    @staticmethod
    def export_excel(df, path="exports/report.xlsx"):
        df.to_excel(path, index=False)

    @staticmethod
    def export_pdf_report(df, path="exports/report.pdf"):
        doc = SimpleDocTemplate(path)
        styles = getSampleStyleSheet()
        story = []

        # Title
        story.append(Paragraph("Analytics Report", styles['Heading1']))
        story.append(Spacer(1, 12))

        # Convert DataFrame to list of lists (header + data)
        data = [df.columns.tolist()] + df.values.tolist()
        table = Table(data, repeatRows=1)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.gray),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ]))
        story.append(table)

        doc.build(story)
