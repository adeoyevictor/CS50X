from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()

pdf.add_page()

pdf.set_font('helvetica', 'B', 16)