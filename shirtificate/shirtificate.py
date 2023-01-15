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
# pdf.set_font("Times", size=12)
# for i in range(1, 41):
    # pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
pdf.output("shirtificate.pdf")