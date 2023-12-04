import random

def main():
    """
    This function interacts with the user. 
    It creates a random number between 1 and 
    the user's input and asks the user to guess it. 
    """
    level = get_level()
    guess_number = generate_random_integer(level)
    # print(guess_number)
    while True: 
        try:
            guess = int(input("Guess: "))
            if guess > 0:  
                if guess == guess_number:
                    print("Just right!")
                    break
                elif guess < guess_number:
                    print("Too small!")
                    continue
                else:
                    print("Too large!")
                    continue
            else:
                continue
        except ValueError:
            continue

def get_level ():
    """
    Prompts the user to enter an integer value. 
    The function then checks if the input is valid and if it's a positive number
    Args: none
    Changes: nothing
    Returns:
    - level_input: integer entered by the user
    """
    while True: 
        input_level = input("Level: ")
        try:
            input_level = int(input_level)
            if input_level > 0:
                return input_level 
            else:
                continue
        # If The user enters an invalid input for the level, reprompt        
        except ValueError:
            continue

def generate_random_integer(n:int) -> int:
    """Generates a random number between 1 and n
    Args:
    n: an integer entered by user
    Changes:
    nothing
    Returns:
    A random integer 
    """
    return random.randint(1, n)

if __name__ == "__main__":
    main()
