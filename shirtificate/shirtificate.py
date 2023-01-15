from fpdf import FPDF

name = input("Name: ")

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 18)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        self.ln(20)


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.image("shirtificate.png", x='C')
pdf.output("shirtificate.pdf")