from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(60, 10, "CS50 Shirtificate", align='C')
pdf.output("shirtificate.pdf")