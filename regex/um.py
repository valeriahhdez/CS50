import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    """
    Counts the number of times 'um' is used in sentence
    Args:
    - input_str: a string entered by the user
    Returns: 
    - um_count: the number of times that 'um' was found in input_string as a word
    """
    # find and count all instances of 'um' as a word
    ums_list = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    count = len(ums_list)
    return count

    # return de number of times 'um' was used in the string

# um can have a space before u \s?
# u and m need to be together
# maybe one or more \.\?\,\!\s]?     


# test: ignoroe case
# eliminate
# If um is at the end of the string it won't have a space and won't be included in the counter
# um can be preceded by white space but followed by white space, nothing or a punctuation sign like '?'


if __name__ == "__main__":
    main()