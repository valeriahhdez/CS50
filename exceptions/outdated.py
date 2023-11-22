
month_numbers = str(list(range(1,13)))

month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

days_list= str(list(range(1,32)))


def valid_month(x, y,z): 
    """ 
    Checks if the month given is in month_names or in month_numbers
    Args: 
    x: month_item
    y: month_names
    z: month_numbers
    Changes: month_item
    Returns: 
    If month_item is valid, it return the month in a double digit number
    If month_item is not in either month_names nor month_numbers, returns False
    """
    # check if month_item is in month_names list
    if x in y:
        # Extract the index number
        month_number = str(y.index(x)+1)
        # turn into double digit number
        return double_digit(month_number)
        
    # if month_item is in month_numbers list, return the month number as double digit
    elif x in z:
        return double_digit(x)
    else: 
        return False
    

def valid_day(d, y): 
    """ 
    Checks if the day given is in days_month
    Args: 
    d: day_item
    y: days_month
    Changes: day_item
    Returns: If day_item is a valid day, then it returns the day as a double digit number
    If day_item is not in days_month list, it returns False
    """
    if d in y:
        return double_digit(d)
    else: 
        return False

def double_digit(v):
    """
    Args:
    v the digit to be converted to a double sigit number
    Changes: v
    Returns:
    v as a double digit number. If v is already a double digit, it returns the number itself
    """
    if v.isdigit():
        return (str(v).zfill(2))
    else: 
        return v 
    


while True:
    try:
        # Prompt the user to enter a date
        input_date = input("Date: ")
        # Separate values by '/'
        date_list = input_date.split('/')

        month_item = date_list[0]
        day_item = date_list[1]
        year_item = date_list[2]
        month_digit = valid_month(month_item, month_names, month_numbers)
        day_digit = valid_day(day_item, days_list)
        
        if (day_digit or month_digit) == False:
            continue
        else:
            print(year_item + "-" + month_digit + "-" + day_digit)
            exit()
            ...

    except EOFError:
        exit()
        ... 


            


# Check if the input is valid,
# month has to be in the list o be within 1-12 interval
# day has to be within the 1-31 range


# Propmt the user again if input isn't valid. 

# Check if input[0] in range(1,13) or input[0] in months_list

# If the first two values of input are numbers and they are single numbers, 
# add a 0 at the beginning

# Print input[2] + '/'+ input[1] + '/' + input[0]



# print(y)