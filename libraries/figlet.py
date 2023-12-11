import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

list_of_fonts = figlet.getFonts()

# def text_to_font():
    

if len(sys.argv) == 3:
    # Check if sys.argv[1] == '--font' or '-f' , otherwise exit program
    if sys.argv[1] in ("--font", "-f"):
        if sys.argv[2] in list_of_fonts:
            font_name = sys.argv[2]
            input_str = input("Input: ")
            output_font = figlet.setFont(font= font_name)
            print(figlet.renderText(input_str))
        else:
            sys.exit("Invalid usage1")
    else: 
        sys.exit("Invalid usage2")
elif len(sys.argv) == 1:
    # Code to generate text with random font
    input_str = input("Input: ")
    get_random_font = random.randint(0,549)
    output_font = figlet.setFont(font= list_of_fonts[get_random_font])
    print(figlet.renderText(input_str))

else:
    sys.exit("Invalid usage3")


# f = Figlet(font='slant')
# print(f.renderText('text to render'))