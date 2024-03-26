from datetime import date
import sys
import inflect


def main():
    """
    Prompts the user to enter a birth date and passes it to
    convert_to_minutes. Prints the number of minutes written in words
    that is returned by convert_to_minutes. 
    """
    # Get date of birth from user
    date_of_birth = input("Date of birth: ")
    print(convert_to_minutes(date_of_birth))

def convert_to_minutes(birth_date):
    """
    Takes a string which is the date of birth entered by the user.
    Calculates the number of minutes that have passed since the date given and today's date.
    Calls convert_to_words and passes the number of minutes as integer.
    It exists the program if the entered date is not in the format: YYYY-MM-DD
    Args:
    - birth_date: a string entered by the user
    Returns:
    - the number of minutes written in words that have elapsed between birth_date and today
    """
    try:
        # Split the input into year, month, and day
        year, month, day = map(int, birth_date.split('-'))

        # Create a date object for the date of birth
        birth_date = date(year, month, day)

        # Get the current date
        # today = '2000-01-01'
        # year, month, day = map(int, today.split('-'))
        # today = date(year, month, day)
        today = date.today()

        # Calculate the difference between the two dates
        delta = today - birth_date

        # Calculate the number of minutes
        number_of_minutes = delta.days * 1440
        
        return convert_to_words(number_of_minutes)
    except:
        # print("Invalid date")
        sys.exit(1)

def convert_to_words(int_minutes):
        """ Takes the number of minutes (integer) that have elapsed since the birthday entered by the user
        and today's date. Returns the number of minutes written in words. 
        Args:
        - int_minutes: minutes elapsep
        Returns:
        - number of minutes written in words"""
        p = inflect.engine()
        # Format the number with commas
        formatted_number = "{:,}".format(int_minutes)
        # Replace commas with spaces
        formatted_number = formatted_number.replace(',', ' ')
        minutes_to_words = p.number_to_words(formatted_number, andword="")
        # Capitalize the first letter of the string
        minutes_to_words = minutes_to_words[0].upper() + minutes_to_words[1:]
        return minutes_to_words + ' minutes'


if __name__ == "__main__":
    main()