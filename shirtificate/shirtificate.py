from fpdf import FPDF

user_name = input("Enter your name: ")

shirt_overlay = f"{user_name} took CS50"

pdf = FPDF(orientation="P", format="A4")
pdf.add_page()

pdf.set_font("helvetica", style="B", size=30)
pdf.cell(0, 50, "CS50 Shirtificate", align="C")
pdf.ln(20)

pdf.image("shirtificate.png", x=15, y=80, w=180)

pdf.set_font("helvetica", size=20)
pdf.set_text_color(255, 255, 255)
pdf.set_y(140)
pdf.cell(0, 10, shirt_overlay, align="C")

pdf.output("shirtificate.pdf")