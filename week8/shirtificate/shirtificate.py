from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Place the shirt image
        self.image("./shirtificate.png", 10, 70, 190)

        # Set font for the CS50 Shirtificate title
        self.set_font("helvetica", "", 48)

        # Add the CS50 Shirtificate title
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)  # Move down after the title


def main():
    name = input("Name: ")
    generate_shirtificate(name)


def generate_shirtificate(name):
    # Create PDF instance
    pdf = PDF()

    # Add a portrait page with A4 format
    pdf.add_page(orientation="portrait", format="a4")

    # Set font for the user's name
    pdf.set_font("helvetica", size=24)

    # Set text color to white
    pdf.set_text_color(255, 255, 255)

    # Add the user's name on top of the shirt image
    pdf.cell(0, 213, f"{name} took CS50", align="C")

    # Output the PDF to a file named "shirtificate.pdf"
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
