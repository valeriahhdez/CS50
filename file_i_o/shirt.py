import sys
import os
from PIL import Image
from PIL import ImageOps

def main():
    """
    Calls validate_input_length and validate_input_extension
    Opens shirt.jpg file and pastes it into a background image
    Args: 
     - None
    Returns:
     - A new image with shirt on
    """
    conditions = [
        validate_input_length(sys.argv),
        validate_input_extension(sys.argv)
    ]
    if all(conditions):
        try:
            # Open the input image
            shirt = Image.open("shirt.png")
            # resize and crop the input image
            shirt_size = shirt.size
            photo = Image.open(sys.argv[1])
            output_file = ImageOps.fit(photo, shirt_size)
            output_file.paste(shirt, shirt)
            output_file.save(sys.argv[2])
        except: 
            sys.exit("Input does not exist")


# Validate input length
def validate_input_length(list_of_args:list)->bool:
    """
    Validates the length of user input
    Args:
        list_of_args:the list of command-line arguments entered by user
    Returns:
        True: if user entered two arguments
        sys.exit: if the length of command-line args is less or greater than 3
    """
    if len(list_of_args) == 3:
        return True
    elif len(list_of_args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(list_of_args) > 3:
        sys.exit("Too many command-line arguments")

# validate_input_length(sys.argv)
# Validate input type 
def validate_input_extension(list_of_args):
    """
    Validates that input and output files have the same extension
    Args:
        list_of_args:the list of command-line arguments entered by user
    Returns:
        True: if both files have the same extension
        sys.exit: if file extensions are not the same or input does not contain a valid file extension
    """
    input_extension, output_extension = os.path.splitext(sys.argv[1])[1].lower(), os.path.splitext(sys.argv[2])[1].lower()
    valid_extensions = ['.jpeg', '.jpg', '.png']
    if input_extension == output_extension and input_extension in valid_extensions:
        return True
    elif input_extension != output_extension and (input_extension or output_extension in valid_extensions):
        sys.exit("Input and output have different extensions")
    elif not(input_extension and output_extension in valid_extensions):
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()


