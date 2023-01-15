from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(80, 0, "CS50 Shirtificate")
pdf.output("shirtificate.pdf")