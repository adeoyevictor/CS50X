from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()

pdf.add_page()

pdf.set_font("helvetica", "B", 30)
pdf.cell(100, 40, "CS50 Shirtificate", align='C')
pdf.output("shirtificate.pdf")