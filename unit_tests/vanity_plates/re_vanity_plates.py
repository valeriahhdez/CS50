from string import punctuation

def main():
    """
    Prompts the user to entered a plate and checks how many conditions the plate complies with
    Prints:
    - Valid if the plate mets all five conditions
    - Invalid if at least one condition isn't met
    """
    input_plate = input('Plate: ')
    if is_valid(input_plate) == 5:
        print('Valid')
    else:
        print('Invalid')
    

def is_valid(input_str):
    """
    Checks if plate entered by user complies with five different conditions
    Aargs:
    - input_str: a string representing the plate entered by user
    Changes: nothing
    Returns:
    - condition_met: the total umber of conditions the plate met
    """
    condition_met = 0
    # Condition 1: first two characters can't be numbers
    if not(any(char.isdigit() for char in input_str[0:2])):
        condition_met += 1
    # Condition 2: plate should have the right length
    if 2 <= len(input_str) <= 6:
        condition_met += 1
    # Condition 3: plates can't contain punctuation signs
    if not any(char in input_str for char in punctuation): 
        condition_met += 1
    # Condition 4: plates can't have spaces
    if ' ' not in input_str:
        condition_met += 1
    # Condition 5: plate can't have numbers in the middle of the string 
    # nor can the leading number be zero 
    digits = "".join(char for char in input_str if char.isdigit())
    if not digits:  # No digits, condition met
        condition_met += 1
    else:
        if digits[0] != '0' and digits == input_str[-len(digits):]:
            condition_met += 1
    return condition_met              
    

if __name__ == "__main__":
    main()