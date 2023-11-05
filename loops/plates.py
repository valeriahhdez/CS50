
from string import punctuation
import re
# Minimum length of plate
min_length = 2
# Max length of plate
max_length = 6


def main():
    """
    Prompts the user to give a string for vanity plate and calls is_valid to evaluate if the string is valid. 
    Expects: plate->string
    Modifies: nothing
    Returns: VALID if is_valid is True, INVALID if it doesn't. 
    """
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(input_str: str) ->bool:
    """
    Checks if all conditions are met

    Expects: 
    input_string

    Modifies: 
    nothing

    Returns: 
    True if all conditions are met, False otherwise. 
    """

    
    start_with_letters = not(any(char.isdigit() for char in input_str[0:2]))
    
    nostart_with_0 = not('0' in input_str[0])

    # List of conditions for vanity plate to be valid
    conditions = [
    start_with_letters,
    nostart_with_0,  
    has_length(input_str, min_length, max_length),    
    middle_numbers(input_str),
    has_punctuation(input_str)
]
    if all(conditions): 
        return True
    else: 
        return False


def has_length(x_str: str, m: int, x: int)-> bool:
    """
    Checks if the plate has a valid length

    Expects: 
    x_str: vanity plate
    m: minimum length
    x: maximum length

    Modifies:
    Nothing

    Returns:
    True if length of vanity plate is is between the min and max values, False if othwerwise.  
    """
    if m <= len(x_str) <= x:
        return True
    else: 
        return False


def has_punctuation(s: str) -> bool:
    """
    Checks if the vanity plate string contains any punctuation mark or space

    Expects: 
    s: vanity plate string

    Modifies: nothing

    Returns:
    True if vanity plate has no punctuation marks nor spaces, False if otherwise
    """
    if any(p in s for p in punctuation):
        return False
    elif ' ' in s: 
        return False
    else:
        return True
   


def middle_numbers(y: str) -> bool:
    """
   Checks if vanity plate contains numbers in the middle. 

   Expects: strin of plate.

   Modifies: nothing

   Returns: True if string contains numbers at the end of the string or no numbers at all. 
   False if it contains numbers in the middle of the string or the first number is 0 
    """
    # Initialize variable to store index where first number is encountered. 
    number_index = None
    # Initialize a variable to store the portion of the string that contains numbers. 
    contains_number = ''
    valid = True
    for i in range(len(y)):
        # check if the first digit is 0
        if y[i].isdigit() and y[i] == '0':
            valid = not valid
            break

        elif y[i].isdigit() and y[i] != '0':
            number_index= i
            # Split string at index of first number and store it in variable contains_number
            contains_number = y[number_index:]
            # Check if contains_numbers has all nnumbers
            if all(char.isdigit() for char in contains_number):
                valid
            else: 
                valid = not valid
            break
    return valid  

main() 