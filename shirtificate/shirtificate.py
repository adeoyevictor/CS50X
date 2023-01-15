from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 45)
pdf.cell(0, 60, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png")
pdf.output("shirtificate.pdf")