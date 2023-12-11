import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

list_of_fonts = figlet.getFonts()

def generate_random_number():
    """
    Generate a random number
    Args: none
    Changes: nothing
    Returns: a random integer between 0 and 549
    """
    random_number = random.randint(0,549)
    return random_number


def text_to_font(l, n):
    """
    Prints the input string formatted as a font from the 
    list_of_fonts
    Args: a list (l) and an index (n)
    Changes: input_str
    Returns: input_str formatted with font"""
    # prompt the user
    input_str = input("Input: ")
    # extract the name of the font
    font = l[n]
    # pass the number to the output str
    output_str = figlet.setFont(font= font)
    # print the formatted str
    print(figlet.renderText(input_str))
    

if len(sys.argv) == 3:
    if sys.argv[1] in ("--font", "-f"):
        if sys.argv[2] in list_of_fonts:
            text_to_font(sys.argv, 2)
        else:
            sys.exit("Invalid usage")
    else: 
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    text_to_font(list_of_fonts, generate_random_number())

else:
    sys.exit("Invalid usage")
