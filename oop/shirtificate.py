from PIL.Image import Image
from fpdf import FPDF, Align    


class Shirtificate(FPDF): # inherit from FPDF
    def __init__(self, name):
        """ 
        Method to create the name
        """
        # Initialize the base class (FPDF)
        super().__init__()
        self.name = name
        # Add a single page when creating the instance
        self.add_page()

    def create_certificate(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Centering the title horizontally
        self.cell(0, 10, f"CS50 shirtificate for {self.name}", 0, 1, "C")
        
def get_name():
    
    name = input("Name: ")
    return Shirtificate(name)
# Instantiation of inherited class
shirtificate = get_name()
shirtificate.create_certificate()
shirtificate.output("new-tuto4.pdf")