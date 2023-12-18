import re

def main():
   while True:
       try:
           user_input = input("Fraction: ")
           percentage = convert(user_input)
           output = gauge(percentage)
           print(output)
           break
       except ValueError:
           continue
       except ZeroDivisionError:
           continue


def convert(fraction):
    """
    Converts a valid X/Y fraction string to a percentage rounded to the nearest int.
    Args:
        fraction: A string in the format "X/Y" where X and Y are integers.
    Returns:
        The corresponding percentage as an int between 0 and 100.
    Raises:
        ValueError: If the format is invalid or X/Y is non-integer.
        ZeroDivisionError: If the denominator (Y) is 0.
    """
         
    num1, num2 = fraction.split("/")
    try:
        num1, num2 = int(num1), int(num2)
    except ValueError:
        raise ValueError

    if num2 == 0:
        raise ZeroDivisionError

    percentage = round(num1 / num2 * 100)
    return percentage


def gauge(percentage: int) -> str:
    """
    Maps a percentage (int) to its corresponding output string.
    Args:
    - percentage: An integer between 0 and 100.
    Returns:
    - "E" if percentage is less than or equal to 1,
    - "F" ifpercentage is greater than or equal to 99,
    - "Z%" otherwise, wherein Z is percentage.
    """
    if 99 <= percentage:
        return "F"
    elif percentage <= 1:
        return "E"
    elif 1 < percentage < 99:
        return f"{percentage}%"
    


if __name__ == "__main__":
    main()
