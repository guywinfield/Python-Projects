from fpdf import FPDF


def main():
    name = input("Name: ")
    pdf = Shirtificate(name, "shirtificate.pdf")
    pdf.set_title()
    pdf.set_shirt()
    pdf.set_shirt_name()
    pdf.output()


class Shirtificate:
    def __init__(self, name, filename, shirt_file = "shirtificate.png", orientation="P", format="A4"):
        self.name = name
        self.shirt_file = shirt_file
        self.filename = filename

        self.pdf = FPDF(orientation=orientation, format=format)
        self.pdf.add_page()
        self.pdf.set_auto_page_break(False)


    def set_title(self, font = "helvetica", size = 32):
        self.pdf.set_font(font, size=size)
        self.pdf.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")

    def set_shirt(self):
        move_x = 5submit50 cs50/problems/2022/python/shirtificate
        move_y = 30
        width = 200
        self.pdf.image(self.shirt_file, x=move_x, y=move_y, w=width)
        # store base Y so name overlay can reference it
        self._image_y = move_y
        self._image_w = width

    def set_shirt_name(self):
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.set_font("helvetica", "B", 26)
        text_x = 50
        text_y = self._image_y + self._image_w * 0.3
        shirt_text = self.name + " took CS50"

        self.pdf.text(text_x, text_y, shirt_text )


    def output(self):
        self.pdf.output(self.filename)


if __name__ == "__main__":
    main()
