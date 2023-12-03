import random


def main():
    level = get_level()
    score = 0
    

    for _ in range(10):
        number_1 = generate_random_integer(level)
        number_2 = generate_random_integer(level)
        
        attempts = 0
        while attempts < 4:
            attempts += 1
            correct_answer = number_1 + number_2
            show_answer = f"{number_1} + {number_2} = {correct_answer}"
            try:
                answer = int(input(f"{number_1} + {number_2} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    if attempts == 3:
                        print(show_answer)
                        break
                    else:
                        print('EEE')
                        continue

            except ValueError:
                if attempts == 3:
                    print(show_answer)
                    break
                else:
                    print('EEE')
                    continue
    print(f"Score: {score}")


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
                return level_input 
            else:
                continue
                
        except ValueError:
            continue

# def generate_random_integer(n: int) -> int:
#     """
#     Generates a random integer with exactly 'n' digits.

#     Args:
#     - n: int
#         The number of digits the generated random integer should have.

#     Returns:
#     - int:
#         A random integer with exactly 'n' digits.

#     """

#     # Validating the input 'n'
#     # if not isinstance(n, int) or n <= 0:
#     #     raise ValueError("n should be a positive integer.")

#     # Generating the lower and upper bounds for the random integer
#     lower_bound = 10 ** (n - 1)  # Smallest n-digit number
#     upper_bound = (10 ** n) - 1  # Largest n-digit number

#     # Generating the random integer within the specified range
#     random_integer = random.randint(lower_bound, upper_bound)

#     return random_integer

def generate_random_integer(n):
    level_ranges = {
        1: (0, 9),
        2: (10, 99),
        3: (100, 999)
    }

    if n not in level_ranges:
        raise ValueError("Invalid level")

    min_value, max_value = level_ranges[n]
    return random.randint(min_value, max_value)


if __name__ == "__main__":
    main()