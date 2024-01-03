import sys
import os
from PIL import Image

# def main():
#     conditions = [
#         validate_input_length(sys.argv),
#         validate_input_extension(sys.argv),
#         input_file_exists(sys.argv)
#     ]
#     if all(conditions):
#         print('True')



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
        print('True')
    elif input_extension != output_extension and (input_extension or output_extension in valid_extensions):
        sys.exit("Input and output have different extensions")
    elif not(input_extension and output_extension in valid_extensions):
        sys.exit("Invalid input")


def input_file_exists(list_of_args):
    valid_inputs = ["before1.jpg", "before2.jpg", "before3.jpg"]
    if list_of_args[1] in valid_inputs:
        return True
    else:
        sys.exit("Input does not exist")

def overlay_image():
    ...


  
    
# User to enters an input and output files

# Check if sys.argv has three arguments
    
# Check if input and output file have the same valid extension (.jpg, .jpeg, .png)
    
# Open input image
        
# Resize it

# Paste template into it
    
# Save into outputimage
# if __name__ == "__main__":
#     main()

# Open the input image
input_image = Image.open("shirt.png")
# resize and crop the input image
shirt_size = input_image.size
resized_input_image = (sys.argv[1], shirt_size)
print(shirt_size)
#Overlay the shirt image onto the input image and save the output file

