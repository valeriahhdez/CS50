import re

def main():
    """Pormpts the user to enter a string. 
    Calls count() and returns the number of times
    that 'um' was found in the input string as a stand alone
    word"""
    print(count(input("Input: ")))


def count(input_str):
    """
    Counts the number of times 'um' is used in sentence
    Args:
    - input_str: a string entered by the user
    Returns: 
    - um_count: the number of times that 'um' was found in input_string as a word
    """
    # find and count all instances of 'um' as a word
    ums_list = re.findall(r"\b(um)\b", input_str, re.IGNORECASE)
    count = len(ums_list)
    return count


if __name__ == "__main__":
    main()