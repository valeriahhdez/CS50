import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """Converts 12-hour time into a 24-hour format
    Args:
    - input_string: a string entered by the user containing 12-hour time
    Returns:
    - entered time converted into a 24-hour format
    Raises: 
    - ValueError: if input is an invalid time, for example, 12:60 AM, 13:00 PM"""
    # after the colon : numbers can only be 00 to 59
    # the colon is optional
    # 1 AM to 11 AM == 1:00 AM to 11:00 AM == 1:00 to 11:00 (24-hour)
    # 1 PM to 11 PM == 1:00 PM to 11: PM == 13:00 to 23:00 (24-hour)
    # 12 AM == 12:00 AM == 00:00 (24-hour)
    # 12 PM == 12:00 PM == 12:00 (24-hour)

    #first check the first number and if the string has a colon
    match = re.search(r'(..?)(:?)(..?) (AM|PM) (?:to) (..?)(:?)(..?) (AM|PM)', s)
    # return len(match)
    try:      

        # match  = re.findall(r'^([1-9]|[0-9]):?([0-5][0-9])$', s)

        # match = re.findall(r'^[1-9]|1[0-2] AM|PM$|^[1-9]|1[0-2]:[0-5][0-9] AM|PM$', s)
        
        if match:
            full_time = match.group(9)
            return full_time
        else:
            return ("No valid time format found.")

    except ValueError:
        return "Not a valid time"





if __name__ == "__main__":
    main()

