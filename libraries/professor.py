import random


def main():
    """
    This function calls get_level and generate_random_level. 
    It produces 10 sum problems (X+Y) with two random number of n digits
    It prompts the user for an answer. The user only has three chances. 
    It keeps a score of how many problems has the user solved correctly. 
    Args: none
    Changes: score
    Returns:
    - score: the number of correct answers
    """
    level = get_level()
    score = 0

    # Generate 10 X+Y problems
    for _ in range(10):
        number_1 = generate_random_integer(level) 
        number_2 = generate_random_integer(level)
        correct_answer = number_1 + number_2
        # Number of times the user tries to solve the X+Y problem
        attempts = 0
        # The user has only three attempts
        while attempts < 4:
            attempts += 1
            answer_to_print = f"{number_1} + {number_2} = {correct_answer}"
            try:
                answer = int(input(f"{number_1} + {number_2} = "))
                # If users answers correctly in the first or second attempt
                # move on to the next X+Y problem and add 1 to score
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    # If the user fails the third attempt, print the correct answer 
                    # present the next problem
                    if attempts == 3:
                        print(answer_to_print)
                        break
                    else:
                    # Print 'EEE' if user fails but hasn't run out of attempts
                    # and reprompt for the correct answer
                        print('EEE')
                        continue

            except ValueError:
                # If user has entered an invalid value three times
                # print the correct answer and move on to the next problem
                if attempts == 3:
                    print(answer_to_print)
                    break
                else:
                # If user has entered an invalid value but hasn't run out of attempts
                # print print 'EEE' and reprompt for the correct answer
                    print('EEE')
                    continue
    # print the final score
    print(f"Score: {score}")


def get_level():
    """
    This function prompts the user to enter a level. 
    It checks if the value entered is between the 1 - 3 range
    Args: none
    Changes: nothing
    Returns: True if the level entered is a valid value
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
        # If The user enters an invalid input for the level, reprompt        
        except ValueError:
            continue

def generate_random_integer(n:int) -> int:
    """Generates a random number with n digits
    Args:
    n: an integer between 1 and 3
    Changes:
    nothing
    Returns:
    A random integer with n digits
    """
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
