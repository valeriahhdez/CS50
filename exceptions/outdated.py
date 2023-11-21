
month_numbers = list(range(1,13))
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

days_month = list(range(1,31))


def valid_month(x, y,z): 
    """ 
    Checks if the month given is month_names or in month_numbers
    Args: month_names, month_numbers, month_item
    Changes: nothing
    Returns: True if month_item is valid 
    """
    # check if month_item is month_names list
    if x in y:
        return True
    # check if month_item is month_numbers list
    elif x in z:
        return True
    else: 
        return False
    
    
def valid_day(x, y): 
    if x in y:
        return True
    else: 
        return False

def valid_date(m,n):
    if valid_day() and valid_month:
        return True
    else: 
        return False

def double_digit_month(v):
    if v.isdigit():
        return (str(v).zfill(2))
    else: 
        return v   

while true:
    try:
        # Prompt the user to enter a date
        input_date = input("Date: ")
        # Separate values by '/'
        date_list = input_date.split('/')

        month_item = date_list[0]
        day_item = date_list[1]
        year_item = date_list[2]
        if valid_date:
            # add a zero at the begining of month (if number) and day if any or both are single digits. 


# Check if the input is valid,
# month has to be in the list o be within 1-12 interval
# day has to be within the 1-31 range


# Propmt the user again if input isn't valid. 

# Check if input[0] in range(1,13) or input[0] in months_list

# If the first two values of input are numbers and they are single numbers, 
# add a 0 at the beginning

# Print input[2] + '/'+ input[1] + '/' + input[0]



# print(y)