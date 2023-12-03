
# If valid, store the input in a variable n

# Generate two random numbers (r_ number1, r_number2) with n digits

# Print r_number1 + r_number2 and prompt the user for answer

# If answer is not correct or is not a number, reprompt

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

def generate_random_integer(n: int) -> int:
    """
    Generates a random integer with exactly 'n' digits.

    Args:
    - n: int
        The number of digits the generated random integer should have.

    Returns:
    - int:
        A random integer with exactly 'n' digits.

    """

    # Validating the input 'n'
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n should be a positive integer.")

    # Generating the lower and upper bounds for the random integer
    lower_bound = 10 ** (n - 1)  # Smallest n-digit number
    upper_bound = (10 ** n) - 1  # Largest n-digit number

    # Generating the random integer within the specified range
    random_integer = random.randint(lower_bound, upper_bound)

    return random_integer


if __name__ == "__main__":
    main()


