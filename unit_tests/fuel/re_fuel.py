import re

def main():
   while True:
       try:
           user_input = input("Fraction: ")
           percentage_value = convert(user_input)
           output = gauge(percentage_value)
           print(output)
           break
       except ValueError:
           continue
        #    break
       except ZeroDivisionError:
           continue


def convert(fraction: str) -> int:
    """
    Converts a valid X/Y fraction string to a percentage rounded to the nearest int.
    Args:
        fraction: A string in the format "X/Y" where X and Y are integers.
    Returns:
        The corresponding percentage as an int between 0 and 100.
    Raises:
        ValueError: If the format is invalid (ex: 5-10), X > Y, or X/Y are non-integers.
        ZeroDivisionError: If the denominator (Y) is 0.
    """
         
    num1, num2 = fraction.split("/")
    try:
        num1, num2 = int(num1), int(num2)
        # Raise a ValueError if X > Y so that main() reprompts the user
        if num2 == 0:
            raise ZeroDivisionError
        elif num1 > num2:
            raise ValueError
            
        # Raise ValueError if the input contains strings or float numbers  
    except ValueError:
        raise ValueError
        
    percentage = round(num1 / num2 * 100)
    return percentage
    
    

def gauge(percentage: int) -> str:
    """
    Maps a percentage (int) to its corresponding output string.
    Args:
    - percentage: An integer between 0 and 100.
    Returns:
    - "E" if percentage is less than or equal to 1,
    - "F" if percentage is greater than or equal to 99,
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
