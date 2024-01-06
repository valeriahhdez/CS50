import sys
import os
from PIL import Image
from PIL import ImageOps

def main():
    """
    Calls is_valid_length and is_valid_extension
    Opens shirt.jpg file and pastes it into input_image
    Args: 
     - None
    Returns:
     - A new image with shirt on stored in output_file
    """
    if is_valid_length(sys.argv) and is_valid_extension(sys.argv):
        try:
            # Open the input image
            shirt = Image.open("shirt.png")
            # resize and crop the input image
            shirt_size = shirt.size
            input_image = Image.open(sys.argv[1])
            output_file = ImageOps.fit(input_image, shirt_size)
            output_file.paste(shirt, shirt)
            output_file.save(sys.argv[2])
        except: 
            sys.exit("Input does not exist")

def is_valid_length(command_line_input:list)->bool:
    """
    Validates if command-line input contains input and output files
    Args:
        command_line_input:the list of command-line arguments entered by user
    Returns:
        True: if user entered all required arguments
        sys.exit: if the length of command-line input is less or greater than 3
    """
    if len(command_line_input) == 3:
        return True
    elif len(command_line_input) < 3:
        sys.exit("Too few command-line arguments")
    elif len(command_line_input) > 3:
        sys.exit("Too many command-line arguments")

def is_valid_extension(command_line_input: list) -> bool:
    """
    Validates if input and output files have the same extension
    Args:
        command_line_input: the list of command-line arguments entered by user
    Returns:
        True: if both files have the same extension
        sys.exit: if file extensions are not the same or input or output does not contain a valid file extension
    """
    # Split the extention from input and output command-line strings 
    # and store them into variables
    input_extension, output_extension = os.path.splitext(command_line_input[1])[1].lower(), os.path.splitext(command_line_input[2])[1].lower()
    valid_extensions = ['.jpeg', '.jpg', '.png']
    if input_extension == output_extension and input_extension in valid_extensions:
        return True
    elif input_extension != output_extension and (input_extension or output_extension in valid_extensions):
        sys.exit("Input and output have different extensions")
    elif not(input_extension and output_extension in valid_extensions):
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()


