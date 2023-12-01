# Prompt the user

# Check if answer is 1,2, or 3
# If input is invalid, reprompt
# If valid, store the input in a variable n

# Generate two random numbers (r_ number1, r_number2) with n digits

# Print r_number1 + r_number2

# Check the ansert of the user

# If answer input is not correct or is not a number, reprompt

# Count the number of attempts, after three attempts, print the correct answer and print the next math problem 




import random


def main():
    ...


def get_level():
    """
    This function prompts the user to enter a level. 
    It checks if the value entered is between the 1 - 3 range
    Args: none
    Changes: nothing
    Returns: True is the level entered is a valid value
    if the value is not in the specific range or is not a valid input, it reprompts the user
    """
    while True: 
        level_input = input("Level: ")
        try:
            level_input = int(level_input)
            if level_input in range(1,4):
                return True
                
            else:
                continue
                
        except ValueError:
            continue



def generate_integer(level):
    ...


if __name__ == "__main__":
    main()


