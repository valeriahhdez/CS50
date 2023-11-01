
from string import punctuation
# Minimum length of plate
l_min = 2
# Max length of plate
l_max = 6


def main():
    """
    Prompts the user to give a string for vanity plate and calls is_valid to evaluate the string. 
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
    Loops over a list of conditions and cheks if they are all met 
    Expects: 
    input_string
    Modifies: 
    nothing
    Returns: 
    True if all conditions are met, False otherwise. 
    """

    # Check if plate starts with two letters at least and store it vairable
    start_with_letters = not(any(char.isdigit() for char in input_str[0:2]))
    # Check if plate contains 0 at first position and store it in variable
    nostart_with_0 = not('0' in input_str[0])

    
    conditions = [
    
    start_with_letters,
    nostart_with_0,
    # Check valid length  
    has_length(input_str, l_min, l_max),    
    # Check if numbers are in the middle of the string
    middle_numbers(input_str),
    # Check if string contains punctuation marks
    has_punctuation(input_str)
]
    # Check if each condition is True
    for condition in conditions:
        if not condition:
            return False
        else: 
            return True

def has_length(x_str, m, x):
    """
    Checks is the plate has valid length
    Expects: 
    x_str: vanity plate
    m: minimum length
    x: maximum length
    Modifies:
    Nothing
    Returns:
    True is length of vanity plate is between 2 and 6, False if othwerwise.  
    """
    m <= len(x_str) <= x


def has_punctuation(s: str) -> bool:
    """
    Checks if the vanity plate string contains any punctuation mark or space
    """
    if any(p in s for p in punctuation):
        return False
    elif ' ' in s: 
        return False
    else:
        return True
   


def middle_numbers(y):
    """
   Returns True if 
    """
    number_index = None
    for i in range(len(y)):
        # check if a string contains digit and extract the index of the first number found
        if y[i].isdigit():
            # store that index in variable
            number_index= i
            break
        # divide the string at index
    contains_number = y[number_index:]
    # Take the second part of string and check if it contains all nnumbers
    if all(char.isdigit() for char in contains_number):
        return True
    else: 
        return False

main() 