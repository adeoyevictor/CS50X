from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()

pdf.add_page()

pdf.set_font('helvetica', 'B', 16)
pdf.cell(60, 10, 'CS50 Shirtificate.', new_x="LMARGIN", new_y="NEXT", align='C')

pdf.image("shirtificate.png", )
pdf.output("shirtificate.pdf")
