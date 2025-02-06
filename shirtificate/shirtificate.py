from fpdf import FPDF

class PDF():
    def __init__(self, name):

        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 40)
        self._pdf.cell(0, 40, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", w = self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x = 45, y = 140, text = f"{name} took CS50")

    def save_document(self, name):
        self._pdf.output(name)

def main():
    name = input("Write your name: ")
    pdf = PDF(name)
    pdf.save_document("shirtificate.pdf")


if __name__ == "__main__":
    main()
