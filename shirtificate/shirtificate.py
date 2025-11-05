from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("path\\to\\image.png", 5, 75, 200)
        self.set_font("helvetica", style="B", size=50)
        self.cell(80)
        self.cell(30, 50, "CS50 Shirtificate", border=0, align="C")
        self.ln(110)
        self.cell(80)
        self.set_text_color(255, 255, 255)
        self.set_font("helvetica", style="B", size=25)
        self.cell(30, 50, f"{name} took CS50", border=0, align="C")

name = input("Name: ").title()
pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")
