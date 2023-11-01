# To check if the plate number contains a punctuation character, import punctuation
from string import punctuation

l_min = 2
l_max = 6


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(input_str):
    start_with_letters = not(any(char.isdigit() for char in input_str[0:2]))
    nostart_with_0 = not('0' in input_str[0])

    # List of conditions to be met
    conditions = [
    # Check if plates start with at least two letters
    start_with_letters,
    # Check valid length  
    has_length(input_str, l_min, l_max),
    # Check if string contains 0 at string[0]
    nostart_with_0,
    # Check if numbers are in the middle of the string
    middle_numbers(input_str),
    # Check if string contains punctuation marks
    has_punctuation(input_str)
]
    for condition in conditions:
        if not condition:
            return False
        else: 
            return True

def has_length(x_str, l_min, l_max):
    l_min <= len(x_str) <=l_max


def has_punctuation(str):
    # punctuation = ['.', '?', '!', ':', ';', ',']
    if any(s in str for s in punctuation):
        return False
    elif ' ' in str: 
        return False
    else:
        return True
   


def middle_numbers(y):
    """
   Splits string in two parts at position of first encountered number. 
   Checks if the second part of the string contains only numbers. If so, it meets the condition.
   Args:
    y: A string representing the vanity plate.

  Returns:
    True if the string does not contain numbers in the middle, False otherwise.
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