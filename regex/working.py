import re

def main():
    """Prompts the user to input a time range
    Calls convert and prints the time range formatted as 24-hour period
    """
    print(convert(input("Hours: ")))


def convert(time_range):
    """
    Splits time range into start and end times. 
    Calls parse_time to extract and store hour, minutes and period in a dict. 
    Calls formatted_time to convert 12-hour format into 24-hour format and prints the new formatted times
    Args:
    - time_range: a string entered by the user that contains a start and end times 
    Returns:
    - 24-hour time range where hours and minutes are expressed with double digits. 
    """
    new_format = ""

    try:
        # Splits time range at the given pattern and stores starting and ending times into variables
        pattern = r"[\s|to]+"  
        split_list = re.split(pattern,time_range)
        start_time = split_list[0:2] # A list containing the start time and period (len = 2)
        end_time = split_list[2:] # A list containing the end time and period (len = 2)
    except: 
        raise ValueError
    
    if len(end_time) == 0:
        raise ValueError
    
    # Parse the time, muntes and period and store them into dict
    start_dict = parse_time(start_time)
    end_dict = parse_time(end_time)

    start_hour, end_hour = start_dict["hour"], end_dict["hour"]
    start_period, end_period = start_dict["period"], end_dict["period"]
    
    if  (start_hour or end_hour) > 12 and ('PM' or 'AM') not in (start_period or end_period):
        new_format = time_range
   
    # Raise valueError if any of the times are invalid
    elif (start_hour > 12 and 'PM' in start_period) or (end_hour > 12 and 'PM' in end_period):
        raise ValueError
        
    elif (start_dict["minutes"] or end_dict["minutes"]) > 59:
        raise ValueError
    
    # Format the 12-hour times as 24-hour and return the new formatted time range
    else:
        formatted_start = format_time(start_dict)
        formatted_end = format_time(end_dict)
        new_format = f"{formatted_start['hour']:02}:{formatted_start['minutes']:02}" + " to " + f"{formatted_end['hour']:02}:{formatted_end['minutes']:02}"
    return new_format

def parse_time(time_str):
    """
    Takes a time string and returns a dictionary containing hours, minutes and period (AM or PM)
    Args:
    - time_str: a time string
    Returns:
    - time_dict: a dictionary containing hours, minutes and period
    """
    time_dict = {}
    try:
        hour, minutes = time_str[0].split(':')
        period = time_str[-1]
        time_dict = {"hour": int(hour), "minutes": int(minutes), "period": period}

    except:
        hour, period = time_str[0], time_str[1]
        time_dict = {"hour": int(hour), "minutes": 0, "period": period}

    
    return time_dict

def format_time(time_dict):
    """
    Takes a dictionary and extracts the hour. Returns the same dict with a 24-hour format
    Args:
    - time_dict: a dictionary containing hours, minutes and period
    Returns:
    time_dict: an updated version of the input dictionary with the a 24-hour format
    """
    if time_dict["period"] == 'AM':
        if time_dict["hour"] == 12:
            time_dict["hour"] = 0
    elif time_dict["period"] == 'PM':
        if 1 <= time_dict["hour"] <= 11: 
            time_dict["hour"] = time_dict["hour"] + 12
    else:
        raise ValueError
        
    return time_dict

if __name__ == "__main__":
    main()

