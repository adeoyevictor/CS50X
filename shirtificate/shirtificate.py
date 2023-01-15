from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()

pdf.add_page()

pdf.set_font('helvetica', 'B', 16)
pdf.cell(40, 10, 'CS50 Shirtificate', 1)