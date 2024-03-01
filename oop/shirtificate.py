from PIL.Image import Image
from fpdf import FPDF, Align    


class Shirtificate(FPDF): # inherit from FPDF
    def __init__(self, name):
        """ 
        Creates the name attribute
        """
        # Initialize the base class (FPDF)
        super().__init__()
        self.name = name
        # Add a single page when creating the instance
        self.add_page()

    def create_certificate(self):
        """
        Adds a page to the PDF file, pastes the t-shirt image and 
        adds a heading and a label with the passed name on top of the shirt
        """
        self.set_font("helvetica", "B", 25)
        # Centering the title horizontally
        self.cell(0, 10, f"CS50 shirtificate", 0, 1, "C")
        
        image_width = 150
        image_path = "shirtificate.png"
        self.image(image_path, x=Align.C, y=50, w=image_width)
        
        text = f"{self.name} took CS50"
        text_width = self.get_string_width(text)
        x_image_center = (self.w - image_width) / 2
        x_text = x_image_center + (image_width - text_width) / 2
        # Set font and position for the text
        self.set_text_color(255, 255, 255)
        self.set_font("helvetica", size=20)
        self.set_xy(x_text, 100)  # Adjust the y-coordinate as needed

        # Add the centered text
        self.cell(text_width, 10, text, border=0, align="C")
        
        
        
def get_name():
    """
    Prompts the user to enter a name and passes the attribute to the 
    Shirtificate class
    """
    name = input("Name: ")
    return Shirtificate(name)
# Instantiation of inherited class
shirtificate = get_name()
# Create page with shirt 
shirtificate.create_certificate()
# Close and name the output PDF file
shirtificate.output("shirtificate.pdf")